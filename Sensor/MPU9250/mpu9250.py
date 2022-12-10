import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

""" portList = []

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

val = input('Select Port: COM')
print(val)

for x in range(0,len(portList)):
    if portList[x].startswith('COM'+str(val)):
        portVar = 'COM'+str(val)
        print(portVar)
 """

def send_first_Mag(portVar):
    serialInst.baudrate = 115200
    serialInst.port = portVar
    serialInst.open()
    val = []
    while True:
        if serialInst.in_waiting:
            packet = serialInst.readline()
            data = packet.strip()
            res = data.decode('utf-8', 'ignore')
            if(res[0:4] == 'magX' or res[0:4] == 'magY' or res[0:4] == 'magZ'):
                val.append(str(res[6:len(res)]))
            if(len(val)>=3):
                serialInst.close()
                return val
                break

def start_taking_reading(port,x,y,z):
    serialInst.baudrate = 115200
    serialInst.port = port
    serialInst.open()
    while True:
        if serialInst.in_waiting:
            packet = serialInst.readline()
            data = packet.strip()
            res = data.decode('utf-8', 'ignore')
            print(res)


"""
from pyfirmata import Arduino
import time
import pyfirmata
port = 'COM4'
board = Arduino(port)
pin = board.get_pin('a:4:5')

it = pyfirmata.util.Iterator(board)
it.start()

while True:
    analog_value = pin.read()
    print(analog_value)
    time.sleep(0.1)
"""