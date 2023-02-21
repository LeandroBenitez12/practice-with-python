import cv2 as cv
import numpy as np

un_peso_moneda_px = 9500
diez_peso_moneda_px = 10500

def ordenarPuntos(puntos):
    n_puntos= np.concatenate([puntos[0],puntos[1],puntos[2],puntos[3]]).tolist()
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
    contorno= cv.findContours(umbral, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[0]
    contorno = sorted(contorno, key= cv.contourArea,reverse=True)[:1]
    for c in contorno:
        epsilon = 0.01*cv.arcLength(c,True)
        approx = cv.approxPolyDP(c,epsilon,True)
        if len(approx)== 4:
            puntos = ordenarPuntos(approx)
            puntos1= np.float32(puntos)
            puntos2= np.float32([[0,0],[ancho,0],[0,alto],[ancho,alto]])
            Perspectiva = cv.getPerspectiveTransform(puntos1,puntos2)
            imagen_alineada = cv.warpPerspective(img, Perspectiva, (ancho,alto))
    return imagen_alineada

capturaVideo = cv.VideoCapture(0)


while True:
    typeCam, enVivo= capturaVideo.read()
    if typeCam == False:
        break

    imagen_A6 = alineamiento(enVivo, ancho= 480 ,alto=650)

    if imagen_A6 is not None:
        puntos= []
        gray = cv.cvtColor(imagen_A6,cv.COLOR_BGR2GRAY)
        blur = cv.GaussianBlur(gray,(5,5),1)
        _,umbral2 = cv.threshold(blur, 0, 255, cv.THRESH_OTSU+cv.THRESH_BINARY_INV)
        cv.imshow('Umbral2', umbral2)
        contorno2= cv.findContours(umbral2, cv.RETR_EXTERNAL ,cv.CHAIN_APPROX_SIMPLE)[0]
        cv.drawContours(imagen_A6, contorno2, -1, (0,0,255), 2 )
        suma1 = 0.0
        suma2 = 0.0
        for c2 in contorno2:
            area = cv.contourArea(c2)
            momentos = cv.moments(c2)
            if (momentos["m00"]) ==0:
                momentos["m00"]=1.0 #momento estatico
            x= int( momentos["m10"]/ momentos["m00"])
            y= int( momentos["m01"]/ momentos["m00"])

            if area<10500 and area>9800:
                font=cv.FONT_HERSHEY_SIMPLEX
                cv.putText(imagen_A6, "10 pesos",(x,y) , font, 0.75, (0,255,0),2)
                suma1=suma1+10.00
            
            if area<9500 and area>8500:
                font=cv.FONT_HERSHEY_SIMPLEX
                cv.putText(imagen_A6, "un peso",(x,y) , font, 0.75, (0,255,0),2)
                suma2=suma2+1.0 
        total = suma1 + suma2
        print(f'Sumatoria total en pesos: ${round(total,2)}')
        cv.imshow("Imagen A6", imagen_A6)
        cv.imshow("enVivo" , enVivo)
    if cv.waitKey(1)== ord('s'):
        break

capturaVideo.release()
cv.destroyAllWindows

