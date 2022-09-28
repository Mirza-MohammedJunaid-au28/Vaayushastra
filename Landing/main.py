def findPath(source_lat, source_log, destination_lat, destination_log):
    
    while True:
        # print(source_lat, source_log)
        if(source_log > destination_log):
            print('Taking Left')
            source_log -= 1
            print("Source Latitude: " + str(source_lat) , ", Source Longitude: " + str(source_log))
        elif(destination_log > source_log):
            print('Taking Right')
            source_log += 1
            print("Source Latitude: " + str(source_lat) , ", Source Longitude: " + str(source_log))
        elif(source_log == destination_log):
            if(source_lat > destination_lat):
                print('Coming Back')
                source_lat -= 1
                print("Source Latitude: " + str(source_lat) , ", Source Longitude: " + str(source_log))
            elif(destination_lat > source_lat):
                print('Going Straight')
                source_lat += 1
                print("Source Latitude: " + str(source_lat) , ", Source Longitude: " + str(source_log))
            elif(source_lat == destination_lat):
                print('You Have Reached Destination')
                break

source_lat = float(input("Enter Your Latitude : "))
source_log = float(input("Enter Your Longitude : "))

destination_lat = float(input("Enter Destination Latitude : "))
destination_log = float(input("Enter Destination Longitude : "))

findPath(source_lat, source_log, destination_lat, destination_log)

"""
sla = 50
slo = 80
dla = 10
dlog = 30

"""

"""
22.010242847157645, 24.988796628301607
22.010242847157645, 29.590226048821116
"""