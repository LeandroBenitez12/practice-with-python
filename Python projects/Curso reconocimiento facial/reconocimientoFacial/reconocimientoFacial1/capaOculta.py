import cv2 as cv
import os
import numpy as np
from time import time

dataRuta = 'C:\\Users\\juana\\Dropbox\\GIT\\practice-with-python\\Python projects\\Curso reconocimiento facial\\reconocimientoFacial\\reconocimientoFacial1\\dataFotos'
listaData = os.listdir(dataRuta)
# print(listaData)
ids = []
rostrosData = []
id = 0

# iniciamos un tiempo con la funcion interna de python que retorna el time en segundos
TiempoInicial = time()
# bucle para acceder a las sub carpetas
for subCarpetas in listaData:
    # entramos en las carpetas contenedoras de img
    rutaCompleta = dataRuta + '\\' + subCarpetas

    print('Iniciando lecturas... ')  # damos inicio a las lecturas de archivos
    # bucle para acceder a los archivos de las sub carpetas
    for archivo in os.listdir(rutaCompleta):
        # imprimimos cada img que accedemos
        print('Imagenes: ', subCarpetas + '/' + archivo)
        # diferenciar las imagenes de cada carpeta contenedora de imagenes
        ids.append(id)
        # pasar las img a escala de grises(sobreescribiendolo) y acceder a cada archivo
        rostrosData.append(cv.imread(rutaCompleta + '\\' + archivo, 0))

    id = id+1   # para darle diferencias a cada carpeta contenedora de imagenes
    tiempoFinalLectura = time()  # tiempo final donde se finalizaron las lecturas
    # calculamos el tiempo total de lectura restando el tiempo final - el inicial
    tiempoTotalLectura = tiempoFinalLectura - TiempoInicial
    # imprimimos el tiempo total de lectura
    print('Tiempo total lectura: ', tiempoTotalLectura)

entrenamientoEigenFaceRecognizer = cv.face.EigenFaceRecognizer_create()
print('Iniciando el entrenamiento, wait...')  # iniciamos el entrenamiento
entrenamientoEigenFaceRecognizer.train(rostrosData, np.array(ids))
tiempoFinalEntrenamiento = time()  # tiempo final en segundos
# hacemos el calculo de tiempo que llevo el traning
tiempoTotalEntrenamiento = tiempoFinalEntrenamiento - tiempoTotalLectura
# imprimimos el tiempo total del training
print('Tiempo total Entrenamiento: ', tiempoTotalEntrenamiento)
# escribimos como se va a nombrar el archivo creado
entrenamientoEigenFaceRecognizer.write('EntrenamientoEigenFaceRecognizer.xml')
print('Entrenamiento completado...')  # finalizamos training
