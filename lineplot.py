#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import re
import os

plotmatrix1 = [[0]*1100 for i in range(1100)]#Matrix to keep track of plotted pixels
plotmatrix2 = [[0]*1100 for i in range(1100)]#Matrix to keep track of plotted pixels
floodfillcalls = 0

def bres_check(a):#Rounding off right for bresnan algorthim
    if ((a-int(a))*10>=5):
        return int(a)+1
    else:
        return int(a)




def plotting_points_into_shape(points, whichmatrix):
    global plotmatrix1
    global plotmatrix2
    plotmatrix = [[0]*1100 for i in range(1100)]#Matrix to keep track of plotted pixels
    points.append (points[0])#add the first point onto the end to close the hull

    for i in range (len(points)-1):#Looping through each pair of point in the list
        p1 = points [i]#Save the first point for comparison into var p1
        p2 = points [i+1]#Save the second point for comparison into var p2
        #print (p1  , p2)

        #----Make sure always plotting from left to right-----
        if(p1[0]>p2[0]):
            temp = p2
            p2 = p1
            p1 = temp
        #_____________________________________________________

        if float(((p1[0])-(p2[0]))) == 0:#Checking for a zero valued slope
            m=999.0
            print("ZeroDiv")#debugging purposes
        else:
            m = ((p2[1])-(p1[1]))/float(((p2[0])-(p1[0])))#Calculating the slope of the line
        c = p1[1]-m*p1[0]#Calculating the intercept

        #debugging purposes
        #print (i)
        #print (m)
        #print (c)
        #print

        #Cases with both positive and negative slopes but -1 < slope < 1 (plotting is the same)
        #Cases printed in green
        if (m>=-1.0 and m<=1.0):
            #step = np.arange(p1[0], p2[0], 1)
            for i in range (p1[0], p2[0]):
                plotmatrix[i][bres_check(m*i+c)]=1
                plt.plot(i, bres_check(m*i+c), 'g.')

        #Case positive slop and slope > 1 (plotting is the same)
        #case printed in red
        if (m>1.0):
            if(m==999.0):
                #print("vertical line")
                #----Make sure always plotting from bottom to top-----
                if(p1[1]>p2[1]):
                    temp = p2
                    p2 = p1
                    p1 = temp
                #______________________________________________________
                #step = np.arange(p1[1], p2[1], 1)
                for i in range (p1[1], p2[1]):
                    plotmatrix[p1[0]][i]=1
                    plt.plot(i*0+p1[0], i, 'r.')
            else:
                #step = np.arange(p1[1], p2[1], 1)
                for i in range (p1[1], p2[1]):
                    plotmatrix[bres_check((i-c)/m)][i]=1
                    plt.plot(bres_check((i-c)/m), i, 'r.')

        #Case negative slope and slope < -1 (plotting is the same)
        #case printed in blue
        if (m<-1.0):
            #step = np.arange(p2[1], p1[1], 1)
            for i in range (p2[1], p1[1]):
                plotmatrix[bres_check((i-c)/m)][i]=1
                plt.plot(bres_check((i-c)/m), i, 'b.')
    if (whichmatrix ==1):
        plotmatrix1 = plotmatrix
    else:
        plotmatrix2 = plotmatrix


def flood_fill_UL(start_pointx,start_pointy):
    global plotmatrix1
    global plotmatrix2
    global floodfillcalls
    floodfillcalls += 1 
    #os.system('cls' if os.name == 'nt' else 'clear')
    #print ("Cells checked: ")
    print floodfillcalls           

    if (plotmatrix1[start_pointx][start_pointy] == 0 and plotmatrix2[start_pointx][start_pointy] == 0):
        plotmatrix1[start_pointx][start_pointy] = 1
        plotmatrix2[start_pointx][start_pointy] = 1  
      
        plt.plot(start_pointx, start_pointy, 'c,')

        #UP
        flood_fill_UL(start_pointx, start_pointy+1)
        #Down
        flood_fill_UL(start_pointx, start_pointy-1)
        #Left
        flood_fill_UL(start_pointx-1, start_pointy)
        #Right
        flood_fill_UL(start_pointx+1, start_pointy)
    else:
        return 0
        


def find_point_in_two_polys():
    global plotmatrix1
    global plotmatrix2



def convex_hull(points):

    # 2D cross product of OA and OB vectors, i.e. z-component of their 3D cross product.
    # Returns a positive value, if OAB makes a counter-clockwise turn,
    # negative for clockwise turn, and zero if the points are collinear.
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    # Build lower hull 
    lower = []
    for i in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], i) <= 0:
            lower.pop()
        lower.append(i)

    # Build upper hull
    upper = []
    for i in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], i) <= 0:
            upper.pop()
        upper.append(i)
 
    return lower[:-1] + upper[:-1]#Return the lower and upper hulls that were built
                                  #(minus the last element which is repeated as the first element in each list)









def main():
    global plotmatrix1
    points = []
    points2 = []
   
    #__________OPENING A FILE WITH ROBUST CHECKING_____________
    check = 0
    
    while (check == 0):
        input_file = raw_input("\nPlease enter the name of the file you wish to open or q to quit:\n")
        if (input_file == 'q'):
            return 0
        else:
            try:
                f = open(input_file, 'r')
                #-----Read first line to check what kind of file-------
                input_type = f.readline()
                #check =1
                input_type = input_type.strip('\r\n')
                if (input_type == 'P' or input_type == 'S' or input_type == 'U'):
                    check = 1
                else:
                    print ("\nFile specified is not correctly formatted")
                #------------------------------------------------------                
            except:
                print ("\nCannot find specified file...")
    #____________________________________________________________

    if (input_type == 'P'):#P Case (Plot polygon given)
        while (check==1):
            try:
                current = f.readline()
                current = re.split('[(,)]', current)
                temp = [int(current[1]), int(current[2])]
                points.append(temp)
            except:
                check=0
        print 'Points:\n', points
        plotting_points_into_shape(points,1)
        #Find a point in the hull to start filling from
        startx = ((points[2][0]+points[0][0])/2)
        starty = ((points[2][1]+points[0][1])/2)
        #while (plotmatrix[startx][starty]==0): 
        qflood = raw_input("\nWould you like to flood fill the shape? This may take a while.\nType y for yes or anything else for no: ")
        if (qflood.lower() == 'y'):
            try:
                flood_fill_UL(startx, starty)
            except (RuntimeError):
                print ("\nSorry, this shape is too big to complete the recursive floodfill method")
                print ("\nPlease try again with a smaller shape")
        



    elif (input_type == 'U'):#U Case (Plotting intersection of 2 polygons)
        current = f.readline()#Reading out the P1
        while (not check == 0):
            try:
                current = f.readline()
                if (current.strip('\r\n') == 'P2'):
                    check = 2
                    current = f.readline()
                if (check == 1):
                    current = re.split('[(,)]', current)
                    temp = [int(current[1]), int(current[2])]
                    points.append(temp)
                if (check == 2):
                    current = re.split('[(,)]', current)
                    temp = [int(current[1]), int(current[2])]
                    points2.append(temp)
            except:
                check=0
        print 'Points:\n', points
        print 'Points2:\n', points2        
        plotting_points_into_shape(points,1)        
        plotting_points_into_shape(points2,2)
        



    else:#S Case (Find Convex hull of given points)
        while (check==1):
            try:
                current = f.readline()
                current = re.split('[(,)]', current)
                temp = [int(current[1]), int(current[2])]
                points.append(temp)
            except:
                check=0
        print 'Points:\n', points        
        
        #Make sure there is more that 1 point
        if len(points) <= 1:
            return 0
        points = convex_hull(points)
        plotting_points_into_shape(points,1)

    #______Setting the sixe of the plot axis________
    y_max = 0
    x_max = 0
    for i in range (len(points)):
        if (points[i][1]>y_max):
            y_max = points[i][1]
        if (points[i][0]>x_max):
            x_max = points[i][0]
    for i in range (len(points2)):
        if (points2[i][1]>y_max):
            y_max = points2[i][1]
        if (points2[i][0]>x_max):
            x_max = points2[i][0]
    #_______________________________________________

    plt.axis([0, x_max+30, 0, y_max+30])
    plt.show()
    f.close()
    print ("Thank you for playing")

main()
            
