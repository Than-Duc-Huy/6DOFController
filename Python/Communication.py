import serial
import time
import matplotlib.pyplot as plt

from Intermediate import *
# Serial Initialize
ESP32 = serial.Serial('COM15')
print(ESP32.name)
print(ESP32.is_open)
print(ESP32)
time.sleep(1)
ESP32.flushInput()

Ard = serial.Serial('COM9')
print(Ard.name)
print(Ard.is_open)
print(Ard)
time.sleep(1)
Ard.flushOutput()

# Visualization


pyplot.ax.view_init(26, -63)  # Elevation, Azimuth

# pyplot.add(OL)
# pyplot.add(OR)
# pyplot.ax.set_xlim3d(-0.3, 0.3)
# pyplot.ax.set_ylim3d(-0.3, 0.3)
# pyplot.ax.set_zlim3d(-0.3, 0.3)


pyplot.add(CL)
pyplot.add(CR)
pyplot.ax.set_xlim3d(-2, 2)
pyplot.ax.set_ylim3d(-2, 2)
pyplot.ax.set_zlim3d(-2, 2)

while(True):
    start = time.perf_counter()
    incoming_data = ESP32.readline()
    decoded = incoming_data.decode().strip('\r\n')

    parseSTR = decoded.split(",")
    print(decoded)
    # if len(decoded.split())
    if(len(parseSTR) != 16):
        continue
    else:
        try:
            parsed = [float(val) for val in parseSTR]
        except:
            parsed = prevparsed
        parsed = np.array(parsed) * (2*np.pi) / 4096.0
        CL.q = parsed[4:10]
        CR.q = parsed[10:16]
        JointL = OL.ikine_LM(CL.fkine(CL.q), [1, 1, 1, 0, 0, 0])
        JointR = OR.ikine_LM(CR.fkine(CR.q), [1, 1, 1, 0, 0, 0])

        # Sending
        for i in range(4):  # Toggle
            Ard.write(bytes(str(parsed[i]), 'ascii'))
            Ard.write(b',')
        for i in range(6):
            Ard.write(bytes(str(JointL.q[i]), 'ascii'))
            Ard.write(b',')
        for i in range(6):
            Ard.write(bytes(str(JointR.q[i]), 'ascii'))
            if (i == 6):
                continue
            else:
                Ard.write(b',')
        Ard.write(b'\n')
        OL.q = JointL.q
        OR.q = JointR.q
        # pyplot.step()
        prevparsed = parsed

    ESP32.flushInput()
    time.sleep(0.001)
    done = time.perfcounter()
    print(f"Loop: {done-start}s")
    # Ard.flushOutput()
