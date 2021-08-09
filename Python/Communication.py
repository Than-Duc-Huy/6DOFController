import serial
import time

ser = serial.Serial('COM15')
print(ser.name)
print(ser.is_open)
print(ser)
ser.flush()
while(True):
	x = ser.readline()
	print(x.decode().strip('\r\n'))