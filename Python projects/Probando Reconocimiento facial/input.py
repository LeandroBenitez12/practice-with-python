import cv2 as cv
import os
import imutils

NOISE = cv.CascadeClassifier('C:/Users/juana/Dropbox/GIT/practice-with-python/Python projects/Curso reconocimiento facial/reconocimientoFacial/Modelos de entrenamiento/haarcascade_frontalface_default.xml')
#paths 
nameFolder='Leandro'
pathFolders= 'C:/Users/juana/Dropbox/GIT/practice-with-python/Python projects/Probando Reconocimiento facial/dataPhotos'
pathPerson= pathFolders + '/' + nameFolder

if not os.path.exists(pathPerson):
    print(f'Path created in: {pathPerson}')
    os.makedirs(pathPerson)

camera = cv.VideoCapture(0)

while True:
    answer, cameraOn = camera.read()
    if answer == False: break

    cameraOn = imutils.resize(cameraOn, width= 640)

    gray = cv.cvtColor(cameraOn, cv.COLOR_BGR2GRAY)

    faces = NOISE.detectMultiScale()

