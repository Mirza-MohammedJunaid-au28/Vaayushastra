""" checkpoints = {'checkpoint1': [6.25, 6.25], 'checkpoint2': [12.5, 12.5], 'checkpoint3': [18.75, 18.75], 'checkpoint4': [25.0, 25.0], 'checkpoint5': [31.25, 31.25], 'checkpoint6': [37.5, 37.5], 'checkpoint7': [43.75, 43.75], 'checkpoint8': [50.0, 50.0], 'checkpoint9': [56.25, 56.25], 'checkpoint10': [62.5, 62.5], 'checkpoint11': [68.75, 68.75], 'checkpoint12': [75.0, 75.0], 'checkpoint13': [81.25, 81.25], 'checkpoint14': [87.5, 87.5], 'checkpoint15': [93.75, 93.75]}

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
    mid_subcheckpoint = {}
    sub_check1 = makeCheckpoints(s[0],s[1],d[0],d[1])
    mid_subcheckpoint['sub_check1'] = sub_check1
    sub_check2 = makeCheckpoints(s[0],s[1],sub_check1[0],sub_check1[1])
    mid_subcheckpoint['sub_check2'] = sub_check2
    sub_check3 = makeCheckpoints(sub_check1[0],sub_check1[1],d[0],d[1])
    mid_subcheckpoint['sub_check3'] = sub_check3
    sub_check4 = makeCheckpoints(s[0],s[1],sub_check2[0],sub_check2[1])
    mid_subcheckpoint['sub_check4'] = sub_check4
    sub_check5 = makeCheckpoints(sub_check2[0],sub_check2[1],sub_check1[0],sub_check1[1])
    mid_subcheckpoint['sub_check5'] = sub_check5
    sub_check6 = makeCheckpoints(sub_check1[0],sub_check1[1],sub_check3[0],sub_check3[1])
    mid_subcheckpoint['sub_check6'] = sub_check6
    sub_check7 = makeCheckpoints(sub_check3[0],sub_check3[1],d[0],d[1])
    mid_subcheckpoint['sub_check7'] = sub_check7

    sub_checkpoints = sort_subCheckpoints(mid_subcheckpoint)
    print(sub_checkpoints)

def sort_subCheckpoints(mid_subcheckpoint):
    sub_checkpoints = {'sub_checkpoints1': [mid_subcheckpoint['sub_check4'][0],mid_subcheckpoint['sub_check4'][1]],
                        'sub_checkpoints2': [mid_subcheckpoint['sub_check2'][0],mid_subcheckpoint['sub_check2'][1]],
                        'sub_checkpoints3': [mid_subcheckpoint['sub_check5'][0],mid_subcheckpoint['sub_check5'][1]],
                        'sub_checkpoints4': [mid_subcheckpoint['sub_check1'][0], mid_subcheckpoint['sub_check1'][1]],
                        'sub_checkpoints5': [mid_subcheckpoint['sub_check6'][0], mid_subcheckpoint['sub_check6'][1]],
                        'sub_checkpoints6': [mid_subcheckpoint['sub_check3'][0], mid_subcheckpoint['sub_check3'][1]],
                        'sub_checkpoints7': [mid_subcheckpoint['sub_check7'][0], mid_subcheckpoint['sub_check7'][1]],
                    }
    return sub_checkpoints

def makeCheckpoints(sl1,sl2,dl1,dl2):
    mid_lat = (sl1 + dl1) / 2
    mid_log = (sl2 + dl2) / 2
    return [mid_lat, mid_log]

create_subCheckpoints([10,10],[20,20])
# create_subCheckpoints([19.29343866919632, 72.85671708304383],[19.293593076385275, 72.85618538149996])

     """
"""
[19.29343866919632, 72.85671708304383]
[19.293593076385275, 72.85618538149996]
[19.29374748357423, 72.85565367995606]
[19.29390189076318, 72.85512197841217]
[19.29405629795213, 72.85459027686828]
[19.294210705141086, 72.85405857532439]
[19.29436511233004, 72.8535268737805]
[19.294519519518992, 72.8529951722366]
[19.294673926707944, 72.85246347069271]
[19.2948283338969, 72.85193176914882]
[19.294982741085853, 72.85140006760493]
[19.295137148274804, 72.85086836606104]
[19.295291555463756, 72.85033666451714]
[19.29544596265271, 72.84980496297325]
[19.295600369841665, 72.84927326142936]
"""

import checkpoints as cp

checkpoints = {}
source_lat = 0
destination_log = 0
destination_lat = 0
source_log = 0 





def findPath(checkpoints):
    while True:
        plane_coordinates =  list(map(float,input("Enter Plane coordinates : ").split()))
        rangee = checkrange(plane_coordinates)
        print(rangee)
        for k,v in rangee.items(): 
            print(k,v)

def checkrange(plane_coordinates):
    global checkpoints
    lat = list(checkpoints.values())
    counter = 0
    for i in lat:
        if(i[1] >= plane_coordinates[1] and i[0] >= plane_coordinates[0]):
            print(f'Next Checkpoint is : Checkpoint{counter+1} , Coordinates {i[0],i[1]}')
            sub_checkpoints = cp.create_subCheckpoints(lat[counter-1],i)
            return sub_checkpoints
            break
        counter += 1





source_lat = float(input("Enter Your Latitude : "))
source_log = float(input("Enter Your Longitude : "))

destination_lat = float(input("Enter Destination Latitude : "))
destination_log = float(input("Enter Destination Longitude : "))

midpoints = cp.createCheckpoints(source_lat, source_log, destination_lat, destination_log)
checkpoints = cp.sortmidpoints(midpoints,source_lat, source_log, destination_lat, destination_log)
findPath(checkpoints)

"""
19.12813570468522, 72.83101128264134
19.152575105680402, 72.84457582236722

3.04

"""

"""
19.29328426200737, 72.85724878458772
19.295754777030616, 72.84874155988547
"""