import serial
import time
import matplotlib.pyplot as plt
import concurrent.futures
import multiprocessing
from Intermediate import *


def inversekine(Controller, Output):
    Output.q = (Output.ikine_LM(Controller.fkine(Controller.q), q0=Output.q)).q


# =================== Variables
first = 1
FTDI = False

# ==================================== Serial Initialize
ESP32 = serial.Serial('COM5')
print(ESP32.name)
print(ESP32.is_open)
print(ESP32)
time.sleep(1)
ESP32.flushInput()
try:
    Ard = serial.Serial('COM17', 115200)
    print(Ard.name)
    print(Ard.is_open)
    print(Ard)
    time.sleep(1)
    Ard.flushOutput()
    FTDI = True
except:
    print("No FTDI")


# ===============================================================VISUALIZATION

pyplot.ax.view_init(90, -0)  # Elevation, Azimuth

pyplot.add(OL)
pyplot.add(OR)
pyplot.add(CL)
pyplot.add(CR)
pyplot.ax.set_xlim3d(-2, 2)
pyplot.ax.set_ylim3d(-2, 2)
pyplot.ax.set_zlim3d(-2, 2)


prevparsed = np.zeros((1, 16))
parsed = prevparsed
# ============================== REF
TLref = CL.fkine([0, 0, 0, 0, 0, 0]).t
TRref = CR.fkine([0, 0, 0, 0, 0, 0]).t
OLref = OL.fkine([0, 0, 0, 0, 0, 0])
ORref = OR.fkine([0, 0, 0, 0, 0, 0])

count = 0
# ================================================================ LOOP
while(True):
    start = time.perf_counter()
    incoming_data = ESP32.readline()
    decoded = incoming_data.decode().strip('\r\n')
    parseSTR = decoded.split(",")
    if(len(parseSTR) != 16):
        continue
    else:
        # ============================ READ DATA
        try:
            parsed = [float(val) for val in parseSTR]
        except:
            parsed = prevparsed
        else:
            parsed[4:16] = np.array(parsed[4:16]) * (2*np.pi) / 4096.0
            CL.q = parsed[4:10]
            CR.q = parsed[10:16]
            PLmeasured = CL.fkine(CL.q)
            PRmeasured = CR.fkine(CR.q)
            print(parsed[0:4])

        # ============================= REFERENCE TOGGLE
        if parsed[3] == 1:  # If the toggle is on
            if (first == 1):
                first = 0
            # Change input reference
            TLref = PLmeasured.t
            TRref = PRmeasured.t
            # Change output reference
            ORref = OR.fkine(OR.q)
            OLref = OL.fkine(OL.q)
        else:
            #Delta in Input
            TLdelta = PLmeasured.t - TLref
            TRdelta = PRmeasured.t - TRref

            #Delta in Output
            OLdelta = TLdelta * ScalingFactor
            ORdelta = TRdelta * ScalingFactor

            #Pose in Output
            PLreconstruct = SE3(OLref.t + OLdelta)*SE3(SO3(PLmeasured.R))
            PRreconstruct = SE3(ORref.t + ORdelta)*SE3(SO3(PRmeasured.R))

            # Inverse Kinematics to find joints
            if (first == 0):
                OR.q = (OR.ikine_LM(PRreconstruct, q0=OR.q)).q
                OL.q = (OL.ikine_LM(PLreconstruct, q0=OL.q)).q

            # # Sending
            if (FTDI == True):
                for i in range(4):  # Toggle
                    Ard.write(bytes(str(parsed[i]), 'ascii'))
                    Ard.write(b',')
                for i in range(6):
                    Ard.write(bytes(str(OL.q[i]*180/np.pi), 'ascii'))
                    Ard.write(b',')
                for i in range(6):
                    Ard.write(bytes(str(OR.q[i]*180/np.pi), 'ascii'))
                    if (i == 6):
                        continue
                    else:
                        Ard.write(b',')
                Ard.write(b'\n')

        # ============================== Troubleshooting
        # count += 1
        # if count % 5 == 0:
        #     print("Posed measured")
        #     print(PLmeasured)
        #     print("Translation Reference: ", TLref)
        #     print("Translation Input Delta: ", TLdelta)
        #     print("Translation Output Delta: ", OLdelta)
        #     print("Output Reference")
        #     print(OLref)
        #     print("Output Pose")
        #     print(PLreconstruct)

        pyplot.step()

    ESP32.flushInput()
    prevparsed = parsed
    done = time.perf_counter()
    print(f"Loop: {round(done-start,2)}s")
    # End of Loop
