import numpy as np
import cv2

def detectColor(color):
    colorList = {'red' : [[20,150,150],[190,255,255]],
                'blue' : [[120,150,150],[180,250, 255]],
                 'yellow' : [[15, 40, 50],[40,255,255]],
                 'orange' : [[10,70,100],[20,255,255]],
                 'purple' : [[227,195,203],[52,25,48]]
                 }
    color_range = colorList[color]
    cap = cv2.VideoCapture(1)

    while(True):

        ret, captured_frame = cap.read()
        output_frame = captured_frame.copy()

        captured_frame_bgr = cv2.cvtColor(captured_frame, cv2.COLOR_BGRA2BGR)
        captured_frame_bgr = cv2.medianBlur(captured_frame_bgr, 3)
        captured_frame_lab = cv2.cvtColor(captured_frame_bgr, cv2.COLOR_BGR2Lab)
        captured_frame_lab_color = cv2.inRange(captured_frame_lab, np.array(color_range[0]), np.array(color_range[1]))
        captured_frame_lab_color = cv2.GaussianBlur(captured_frame_lab_color, (5, 5), 2, 2)
        circles = cv2.HoughCircles(captured_frame_lab_color, cv2.HOUGH_GRADIENT, 1, captured_frame_lab_color.shape[0] / 8, param1=100, param2=18, minRadius=5, maxRadius=60)

        if circles is not None:
            circles = np.round(circles[0, :]).astype("int")
            print(circles[0, 2])
            cv2.circle(output_frame, center=(circles[0, 0], circles[0, 1]), radius=circles[0, 2], color=(0, 255, 0), thickness=2)
            cv2.putText(output_frame,'Diameter : ' + str(2 * circles[0,2]),(20,20), cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,255))
        cv2.imshow('frame', output_frame)
        final_result = cv2.bitwise_and(output_frame,output_frame,mask=captured_frame_lab_color)
        cv2.imshow('red', final_result)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

colors = ['blue','red','yellow','purple','orange']
colorInput = input("Enter Color Name : ")

if(colorInput.lower() in colors):
    detectColor(colorInput.lower())
else:
    print('Invalid colors')