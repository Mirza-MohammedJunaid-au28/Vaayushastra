import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def draw_horizontal_grid(frame,height,width):
    h = height // 3
    cv2.line(frame,(0,h),(width,h),(255,0,0),3)
    cv2.line(frame,(0,h+h),(width,h+h),(255,0,0),3)
    return

def draw_vertical_grid(frame,height,width):
    w = width // 3
    cv2.line(frame,(w,0),(w,height),(255,0,0),3)
    cv2.line(frame,(w+w,0),(w+w,height),(255,0,0),3)
    return


def frame_grid(frame,height,width):
    draw_horizontal_grid(frame,height,width)
    draw_vertical_grid(frame,height,width)
    return

while True:
    key = cv2.waitKey(1)
    _,frame = cap.read() 
    output_frame = frame.copy()
    height = frame.shape[0]
    width = frame.shape[1]
    frame_grid(output_frame,height,width)
    cv2.imshow("Frame", frame)
    cv2.imshow("Output Frame", output_frame)
    if key == 27:
        break