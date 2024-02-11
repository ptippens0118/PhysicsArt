import math
import random
import operator
import matplotlib.pyplot as plt
import numpy as np

def propagate(posX, posY, velX, velY, m, dt): 
    g = -9.81 #gravity

    #Drag calculation
    cd = 0.47
    A = 1
    rho = np.random.normal(1.225, 0.1)

    while posY[-1] >= 0:
        drgFx = -0.5*cd*A*rho*velX[-1]**2
        drgFy = -0.5*cd*A*rho*velY[-1]**2

        Fg = m*g

        Fx = drgFx
        Fy = drgFy + Fg

        ax = Fx/m
        ay = Fy/m

        velX.append(velX[-1]+ax*dt)
        velY.append(velY[-1]+ay*dt)

        posX.append(posX[-1]+velX[-1]*dt)
        posY.append(posY[-1]+velY[-1]*dt)

    return posX, velX, posY, velY


xInit = [0]
yInit = [0]
xVInit = [30]
yVinit = [10]

m = 100
dt = .01


for i in range(1,100):
    xInit = [0]
    yInit = [0]
    xVInit = [np.random.normal(30, 3*0.3)]
    yVinit = [np.random.normal(10, 3*0.1)]

    posX, velX, posY, velY = propagate(xInit, yInit, xVInit, yVinit, m, dt)
    plt.plot(posX, posY, linewidth = 2)

plt.show()

for i in range(1,100):
    xInit = [0]
    yInit = [0]
    xVInit = [30*random.random()]
    yVinit = [10*random.random()]

    posX, velX, posY, velY = propagate(xInit, yInit, xVInit, yVinit, m, dt)
    plt.plot(posX, posY, linewidth = 0.5)
plt.show()
