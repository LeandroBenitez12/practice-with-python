import cv2 as cv
import os
import numpy as np

dataRuta = 'C:\\Users\\juana\\Dropbox\\GIT\\practice-with-python\\Python projects\\Curso reconocimiento facial\\reconocimientoFacial\\reconocimientoFacial1\\dataFotos'
listaData=os.listdir(dataRuta)
# print(listaData)
ids= []
rostrosData= []
id= 0

for subCarpetas in listaData:
    rutaCompleta= dataRuta + '\\' + subCarpetas 
    for archivo in os.listdir(rutaCompleta):
        ids.append(id)
        rostrosData.append(cv.imread(rutaCompleta+ '\\'+ archivo,0))
    id = id+1

entrenamientoEigenFaceRecognizer= cv.face.EigenFaceRecognizer_create()
print('Iniciando el entrenamiento, wait...')
entrenamientoEigenFaceRecognizer.train(rostrosData, np.array(ids))