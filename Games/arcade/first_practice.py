import arcade as arc

#Constants
SCREEN_ANCHO  = 800
SCREEN_LARGO  = 800
SCREEN_TITULO  = 'PRUEBA 1'

# Variables globals



# funciones 
def getGrilla(min_dist_borde, max_dist_borde,separacionGrillas):
    for x in range(min_dist_borde, max_dist_borde, separacionGrillas):
        arc.draw_line(start_x=x , start_y= min_dist_borde, end_x = x, end_y= max_dist_borde, color= arc.color.BLUE_BELL, line_width= 3)

    for y in range( min_dist_borde, max_dist_borde, separacionGrillas):
        arc.draw_line(start_x=min_dist_borde,start_y=y, end_x=max_dist_borde, end_y=y, color=arc.color.BLUE_BELL, line_width= 3)

# abrir ventana
arc.open_window(SCREEN_ANCHO, SCREEN_LARGO, SCREEN_TITULO)

# cambiar color de fondo ( background)
arc.set_background_color(arc.color.WHITE_SMOKE)

#limpia la screen y dibuja
arc.start_render()
# dibujo matriz de 3 x 3 para poner las figuras
getGrilla(min_dist_borde=100, max_dist_borde= 701, separacionGrillas= 200)

# deja de dibujar
arc.finish_render()


arc.run()