import mpu9250 as mpu

port = int(input('Port No : '))
port = 'COM'+str(port)
value = mpu.send_first_Mag(port)
x = float(value[0])
y = float(value[1])
z = float(value[2])
print(x,y,z)


def start_taking_reading():
    mpu.start_taking_reading(port,x,y,z)

start_taking_reading()