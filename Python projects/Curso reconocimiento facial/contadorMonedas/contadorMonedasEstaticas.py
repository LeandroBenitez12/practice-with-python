import cv2 as cv
import numpy as np
value_gauss= 3 
value_kernel= 8
original = cv.imread('C:\\Users\\juana\\OneDrive\\Documentos\\Downloads\\monedascontorno\\monedascontorno\\monedas2.jpg')
gray = cv.cvtColor(original , cv.COLOR_BGR2GRAY)
gauss = cv.GaussianBlur(gray, (value_gauss , value_gauss), 0)
canny = cv.Canny(gauss,50,99)
kernel = np.ones((value_kernel, value_kernel), np.uint8)
cierre= cv.morphologyEx(canny, cv.MORPH_CLOSE, kernel)


contorno, jerarquia = cv.findContours(cierre.copy(), cv.RETR_EXTERNAL ,cv.CHAIN_APPROX_SIMPLE)

print(f'Monedas encontradas: {format(len(contorno))}')
cv.drawContours(original, contorno, -1, (255,50,130), 2)


#mostrar resultado
# cv.imshow('Original Image', original)
# cv.imshow('Gray Image', gray)
# cv.imshow('Gauss Image', gauss)
# cv.imshow('canny Image', canny)
cv.imshow('cierre', cierre)
cv.imshow('Resultado', original)
cv.waitKey(0)
cv.destroyAllWindows()