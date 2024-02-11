import math
import random
import operator
import matplotlib.pyplot as plt
import numpy as np

class celestialBody: 
    def __init__(self, name, G, m, xPos, yPos, velX, velY, ax, ay):

        self.name = name
        self.G = G
        self.m = m
        self.mu = G*m
        self.posX = [xPos]
        self.posY = [yPos]
        self.velX = [velX]
        self.velY = [velY]
        self.ax = [ax]
        self.ay = [ay]

class celestialBodyElemental: 
    def __init__(self, name, a, e, ta, m):

        ta = ta*math.pi/180
        muSun = 132712*10**6
        r = a*(1-e**2)/(1+e*math.cos(ta))
        eps = -muSun/(2*a)
        vel = math.sqrt(2*(muSun/r + eps))

        self.name = name
        self.m = m
        self.G = 6.673*10**(-11)
        self.mu = G*m
        self.posX = [r*math.cos(ta)]
        self.posY = [r*math.sin(ta)]
        self.velX = [-vel*math.sin(ta)]
        self.velY = [vel*math.cos(ta)]
        self.ax = [0]
        self.ay = [0]

class spacecraft: 
    def __init__(self, name, a, e, ta, m, body):
        ta = ta*math.pi/180
        r = a*(1-e**2)/(1+e*math.cos(ta))
        eps = -body.mu/(2*a)
        vel = math.sqrt(2*(body.mu/r + eps))

        self.name = name
        self.m = m
        self.posX = [(body.posX + r*math.cos(ta))]
        self.posY = [body.posY + r*math.sin(ta)]
        self.velX = [body.velX + vel*math.sin(ta)]
        self.velY = [body.velY + vel*math.cos(ta)]
        self.ax = [0]
        self.ay = [0]

def runOrbitSim(Bodies, dt, t, Tf):

    while t < Tf:

        for Body in Bodies:
            Fgx1, Fgy1 = gravForce("Sun", Body)

            Fx1 = Fgx1
            Fy1 = Fgy1

            Body.ax.append(Fx1/Body.m)
            Body.ay.append(Fy1/Body.m)

            Body.velX.append(Body.velX[-1] + Body.ax[-1]*dt)
            Body.velY.append(Body.velY[-1] + Body.ay[-1]*dt)

            Body.posX.append(Body.posX[-1] + Body.velX[-1]*dt)
            Body.posY.append(Body.posY[-1] + Body.velY[-1]*dt)

        t = t+dt

    return Bodies

def gravForce(object1, object2):
    #Calculate force object 1 exerts on object 2
    if object1 == "Sun":
        posX1 = 0
        posY1 = 0
        mu1 = 132712*10**6
    else:
        posX1 = object1.posX[-1]
        posY1 = object1.posX[-1]
        mu1 = object1.mu

    posX2 = object2.posX[-1]
    posY2 = object2.posY[-1]
    mu2 = object2.mu

    dX = posX2 - posX1
    dY = posY2 - posY1

    r = math.sqrt(dX**2 + dY**2)

    Fg = (mu1*object2.m)/(r**2)
    theta = math.atan(dY/dX)

    if dX >= 0:
        Fgx = -abs(math.cos(theta)*Fg)
    else: 
        Fgx = abs(math.cos(theta)*Fg)

    if dY >= 0:
        Fgy = -abs(math.sin(theta)*Fg)
    else: 
        Fgy = abs(math.sin(theta)*Fg)

    return Fgx, Fgy



    


muSun = 132712*10**6
Rs2e = 149.6*10**9 #m
earthYVInit = math.sqrt(muSun/Rs2e)
G = 6.673*10**(-11)
#Earth = celestialBody("Earth", 6.673*10**(-11), 5.976*10**24, Rs2e, 0, 0, earthYVInit, 0, 0)
Mercury = celestialBodyElemental("Mercury", 57.9*10**6, 0.206, 0, 0.33*10**24)
Venus = celestialBodyElemental("Venus", 108.2*10**6, 0.007, 0, 4.87*10**24)
Earth = celestialBodyElemental("Earth", 150*10**6, 0.1, 0, 5.976*10**24)
Mars = celestialBodyElemental("Mars", 228*10**6, .094, 0, 0.642*10**24)
Jupiter = celestialBodyElemental("Jupiter", 778.5*10**6, 0.049, 0, 1898*10**24)
Saturn = celestialBodyElemental("Saturn", 1432*10**6, 0.052, 0, 568*10**24)
Uranus = celestialBodyElemental("Uranus", 2867*10**6, 0.047, 0, 86.8*10**24)
Neptune = celestialBodyElemental("Neptune", 4514*10**6, 0.010, 0, 102*10**24)
Pluto = celestialBodyElemental("Pluto", 5906.4*10**6, 0.244, 0, 0.0130*10**24)

#Orion = spacecraft("Artemis", 924000000, 0, 0, 26375, Earth)
#248
yearS = 31536000
propTime = 248*yearS
dt = .01*yearS
bodyList = [Mercury,Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto]
runOrbitSim(bodyList, dt, 0, propTime)

for body in bodyList:
    plt.plot(body.posX, body.posY)
    
plt.show()

