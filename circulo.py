from PIL import Image # se importa esta libreria para cargar la imagen
import matplotlib.pyplot as plt # Se importa esta libreria para mostrar la imagen
import numpy as np                # funciones numéricas (arrays, matrices, etc.)
import matplotlib.pyplot as plt   # funciones para representación gráfica
import random
from matplotlib.pylab import hist, show
import cv2
#I = Image.open("./lena.jpg")
#I.size, I.mode, I.format Informaciond e la imagen 

def find(matriz, func):
            return [i for (i, val) in enumerate(a) for (i, val) in enumerate(a) if func(v)]
class circulo():
    def __init__(self, h, w ,cx, cy ,r): # le ingresa el ancho y el alto
                                         # el centro y el radio 
        self.height=h
        self.width=w
        self.cx=cx
        self.cy=cy
        self.radius=r
        self.grosor=3
    def __createMatrix(self):
        self.circulo=np.zeros((self.height,self.width))
    def __createCircle(self):
        self.__createMatrix()
        for i in range(self.height): # Recorrido en x
            for j in range(self.width): # Recorrido en y 
                ecuation=(i-self.cx)**2+(j-self.cy)**2
                if  ecuation<self.radius**2 and ecuation>((self.radius-self.grosor)**2) :
                    self.circulo[i,j]=255
    def printCircle(self):
        self.__createCircle()
        plt.imshow(self.circulo) # estas dos lineas de codigo permiten visualizar la imagen
        plt.show()
        return(self.circulo)
    def __find (self):
        pass
        
''' CREAR CIRCULO'''

''' ENCONTRAR CENTRO '''

'''
v=range(0,21)
data=[]
for i in range(1000):
    data.append(random.choice(v))

hist(data,21, (0,20))
show()
'''
