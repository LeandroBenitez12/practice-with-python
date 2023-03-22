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

def drawPoints():
    x_text = 308
    y_text =  504
    arc.draw_text('Draw of various points',x_text, y_text, arc.color.BLACK)
    listPoint = (
        (380, 575),
        (380, 600),
        (420, 625),
        (420, 650)       
    )
    arc.draw_points(listPoint, arc.color.BLEU_DE_FRANCE, 10)

def drawRectangle():
    position_x = 600
    position_y = 600
    x_text = 508
    y_text =  504
    width = 50
    height = 50
    arc.draw_text('Draw Rectangle',x_text, y_text, arc.color.BLACK)
    arc.draw_rectangle_outline(position_x , position_y, width , height, arc.color.BLUE_BELL)
    arc.draw_rectangle_filled(625 , 625, width , height, arc.color.BLEU_DE_FRANCE)

#dibujar circulo
def drawCircle():
    x_text = 110
    y_text =  304
    arc.draw_text('Draw Circle', x_text, y_text, arc.color.BLACK)
    arc.draw_circle_outline(200, 400, 50, arc.color.BLUE_BELL)
    arc.draw_circle_filled(225, 425, 50, arc.color.BLACK_BEAN)

def drawLine():
    # Draw a line
    arc.draw_text("draw_line", 310, 304, arc.color.BLACK, 12)
    arc.draw_line(300, 300, 500, 500, arc.color.WARM_BLACK, 3)

def variousLines():
    arc.draw_text("draw_lines", 410, 304, arc.color.BLACK, 12)
    listLnes = ( 
        (505, 370),
        (505, 430),
        (520, 370),
        (520, 430),
        (540, 370),
        (540, 430),
        (580, 370),
        (580, 430),
        (605, 370),
        (605, 430),
        (620, 370),
        (620, 430),
        (640, 370),
        (640, 430),
        (680, 370),
        (680, 430),
        (695, 370),
        (695, 430)
    )
    arc.draw_lines(listLnes, arc.color.RED_DEVIL, 3)

def drawImg():
    # Load and draw an image to the screen
    # Image from kenney.nl asset pack #1
    arc.draw_text("draw_mario bros", 605, 103, arc.color.BLACK, 12)
    texture = arc.load_texture("mario_bros.png")
    scale = .6
    arc.draw_scaled_texture_rectangle(700, 120, texture, scale, 0)
    arc.draw_scaled_texture_rectangle(700, 160, texture, scale, 45)
# abrir ventana
arc.open_window(SCREEN_ANCHO, SCREEN_LARGO, SCREEN_TITULO)

# cambiar color de fondo ( background)
arc.set_background_color(arc.color.WHITE_SMOKE)

#limpia la screen y dibuja
arc.start_render()
# dibujo matriz de 3 x 3 para poner las figuras
getMatriz(min_dist_borde=100, max_dist_borde= 701, separacionMatrices= 200)

# dibujo en la primera fila primera columna  
getPoint()

# dibujo varios puntos 
drawPoints()

# dibujo rectangulo
drawRectangle()

# dibujo circulo
drawCircle()

# dibujo linea
drawLine()

#dibujo varias lineas
variousLines()

# dibujo imagen
drawImg()


# deja de dibujar
arc.finish_render()


arc.run()