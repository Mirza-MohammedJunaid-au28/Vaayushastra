import math
ckpts = []

def giveMeCheckpoints(altittude,distance,speed):

    # drp_h = int(input("enter the hieght at which the plane was dropped: "))
    drp_h = altittude
    # calc_x = int(input("enter the calculated horizontal distance"))
    calc_x = distance
    slp = drp_h/calc_x
    incln = math.atan(slp)
    incln = incln*(180/math.pi)
    # a_speed = int(input("Enter the speed at which the pada is dropped"))
    a_speed = speed
    as_y = -1*(a_speed*math.sin(a_speed))
    as_x = a_speed*math.cos(a_speed)
    c_alt = drp_h
    c_dst = calc_x
    t = 1
    while(True):
        ckpts.append(round(c_alt))
        if ((t * as_y)<0):
            c_alt = drp_h + (t * as_y)
        else:
            c_alt = drp_h - (t * as_y)
        if(c_alt<5):
            break
        t = t+1
    
    return ckpts

# giveMeCheckpoints()