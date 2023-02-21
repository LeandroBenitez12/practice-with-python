import cv2 as cv

camara = cv.VideoCapture(0)

if not camara.isOpened():
    print('No hay camara...')
    exit()

while True:
    _, enVivo = camara.read()
    gray = cv.cvtColor(enVivo, cv.COLOR_BGR2GRAY)
    cv.imshow('En vivo', gray)
    teclado = cv.waitKey(1)
    if teclado == ord('q'):
        break

camara.release()
cv.destroyAllWindows()


