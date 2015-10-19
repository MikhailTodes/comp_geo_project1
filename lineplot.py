#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

points = [(150,300),(450,300),(570,525),(653,780),(495,845),(350,740),(100,345)]
points.append (points[0])#add the first point onto the end to close the hull

for i in range (len(points)-1):#Looping through each pair of point in the list
    p1 = points [i]#Save the first point for comparison into var p1
    p2 = points [i+1]#Save the second point for comparison into var p2
    print (p1  , p2)

    #----Make sure always plotting from left to right-----
    if(p1[0]>p2[0]):
        temp = p2
        p2 = p1
        p1 = temp
    #_____________________________________________________

    if float(((p1[0])-(p2[0]))) == 0:#Checking for a zero valued slope
        m=0.0
        print("ZeroDiv")#debugging purposes
    else:
        m = ((p2[1])-(p1[1]))/float(((p2[0])-(p1[0])))#Calculating the slope of the line
    c = p1[1]-m*p1[0]#Calculating the intercept

    #debugging purposes
    print (i)
    print (m)
    print (c)
    print

    #Cases with both positive and negative slopes but -1 < slope < 1 (plotting is the same)
    #Cases printed in green
    if (m>-1.0 and m<=1.0):
        step = np.arange(p1[0], p2[0], 1)
        plt.plot(step, m*step + c, 'g,')

    #Case positive slop and slope > 1 (plotting is the same)
    #case printed in red
    if (m>1.0):
        step = np.arange(p1[1], p2[1], 1)
        plt.plot((step-c)/m, step, 'r,')

    #Case negative slope and slope < -1 (plotting is the same)
    #case printed in blue
    if (m<-1.0):
        step = np.arange(p2[1], p1[1], 1)
        plt.plot((step-c)/m, step, 'b,')

plt.axis([0, 1000, 0, 1000])
plt.show()

