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
# Propiedades de la imagen 
# img.shape, img.size, img.dtype 
def properties(img):
    print("Dimensiones:  "+str(img.shape))
    print("Cantidad: "+str(img.size))
    print("Tipo de datos: "+str(img.dtype))
# Imagen origninal 

# Cargamos la imagen
original = cv2.imread("circulo2.jpg")
cv2.imshow("original", original)
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
cv2.imshow("canny", canny)


# 4. Se buscan y dibujan los contornos 
(_, contornos,_) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#cv2.imshow("cannyup", cannyup)

canvas=np.zeros_like(original[:])
cv2.drawContours(original,contornos,-1,(255,255,255), 2)
cv2.drawContours(canvas,contornos,-1,(255,255,255), 2)
cv2.imshow("contornos", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
hist(ana.allradius(Creducido))
show()
# 1. Convertir imagen a escala de grises 
gris= cv2.imread('circulo2.jpg', cv2.COLOR_BGR2GRAY)
#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

# 2. Aplicar filtro gausiano--> con una mascara se recorre la matriz y se suaviza
gaussiana = cv2.GaussianBlur(gris, (50,150),0)
cv2.imshow("gris", gaussiana)

cv2.waitKey(0)
cv2.destroyAllWindows()

# 3. Deteccion de bordes 
    #3.1 Detección de bordes con Sobel--> detecta cambios de intensidad(Gradiente)
    #3.2 Supresión de píxeles fuera del borde-->solo se queda con bordes de cierto grosor
    #3.3 Aplicar umbral por histéresis--> se establecen 2 umbrales uno por max yuno minimo 
#    Si el valor del píxel es mayor que el umbral máximo, el píxel se considera parte del borde.
#    Un píxel se considera que no es borde si su valor es menor que el umbral mínimo,
#    Si está entre el máximo y el mínimo, será parte del borde si está conectado con un píxel que forma ya parte del borde.
canny = cv2.Canny(gaussiana, 50, 150)
cv2.imshow("canny", canny)

cv2.waitKey(0)
cv2.destroyAllWindows()
# Borde vs Contorno:
#  Borde=> Cambios de intensidad pronunciados
#  Contorno=> curva sin huevos ni saltos 

# Buscamos los contornos

(_, contornos,_) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  
cv2.drawContours(original,contornos,-1,(0,0,255), 2)
cv2.imshow("contornos", original)
 
cv2.waitKey(0)
'''
    
#(imagen, contornos, jerarquia) = cv2.findContours(imagenbinarizada, modo_contorno, metodo_aproximacion)
