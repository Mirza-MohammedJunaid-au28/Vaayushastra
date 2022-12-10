import cv2
import numpy as np

# width,height = pyautogui.size()
cap = cv2.VideoCapture(1)

colour_ranges = {"RED":[[140, 85, 110], [348, 255, 255]],
                 "BLUE" : [[94, 80, 2], [126, 255, 255]],
                 "GREEN" : [[50, 52, 50], [85, 255, 260]],
                 "YELLOW" : [[15, 40, 50], [40, 255, 255]],
                 "ORANGE" : [[10, 100, 20], [25, 255, 255]]}

def grid(col):

    red = colour_ranges['RED']
    blue = colour_ranges['BLUE']
    green = colour_ranges['GREEN']
    yellow = colour_ranges['YELLOW']
    orange = colour_ranges['ORANGE']
    priority = col.lower()
    """ color = colour_ranges[col]
    lower = np.array(color[0])
    upper = np.array(color[1]) """
    while True:
        key = cv2.waitKey(1)
        _,frame = cap.read() 
        output = frame.copy()
        height = frame.shape[0]
        width = frame.shape[1]
        HSV_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        HSV_frame = cv2.medianBlur(HSV_frame, 3)
        red_frame_lab = cv2.inRange(HSV_frame, np.array(red[0]),np.array(red[1]))
        red_frame_gaussian = cv2.GaussianBlur(red_frame_lab, (5, 5), 2, 2)
        red_circles = cv2.HoughCircles(red_frame_gaussian, cv2.HOUGH_GRADIENT, 1, 30 , param1=80, param2=100, minRadius=10, maxRadius=0)
        blue_frame_lab = cv2.inRange(HSV_frame, np.array(blue[0]),np.array(blue[1]))
        blue_frame_gaussian = cv2.GaussianBlur(blue_frame_lab, (5, 5), 2, 2)
        blue_circles = cv2.HoughCircles(blue_frame_gaussian, cv2.HOUGH_GRADIENT, 1, 30 , param1=80, param2=100, minRadius=10, maxRadius=0)
        green_frame_lab = cv2.inRange(HSV_frame, np.array(green[0]),np.array(green[1]))
        green_frame_gaussian = cv2.GaussianBlur(green_frame_lab, (5, 5), 2, 2)
        green_circles = cv2.HoughCircles(green_frame_gaussian, cv2.HOUGH_GRADIENT, 1, 30 , param1=80, param2=100, minRadius=10, maxRadius=0)
        if red_circles is not None:
            red_circles = np.round(red_circles[0, :]).astype("int")
            cv2.circle(frame, center=(red_circles[0, 0], red_circles[0, 1]), radius=red_circles[0, 2], color=(0, 0, 0), thickness=2)
            cv2.line(output,(red_circles[0,0],red_circles[0,1]),(width//2,height//2),(0,255,0),3) 
        if blue_circles is not None:
            blue_circles = np.round(blue_circles[0, :]).astype("int")
            cv2.circle(frame, center=(blue_circles[0, 0], blue_circles[0, 1]), radius=blue_circles[0, 2], color=(0, 0, 0), thickness=2)
            cv2.line(output,(blue_circles[0,0],blue_circles[0,1]),(width//2,height//2),(0,255,0),3) 
        if green_circles is not None:
            green_circles = np.round(blue_circles[0, :]).astype("int")
            cv2.circle(frame, center=(green_circles[0, 0], green_circles[0, 1]), radius=green_circles[0, 2], color=(0, 0, 0), thickness=2)
            cv2.line(output,(green_circles[0,0],green_circles[0,1]),(width//2,height//2),(0,255,0),3) 
        red_output_frame = cv2.bitwise_and(frame,frame,mask=red_frame_lab)
        blue_output_frame = cv2.bitwise_and(frame,frame,mask=blue_frame_lab)
        green_output_frame = cv2.bitwise_and(frame,frame,mask=green_frame_lab)
        cv2.imshow("Frame", frame)
        cv2.imshow("RedMask", red_output_frame)
        cv2.imshow("Blue Mask", blue_output_frame)
        cv2.imshow("Green Mask", green_output_frame)
        cv2.imshow("Output", output)
        if key == 27:
            break

print('1. Red \n2. Blue \n3. Green \n4. Yellow \n5. Orange')
ch = int(input('Enter : '))
keys = list(colour_ranges.keys())
# keys.pop(,keys)
# print(col,keys)
grid(keys[ch-1])