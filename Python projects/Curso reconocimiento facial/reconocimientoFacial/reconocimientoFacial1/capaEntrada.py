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
    caras =ruidos.detectMultiScale(gray,
    scaleFactor= 1.2,
    minNeighbors=3,
    minSize=(60,60),
    maxSize= (200,200))
    font=cv.FONT_HERSHEY_SIMPLEX
    for(x,y,h,b) in caras:
        cv.rectangle(enVivo, (x,y), (x+h,y+b), (0,0,0), 2)

    cv.putText(enVivo, "Mire Frontalmente a la camara y sonria", (50,400) , font, 0.75, (0,0,0),2)
    cv.imshow('Cara', enVivo)
    
    if cv.waitKey(1) == ord('q'):
        break

camara.release
cv.destroyAllWindows()