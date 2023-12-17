### Python Package Manager

# pip es un gestor para descargar actualizacion y librerias

import numpy as np

print(np.version.release)

np_array = np.array([1,2,3,4,5,6])

print(type(np_array))
print(np_array)
print(np_array * .5)

array = [0,1,2,3,4,5,6]
print(array * 2) #diferencias con libreria 

import pandas as pd 

# pip list
# pip uninstall (lib)

import requests as rq 

response = rq.get("https://pokeapi.co/api/v2/pokemon?limit=151")

print(response.status_code)
# print(response.json())

from mypackage import arithmetics

print(arithmetics.sum_two_values(2,3))