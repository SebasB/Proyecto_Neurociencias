# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 20:20:58 2018

@author: USER
"""

def distance(array, angle):
    w=array.shape[0]
    h=array.shape[1]
    cx=int(w/2)
    cy=int(h/2)
    threshold=0
    j=0
    for (i) in range(w):
        for (j) in range(h):
            if(90<angle<=180):  # segun los angulos 
                i=-i
            elif(180<angle<270):
                i=-i
                j=-j
            elif(270<angle<=360):
                j=-j
            tang=round(math.tan(math.radians(angle)))
            if(j==(round((tang)*i))): # cuando la tangente existe
                print(i,j,array[i+cx,j+cy])
                if (array[i+cx,j+cy]>threshold):