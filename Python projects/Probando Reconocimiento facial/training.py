import cv2 as cv
import os
from time import time
import numpy as np
MINUTE = 0.0166667
pathPersons = 'D:/dataPhotos'

listPersons = os.listdir(pathPersons)
diferenttiate_files = []
dataFace= []
id = 0
first_time = time()
for subpath in listPersons:
    pathPerson = pathPersons + '/' + subpath
    print('Iniciando recorrido de fotos')
    for file in os.listdir(pathPerson):
        print(f'Image: {subpath}/{file}')
        diferenttiate_files.append(id)
        dataFace.append(cv.imread(pathPerson + '/' + file,0))
    id = id +1 
    finishTimeRead = time()
    totalTimeRead = (finishTimeRead - first_time) * MINUTE
    print(f'The time Read is: {totalTimeRead:.2} Minutes.')

trainEigenFaceRecognizer = cv.face.EigenFaceRecognizer_create()
print('Starting the training, wait please...')
trainEigenFaceRecognizer.train(dataFace, np.array(diferenttiate_files))
lastTime = time()
totalTimeTrain= (lastTime -finishTimeRead) * MINUTE
print(F'The time of training is : {totalTimeTrain} Minutes.')
trainEigenFaceRecognizer.write('C:/Users/juana/Dropbox/GIT/Train-RecFacial/test_two/trainEigenFaceRecognize.xml')
print('Training Finalized, thanks')