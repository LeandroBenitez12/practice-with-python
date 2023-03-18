import arcade as arc

#Constants
SCREEN_ANCHO  = 600
SCREEN_LARGO  = 600
SCREEN_TITULO  = 'PRUEBA 1'

# Variables globals



# abrir ventana
arc.open_window(SCREEN_ANCHO, SCREEN_LARGO, SCREEN_TITULO)

# cambiar color de fondo ( background)
arc.set_background_color(arc.color.AERO_BLUE)

#limpia la screen y dibuja
arc.start_render()

# dibujar 2 cuadrados

# deja de dibujar
arc.finish_render()


arc.run()