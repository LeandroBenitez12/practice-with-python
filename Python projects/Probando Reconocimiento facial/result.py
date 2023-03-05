import cv2 as cv
import os
import imutils
max_result = 20000

pathPersons= 'D:/dataPhotos'
listPerson= os.listdir(pathPersons)
trainingEigenFaceRecognizer=cv.face.EigenFaceRecognizer_create()
trainingEigenFaceRecognizer.read('C:/Users/juana/Dropbox/GIT/Train-RecFacial/test_two/trainEigenFaceRecognize.xml')
NOISE = cv.CascadeClassifier('C:/Users/juana/Dropbox/GIT/practice-with-python/Python projects/Curso reconocimiento facial/reconocimientoFacial/Modelos de entrenamiento/haarcascade_frontalface_default.xml')

# En vivo le decimos que la video captura es interna (0)
camera = cv.VideoCapture(0)

# video Auron
# camera = cv.VideoCapture('C:/Users/juana/Dropbox/GIT/practice-with-python/Python projects/Probando Reconocimiento facial/videos/videoauron.mp4')

# video Elon
# camera = cv.VideoCapture('C:/Users/juana/Dropbox/GIT/practice-with-python/Python projects/Probando Reconocimiento facial/videos/ElonMusk.mp4')

# video Juana
# camera = cv.VideoCapture('C:/Users/juana/Dropbox/GIT/practice-with-python/Python projects/Probando Reconocimiento facial/videos/Juana.mp4')

# video Juan 33 ~ 41
#camera = cv.VideoCapture('C:/Users/juana/Dropbox/GIT/practice-with-python/Python projects/Probando Reconocimiento facial/videos/Juan.mp4')

# video Leandro
#camera = cv.VideoCapture('C:/Users/juana/Dropbox/GIT/practice-with-python/Python projects/Probando Reconocimiento facial/videos/Leandro.mp4')

while True:
    answer,cameraOn=camera.read()
    if answer==False:break
    cameraOn=imutils.resize(cameraOn,width=640)
    gray=cv.cvtColor(cameraOn, cv.COLOR_BGR2GRAY)
    idcapture=gray.copy()
    faces=NOISE.detectMultiScale(gray,1.3,5)
    for(x,y,e1,e2) in faces:
        faceCapture=idcapture[y:y+e2,x:x+e1]
        faceCapture=cv.resize(faceCapture, (160,160),interpolation=cv.INTER_CUBIC)
        result=trainingEigenFaceRecognizer.predict(faceCapture)
        cv.putText(cameraOn, '{}'.format(result), (x,y-5), 1,1.3,(0,255,0),1,cv.LINE_AA)
        if result[1]< max_result:
            cv.putText(cameraOn, '{}'.format(listPerson[result[0]]), (x,y-20), 2,1.1,(0,255,0),1,cv.LINE_AA)
            cv.rectangle(cameraOn, (x,y), (x+e1,y+e2), (255,0,0),2)
        else:
            cv.putText(cameraOn,"is not found face...", (x,y-20), 2,0.7,(0,0,100),1,cv.LINE_AA)
            cv.rectangle(cameraOn, (x,y), (x+e1,y+e2), (0,0,100),2)

       
    cv.imshow("Results", cameraOn)
    if cv.waitKey(1)==ord('s'):
        break
camera.release()
cv.destroyAllWindows()