# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 15:09:40 2018

@author: Sebastian Buitrago
"""
from circulo import circulo
import matplotlib.pyplot as plt 
import numpy as np
import math
from matplotlib.pylab import hist,show

def find(array, treshold): # Encuentra todos las posiciones 
                           # de los valores que están por encima de 
                            #en umbral 
            I=[] # Se guardan las posiciones en X
            J=[] # Se guardan las posiciones en y 
            for (i) in range(array.shape[0]):
                for (j) in range(array.shape[1]):
                    if array[i,j]>treshold:
                        I+=[i,]
                        J+=[j,]
            return [I,J]
def center(I,J):
    maxi=max(I);
    minj=min(J);
    maxj=max(J);
    mini=min(I);
    centerx=int((mini+maxi)/2)
    centery=int((minj+maxj)/2)
    return([mini, maxi, minj, maxj,centerx, centery])
    
def distance(array, angle):
    w=array.shape[0]
    h=array.shape[1]
    cx=int(w/2)
    cy=int(h/2)
    threshold=0
    j=0
    tang=round(math.tan(math.radians(angle)))
    #print("OTRO"+str(angle))
    
    for (i) in range(w):
            if (angle==90):
                j=i
                i=0
            elif(angle==270): 
                j=-i
                i=0
            else:
                j=round(tang*i)# segun el angulo
            if(90<angle<=180):  # segun los angulos 
                    i=-i
            elif(180<angle<270):
                    i=-i
                    j=-j
            elif(270<angle<=360):
                    j=-j
            #print(i,j,array[i+cx,j+cy])
            a=array[i+cx,j+cy]
            if (a>threshold): # se avalua si hay pixeles 
                    return (np.sqrt(i**2+j**2)) # se calcula la distancia
                    
def allradius(array):
    #angles=list(range(0,361,10))
    angles=list(range(0,76))
    print(angles)
    radius=[]
    for a in angles:
        radius.append(round(distance(array,a)))
    return(radius)
      
C1=circulo(1000,1000,200,200,50)
C=C1.printCircle()
I,J=find(C,0)
rangos=center(I,J)
Creducido=C[rangos[0]:rangos[1],rangos[2]:rangos[3]]
plt.imshow(Creducido) # estas dos lineas de codigo permiten visualizar la imagen
plt.show()
hist(allradius(Creducido))
show()



#print(I)
#print(J)
