import arcade as arc

#Constants
SCREEN_ANCHO  = 800
SCREEN_LARGO  = 800
SCREEN_TITULO  = 'PRUEBA 1'

# Variables globals



# abrir ventana
arc.open_window(SCREEN_ANCHO, SCREEN_LARGO, SCREEN_TITULO)

# cambiar color de fondo ( background)
arc.set_background_color(arc.color.WHITE_SMOKE)

#limpia la screen y dibuja
arc.start_render()

# dibujo matriz de 3 x 3 para poner las figuras
for x in range(100, 701, 200):
    arc.draw_line(start_x=x , start_y= 100, end_x = x, end_y= 700, color= arc.color.BLUE_BELL, line_width= 3)

for y in range( 100, 701, 200):
    arc.draw_line(start_x=100,start_y=y, end_x=700, end_y=y, color=arc.color.BLUE_BELL, line_width= 3)

# deja de dibujar
arc.finish_render()


arc.run()