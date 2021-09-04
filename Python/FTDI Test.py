import serial
import time

message = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
parsed = [0, 1, 0, 1]
OL = [200, 200, 300, 400, 500, 600]
OR = [200, 300, 400, 500, 600, 500]
ard = serial.Serial('COM17', 115200)
print(ard)
count = 0
while True:
    for i in range(4):  # Toggle
        ard.write(bytes(str(parsed[i]), 'ascii'))
        ard.write(b',')
    for j in range(6):
        ard.write(bytes(str(OL[j]), 'ascii'))
        ard.write(b',')
    for k in range(6):
        ard.write(bytes(str(OR[k]), 'ascii'))
        if (k == 5):
            continue
        else:
            ard.write(b',')
        time.sleep(0.000001)
    ard.write(b'\n')
