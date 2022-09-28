checkpoints = {'checkpoint1': [6.25, 6.25], 'checkpoint2': [12.5, 12.5], 'checkpoint3': [18.75, 18.75], 'checkpoint4': [25.0, 25.0], 'checkpoint5': [31.25, 31.25], 'checkpoint6': [37.5, 37.5], 'checkpoint7': [43.75, 43.75], 'checkpoint8': [50.0, 50.0], 'checkpoint9': [56.25, 56.25], 'checkpoint10': [62.5, 62.5], 'checkpoint11': [68.75, 68.75], 'checkpoint12': [75.0, 75.0], 'checkpoint13': [81.25, 81.25], 'checkpoint14': [87.5, 87.5], 'checkpoint15': [93.75, 93.75]}

def checkpath(checkpoints):
    plane_coordinates=[38,89]
    lat = list(checkpoints.values())
    all_lat = []
    all_log = []
    counter = 0
    for i in lat:
        if(i[1] > plane_coordinates[1] and i[0] > plane_coordinates[0]):
            print(f'Next Checkpoint is : Checkpoint{counter+1} , Coordinates {i[0],i[1]}')
        counter += 1
    
# checkpath(checkpoints)

def create_subCheckpoints(s,d):
    sub_check1 = makeCheckpoints(s[0],s[1],d[0],d[1])
    print(sub_check1)

def makeCheckpoints(sl1,sl2,dl1,dl2):
    mid_lat = (sl1 + dl1) / 2
    mid_log = (sl2 + dl2) / 2
    return [mid_lat, mid_log]

create_subCheckpoints([50,50],[56.25,56.25])
    