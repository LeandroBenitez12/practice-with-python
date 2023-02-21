import cv2 as cv
import numpy as np

Origin = cv.imread('')
gray = cv.cvtColor(Origin ,cv.COLOR_BAYER_BG2BGR, )
_, umbralizada= cv.threshold(gray,100,255,cv.THRESH_BINARY)

#Mostrar imgs
cv.imshow('Origin', Origin)
cv.waitKey(1)
cv.destroyAllWindows()