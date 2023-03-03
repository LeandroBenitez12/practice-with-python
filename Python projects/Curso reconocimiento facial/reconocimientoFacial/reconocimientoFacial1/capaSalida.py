import cv2 as cv
import os
min_Result_Lean = 14000
max_Result_Lean = 22000
font=cv.FONT_HERSHEY_DUPLEX

Contenedores_Fotos_ruta = 'C:/Users/juana/Dropbox/GIT/practice-with-python/Python projects/Curso reconocimiento facial/reconocimientoFacial/reconocimientoFacial1/dataFotos'
listRuta= os.listdir(Contenedores_Fotos_ruta)

entrenamientoEigenFaceRecognizer= cv.face.EigenFaceRecognizer_create()
entrenamientoEigenFaceRecognizer.read('C:/Users/juana/Dropbox/GIT/Train-RecFacial/test_one/EntrenamientoEigenFaceRecognizer.xml')
ruidos = cv.CascadeClassifier('C:/Users/juana/Dropbox/GIT/practice-with-python/Python projects/Curso reconocimiento facial/reconocimientoFacial/Modelos de entrenamiento/haarcascade_frontalface_default.xml')

camera = cv.VideoCapture(0)

while True:

    respuesta, enVivo= camera.read()

    if respuesta == False:
        break
    gray= cv.cvtColor(enVivo, cv.COLOR_RGB2GRAY)
    idCapture= gray.copy()
    
    #detectamos las caras
    caras =ruidos.detectMultiScale(gray,
        scaleFactor=1.29,
        minNeighbors=4,
        minSize=[30,30])
    
    for x,y,b,h in caras:
        # cv.rectangle(gray, (x,y), (x+b,y+h), (255, 0 , 0), 2)
        rostro_capture= idCapture[y:y+h,x:x+b]
        rostro_capture= cv.resize(rostro_capture,[600,600], interpolation=cv.INTER_CUBIC)
        resultado= entrenamientoEigenFaceRecognizer.predict(rostro_capture)
        cv.putText(enVivo, f'{resultado}', (x,y-10),font ,1.2, (0,0,0), 2)
        
        if resultado[1] > min_Result_Lean and resultado[1] < max_Result_Lean:
            cv.rectangle(enVivo, (x,y), (x+b,y+h), (0,255,0), 2)
            cv.putText(enVivo, f'The person is: {listRuta[resultado[2]]}', (x,y-40), font, 1.1 , (0,0,0), 2, cv.LINE_AA)

        else:
            cv.rectangle(enVivo, (x,y), (x+b,y+h), (0,0,255), 2)
            cv.putText(enVivo, f'The person is not found...', (x,y-40), font, 1.1 , (0,0,255), 2, cv.LINE_AA)
    cv.imshow('Camara Resultado',enVivo)
    if cv.waitKey(1) == ord('s'):
        break

enVivo.release()
cv.destroyAllWindows()