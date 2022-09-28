checkpoints = {}
def createCheckpoints(sl1,sl2,dl1,dl2):
    global checkpoints
    midpoints = {}
    mid1 = makeCheckpoints(sl1,sl2,dl1,dl2)
    midpoints['mid1'] = mid1
    mid2 = makeCheckpoints(sl1,sl2,midpoints["mid1"][0],midpoints["mid1"][1])
    midpoints['mid2'] = mid2
    mid3 = makeCheckpoints(midpoints["mid1"][0],midpoints["mid1"][1],dl1,dl2)
    midpoints['mid3'] = mid3
    mid4 = makeCheckpoints(sl1,sl2,midpoints["mid2"][0],midpoints["mid2"][1])
    midpoints['mid4'] = mid4
    mid5 = makeCheckpoints(midpoints["mid2"][0],midpoints["mid2"][1],midpoints["mid1"][0],midpoints["mid1"][1])
    midpoints['mid5'] = mid5
    mid6 = makeCheckpoints(midpoints["mid1"][0],midpoints["mid1"][1],midpoints["mid3"][0],midpoints["mid3"][1])
    midpoints['mid6'] = mid6
    mid7 = makeCheckpoints(midpoints["mid3"][0],midpoints["mid3"][1],dl1,dl2)
    midpoints['mid7'] = mid7
    mid8 = makeCheckpoints(sl1,sl2,midpoints["mid4"][0],midpoints["mid4"][1])
    midpoints['mid8'] = mid8
    mid9 = makeCheckpoints(midpoints["mid4"][0],midpoints["mid4"][1],midpoints["mid2"][0],midpoints["mid2"][1])
    midpoints['mid9'] = mid9
    mid10 = makeCheckpoints(midpoints["mid2"][0],midpoints["mid2"][1],midpoints["mid5"][0],midpoints["mid5"][1])
    midpoints['mid10'] = mid10
    mid11 = makeCheckpoints(midpoints["mid5"][0],midpoints["mid5"][1],midpoints["mid1"][0],midpoints["mid1"][1])
    midpoints['mid11'] = mid11
    mid12 = makeCheckpoints(midpoints["mid1"][0],midpoints["mid1"][1],midpoints["mid6"][0],midpoints["mid6"][1])
    midpoints['mid12'] = mid12
    mid13 = makeCheckpoints(midpoints["mid6"][0],midpoints["mid6"][1],midpoints["mid3"][0],midpoints["mid3"][1])
    midpoints['mid13'] = mid13
    mid14 = makeCheckpoints(midpoints["mid3"][0],midpoints["mid3"][1],midpoints["mid7"][0],midpoints["mid7"][1])
    midpoints['mid14'] = mid14
    mid15 = makeCheckpoints(midpoints["mid7"][0],midpoints["mid7"][1],dl1,dl2)
    midpoints['mid15'] = mid15


    checkpoints = sortmidpoints(midpoints)
    findPath(checkpoints)

def findPath(checkpoints):
    while True:
        plane_coordinates =  list(map(float,input("Enter Plane coordinates : ").split()))
        plane_height = float(input("Enter Plane height : "))
        checkpath(plane_coordinates)

def checkpath(plane_coordinates):
    global checkpoints
    lat = list(checkpoints.values())
    counter = 0
    for i in lat:
        if(i[1] > plane_coordinates[1] and i[0] > plane_coordinates[0]):
            print(f'Next Checkpoint is : Checkpoint{counter+1} , Coordinates {i[0],i[1]}')
            break
        counter += 1


def makeCheckpoints(sl1,sl2,dl1,dl2):
    mid_lat = (sl1 + dl1) / 2
    mid_log = (sl2 + dl2) / 2
    return [mid_lat, mid_log]

def sortmidpoints(midpoints):
    checkpoints = {'checkpoint1' : [midpoints['mid8'][0], midpoints['mid8'][1]],    
           'checkpoint2' : [midpoints['mid4'][0], midpoints['mid4'][1]],
           'checkpoint3' : [midpoints['mid9'][0], midpoints['mid9'][1]],
           'checkpoint4' : [midpoints['mid2'][0], midpoints['mid2'][1]],
           'checkpoint5' : [midpoints['mid10'][0], midpoints['mid10'][1]],
           'checkpoint6' : [midpoints['mid5'][0], midpoints['mid5'][1]],
           'checkpoint7' : [midpoints['mid11'][0], midpoints['mid11'][1]],
           'checkpoint8' : [midpoints['mid1'][0], midpoints['mid1'][1]],
           'checkpoint9' : [midpoints['mid12'][0], midpoints['mid12'][1]],
           'checkpoint10' : [midpoints['mid6'][0], midpoints['mid6'][1]],
           'checkpoint11' : [midpoints['mid13'][0], midpoints['mid13'][1]],
           'checkpoint12' : [midpoints['mid3'][0], midpoints['mid3'][1]],
           'checkpoint13' : [midpoints['mid14'][0], midpoints['mid14'][1]],
           'checkpoint14' : [midpoints['mid7'][0], midpoints['mid7'][1]],
           'checkpoint15' : [midpoints['mid15'][0], midpoints['mid15'][1]],
    }
    return checkpoints


source_lat = float(input("Enter Your Latitude : "))
source_log = float(input("Enter Your Longitude : "))

destination_lat = float(input("Enter Destination Latitude : "))
destination_log = float(input("Enter Destination Longitude : "))

createCheckpoints(source_lat, source_log, destination_lat, destination_log)

"""
19.12813570468522, 72.83101128264134
19.152575105680402, 72.84457582236722

3.04

"""