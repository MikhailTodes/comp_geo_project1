#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import PIL



def bresenham_get_points(x1,y1,x2,y2):
    points = []
    issteep = abs(y2-y1) > abs(x2-x1)
    if issteep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    rev = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        rev = True
    deltax = x2 - x1
    deltay = abs(y2-y1)
    error = int(deltax / 2)
    y = y1
    ystep = None
    if y1 < y2:
        ystep = 1
    else:
        ystep = -1
    for x in range(x1, x2 + 1):
        if issteep:
            points.append((y, x))
        else:
            points.append((x, y))
        error -= deltay
        if error < 0:
            y += ystep
            error += deltax
    if rev:
        points.reverse()
    return points



def bresenham(pt1, pt2, arr):
    """
    Pass in two points, and return modified arr where we have set all correct
    line pixels to be one.
    """
    points = bresenham_get_points(pt1[0], pt1[1], pt2[0], pt2[1])
    for p in points:
        arr[p] = 1
    return arr


# Let's define a series of points
points = np.array([
    [50,50],
    [100,50],
    [100,75],
    [50,75]
    ])
points = np.vstack((points, points[0]))


# Get image for polygon:
poly_arr = np.zeros((150,150), dtype=np.uint8)
for i,p in enumerate(points[:-1]):
    bresenham(p, points[i+1], poly_arr)


plt.hold(True)
plt.plot(points[:,0], points[:,1], 'r-o')
arr = np.swapaxes(arr, 0, 1)
plt.imshow(arr, cmap='gray_r', alpha=0.2, zorder=-10, origin='lower')
ax = plt.gca()
ax.set_xlim([0,150])
ax.set_ylim([0,150])
plt.hold(False)
plt.show()




# arr = np.zeros((150,150), dtype=np.uint8)
# arr[0:60, 20:40] = 1


# plt.hold(True)
# plt.plot(points[:,0], points[:,1], 'r-o')
# arr = np.swapaxes(arr, 0, 1)
# plt.imshow(arr, cmap='gray_r', alpha=0.2, zorder=-10, origin='lower')
# ax = plt.gca()
# ax.set_xlim([0,150])
# ax.set_ylim([0,150])
# plt.hold(False)
# plt.show()

