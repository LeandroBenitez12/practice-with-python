import cv2 as cv
import numpy as np
import os
import imutils

#declaramos rutas

#PONEMOS NOMBRE A LA CARPETA
modelo= 'Leandro Benitez'
ruta1= 'C:/Users/juana/Dropbox/GIT/practice-with-python/Python projects/Curso reconocimiento facial/reconocimientoFacial/reconocimientoFacial1/dataFotos'
rutaCompleta =ruta1 +'/'+ modelo
#ruidos de archivo xml
ruidos=cv.CascadeClassifier('C:/Users/juana/Dropbox/GIT/practice-with-python/Python projects/Curso reconocimiento facial/reconocimientoFacial/Modelos de entrenamiento/haarcascade_frontalface_default.xml')

#creamos carpeta
if not os.path.exists(rutaCompleta):
    os.makedirs(rutaCompleta)

#En vivo le decimos que la video captura es interna (0)
camara = cv.VideoCapture(0)
#video Auron
# camara = cv.VideoCapture('C:/Users/juana/Dropbox/GIT/practice-with-python/Python projects/Curso reconocimiento facial/reconocimientoFacial/reconocimientoFacial1/videos/videoauron.mp4')
#video Elon
# camara = cv.VideoCapture('C:/Users/juana/Dropbox/GIT/practice-with-python/Python projects/Curso reconocimiento facial/reconocimientoFacial/reconocimientoFacial1/videos/ElonMusk.mp4')
#cuenta las capturas
id = 150
while True:
    #Encontramos la camara
    respuesta, enVivo = camara.read()
    #bajamos resolucion para que no pese tanto al img
    enVivo= imutils.resize(enVivo, width= 640)
    if respuesta == False:
        break
    #Pasamos el video a escala de grises
    gray= cv.cvtColor(enVivo, cv.COLOR_RGB2GRAY)

    #detectamos las caras
    caras =ruidos.detectMultiScale(gray,
        scaleFactor=1.29,
        minNeighbors=4,
        minSize=[30,30])
    #fuente de la letra del video
    font=cv.FONT_HERSHEY_DUPLEX

    #ahorra recursos
    idcaptura = enVivo.copy()

    #Creamos nuestro rectangulo
    for(x,y,h,b) in caras:
        cv.rectangle(enVivo, (x,y), (x+b,y+h), (0,0,0), 2)
        #
        rostroCapturado=idcaptura[y:y+h,x:x+b]
        rostroCapturado=cv.resize(rostroCapturado, [600,600], interpolation= cv.INTER_CUBIC)
        cv.imwrite(rutaCompleta+f'/img_{id}.jpg', rostroCapturado)
        id = 1 +  id

    #mensaje en el video para el usuario
    # cv.putText(enVivo, "Mire Frontalmente a la camara y sonria", (50,400) , font, 0.75, (0,0,0),2)
    #mostramos camara en vivo con dettecion de rostros
    cv.imshow('Resultado', enVivo)
    # cv.waitKey(200)
    #cerrar programa
    if id == 201:
        break
    # if cv.waitKey(1) == ord('q'):
    #     break

#detener camara
camara.release()
#cerrar todas las ventanas
cv.destroyAllWindows()