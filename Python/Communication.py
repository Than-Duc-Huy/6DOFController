import serial
import time
import matplotlib.pyplot as plt
import concurrent.futures
import multiprocessing


def inversekine(Controller, Output):
    Output.q = (Output.ikine_LM(Controller.fkine(Controller.q), q0=Output.q)).q


if __name__ == '__main__':
    from Intermediate import *
    # ==================================== Serial Initialize
    ESP32 = serial.Serial('COM15')
    print(ESP32.name)
    print(ESP32.is_open)
    print(ESP32)
    time.sleep(1)
    ESP32.flushInput()

    # Ard = serial.Serial('COM9')
    # print(Ard.name)
    # print(Ard.is_open)
    # print(Ard)
    # time.sleep(1)
    # Ard.flushOutput()
    # ===============================================================VISUALIZATION

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
    # ================================================================ LOOP
    prevparsed = np.zeros((1, 16))
    parsed = prevparsed

    while(True):
        start = time.perf_counter()
        incoming_data = ESP32.readline()
        decoded = incoming_data.decode().strip('\r\n')

        parseSTR = decoded.split(",")
        # print(decoded)
        if(len(parseSTR) != 16):
            continue
        else:
            try:
                parsed = [float(val) for val in parseSTR]
            except:
                parsed = prevparsed
            else:
                parsed = np.array(parsed) * (2*np.pi) / 4096.0
                CL.q = parsed[4:10]
                CR.q = parsed[10:16]

            inversekine(CL, OL)
            inversekine(CR, OR)

           # with concurrent.futures.ProcessPoolExecutor() as executor:
            #     executor.submit(inversekine, CL, OL)
            #     executor.submit(inversekine, CR, OR)

            # Sending
            # for i in range(4):  # Toggle
            #     Ard.write(bytes(str(parsed[i]), 'ascii'))
            #     Ard.write(b',')
            # for i in range(6):
            #     Ard.write(bytes(str(JointL.q[i]), 'ascii'))
            #     Ard.write(b',')
            # for i in range(6):
            #     Ard.write(bytes(str(JointR.q[i]), 'ascii'))
            #     if (i == 6):
            #         continue
            #     else:
            #         Ard.write(b',')
            # Ard.write(b'\n')

            pyplot.step()

        ESP32.flushInput()
        prevparsed = parsed
        print(prevparsed.round(2))
        done = time.perf_counter()
        print(f"Loop: {round(done-start,2)}s")
        # End of Loop
