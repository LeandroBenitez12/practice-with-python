import arcade as arc

#Constants
SCREEN_ANCHO  = 800
SCREEN_LARGO  = 800
SCREEN_TITULO  = 'PRUEBA 1'

# Variables globals



# funciones 
def getMatriz(min_dist_borde, max_dist_borde,separacionMatrices):
    for x in range(min_dist_borde, max_dist_borde, separacionMatrices):
        arc.draw_line(start_x=x , start_y= min_dist_borde, end_x = x, end_y= max_dist_borde, color= arc.color.BLUE_BELL, line_width= 3)

    for y in range( min_dist_borde, max_dist_borde, separacionMatrices):
        arc.draw_line(start_x=min_dist_borde,start_y=y, end_x=max_dist_borde, end_y=y, color=arc.color.BLUE_BELL, line_width= 3)

def getPoint():
    x_point = 200
    y_point = 600
    x_text = 108
    y_text =  504
    arc.draw_text('Draw point', x_text, y_text, arc.color.BLACK)
    arc.draw_point(x_point, y_point, arc.color.GREEN, 10)

# abrir ventana
arc.open_window(SCREEN_ANCHO, SCREEN_LARGO, SCREEN_TITULO)

# cambiar color de fondo ( background)
arc.set_background_color(arc.color.WHITE_SMOKE)

#limpia la screen y dibuja
arc.start_render()
# dibujo matriz de 3 x 3 para poner las figuras
getMatriz(min_dist_borde=100, max_dist_borde= 701, separacionMatrices= 200)

# dijuo en la primera fila primera columna un 
getPoint()
# deja de dibujar
arc.finish_render()


arc.run()