""" servo pyfirmata"""

import pyfirmata
import keyboard
from tkinter import *

def move_servo(angle):
    pin9.write(angle)
    
def main():
    global pin9
    key = 0
    
    board=pyfirmata.Arduino('COM5')

    iter8 = pyfirmata.util.Iterator(board)
    iter8.start()

    pin9 = board.get_pin('d:9:s')
    
    while True:
        rot_angle = float(input('Enter Angle : '))
        move_servo(rot_angle)
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            break
        
    # root = Tk()
    # scale = Scale(root, command = move_servo, to = 180, 
    #               orient = HORIZONTAL, length = 400, label = 'Angle')
    # scale.pack(anchor = CENTER)

    # root.mainloop()

main()