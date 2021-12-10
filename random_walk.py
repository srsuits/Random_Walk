# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 20:20:13 2021

@author: shelb
"""

# EQUATION FOR RANDOM WALK
# y(t) = y(t-1) + e


# import libraries
import matplotlib.pyplot as plt
import random

# number of steps
n = 10

# lists for x and y coordinates, respectively
# start at origin
xList = [0]
yList = [0]


# add n random steps to coordinate lists
for z in range(n):
    r = random.randint(1, 4)
    if r == 1:
        x = xList[-1] - 1
        y = yList[-1]
    elif r == 2:
        x = xList[-1] + 1
        y = yList[-1]
    elif r == 3:
        x = xList[-1]
        y = yList[-1] - 1
    elif r == 4:
        x = xList[-1]
        y = yList[-1] + 1
    
    # append new coordinates to coordinate lists
    xList.append(x)
    yList.append(y)

# plot the walk
plt.plot(xList, yList, 'bo-')









