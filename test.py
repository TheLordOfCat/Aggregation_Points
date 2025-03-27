import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import *
import math

def get_angles(change):
    curAngle = change
    MOD = 360
    ans = []
    while curAngle != 0:
        ans.append(curAngle)
        curAngle = (curAngle + change)%MOD
    ans.append(0)
    return ans

def convert_degree_to_rad(ang):
    ans = []
    for a in ang:
        ans.append(np.radians(a))
    return ans

boundry = 5

x_points = []
y_points = []

x_next = [0]
y_next = [0]

def next_point(x, y):
    found = False

    for i in range(0, len(x_next)):
        if x_next[i] == x and y_next[i] == y:
            found = True
            break

    if not(found):
        x_next.append(x)
        y_next.append(y)

def procesPoint(xS, yS, angles_rad):
    global x_points, y_points, boundry

    for a in angles_rad:
        x = math.cos(a)*r + xS
        y = math.sin(a)*r + yS
        
        if -1 * boundry <= x and x <= boundry and -1 * boundry <= y and y <= boundry:
            x_points.append(x)
            y_points.append(y)
            next_point(x, y)

r = 1
angles_degree = get_angles(180)
angles_rad = convert_degree_to_rad(angles_degree)

ind = 0
while ind < len(x_next) and len(x_next) < 10000:
    procesPoint(x_next[ind], y_next[ind], angles_rad)
    ind += 1


fig, ax = plt.subplots(figsize = (10,10))

ax.plot(x_points, y_points, 'ko')
plt.show()
