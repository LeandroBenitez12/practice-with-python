import cv2 as cv
import os

font=cv.FONT_HERSHEY_DUPLEX

Contenedores_Fotos_ruta = 'C:/Users/juana/Dropbox/GIT/practice-with-python/Python projects/Curso reconocimiento facial/reconocimientoFacial/reconocimientoFacial1/dataFotos'
listRuta= os.listdir(Contenedores_Fotos_ruta)

entrenamientoEigenFaceRecognizer= cv.face.EigenFaceRecognizer_create()
entrenamientoEigenFaceRecognizer.read('C:/Users/juana/Dropbox/GIT/practice-with-python/Python projects/Curso reconocimiento facial/reconocimientoFacial/reconocimientoFacial1/EntrenamientoEigenFaceRecognizer.xml')
ruidos = cv.CascadeClassifier('C:/Users/juana/Dropbox/GIT/practice-with-python/Python projects/Curso reconocimiento facial/reconocimientoFacial/Modelos de entrenamiento/haarcascade_frontalface_default.xml')

camera = cv.VideoCapture(0)

while True:

    respuesta, enVivo= camera.read()

    if respuesta == False:
        break
    gray= cv.cvtColor(enVivo, cv.COLOR_RGB2GRAY)
    idCapture= gray.copy()
    caras =ruidos.detectMultiScale(gray,1.25,3)
    for x,y,b,h in caras:
        # cv.rectangle(gray, (x,y), (x+b,y+h), (255, 0 , 0), 2)
        rostro_capture= idCapture[y:y+h,x:x+b]
        rostro_capture= cv.resize(rostro_capture,[600,600], interpolation=cv.INTER_CUBIC)
        resultado= entrenamientoEigenFaceRecognizer.predict(rostro_capture)
        cv.putText(enVivo, f'{resultado}', (x,y-7),font ,1.2, (0,0,0), 2)
        cv.rectangle(enVivo, ( x,y),(y+h,x+b), (255,0,0),2)
    cv.imshow('Camara Resultado',enVivo)
    if cv.waitKey(1) == ord('s'):
        break

enVivo.release()
cv.destroyAllWindows()