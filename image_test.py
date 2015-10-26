#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import cv2


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



def flood_fill_UL_nonrecurse(start_pointx, start_pointy, edgearray):
    fill_set = set()
    fill_set.add((start_pointx, start_pointy))
    fill_array = edgearray.copy()
    while fill_set:
        (x,y) = fill_set.pop()
        if not fill_array[x][y]:
            fill_set.add((x,y+1))
            fill_set.add((x,y-1))
            fill_set.add((x-1,y))
            fill_set.add((x+1,y))
            fill_array[x][y] = 1
    return fill_array



# Let's define a series of points
points = np.array([
    [150,300],
    [450,300],
    [570,525],
    [653,780],
    [495,845],
    [350,740],
    [100,345]
    ])
points = np.vstack((points, points[0]))


# get array that represents edges of the polygon::
size = int(np.max(points)*(1.25))
poly_arr = np.zeros((size,size), dtype=np.uint8)
for i,p in enumerate(points[:-1]):
    bresenham(p, points[i+1], poly_arr)

# get array for fill:
fill_arr = flood_fill_UL_nonrecurse(size>>1, size>>1, poly_arr)

# convert poly array:
poly_rgb = np.zeros((poly_arr.shape[0], poly_arr.shape[1], 3), dtype=np.uint8)
poly_rgb[:,:,0] = 128
poly_rgb = cv2.bitwise_and(poly_rgb, poly_rgb, mask=poly_arr)

# convert fill array
fill_rgb = np.zeros((fill_arr.shape[0], fill_arr.shape[1], 3), dtype=np.uint8)
fill_rgb[:,:,1:] = 128
fill_rgb = cv2.bitwise_and(fill_rgb, fill_rgb, mask=fill_arr)

# combine images:
plot_img = cv2.add(poly_rgb, fill_rgb)

# show image:
plt.hold(True)
plot_img = np.swapaxes(plot_img, 0, 1)
plt.imshow(plot_img, zorder=-10, origin='lower', interpolation='none')
ax = plt.gca()
ax.set_xlim([0,size])
ax.set_ylim([0,size])
plt.hold(False)
plt.show()


