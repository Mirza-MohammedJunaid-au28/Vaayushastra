import cv2
import numpy as np


def detectColor(color):
    """ colorList = {'red' : [[0,0,115],[116,97,255]],
                 'blue' : [[255,1,0],[255,199,89]],
                 'yellow' : [[0,200,231],[181,255,255]],
                 'orange' : [[0,109,255],[128,185,255]],
                 'purple' : [[213,0,121],[255,155,255]]
                 } """
    colorList = {'red' : [[161,155,84],[179,255,255]],
                 'blue' : [[110,50,50],[130,255,255]],
                 'yellow' : [[22,93,0],[45,255,255]],
                 'orange' : [[10,100,20],[25,255,255]],
                 'purple' : [[227,195,203],[52,25,48]]
                 }
    color_range = colorList[color]
    lower_bound = np.array(color_range[0])
    higher_bound = np.array(color_range[1])

    cap = cv2.VideoCapture(1)

    while True:
        ret, frame = cap.read()
        width = int(cap.get(3))
        height = int(cap.get(4))
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv,lower_bound,higher_bound)

        result = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow('frame', result)
        cv2.imshow(f'{color} detection', mask)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows() 




colors = ['blue','red','yellow','purple','orange']
colorInput = input("Enter Color Name : ")

if(colorInput.lower() in colors):
    detectColor(colorInput.lower())
else:
    print('Invalid colors')