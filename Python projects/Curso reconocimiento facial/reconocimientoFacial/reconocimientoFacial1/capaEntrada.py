import cv2 as cv
import numpy as np

ruidos=cv.CascadeClassifier('C:\\Users\\juana\\Dropbox\\GIT\\practice-with-python\\Python projects\\Curso reconocimiento facial\\reconocimientoFacial\\Modelos de entrenamiento\\haarcascade_frontalface_default.xml')

#le decimos que la video captura es interna (0)
camara = cv.VideoCapture(0)

while True:
    #Encontramos la camara
    type_cam, enVivo = camara.read()
    
    #Pasamos el video a escala de grises
    gray= cv.cvtColor(enVivo, cv.COLOR_RGB2GRAY)
    #
    cara=ruidos.detectMultiScale(gray,1.4,4)
    
    for(x,y,e1,e2) in cara:
        cv.rectangle(enVivo, (x,y), (x+e1,y+e2), (220,255,255), 2)
    
    cv.imshow('Cara', enVivo)
    
    if cv.waitKey(1) == ord('q'):
        break

camara.release
cv.destroyAllWindows()