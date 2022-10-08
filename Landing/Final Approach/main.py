import checkpoints as cp
checkpoints = []
copied_checkpoint = []
def checkPath(checkpointss):
    global copied_checkpoint,checkpoints
    copied_checkpoint = checkpointss
    while True:
        plane_coordinates =  list(map(float,input("Enter Plane coordinates : ").split()))
        plane_altitude = float(input("Enter Altitude : "))
        curved_altitude = cp.findaltitude(plane_coordinates[0],plane_coordinates[1],destination_lat,destination_log)
        checkrange(plane_coordinates)
        print('Check Point Altitude is : ',curved_altitude)
        counter = 0

        for i in range(1,len(copied_checkpoint)):
            dist_lat = abs(plane_coordinates[0] - checkpointss[i][0])
            dist_log = abs(plane_coordinates[1] - checkpointss[i][1])
            dis_alt = abs(curved_altitude - plane_altitude)
            
            if(dist_lat < 6):
                print('Dist_lat ',dist_lat)
                if(plane_coordinates[0] == checkpoints[i][0] and plane_coordinates[1] == checkpoints[i][1] and plane_altitude == curved_altitude):
                    print(f'Crossed the Checkpoint{i} : {i}')
                    checkpointss.pop(i)
                    break

                elif(plane_coordinates[0] == checkpoints[i][0] and plane_coordinates[1] == checkpoints[i][1] and plane_altitude > curved_altitude):
                    print(f'Move Down : {dis_alt}')
                    checkpointss.pop(i)
                    break
                    
                elif(plane_coordinates[0] == checkpoints[i][0] and plane_coordinates[1] == checkpoints[i][1] and plane_altitude < curved_altitude):
                    print(f'Move Up : {dis_alt}')
                    checkpointss.pop(i)
                    break
                
                elif(plane_coordinates[0] > checkpoints[i][0] and plane_coordinates[1] == checkpoints[i][1] and plane_altitude == curved_altitude):
                    print(f'Move Left  : {dist_lat}')
                    checkpointss.pop(i)
                    break
                    
                elif(plane_coordinates[0] < checkpoints[i][0] and plane_coordinates[1] == checkpoints[i][1] and plane_altitude == curved_altitude):
                    print(f'Move Right  : {dist_lat}')
                    # checkpointss.pop(i)
                    break
                    
                elif(plane_coordinates[0] > checkpoints[i][0] and plane_coordinates[1] == checkpoints[i][1] and plane_altitude > curved_altitude):
                    print(f'Move Down  : {dis_alt} & Move Right : {dist_lat}')
                    checkpointss.pop(i)
                    break
                    
                elif(plane_coordinates[0] > checkpoints[i][0] and plane_coordinates[1] == checkpoints[i][1] and plane_altitude < curved_altitude):
                    print(f'Move Up  : {dis_alt} & Move Right : {dist_lat}')
                    checkpointss.pop(i)
                    break
                    
                elif(plane_coordinates[0] < checkpoints[i][0] and plane_coordinates[1] == checkpoints[i][1] and plane_altitude > curved_altitude):
                    print(f'Move Down  : {dis_alt} & Move Left : {dist_lat}')
                    # checkpointss.pop(i)
                    break
                    
                elif(plane_coordinates[0] < checkpoints[i][0] and plane_coordinates[1] == checkpoints[i][1] and plane_altitude < curved_altitude):    
                    print(f'Move Up  : {dis_alt} & Move Left : {dist_lat}')
                    # checkpointss.pop(i)
                    break
                    
                elif(plane_coordinates[0] > checkpoints[i][0] and plane_coordinates[1] > checkpoints[i][1] and plane_altitude == curved_altitude):
                    print(f'Move Left  : {dist_lat} & Move Straight : {dist_log}')
                    checkpointss.pop(i)
                    break
                    
                elif(plane_coordinates[0] > checkpoints[i][0] and plane_coordinates[1] < checkpoints[i][1] and plane_altitude == curved_altitude):
                        #create New Route
                    print(f'Move Left  : {dist_lat} & Plane is Back to Much : {dist_log}')
                    checkpointss.pop(i)
                    break

                elif(plane_coordinates[0] < checkpoints[i][0] and plane_coordinates[1] > checkpoints[i][1] and plane_altitude == curved_altitude):
                    print(f'Move Right  : {dist_lat} & Plane has Across the Checkpoint form Left Side : {dist_log}')
                    # checkpointss.pop(i)
                    break

                elif(plane_coordinates[0] < checkpoints[i][0] and plane_coordinates[1] < checkpoints[i][1] and plane_altitude == curved_altitude):
                    print(f'Move Right  : {dist_lat} & Plane is Behind the Checkpoint form Left Side : {dist_log}')
                    # checkpointss.pop(i)
                    break

                elif(plane_coordinates[0] > checkpoints[i][0] and plane_coordinates[1] > checkpoints[i][1] and plane_altitude > curved_altitude):
                    print(f'Move Left  : {dist_lat} & Plane has Acros the Checkpoint form Right Side : {dist_log} & Move Down : {dis_alt}')
                    checkpointss.pop(i)
                    break

                elif(plane_coordinates[0] > checkpoints[i][0] and plane_coordinates[1] > checkpoints[i][1] and plane_altitude < curved_altitude):
                    print(f'Move Left  : {dist_lat} & Plane has Acros the Checkpoint form Right Side : {dist_log} & Move Up : {dis_alt}')
                    checkpointss.pop(i)
                    break

                elif(plane_coordinates[0] > checkpoints[i][0] and plane_coordinates[1] < checkpoints[i][1] and plane_altitude > curved_altitude):
                    print(f'Move Left  : {dist_lat} & Plane is behind the Checkpoint form Right Side : {dist_log} & Move Down : {dis_alt}')
                    checkpointss.pop(i)
                    break

                elif(plane_coordinates[0] > checkpoints[i][0] and plane_coordinates[1] < checkpoints[i][1] and plane_altitude < curved_altitude):
                    print(f'Move Left  : {dist_lat} & Plane is behind the Checkpoint form Right Side : {dist_log} & Move Up : {dis_alt}')
                    checkpointss.pop(i)
                    break

                elif(plane_coordinates[0] < checkpoints[i][0] and plane_coordinates[1] > checkpoints[i][1] and plane_altitude > curved_altitude):
                    print(f'Move Right  : {dist_lat} & Plane has Acros the Checkpoint form Left Side : {dist_log} & Move Down : {dis_alt}')
                    # checkpointss.pop(i)
                    break

                elif(plane_coordinates[0] < checkpoints[i][0] and plane_coordinates[1] > checkpoints[i][1] and plane_altitude < curved_altitude):
                    print(f'Move Right  : {dist_lat} & Plane has Acros the Checkpoint form Left Side : {dist_log} & Move Up : {dis_alt}')
                    # checkpointss.pop(i)
                    break

                elif(plane_coordinates[0] < checkpoints[i][0] and plane_coordinates[1] < checkpoints[i][1] and plane_altitude > curved_altitude):
                    print(f'Move Right  : {dist_lat} & Plane is behind the Checkpoint form Left Side : {dist_log} & Move Down : {dis_alt}')
                    # checkpointss.pop(i)
                    break

                elif(plane_coordinates[0] < checkpoints[i][0] and plane_coordinates[1] < checkpoints[i][1] and plane_altitude < curved_altitude):
                    print(f'Move Right  : {dist_lat} & Plane is behind the Checkpoint form Left Side : {dist_log} & Move Up : {dis_alt}')
                    # checkpointss.pop(i)
                    break
            
            else:
                print('New Route')
                checkpoints = cp.create_checkpoint(plane_coordinates[0],plane_coordinates[1],destination_lat, destination_log, plane_length)
                print(checkpoints)
                checkPath(checkpoints)
            

def checkrange(plane_coordinates):
    global checkpoints , copied_checkpoint
    counter = 0
    for i in checkpoints:
        if(i[1] >= plane_coordinates[1] and i[0] >= plane_coordinates[0]):
            print(f'Next Checkpoint is : Checkpoint{copied_checkpoint.index(i) + 1} , Coordinates {i[0],i[1]}')
            break
        counter += 1

source_lat = 0
source_log = 0
destination_lat = 200
destination_log = 200
plane_length = 2

checkpoints = cp.create_checkpoint(source_lat, source_log,destination_lat, destination_log, plane_length)
checkPath(checkpoints)