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
            for (i) in range(array.shape[0]): # Se recorre la matriz 
                for (j) in range(array.shape[1]):
                    if array[i,j]>treshold:
                        I+=[i,]
                        J+=[j,]
            return [I,J]
def center(I,J): # esta funcion encuentra el centro y los puntos extremos del 
                 # objeto 
    maxi=max(I)+1
    minj=min(J)-1
    maxj=max(J)+1
    mini=min(I)-1
    centerx=int((mini+maxi)/2)
    centery=int((minj+maxj)/2)
    return([mini, maxi, minj, maxj,centerx,centery])
    
def distance(array, angle): # Esta funcion evalua todas las distancias del 
                            # centro a todos los puntos del dibujo
    global Creducido
    w=array.shape[0]
    h=array.shape[1]
    cx=int(w/2)
    cy=int(h/2)
    threshold=200
    j=0
    tang=math.tan(math.radians(angle))
    #print("OTRO"+str(angle))
    for (i) in range(w):
            
            if (angle==90): # dependiendo del angulo cambio las coordenadas
                j=i
                i=0         # singularidades de la tangente 
            elif(angle==270): 
                j=-i
                i=0
            elif (0<angle<90):
                j=round(tang*i) # 1er cuadrante i+ y j+   
            elif(90<angle<=180):  
                    i=-i       #2do cuadrante i- y j+
                    j=round(tang*i)
            elif(180<angle<270):
                    i=-i     #3er cuadrante i- y j-
                    j=round(tang*i)
            elif(270<angle<=360):
                    j=round(tang*i)  #3er cuadrante i+ y j-
            a=array[i+cx,j+cy] # se ubica el punto teniendo en cuenta el centro 
            #print(i,j,a)
            if (a>threshold): # se avalua si hay pixeles
                    a=i+cx-5
                    b=i+cx+5
                    c=j+cy-5
                    d=j+cx+5
                    Creducido[a:b,c:d]=115
                    return (np.sqrt(i**2+j**2)) # se calcula la distancia
                    
def allradius(array): # se encuentran todos los radios 
    angles=list(range(0,360,2))
    radius=[]
    errores=[]
    c=0
    for a in angles:
        try:
            radius.append(round(distance(array,a)))
        except:
            c+=1
            errores.append(a)
   # print(errores)
    print("total"+str(c))
   # print(radius)
    return(radius)
#def distance2():

C1=circulo(2000,2000,500,500,500)
C=C1.printCircle()
I,J=find(C,0)
rangos=center(I,J)
Creducido=C[rangos[0]:rangos[1],rangos[2]:rangos[3]]
plt.imshow(Creducido) # estas dos lineas de codigo permiten visualizar la imagen
plt.show()
hist(allradius(Creducido))
show()
plt.imshow(Creducido) # estas dos lineas de codigo permiten visualizar la imagen
plt.show()


#print(I)
#print(J)
