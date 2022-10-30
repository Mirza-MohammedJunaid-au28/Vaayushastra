import re
import time
speed_det = []

"""
def startAll():
    while True:
        ch = input()
        if():
            pass
"""  

def find_speed():

    while True:
        try:
            speed = int(input('Enter Speed : '))
            speed_det.append(speed)
        except KeyboardInterrupt:
            break

def sum():
    total = 0
    for i in speed_det:
        total += i
    return total

"""
def timer():
    while True:
        try:
            print("Stopwatch has started")
            start_time=time.time()
            while True:
                print("Time elapsed:",round(time.time()-start_time,0),'secs',end='\n')
                time.sleep(1)
        except KeyboardInterrupt:
            print("Timer has stopped")
            end_time=time.time()
            timee = round(end_time-start_time,2)
            break
"""


# result = startAll()
spped = find_speed()
sum_of_speed = sum()
avg_speed = sum_of_speed / len(speed_det)
print('The Average Speed is : ',avg_speed) 
