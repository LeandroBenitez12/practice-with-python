import cv2 as cv
import numpy as np

def ordenarPutos(puntos):
    n_puntos= np.concatenate(puntos[0],puntos[1],puntos[2],puntos[3]).tolist()
    y_order = sorted(n_puntos, key=lambda n_puntos : n_puntos[1])
    x1_order = y_order[:2]
    x1_order = sorted(x1_order, key=lambda x1_order : x1_order[0])
    x2_order = y_order[2:4]
    x2_order = sorted(x2_order, key=lambda x2_order:x2_order[0])
    return [x1_order[0],x1_order[1],x2_order[0],x2_order[1]]

def alineamiento(img,ancho,alto):
    imagen_alineada= None
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    type_umbral, umbral = cv.threshold(gray, 140, 255, cv.THRESH_BINARY)
    cv.imshow('Umbral', umbral)
    contorno, jerarquia = cv.findContours(umbral, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[0]
    contorno = sorted(contorno, key= cv.contourArea,reverse=True)[:1]
    for c in contorno:
        epsilon = .01*cv.arcLength(c,True)
        approx = cv.approxPolyDP(c,epsilon,True)
        if (approx)== 4:
            puntos = ordenarPutos(approx)
            puntos1= np.float32(puntos)
            puntos2= np.float32([[0,0],[ancho,0][0,alto],[ancho,alto]])
            Perspectiva = cv.getPerspectiveTransform(puntos1,puntos2)
            imagen_alineada = cv.warpPerspective(img, Perspectiva, (ancho,alto))
    return imagen_alineada

capturaVideo = cv.VideoCapture(0)


while True:
    typeCam, enVivo= capturaVideo.read()
    if typeCam == False:
        break

    imagen_A6 = alineamiento(enVivo, ancho= 480,alto=677)

    if imagen_A6 is not None:
        puntos= []
        gray = cv.cvtColor(imagen_A6,cv.COLOR_BGR2GRAY)
        blur = cv.GaussianBlur(gray,(5,5),1)
        _,umbral = cv.threshold(blur, 0, 255, cv.THRESH_BINARY_INV)
        cv.imshow('Umbral', umbral)
        contorno2, jerarquia2 = cv.findContours(umbral, cv.RETR_EXTERNAL ,cv.CHAIN_APPROX_SIMPLE)[0]
        cv.drawContours(imagen_A6, contorno2, -1, (0,255,0), 2 )
        suma1 = 0.0
        suma2 = 0.0
        for c2 in contorno2:
            area = cv.contourArea(c2)
            momentos = cv.moments(c2)
            if (momentos["m00"]) ==0:
                momentos["m00"]=1.0 #momento estatico


    cv.imshow('En vivo', enVivo)
    if ord() == 'q':
        break

capturaVideo.release()
cv.destroyAllWindows

