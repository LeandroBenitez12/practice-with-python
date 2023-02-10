import cv2 as cv
import numpy as np
value_gauss= 3 
original = cv.imread('D:\DESCARGAS\monedascontorno\monedascontorno\monedas.jpg')
gray = cv.cvtColor(original , cv.COLOR_BGR2GRAY)
gauss = cv.GaussianBlur(gray, (value_gauss , value_gauss), 0)
canny = cv.Canny(gauss,50,99)

#mostrar resultado
# cv.imshow('Original Image', original)
cv.imshow('Gray Image', gray)
cv.imshow('Gauss Image', gauss)
cv.imshow('canny Image', canny)
cv.waitKey(0)
cv.destroyAllWindows()