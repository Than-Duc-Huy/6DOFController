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

# Ard = serial.Serial('')
# print(Ard.name)
# print(Ard.is_open)
# print(Ard)
# time.sleep(1)
# Ard.flushOutput()

# Visualization

pyplot.add(CL)
pyplot.add(CR)
# pyplot.add(OL)
# pyplot.add(OR)

pyplot.ax.view_init(26, -63)  # Elevation, Azimuth
pyplot.ax.set_xlim3d(-0.3, 0.3)
pyplot.ax.set_ylim3d(-0.3, 0.3)
pyplot.ax.set_zlim3d(-0.3, 0.3)


while(True):
    try:
        incoming_data = ESP32.readline()
        decoded = incoming_data.decode().strip('\r\n')

        print(decoded)
        parsed = [float(val) for val in decoded.split(',')]
        parsed = np.array(parsed) * (2*np.pi) / 4096.0
        CL.q = parsed[4:10]
        CR.q = parsed[10:16]
        JointL = OL.ikine_LM(CL.fkine(CL.q))
        JointR = OR.ikine_LM(CR.fkine(CR.q))

        # Sending
        # for i in range(4): # Toggle
        # 	Ard.write(bytes(parsed[i],'ascii'))
        # 	Ard.write(b',')
        # for i in range(6):
        # 	Ard.write(bytes(JointL.q[i],'ascii'))
        # 	Ard.write(b',')
        # for i in range(6):
        # 	Ard.write(bytes(JointR.q[i],'ascii'))
        # 	Ard.write(b',')

        # OL.q = JointL.q
        # OR.q = JointR.q
        pyplot.step()
    except:
        continue
    finally:
        ESP32.flushInput()
        # Ard.flushOutput()
