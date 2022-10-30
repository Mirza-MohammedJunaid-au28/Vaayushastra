import cv2
import numpy as np

def nothing(x):
    # any operation
    pass

cap = cv2.VideoCapture(1)
lower_red = np.array([l_h, l_s, l_v])
upper_red = np.array([u_h, u_s, u_v])

mask = cv2.inRange(hsv, lower_red, upper_red)
kernel = np.ones((5, 5), np.uint8)
mask = cv2.erode(mask, kernel)