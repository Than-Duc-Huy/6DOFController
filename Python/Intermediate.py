import serial
import roboticstoolbox as rtb

### Initiate communication

import roboticstoolbox as rtb
from spatialmath import *
import numpy as np

### Controller
## Left
CL1 = rtb.robot.RevoluteDH(d = 0, a = 0, alpha = 0, offset = 0, qlim = [0,2*np.pi])
CL2 = rtb.robot.RevoluteDH(d = 0, a = 0, alpha = 0, offset = 0, qlim = [0,2*np.pi])
CL3 = rtb.robot.RevoluteDH(d = 0, a = 0, alpha = 0, offset = 0, qlim = [0,2*np.pi])
CL4 = rtb.robot.RevoluteDH(d = 0, a = 0, alpha = 0, offset = 0, qlim = [0,2*np.pi])
CL5 = rtb.robot.RevoluteDH(d = 0, a = 0, alpha = 0, offset = 0, qlim = [0,2*np.pi])
CL6 = rtb.robot.RevoluteDH(d = 0, a = 0, alpha = 0, offset = 0, qlim = [0,2*np.pi])
CL0 = SE3(0,0,0)*SE3.RPY([0,0,0],order = 'xyz')
CLE = SE3(0,0,0)*SE3.RPY([0,0,0],order = 'xyz')
CL = rtb.robot.DHRobot([CL1,CL2,CL3,CL4,CL5,CL6], name = "Controller Left", base = CL0, tool = CLE)
print(CL)

## Right
CR1 = rtb.robot.RevoluteDH(d = 0, a = 0, alpha = 0, offset = 0, qlim = [0,2*np.pi])
CR2 = rtb.robot.RevoluteDH(d = 0, a = 0, alpha = 0, offset = 0, qlim = [0,2*np.pi])
CR3 = rtb.robot.RevoluteDH(d = 0, a = 0, alpha = 0, offset = 0, qlim = [0,2*np.pi])
CR4 = rtb.robot.RevoluteDH(d = 0, a = 0, alpha = 0, offset = 0, qlim = [0,2*np.pi])
CR5 = rtb.robot.RevoluteDH(d = 0, a = 0, alpha = 0, offset = 0, qlim = [0,2*np.pi])
CR6 = rtb.robot.RevoluteDH(d = 0, a = 0, alpha = 0, offset = 0, qlim = [0,2*np.pi])
CR0 = SE3(0,0,0)*SE3.RPY([0,0,0],order = 'xyz')
CRE = SE3(0,0,0)*SE3.RPY([0,0,0],order = 'xyz')
CR = rtb.robot.DHRobot([CR1,CR2,CR3,CR4,CR5,CR6], name = "Controller Right", base = CR0, tool = CRE)

print(CR)
### Output
## Left
OL1 = rtb.robot.RevoluteDH(d = 0, a = 0, alpha = 0, offset = 0, qlim = [0,2*np.pi])
OL2 = rtb.robot.RevoluteDH(d = 0, a = 0, alpha = 0, offset = 0, qlim = [0,2*np.pi])
OL3 = rtb.robot.RevoluteDH(d = 0, a = 0, alpha = 0, offset = 0, qlim = [0,2*np.pi])
OL4 = rtb.robot.RevoluteDH(d = 0, a = 0, alpha = 0, offset = 0, qlim = [0,2*np.pi])
OL5 = rtb.robot.RevoluteDH(d = 0, a = 0, alpha = 0, offset = 0, qlim = [0,2*np.pi])
OL6 = rtb.robot.RevoluteDH(d = 0, a = 0, alpha = 0, offset = 0, qlim = [0,2*np.pi])
OL0 = SE3(0,0,0)*SE3.RPY([0,0,0],order = 'xyz')
OLE = SE3(0,0,0)*SE3.RPY([0,0,0],order = 'xyz')
OL = rtb.robot.DHRobot([OL1,OL2,OL3,OL4,OL5,OL6], name = "Output Left", base = OL0, tool = OLE)
print(OL)

## Right
OR1 = rtb.robot.RevoluteDH(d = 0.1, a = 0.1, alpha = 1, offset = 0, qlim = [0,2*np.pi])
OR2 = rtb.robot.RevoluteDH(d = 0.2, a = 0.2, alpha = 1, offset = 0, qlim = [0,2*np.pi])
OR3 = rtb.robot.RevoluteDH(d = 0.3, a = 0.3, alpha = 1, offset = 0, qlim = [0,2*np.pi])
OR4 = rtb.robot.RevoluteDH(d = 0.1, a = 0.2, alpha = 1, offset = 0, qlim = [0,2*np.pi])
OR5 = rtb.robot.RevoluteDH(d = 0.1, a = 0.1, alpha = 1, offset = 0, qlim = [0,2*np.pi])
OR6 = rtb.robot.RevoluteDH(d = 0.1, a = 0.1, alpha = 1, offset = 0, qlim = [0,2*np.pi])
OR0 = SE3(0,0,0)*SE3.RPY([0,0,0],order = 'xyz')
ORE = SE3(0,0,0)*SE3.RPY([0,0,0],order = 'xyz')
OR = rtb.robot.DHRobot([OR1,OR2,OR3,OR4,OR5,OR6], name = "Output Right", base = OR0, tool = ORE)
print(OR)

TL = CL.fkine([0,0.2, 0.3, 0.4, 0.5, 0.6])
print(TL)
TR = CR.fkine([0,0.3,0.4,0.5,0.6,0.7])
print(TR)

sol = OR.ikine_LM(TL)
print(sol.q)
OR.fkine(sol.q)

OR.plot(sol.q, eeframe = True, vellipse = True, jointaxes = True,block = True)