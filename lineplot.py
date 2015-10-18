#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

points = [[2,2],[3,3],[6,8],[7,2],[3,2]]

for i in range (len(points)-1):
    if float(((points[i+1][0])-(points[i][0]))) == 0:
        m=0.0
        print("ZeroDiv")
    else:
        m = ((points[i+1][1])-(points[i][1]))/float(((points[i+1][0])-(points[i][0])))
    c = points[i][1]-m*points[i][0]
    print (i)
    print (m)
    print (c)
    print

    x = np.arange(points[i][0], points[i+1][0], 0.01)

    # red dashes, blue squares and green triangles
    plt.plot(x, m*x + c, 'g,')
    plt.axis([0, 11, 0, 11])

if float(((points[0][0])-(points[len(points)-1][0]))) == 0:
    m=0.0
    print("ZeroDiv")
else:
    m = ((points[0][1])-(points[len(points)-1][1]))/float(((points[0][0])-([len(points)-1][0])))
c = points[0][1]-m*points[0][0]
print (m)
print (c)
print

x = np.arange(points[0][0], points[len(points)-1][0], 0.01)

# red dashes, blue squares and green triangles
plt.plot(x, m*x + c, 'g,')
plt.axis([0, 11, 0, 11])


plt.show()

