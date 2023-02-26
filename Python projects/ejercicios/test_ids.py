import os
import cv2 as cv

semi_ruta= 'D:/dataFotos'
lista_ruta = os.listdir(semi_ruta)
print(lista_ruta)
ids =[]
rostrosData = []
id = 0
for contenedoras_img in lista_ruta:
    rutaCompleta = semi_ruta + '/' + contenedoras_img
    for archivo in rutaCompleta:
        ids.append(id)
        rostrosData.append(cv.imread(rutaCompleta + '/' + archivo,0))
        imagenes = cv.imread(rutaCompleta+ '\\'+ archivo,0)
    id = id+1

print(imagenes)
