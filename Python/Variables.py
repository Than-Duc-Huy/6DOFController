import numpy as np
# Number placeholder
p180 = np.pi
p360 = 2*np.pi
p90 = np.pi/2
n90 = -np.pi/2

# Length

# Controller
CL = [2.0, 0.6, 0.3, 1.9, 1.05]
# Output
OL = [0.5, 0.6, 0.75, 0.5, 0.5]
OB = 0.5
ScalingFactor = 0.5

# Standard Denavitt Hartenberg notation
DHparam = np.zeros((4, 7, 4))
# B123456T
# Controller Left (CL)
DHparam[0][0] = [0, 0, 0, 0]
DHparam[0][1] = [0, 0, -CL[0], 0]
DHparam[0][2] = [n90, -CL[1], 0, n90]
DHparam[0][3] = [0, CL[2], CL[3], 0]
DHparam[0][4] = [p90, CL[4], 0, p90]
DHparam[0][5] = [p90, 0, 0, n90]
DHparam[0][6] = [0, 0, 0, n90]


# Controller Right (CR)
DHparam[1][0] = [0, 0, 0, 0]
DHparam[1][1] = [0, 0, CL[0], 0]
DHparam[1][2] = [n90, -CL[1], 0, n90]
DHparam[1][3] = [0, -CL[2], CL[3], 0]
DHparam[1][4] = [p90, -CL[4], 0, p90]
DHparam[1][5] = [p90, 0, 0, n90]
DHparam[1][6] = [0, 0, 0, n90]


# Output Left (OL)

DHparam[2][0] = [0, 0, 0, 0]
DHparam[2][1] = [0, OL[0], 0, p90]
DHparam[2][2] = [p90, 0, OL[1], 0]
DHparam[2][3] = [0, 0, OL[2], p90]
DHparam[2][4] = [0, OL[3], 0, p90]
DHparam[2][5] = [0, 0, 0, p90]
DHparam[2][6] = [p90, OL[4], 0, 0]

# Output Right (OR)
DHparam[3][0] = [0, 0, 0, 0]
DHparam[3][1] = [0, OL[0], 0, p90]
DHparam[3][2] = [p90, 0, OL[1], 0]
DHparam[3][3] = [0, 0, OL[2], p90]
DHparam[3][4] = [0, OL[3], 0, p90]
DHparam[3][5] = [0, 0, 0, p90]
DHparam[3][6] = [p90, OL[4], 0, 0]


print(DHparam)
