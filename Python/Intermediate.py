import serial
import roboticstoolbox as rtb

### Initiate communication


robot = rtb.models.DH.Puma560()
print(robot)
sol = robot.ikine_LM(robot.fkine([0.1,0.2,0.3,0.4,0.5,0.6]))
print(sol)
robot.plot(sol.q)
a = input("Wait for input")