import turtle 
import time
posponer= 0.12
recorrido = 20
minimoArea= 290


ventana =  turtle.Screen()
ventana.title('Game of python')
ventana.bgcolor('black')
ventana.setup( width = 600, height= 600)
ventana.tracer(0)

cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape('square')
cabeza.color('white')
cabeza.penup()
cabeza.goto(100,0)
cabeza.direction = 'stop'

cabeza2 = turtle.Turtle()
cabeza2.speed(0)
cabeza2.shape('square')
cabeza2.color('red')
cabeza2.penup()
cabeza2.goto(-100,0)
cabeza2.direction = 'stop'

def forward1():
    cabeza.direction = 'forward'

def backward1():
    cabeza.direction = 'backward'

def left1():
    cabeza.direction = 'left'

def right1():
    cabeza.direction = 'right'

def forward2():
    cabeza2.direction = 'forward'

def backward2():
    cabeza2.direction = 'backward'

def left2():
    cabeza2.direction = 'left'

def right2():
    cabeza2.direction = 'right'

def mov():
    if cabeza.direction == 'forward':
        y = cabeza.ycor()
        cabeza.sety(y + recorrido)

    if cabeza.direction == 'backward':
        y = cabeza.ycor()
        cabeza.sety(y - recorrido)

    if cabeza.direction == 'right':
        x = cabeza.xcor()
        cabeza.setx(x + recorrido)

    if cabeza.direction == 'left':
        x = cabeza.xcor()
        cabeza.setx(x - recorrido)

    if cabeza.ycor() > minimoArea or cabeza.ycor() < -minimoArea:
        cabeza.direction = 'stop'
    
    if cabeza.xcor() > minimoArea or cabeza.xcor() < -minimoArea:
        cabeza.direction = 'stop'

def mov2():
    if cabeza2.direction == 'forward':
        y = cabeza2.ycor()
        cabeza2.sety(y + recorrido)

    if cabeza2.direction == 'backward':
        y = cabeza2.ycor()
        cabeza2.sety(y - recorrido)

    if cabeza2.direction == 'right':
        x = cabeza2.xcor()
        cabeza2.setx(x + recorrido)

    if cabeza2.direction == 'left':
        x = cabeza2.xcor()
        cabeza2.setx(x - recorrido)

    if cabeza2.ycor() > minimoArea or cabeza2.ycor() < -minimoArea:
        cabeza2.direction = 'stop'
    
    if cabeza2.xcor() > minimoArea or cabeza2.xcor() < -minimoArea:
        cabeza2.direction = 'stop'

#teclado
ventana.listen()
ventana.onkeypress(forward1, 'Up')
ventana.onkeypress(backward1, 'Down')
ventana.onkeypress(left1, 'Left')
ventana.onkeypress(right1, 'Right')
ventana.onkeypress(forward2, 'w')
ventana.onkeypress(backward2, 's')
ventana.onkeypress(left2, 'a')
ventana.onkeypress(right2, 'd')

while True:
    ventana.update()

    mov()
    mov2()
    time.sleep(posponer)