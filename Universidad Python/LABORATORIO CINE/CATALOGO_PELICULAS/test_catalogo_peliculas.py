from DOMINIO.Pelicula import Pelicula
from SERVICIOS.catalogoPeliculas import CatalogoPeliculas as cp
ValueMenu = None
while ValueMenu != 4:
    try:
        print('''
            ----------Menu----------
            1.Agregar pelicula
            2.Listar pelicula
            3.Eliminar pelicula
            4. Salir
            '''
            )
        ValueMenu = int(input(f' Ingrese un valor(1-4): '))        
        if ValueMenu == 1:
            nombrePelicula = input('Ingrese el nombre de la pelicula:    ')
            Peli = Pelicula(nombrePelicula)
            cp.addMovie(Peli)
        elif ValueMenu == 2:
            cp.listarPelis()
        elif ValueMenu == 3:
            cp.eliminate()

    except Exception as e:
        print ("Ocurrio un error {e}")
        ValueMenu = None

else:
    print ("Salimos del programa...")