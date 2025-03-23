import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import *

def plotCircle(posX, posY, r, ax):
    point = Point(posX, posY)

    cricle = point.buffer(r)

    x1, y1 = cricle.exterior.xy
    ax.plot(x1,y1, color = "blue")


fig, ax = plt.subplots(figsize = (10,10))

val = 100
r = 5

while val > 0.01:
    plotCircle(1,1,r,ax)
    plotCircle(20,20,r,ax)
    val /= 5
    r += 5


plt.show()
