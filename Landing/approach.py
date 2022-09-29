from math import ceil, sin, cos, sqrt, atan2, radians
def findDistance(sl1,sl2,dl1,dl2):

# approximate radius of earth in km
    R = 6373.0

    lat1 = radians(sl1)
    lon1 = radians(sl2)
    lat2 = radians(dl1)
    lon2 = radians(dl2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c * 1000
    print(ceil(distance))
    print("Result:", distance)


source_lat = float(input("Enter Your Latitude : "))
source_log = float(input("Enter Your Longitude : "))

destination_lat = float(input("Enter Destination Latitude : "))
destination_log = float(input("Enter Destination Longitude : "))

distance = findDistance(source_lat, source_log, destination_lat, destination_log)

# createCheckpoints(source_lat, source_log, destination_lat, destination_log)

"""
19.29328426200737, 72.85724878458772
19.295754777030616, 72.84874155988547
"""