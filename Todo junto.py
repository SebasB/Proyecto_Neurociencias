# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 15:49:13 2018

@author: USER
"""

# -*- coding: utf-8 -*-
"""
Detector de contornos

Convertir la imagen a escala de grises
Filtrar la imagen para eliminar el ruido
Aplicar el detector de bordes Canny
Buscar los contornos dentro de los bordes detectados
Dibujar dichos contornos

OPENCV: MODO BGR
MATPLOTLIB: MODO RGB

"""


import numpy as np
import cv2
from matplotlib import pyplot as plt
from skimage import color 
from matplotlib.pylab import hist,show
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
    c=0
    for a in angles:
        try:
            radius.append(round(distance(array,a)))
        except:
            c+=1
   # print(errores)
    print("total"+str(c))
   # print(radius)
    return(radius)
#def distance2():
# Propiedades de la imagen 
# img.shape, img.size, img.dtype 
def properties(img):
    print("Dimensiones:  "+str(img.shape))
    print("Cantidad: "+str(img.size))
    print("Tipo de datos: "+str(img.dtype))
# Imagen origninal 

# Cargamos la imagen
original = cv2.imread("circulo2.jpg")
#cv2.imshow("original", original)
properties(original)
# 1. Convertir imagen a escala de grises 
gris= cv2.imread('circulo2.jpg', cv2.COLOR_BGR2GRAY)
#cv2.imshow('gris',gris)


# 2. Aplicar filtro gausiano--> con una mascara se recorre la matriz y se suaviza
gaussiana = cv2.GaussianBlur(gris, (5,5),0) #CV2.Gaussiana(Imagen, Dimensiones kernel, desviacion estandar de la gaussiana)
#cv2.imshow("suavisada", gaussiana)


# 3. Deteccion de bordes 
    #3.1 Detección de bordes con Sobel--> detecta cambios de intensidad(Gradiente)
    #3.2 Supresión de píxeles fuera del borde-->solo se queda con bordes de cierto grosor
    #3.3 Aplicar umbral por histéresis--> se establecen 2 umbrales uno por max yuno minimo 
#    Si el valor del píxel es mayor que el umbral máximo, el píxel se considera parte del borde.
#    Un píxel se considera que no es borde si su valor es menor que el umbral mínimo,
#    Si está entre el máximo y el mínimo, será parte del borde si está conectado con un píxel que forma ya parte del borde.

canny = cv2.Canny(gaussiana, 50, 150) #canny = cv2.Canny(imagen, umbral_minimo, umbral_maximo)
#cv2.imshow("canny", canny)


# 4. Se buscan y dibujan los contornos 
(_, contornos,_) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#cv2.imshow("cannyup", cannyup)

canvas=np.zeros_like(original[:])
cv2.drawContours(original,contornos,-1,(255,255,255), 2)
cv2.drawContours(canvas,contornos,-1,(255,255,255), 1)
#cv2.imshow("contornos", canvas)

canvas = color.rgb2gray(canvas)
I,J=find(canvas,0)
rangos=center(I,J)
Creducido=canvas[rangos[0]:rangos[1],rangos[2]:rangos[3]]
plt.imshow(Creducido) # estas dos lineas de codigo permiten visualizar la imagen
plt.show()

hist(allradius(Creducido))
show()

plt.imshow(Creducido) # estas dos lineas de codigo permiten visualizar la imagen
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

