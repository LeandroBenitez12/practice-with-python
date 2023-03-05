import cv2 as cv
import os
import imutils

NOISE = cv.CascadeClassifier('C:/Users/juana/Dropbox/GIT/practice-with-python/Python projects/Curso reconocimiento facial/reconocimientoFacial/Modelos de entrenamiento/haarcascade_frontalface_default.xml')

max_id = 351

#paths 
nameFolder='Auron'
pathFolders= 'D:/dataPhotos'
pathPerson= pathFolders + '/' + nameFolder


if not os.path.exists(pathPerson):
    print(f'Path created in: {pathPerson}')
    os.makedirs(pathPerson)

# En vivo le decimos que la video captura es interna (0)
# camera = cv.VideoCapture(0)

# video Auron
camera = cv.VideoCapture('C:/Users/juana/Dropbox/GIT/practice-with-python/Python projects/Probando Reconocimiento facial/videos/videoauron.mp4')

# video Elon
# camera = cv.VideoCapture('C:/Users/juana/Dropbox/GIT/practice-with-python/Python projects/Probando Reconocimiento facial/videos/ElonMusk.mp4')

# video Juana
# camera = cv.VideoCapture('C:/Users/juana/Dropbox/GIT/practice-with-python/Python projects/Probando Reconocimiento facial/videos/Juana.mp4')

# video Juan
# camera = cv.VideoCapture('C:/Users/juana/Dropbox/GIT/practice-with-python/Python projects/Probando Reconocimiento facial/videos/Juan.mp4')

# video Leandro
# camera = cv.VideoCapture('C:/Users/juana/Dropbox/GIT/practice-with-python/Python projects/Probando Reconocimiento facial/videos/Leandro.mp4')
id=0
while True:
    answer, cameraOn = camera.read()
    if answer == False: break

    cameraOn = imutils.resize(cameraOn, width= 640)

    gray = cv.cvtColor(cameraOn, cv.COLOR_BGR2GRAY)

    faces = NOISE.detectMultiScale(gray,1.3,5)

    id_capture = cameraOn.copy()
    
    for (x,y,h,b) in faces:
        cv.rectangle(cameraOn, (x,y), (x+h,y+b), (0,100,0),2)
        captureFace = id_capture[y:y+h,x:x+b]
        captureFace = cv.resize(captureFace, [600,600],interpolation=cv.INTER_CUBIC)
        cv.imwrite(pathPerson+f'/img_{id}.jpg', captureFace)
        id= id +1
    cv.imshow('Capturing...', cameraOn)
    if id > max_id: break
    
camera.release()
cv.destroyAllWindows()

