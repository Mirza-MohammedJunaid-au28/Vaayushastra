import cv2
import numpy as np
import time
# import math
import pada as pd
from threading import Thread


check = True
colour_ranges = {"RED":[[140, 85, 110], [348, 255, 255]],
          "BLUE" : [[94, 80, 2], [126, 255, 255]],
          "GREEN" : [[50, 52, 50], [85, 255, 260]],
          "YELLOW" : [[15, 40, 50], [40, 255, 255]],
          "ORANGE" : [[10, 100, 20], [25, 255, 255]]}
final_distance = 0

class FirstRound():

    def __init__(self,speed):
        self.speed = speed

    def colour_det(self,colour_in):
        global check
        cap = cv2.VideoCapture(0)
        coul_name = colour_ranges[colour_in]
        low_bound = np.array(coul_name[0])
        high_bound = np.array(coul_name[1])
        while True:
            key = cv2.waitKey(1)
            _, frame = cap.read()
            output_frame = frame.copy()
            HSV_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            HSV_frame = cv2.medianBlur(HSV_frame, 3)
            frame_lab = cv2.inRange(HSV_frame, low_bound, high_bound)
            frame_gaussian = cv2.GaussianBlur(frame_lab, (5, 5), 2, 2)
            circles = cv2.HoughCircles(frame_gaussian, cv2.HOUGH_GRADIENT, 1, frame_gaussian.shape[0] / 8, param1=100, param2=18, minRadius=10, maxRadius=100)

            if circles is not None:
                circles = np.round(circles[0, :]).astype("int")
                for i in circles:
                    cv2.circle(output_frame, center=(circles[0, 0], circles[0, 1]), radius=circles[0, 2], color=(0, 0, 0), thickness=2)
                    cv2.putText(output_frame, 'Diameter : ' + str(2 * circles[0, 2]), (0, 20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
                    check = False
            cv2.imshow("detected circles", output_frame)
            cv2.imshow("Frame", frame)
            if key == 27:
                break

    def calc(self):
        global final_distance

        count = 0
        timee = 0
        avg_speed = 0
        history_avg_salary = []
        total_speed = 0
        while(check):
            print('Speed : ',speed[count])
            time.sleep(1)
            timee += 1
            history_avg_salary.append(avg_speed)
            total_speed += speed[count]
            avg_speed = total_speed / timee
            count += 1
            if count == len(speed):
                print('Avg Speed :',avg_speed)
                break
        
        avg_speed = round(avg_speed)
        """ if avg_speed - math.floor(avg_speed) < 0.5:
            avg_speed = math.floor(avg_speed)
        else:
            avg_speed = math.ceil(avg_speed) """
        
        print('New Avg Speed',avg_speed)
        distance = avg_speed * timee
        print('Distance is :',distance)
        final_distance = distance
        self.sendTOpada()
        return
    
    def sendTOpada(self):
        print('Final distance : ',final_distance)
        print('First Round is Completed')
        print('PADA Dropped')
        pd.Pada_Operatiosns(45,final_distance,7)

speed = [12,13,12,14,15,15,15,14,13,12,14,13,11,13,12,13,12,14,15,15,15,14,13,12,14,13,11,13,12,13,12,14,15,15,15,14,13,12,14,12,13,12,14,15,15,15,14,13,12,14,13,11,13,12,13,12,14,15,15,15,14,13,12,14,13,11,13,12,13,12,14,15,15,15,14,13,12,14,13,11,13,13,11,13]
firstRound_obj = FirstRound(speed)

color_detection = Thread(target = firstRound_obj.colour_det , args=('RED',))
calculate_speed = Thread(target = firstRound_obj.calc)
x = color_detection.start()
y = calculate_speed.start()

""" while(final_distance != 0):
    
    break """