import cv2 as cv
import os
import imutils
max_result = 20000
NOISE = cv.CascadeClassifier(
    'C:/Users/juana/Dropbox/GIT/practice-with-python/Python projects/Curso reconocimiento facial/reconocimientoFacial/Modelos de entrenamiento/haarcascade_frontalface_default.xml')
pathPersons = 'D:/dataPhotos'
listPerson = os.listdir(pathPersons)
entrenamientoEigenFaceRecognizer = cv.face.EigenFaceRecognizer_create()
entrenamientoEigenFaceRecognizer.read(
    'C:/Users/juana/Dropbox/GIT/Train-RecFacial/test_two/trainEigenFaceRecognize.xml')

camera = cv.VideoCapture(0)


while True:
    answer, cameraOn = camera.read()
    if answer == False:
        break
    cameraOn = imutils.resize(cameraOn, width=640)
    gray = cv.cvtColor(cameraOn, cv.COLOR_BGR2GRAY)

    idcapture = cameraOn.copy()

    face = NOISE.detectMultiScale(gray, 1.3, 5)

    for(x, y, e1, e2) in face:
        rostrocapturado = idcapture[y:y+e2, x:x+e1]
        rostrocapturado = cv.resize(
            rostrocapturado, (160, 160), interpolation=cv.INTER_CUBIC)
        resultado = entrenamientoEigenFaceRecognizer.predict(rostrocapturado)
        cv.putText(cameraOn, '{}'.format(resultado), (x, y-5),
                   1, 1.3, (0, 255, 0), 1, cv.LINE_AA)
        if resultado[1] < max_result:
            cv.putText(cameraOn, '{}'.format(
                listPerson[resultado[0]]), (x, y-20), 2, 1.1, (0, 255, 0), 1, cv.LINE_AA)
            cv.rectangle(cameraOn, (x, y), (x+e1, y+e2), (255, 0, 0), 2)
        else:
            cv.putText(cameraOn, "No encontrado", (x, y-20),
                       2, 0.7, (0, 255, 0), 1, cv.LINE_AA)
            cv.rectangle(cameraOn, (x, y), (x+e1, y+e2), (255, 0, 0), 2)
    '''for (x,y,h,b) in faces:
        faceCapture= id_capture[y:y+b, x:x+h]
        faceCapture= cv.resize(faceCapture, (160,160), interpolation=cv.INTER_CUBIC)
        result = trainEigenFaceRecognizer.predict(faceCapture)
        cv.putText(cameraOn, '{}'.format(result), (x,y-5), 1,1.3,(0,255,0),1,cv.LINE_AA)
        if result[1]< max_result:
            cv.putText(cameraOn, '{}'.format(listPerson[result[0]]), (x,y-20), 2,1.1,(0,255,0),1,cv.LINE_AA)
            cv.rectangle(cameraOn, (x,y), (x+h,y+b), (255,0,0),2)
        else:
            cv.putText(cameraOn,"No encontrado", (x,y-20), 2,0.7,(0,255,0),1,cv.LINE_AA)
            cv.rectangle(cameraOn, (x,y), (x+h,y+b), (255,0,0),2)
            '''
    cv.imshow('result', cameraOn)

    if cv.waitKey(1) == ord('s'):
        break

camera.release()
cv.destroyAllWindows()
