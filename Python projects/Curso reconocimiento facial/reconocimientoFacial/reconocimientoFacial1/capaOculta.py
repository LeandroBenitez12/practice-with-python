import cv2 as cv
import os
import numpy as np
from time import time

dataRuta = 'C:\\Users\\juana\\Dropbox\\GIT\\practice-with-python\\Python projects\\Curso reconocimiento facial\\reconocimientoFacial\\reconocimientoFacial1\\dataFotos'
listaData=os.listdir(dataRuta)
# print(listaData)
ids= []
rostrosData= []
id= 0

TiempoInicial = time()  #iniciamos un tiempo con la funcion interna de python que retorna el time en segundos
#bucle para acceder a las sub carpetas
for subCarpetas in listaData:
    rutaCompleta= dataRuta + '\\' + subCarpetas #entramos en las carpetas contenedoras de img 

    print('Iniciando lecturas... ') #damos inicio a las lecturas de archivos
    for archivo in os.listdir(rutaCompleta): #bucle para acceder a los archivos de las sub carpetas
        print('Imagenes: ',subCarpetas + '/' + archivo) #imprimimos cada img que accedemos
        ids.append(id)  #diferenciar las imagenes de cada carpeta contenedora de imagenes
        rostrosData.append(cv.imread(rutaCompleta+ '\\'+ archivo,0))    #pasar las img a escala de grises(sobreescribiendolo) y acceder a cada archivo

    id = id+1   # para darle diferencias a cada carpeta contenedora de imagenes
    tiempoFinalLectura = time() # tiempo final donde se finalizaron las lecturas
    tiempoTotalLectura = tiempoFinalLectura - TiempoInicial #calculamos el tiempo total de lectura restando el tiempo final - el inicial
    print('Tiempo total lectura: ',tiempoTotalLectura)  #imprimimos el tiempo total de lectura

entrenamientoEigenFaceRecognizer= cv.face.EigenFaceRecognizer_create()
print('Iniciando el entrenamiento, wait...')    #iniciamos el entrenamiento
entrenamientoEigenFaceRecognizer.train(rostrosData, np.array(ids))  
tiempoFinalEntrenamiento = time()   #tiempo final en segundos
tiempoTotalEntrenamiento = tiempoFinalEntrenamiento - tiempoTotalLectura #hacemos el calculo de tiempo que llevo el traning 
print('Tiempo total Entrenamiento: ',tiempoTotalEntrenamiento)  # imprimimos el tiempo total del training
entrenamientoEigenFaceRecognizer.write('EntrenamientoEigenFaceRecognizer.xml') # escribimos como se va a nombrar el archivo creado
print('Entrenamiento completado...') # finalizamos training