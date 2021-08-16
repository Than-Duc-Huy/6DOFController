import serial
import roboticstoolbox as rtb

### Initiate communication

import roboticstoolbox as rtb
from spatialmath import *
from Variables import *
import numpy as np


pyplot = rtb.backends.PyPlot.PyPlot()
pyplot.launch()

##### PREPARE THE VARIABLES


### Controller
## Left
CL1 = rtb.robot.RevoluteDH(offset = DHparam[0][1][0], d = DHparam[0][1][1], a = DHparam[0][1][2], alpha = DHparam[0][1][3], qlim = [0,p360])
CL2 = rtb.robot.RevoluteDH(offset = DHparam[0][2][0], d = DHparam[0][2][1], a = DHparam[0][2][2], alpha = DHparam[0][2][3], qlim = [0,p360])
CL3 = rtb.robot.RevoluteDH(offset = DHparam[0][3][0], d = DHparam[0][3][1], a = DHparam[0][3][2], alpha = DHparam[0][3][3], qlim = [0,p360])
CL4 = rtb.robot.RevoluteDH(offset = DHparam[0][4][0], d = DHparam[0][4][1], a = DHparam[0][4][2], alpha = DHparam[0][4][3], qlim = [0,p360])
CL5 = rtb.robot.RevoluteDH(offset = DHparam[0][5][0], d = DHparam[0][5][1], a = DHparam[0][5][2], alpha = DHparam[0][5][3], qlim = [0,p360])
CL6 = rtb.robot.RevoluteDH(offset = DHparam[0][6][0], d = DHparam[0][6][1], a = DHparam[0][6][2], alpha = DHparam[0][6][3], qlim = [0,p360])


CLB = SE3(-0.1,0,0)*SE3.RPY([0,0,0],order = 'xyz')
CLT = SE3(0,0,0)*SE3.RPY([0,0,0],order = 'xyz')
CL = rtb.robot.DHRobot([CL1,CL2,CL3,CL4,CL5,CL6], name = "Controller Left", base = CLB, tool = CLT)
print(CL)

## Right
CR1 = rtb.robot.RevoluteDH(offset = DHparam[1][1][0], d = DHparam[1][1][1], a = DHparam[1][1][2], alpha = DHparam[1][1][3], qlim = [0,p360])
CR2 = rtb.robot.RevoluteDH(offset = DHparam[1][2][0], d = DHparam[1][2][1], a = DHparam[1][2][2], alpha = DHparam[1][2][3], qlim = [0,p360])
CR3 = rtb.robot.RevoluteDH(offset = DHparam[1][3][0], d = DHparam[1][3][1], a = DHparam[1][3][2], alpha = DHparam[1][3][3], qlim = [0,p360])
CR4 = rtb.robot.RevoluteDH(offset = DHparam[1][4][0], d = DHparam[1][4][1], a = DHparam[1][4][2], alpha = DHparam[1][4][3], qlim = [0,p360])
CR5 = rtb.robot.RevoluteDH(offset = DHparam[1][5][0], d = DHparam[1][5][1], a = DHparam[1][5][2], alpha = DHparam[1][5][3], qlim = [0,p360])
CR6 = rtb.robot.RevoluteDH(offset = DHparam[1][6][0], d = DHparam[1][6][1], a = DHparam[1][6][2], alpha = DHparam[1][6][3], qlim = [0,p360])

CRB = SE3(0.1,0,0)*SE3.RPY([0,0,0],order = 'xyz')
CRT = SE3(0,0,0)*SE3.RPY([0,0,0],order = 'xyz')
CR = rtb.robot.DHRobot([CR1,CR2,CR3,CR4,CR5,CR6], name = "Controller Right", base = CRB, tool = CRT)
print(CR)

### Output
## Left
OL1 = rtb.robot.RevoluteDH(offset = DHparam[2][1][0], d = DHparam[2][1][1], a = DHparam[2][1][2], alpha = DHparam[2][1][3], qlim = [0,p360])
OL2 = rtb.robot.RevoluteDH(offset = DHparam[2][2][0], d = DHparam[2][2][1], a = DHparam[2][2][2], alpha = DHparam[2][2][3], qlim = [0,p360])
OL3 = rtb.robot.RevoluteDH(offset = DHparam[2][3][0], d = DHparam[2][3][1], a = DHparam[2][3][2], alpha = DHparam[2][3][3], qlim = [0,p360])
OL4 = rtb.robot.RevoluteDH(offset = DHparam[2][4][0], d = DHparam[2][4][1], a = DHparam[2][4][2], alpha = DHparam[2][4][3], qlim = [0,p360])
OL5 = rtb.robot.RevoluteDH(offset = DHparam[2][5][0], d = DHparam[2][5][1], a = DHparam[2][5][2], alpha = DHparam[2][5][3], qlim = [0,p360])
OL6 = rtb.robot.RevoluteDH(offset = DHparam[2][6][0], d = DHparam[2][6][1], a = DHparam[2][6][2], alpha = DHparam[2][6][3], qlim = [0,p360])

OLB = SE3(-OB,0,0)*SE3.Rz(p90)
OLT = SE3(0,0,0)*SE3.RPY([0,0,0],order = 'xyz')
OL = rtb.robot.DHRobot([OL1,OL2,OL3,OL4,OL5,OL6], name = "Output Left", base = OLB, tool = OLT)
print(OL)


## Right
OR1 = rtb.robot.RevoluteDH(offset = DHparam[3][1][0], d = DHparam[3][1][1], a = DHparam[3][1][2], alpha = DHparam[3][1][3], qlim = [0,p360])
OR2 = rtb.robot.RevoluteDH(offset = DHparam[3][2][0], d = DHparam[3][2][1], a = DHparam[3][2][2], alpha = DHparam[3][2][3], qlim = [0,p360])
OR3 = rtb.robot.RevoluteDH(offset = DHparam[3][3][0], d = DHparam[3][3][1], a = DHparam[3][3][2], alpha = DHparam[3][3][3], qlim = [0,p360])
OR4 = rtb.robot.RevoluteDH(offset = DHparam[3][4][0], d = DHparam[3][4][1], a = DHparam[3][4][2], alpha = DHparam[3][4][3], qlim = [0,p360])
OR5 = rtb.robot.RevoluteDH(offset = DHparam[3][5][0], d = DHparam[3][5][1], a = DHparam[3][5][2], alpha = DHparam[3][5][3], qlim = [0,p360])
OR6 = rtb.robot.RevoluteDH(offset = DHparam[3][6][0], d = DHparam[3][6][1], a = DHparam[3][6][2], alpha = DHparam[3][6][3], qlim = [0,p360])

ORB = SE3(OB,0,0)*SE3.Rz(p90)
ORT = SE3(0,0,0)*SE3.RPY([0,0,0],order = 'xyz')
OR = rtb.robot.DHRobot([OR1,OR2,OR3,OR4,OR5,OR6], name = "Output Right", base = ORB, tool = ORT)
print(OR)



pyplot.add(OL)
pyplot.add(OR)
pyplot.ax.view_init(26,-63) #Elevation, Azimuth
pyplot.ax.set_xlim3d(-0.3,0.3)
pyplot.ax.set_ylim3d(-0.3,0.3)
pyplot.ax.set_zlim3d(-0.3,0.3)


pyplot.step()
pyplot.hold()


