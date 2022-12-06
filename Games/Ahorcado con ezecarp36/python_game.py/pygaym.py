#importando librerias
import turtle 
import time
import random

#constantes y variables
posponer= 0.12
recorrido = 20
minimoArea= 290
cuerpos = []
distanciaAlimentacion = 20

#creando la pantalla del juego
ventana =  turtle.Screen()
ventana.title('Game of python')
ventana.bgcolor('black')
ventana.setup( width = 600, height= 600)
ventana.tracer(0)

#creando la cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape('square')
cabeza.color('yellow')
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = 'stop'

#creando la comida de la serpiente
comida = turtle.Turtle()
comida.speed(0)
comida.shape('circle')
comida.color('red')
comida.penup()
comida.goto(0,100)

#marcadores
score = 0
highscore = 0

#genero el texto del marcador
texto = turtle.Turtle()
texto.speed(0)
texto.color('white')
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write('score: 0     High Score:  0 ', 
    align= "center", font=('courier', 18, 'normal'))

def forward():
    cabeza.direction = 'forward'

def backward():
    cabeza.direction = 'backward'

def left():
    cabeza.direction = 'left'

def right():
    cabeza.direction = 'right'
#--------------------------------------------------------------------------------------------
#funcion del movimiento de la serpiente
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

#configurando teclas para mover a la serpiente
ventana.listen()
ventana.onkeypress(forward, 'Up')
ventana.onkeypress(backward, 'Down')
ventana.onkeypress(left, 'Left')
ventana.onkeypress(right, 'Right')

#juego en si
while True:
    
    #inicializamos ventana
    ventana.update()

    #choques contra los bordes
    if cabeza.xcor() > 280 or cabeza.ycor() < -280 or cabeza.ycor() > 280 or cabeza.xcor() < -280:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = 'stop'

        #manda al cuerpo de la serpiente lejos 
        for cuerpo in cuerpos:
            cuerpo.goto(1000,1000)

        #limpia los cuerpos
        cuerpos.clear()
        
        #resetear marcador
        score = 0
        texto.clear()
        texto.write('score: {}     High Score: {}'.format(score,highscore), 
    align= "center", font=('courier', 24, 'normal'))

    #serpiente se alimenta
    if cabeza.distance(comida) < distanciaAlimentacion:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x,y)
        #aumenta los puntos
        score += 10
        
        #genera nuevo cuerpo
        nuevoCuerpo = turtle.Turtle()
        nuevoCuerpo.speed(0)
        nuevoCuerpo.shape('square')
        nuevoCuerpo.color('blue')
        nuevoCuerpo.penup()
        cuerpos.append(nuevoCuerpo)

    #si hay nuevo record se reemplaza
    if score > highscore :
        highscore = score

    #texto para el tablero
    texto.clear()
    texto.write('score: {}     High Score: {}'.format(score,highscore), 
    align= "center", font=('courier', 24, 'normal'))

    #mover el cuerpo the python
    totalCuerpos = len(cuerpos)
    for index in range(totalCuerpos -1, 0, - 1):
        x = cuerpos[index -1].xcor()
        y = cuerpos[index -1].ycor()
        cuerpos[index].goto(x,y)
    if totalCuerpos > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        cuerpos[0].goto(x,y)

    #invoco a la funcion para que se mueva
    mov()

    #colisiones con el cuerpo
    for cuerpo in cuerpos:
        if cuerpo.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = 'stop'

            #manda al cuerpo de la serpiente lejos 
            for cuerpo in cuerpos:
                cuerpo.goto(1000,1000)
                
            #limpia los cuerpos
            cuerpos.clear()

            #resetear marcador
            score = 0
            texto.clear()
            texto.write('score: {}     High Score: {}'.format(score,highscore), 
                align= "center", font=('courier', 24, 'normal'))


    time.sleep(posponer)