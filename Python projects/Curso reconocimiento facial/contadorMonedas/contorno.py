import cv2 as cv

img = cv.imread('D:\\DESCARGAS\\2+Instalando+OpenCv\\monedascontorno\\contorno.jpg')
grey = cv.cvtColor(img ,cv.COLOR_BGR2GRAY)
typeUmbral,umbral = cv.threshold(grey,100,255,cv.THRESH_BINARY)
contorno, jerarquia = cv.findContours(umbral, cv.RETR_LIST , cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img, contorno, -1, (255,255,255), 3)


# Mostrar IMG
# cv.imshow('Umbral', umbral)
# cv.imshow('Grey Scale ', grey)
cv.imshow('Original Image', img)
cv.waitKey(0)
cv.destroyAllWindows()
# print(f'El umbral trabajado es: {typeUmbral}')
