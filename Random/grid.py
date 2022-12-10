import cv2
import numpy as np

# width,height = pyautogui.size()
cap = cv2.VideoCapture(1)

colour_ranges = {"RED":[[140, 85, 110], [348, 255, 255]],
                 "BLUE" : [[94, 80, 2], [126, 255, 255]],
                 "GREEN" : [[50, 52, 50], [85, 255, 260]],
                 "YELLOW" : [[15, 40, 50], [40, 255, 255]],
                 "ORANGE" : [[10, 100, 20], [25, 255, 255]]}
"""
def draw_leftTop_Grid(frame,height,width):
    h = height // 2
    w = width // 2
    cv2.line(frame,(0,h//2),(w,h//2),(255,0,0),3)
    cv2.line(frame,(w//2,0),(w//2,h),(255,0,0),3) 
    return

def draw_leftDown_Grid(frame,height,width):
    h = height // 2
    w = width // 2
    cv2.line(frame,(w//2,h),(w//2,height),(255,0,0),3)
    cv2.line(frame,(0,h+h//2),(w,h+h//2),(255,0,0),3) 
    return

def draw_rightTop_Grid(frame,height,width):
    h = height // 2
    w = width // 2
    cv2.line(frame,(w,h//2),(width,h//2),(255,0,0),3)
    cv2.line(frame,(w+w//2,0),(w + w//2,h),(255,0,0),3) 
    return

def draw_rightDown_Grid(frame,height,width):
    h = height // 2
    w = width // 2
    cv2.line(frame,(w,h+h//2),(width,h+h//2),(255,0,0),3)
    cv2.line(frame,(w+w//2,h),(w + w//2,height),(255,0,0),3) 
    return

"""
""" 
def frame_grid(frame,height,width):
    cv2.line(frame,(0,height//2),(width,height//2),(255,0,0),3) 
    cv2.line(frame,(width//2,0),(width//2,height),(255,0,0),3)
    return
"""

def draw_horizontal_grid(frame,height,width):
    """
    h = height // 3
    cv2.line(frame,(0,h),(width,h),(255,0,0),3)
    cv2.line(frame,(0,h+h),(width,h+h),(255,0,0),3)
    """
    h = height // 2
    cv2.line(frame,(0,h),(width,h),(255,0,0),3)
    return

def draw_vertical_grid(frame,height,width):
    """
    w = width // 3
    cv2.line(frame,(w,0),(w,height),(255,0,0),3)
    cv2.line(frame,(w+w,0),(w+w,height),(255,0,0),3)
    """
    w = width // 2
    cv2.line(frame,(w,0),(w,height),(255,0,0),3)
    return


def frame_grid(frame,height,width):
    draw_horizontal_grid(frame,height,width)
    draw_vertical_grid(frame,height,width)
    return


def showDirection(circle_x,circle_y,height,width):
    """
    h = height // 3
    w = width // 3

    if((circle_x >= 0 and circle_x <= width) and (circle_y >= 0 and circle_y <= h)):
        print('Cirlce is to Far , Can Land Safely');
        if(circle_x <= w):
            print('Zone is in Top Left')
        elif(circle_x > w and circle_x <= w+w):
            print('Zone is in Top Center')
        elif(circle_x > w+w and circle_x <= width):
            print('Zone is in Top Right')

    elif((circle_x >= 0 and circle_x <= width) and (circle_y > h and circle_y <= h+h)):
        print('Cirlce is little Close');
        if(circle_x <= w):
            print('Zone is in Mid Left')
        elif(circle_x > w and circle_x <= w+w):
            print('Zone is in Mid Center')
        elif(circle_x > w+w and circle_x <= width):
            print('Zone is in Mid Right')

    elif((circle_x >= 0 and circle_x <= width) and (circle_y > h+h and circle_y <= height)):
        print('Circle is Too Close');
        if(circle_x <= w):
            print('Zone is in Bottom Left')
        elif(circle_x > w and circle_x <= w+w):
            print('Zone is in Bottom Center')
        elif(circle_x > w+w and circle_x <= width):
            print('Zone is in Bottom Right')

    """
    x = width // 2
    y = height // 2
    if(circle_x <= x and circle_y <= y):
        print('Circle is in 1st Quadrant')
    
    elif(circle_x >= x and circle_y <= y):
        print('Cirlce is in 2nd Quadrant')
    
    elif(circle_x <= x and circle_y >= y):
        print('Circle is in 3rd Quadrant')
    
    elif(circle_x >= x and circle_y >= y):
        print('Cirlce is in 4th Quadrant')
    


def grid(col):
    color = colour_ranges[col]
    lower = np.array(color[0])
    upper = np.array(color[1])
    while True:
        key = cv2.waitKey(1)
        _,frame = cap.read() 
        output = frame.copy()
        height = frame.shape[0]
        width = frame.shape[1]
        frame_grid(output,height,width)
        HSV_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        HSV_frame = cv2.medianBlur(HSV_frame, 3)
        frame_lab = cv2.inRange(HSV_frame, lower, upper)
        frame_gaussian = cv2.GaussianBlur(frame_lab, (5, 5), 2, 2)
        circles = cv2.HoughCircles(frame_gaussian, cv2.HOUGH_GRADIENT, 1, 30 , param1=80, param2=53, minRadius=10, maxRadius=0)
        if circles is not None:
            circles = np.round(circles[0, :]).astype("int")
            cv2.circle(frame, center=(circles[0, 0], circles[0, 1]), radius=circles[0, 2], color=(0, 0, 0), thickness=2)
            cv2.line(output,(circles[0,0],circles[0,1]),(width//2,height//2),(0,255,0),3) 
            showDirection(circles[0,0],circles[0,1],height,width)       
        output_frame = cv2.bitwise_and(frame,frame,mask=frame_lab)
        cv2.imshow("Frame", frame)
        cv2.imshow("Mask", output_frame)
        cv2.imshow("Output", output)
        if key == 27:
            break
# grid()
"""
        draw_leftTop_Grid(frame,height,width)
        draw_leftDown_Grid(frame,height,width)
        draw_rightTop_Grid(frame,height,width)
        draw_rightDown_Grid(frame,height,width)
        """

print('1. Red \n2. Blue \n3. Green \n4. Yellow \n5. Orange')
ch = int(input('Enter : '))
keys = list(colour_ranges.keys())
grid(keys[ch-1])