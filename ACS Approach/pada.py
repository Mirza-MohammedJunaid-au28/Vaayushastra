import utils as utils
import time
from threading import Thread

reached = False

class Pada():
    def __init__(self):
        pass
    
    def pada_path(self,checkpoints):
        global reached
        idx = 0
        pada_altitude = [45,41,35,32,26,22,16,11,6]
        # [45, 40, 36, 31, 27, 22, 17, 13, 8]
        while(reached != True):
            # alt = int(input('Enter Pada Altitude : '))
            alt = pada_altitude[idx]
            if alt > 6 and idx <= len(pada_altitude)-1 :
                print(f'Pada Altitude {alt} & Checkpoint Altitude {checkpoints[idx]}')
                if alt > checkpoints[idx] : 
                    print('Move Down')
                elif alt < checkpoints[idx] : 
                    print('Move Up')
                elif alt == checkpoints[idx]:
                    print('Good go to Next Checkpoint')
            else:
                reached = True
                print('Stop Motor')  
            time.sleep(1)
            idx += 1

class Pada_Operatiosns():
    def __init__(self,altitude,distance,speed):
        self.altitude = altitude
        self.distance = distance
        self.speed = speed
        self.navigations()
    
    def navigations(self):
        checkpoints = utils.giveMeCheckpoints(self.altitude,self.distance,self.speed)
        print(checkpoints)
        pada_obj = Pada()
        pada_obj.pada_path(checkpoints)
        # pada_path = Thread(target = pada_obj.colour_det , args=('RED',))
        # calculate_speed = Thread(target = firstRound_obj.calc)
        # x = pada_path.start()
        # y = calculate_speed.start()
