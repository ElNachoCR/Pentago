from Matriz import *

def setup():
    
    global jugador1Coloca, jugador1Rota, jugador1Direccion, jugador2Coloca, jugador2Rota, jugador2Direccion, c1, c2, c3, c4, jugador1Gana, jugador2Gana, rotada
    
    # Variables de control de turnos
    jugador1Coloca = True
    jugador1Rota = False
    jugador1Direccion = False
    
    jugador2Coloca = False
    jugador2Rota = False
    jugador2Direccion = False
    
    jugador1Gana = False
    jugador2Gana = False
    
    empate = False
    
    rotada = 0
    
    
    # Ventana
    size(800,700)
    background(100)
    
    # Cuadrantes
    c1 = Matriz(240,130)
    c2 = Matriz(440,130)
    c3 = Matriz(240,330)
    c4 = Matriz(440,330)

def draw():
    global jugador1Coloca, jugador1Rota, jugador2Coloca, jugador2Rota
    background(100)
    fill(139,40,0)
    strokeWeight(4)
    rectMode(CORNER)
    rect(200,100,400,400,15)
    line(400,100,400,500)
    line(200,300,600,300)
    
    c1.display()
    c2.display()
    c3.display()
    c4.display()
    
    textAlign(CENTER)
    textSize(30)
    
    
    
    if jugador1Coloca:
        fill(255)
        text("Jugador 1, coloque su ficha", width/2,600)
    
    elif jugador1Rota:
        fill(255)
        text("Jugador 1, rote una seccion",width/2,600)
        
    elif jugador1Direccion:
        fill(255)
        text("Jugador 1, elija la direccion de la rotacion",width/2,600)
        fill(139,40,0)
        strokeWeight(1)
        rectMode(CENTER)
        rect(width/2-150,650,120,60)
        fill(255)
        textSize(20)
        text("Izquierda",width/2-150,655)
        fill(139,40,0)
        rect(width/2+150,650,120,60)
        fill(255)
        text("Derecha",width/2+150,655)
    
    elif jugador2Coloca:
        fill(0)
        text("Jugador 2, coloque su ficha",width/2,600)
    
    elif jugador2Rota:
        fill(0)
        text("Jugador 2, rote una seccion",width/2,600)
    
    elif jugador2Direccion:
        fill(0)
        text("Jugador 2, elija la direccion de la rotacion", width/2,600)
        fill(139,40,0)
        strokeWeight(1)
        rectMode(CENTER)
        rect(width/2-150,650,120,60)
        fill(0)
        textSize(20)
        text("Izquierda",width/2-150,655)
        fill(139,40,0)
        rect(width/2+150,650,120,60)
        fill(0)
        text("Derecha",width/2+150,655)
    
    elif jugador1Gana:
        fill(255)
        text("Gana el jugador 1!", width/2,600)
    
    elif jugador2Gana:
        fill(0)
        text("Gana el jugador 2!", width/2,600)
    
    elif empate:
        fill(255)
        text("Empate!", width/2,600)
    
    
    strokeWeight(1)
    fill(139,40,0)
    rectMode(CORNER)
    rect(675,5,100,50)
    fill(255)
    textSize(30)
    text("Reset", width-75,40)
    mouseOver()


    
def mousePressed():
    global jugador1Coloca, jugador2Coloca, jugador1Rota, jugador2Rota, jugador1Direccion, jugador1Direccion, jugador2Direccion        
    juego()
    rotada = 0


## Dependiendo de la etapa en la que se encuentra el juego
## esta función crea un fantasma blanco si es el turno del
## jugador 1 o negro si es del jugador 2, o si el juego se
## terminó, no crea ningun fantasma.
## Entradas:
##      None
## Salidas:
##      Fantasma del color del jugador
## Restricciones:
##      None
def mouseOver():
    ## Señala el espacio
    if jugador1Coloca or jugador1Rota or jugador1Direccion:
        fill(255,255,255,75)
        
    elif jugador2Coloca or jugador2Rota or jugador2Direccion:
        fill(0,0,0,175)
    
    if (675 <= mouseX <= 775) and (5 <= mouseY <= 55):
        rect(675,5,100,50)
        
    # Cuadrante 1 - 0,0
    if (220 <= mouseX <= 260) and (110 <= mouseY <= 150) and c1.matriz[0][0] == 0 and (jugador1Coloca or jugador2Coloca):
        ellipse(240,130,40,40)
        
    # Cuadrante 1 - 0,1
    if (280 <= mouseX <= 320) and (110 <= mouseY <= 150) and c1.matriz[0][1] == 0 and (jugador1Coloca or jugador2Coloca):
        ellipse(300,130,40,40)
        
    # Cuadrante 1 - 0,2
    if (340 <= mouseX <= 380) and (110 <= mouseY <= 150) and c1.matriz[0][2] == 0 and (jugador1Coloca or jugador2Coloca):
        ellipse(360,130,40,40)
    
    # Cuadrante 1 - 1,0
    if (220 <= mouseX <= 260) and (180 <= mouseY <= 220) and c1.matriz[1][0] == 0 and (jugador1Coloca or jugador2Coloca):
        ellipse(240,200,40,40)
        
    # Cuadrante 1 - 1,1
    if (280 <= mouseX <= 320) and (180 <= mouseY <= 220) and c1.matriz[1][1] == 0 and (jugador1Coloca or jugador2Coloca):
        ellipse(300,200,40,40)
        
    # Cuadrante 1 - 1,2
    if (340 <= mouseX <= 380) and (180 <= mouseY <= 220) and c1.matriz[1][2] == 0 and (jugador1Coloca or jugador2Coloca):
        ellipse(360,200,40,40)
        
    # Cuadrante 1 - 2,0
    if (220 <= mouseX <= 260) and (250 <= mouseY <= 290) and c1.matriz[2][0] == 0 and (jugador1Coloca or jugador2Coloca):
        ellipse(240,270,40,40)
        
    # Cuadrante 1 - 2,1
    if (280 <= mouseX <= 320) and (250 <= mouseY <= 290) and c1.matriz[2][1] == 0 and (jugador1Coloca or jugador2Coloca):
        ellipse(300,270,40,40)
    
    # Cuadrante 1 - 2,2
    if (340 <= mouseX <= 380) and (250 <= mouseY <= 290) and c1.matriz[2][2] == 0 and (jugador1Coloca or jugador2Coloca):
        ellipse(360,270,40,40)
        
        
    # Cuadrante 2 - 0,0
    if (420 <= mouseX <= 460) and (110 <= mouseY <= 150) and c2.matriz[0][0] == 0 and (jugador1Coloca or jugador2Coloca):
        ellipse(440,130,40,40)
        
    # Cuadrante 2 - 0,1
    if (480 <= mouseX <= 520) and (110 <= mouseY <= 150) and c2.matriz[0][1] == 0 and (jugador1Coloca or jugador2Coloca):
        ellipse(500,130,40,40)
        
    # Cuadrante 2 - 0,2
    if (540 <= mouseX <= 580) and (110 <= mouseY <= 150) and c2.matriz[0][2] == 0 and (jugador1Coloca or jugador2Coloca):
        ellipse(560,130,40,40)
        
    # Cuadrante 2 - 1,0
    if (420 <= mouseX <= 460) and (180 <= mouseY <= 220) and c2.matriz[1][0] == 0 and (jugador1Coloca or jugador2Coloca):
        ellipse(440,200,40,40)
    
    # Cuadrante 2 - 1,1
    if (480 <= mouseX <= 520) and (180 <= mouseY <= 220) and c2.matriz[1][1] == 0 and (jugador1Coloca or jugador2Coloca):
        ellipse(500,200,40,40)
        
    # Cuadrante 2 - 1,2
    if (540 <= mouseX <= 580) and (180 <= mouseY <= 220) and c2.matriz[1][2] == 0 and (jugador1Coloca or jugador2Coloca):
        ellipse(560,200,40,40)
    
    # Cuadrante 2 - 2,0
    if (420 <= mouseX <= 460) and (250 <= mouseY <= 290) and c2.matriz[2][0] == 0 and (jugador1Coloca or jugador2Coloca):
        ellipse(440,270,40,40)
        
    # Cuadrante 2 - 2,1
    if (480 <= mouseX <= 520) and (250 <= mouseY <= 290) and c2.matriz[2][1] == 0 and (jugador1Coloca or jugador2Coloca):
        ellipse(500,270,40,40)
        
    # Cuadrante 2 - 2,2
    if (540 <= mouseX <= 580) and (250 <= mouseY <= 290) and c2.matriz[2][2] == 0 and (jugador1Coloca or jugador2Coloca):
        ellipse(560,270,40,40)
    
    # Cuadrante 3 - 0,0
    if (220 <= mouseX <= 260) and (310 <= mouseY <= 350) and c3.matriz[0][0] == 0 and (jugador1Coloca or jugador2Coloca):
        ellipse(240,330,40,40)
        
    # Cuadrante 3 - 0,1
    if (280 <= mouseX <= 320) and (310 <= mouseY <= 350) and c3.matriz[0][1] == 0 and (jugador1Coloca or jugador2Coloca):
        ellipse(300,330,40,40)
    
    # Cuadrante 3 - 0,2
    if (340 <= mouseX <= 380) and (310 <= mouseY <= 350) and c3.matriz[0][2] == 0 and (jugador1Coloca or jugador2Coloca):
        ellipse(360,330,40,40)
        
    # Cuadrante 3 - 1,0
    if (220 <= mouseX <= 260) and (380 <= mouseY <= 420) and c3.matriz[1][0] == 0 and (jugador1Coloca or jugador2Coloca):
        ellipse(240,400,40,40)
    
    # Cuadrante 3 - 1,1
    if (280 <= mouseX <= 320) and (380 <= mouseY <= 420) and c3.matriz[1][1] == 0 and (jugador1Coloca or jugador2Coloca):
        ellipse(300,400,40,40)
        
    # Cuadrante 3 - 1,2
    if (340 <= mouseX <= 380) and (380 <= mouseY <= 420) and c3.matriz[1][2] == 0 and (jugador1Coloca or jugador2Coloca):
        ellipse(360,400,40,40)
        
    # Cuadrante 3 - 2,0
    if (220 <= mouseX <= 260) and (450 <= mouseY <= 490) and c3.matriz[2][0] == 0 and (jugador1Coloca or jugador2Coloca):
        ellipse(240,470,40,40)
        
    # Cuadrante 3 - 2,1
    if (280 <= mouseX <= 320) and (450 <= mouseY <= 490) and c3.matriz[2][1] == 0 and (jugador1Coloca or jugador2Coloca):
        ellipse(300,470,40,40)
        
    # Cuadrante 3 - 2,2
    if (340 <= mouseX <= 380) and (450 <= mouseY <= 490) and c3.matriz[2][2] == 0 and (jugador1Coloca or jugador2Coloca):
        ellipse(360,470,40,40)
        
    # Cuadrante 4 - 0,0
    if (420 <= mouseX <= 460) and (310 <= mouseY <= 350) and c4.matriz[0][0] == 0 and (jugador1Coloca or jugador2Coloca):
        ellipse(440,330,40,40)
        
    # Cuadrante 4 - 0,1
    if (480 <= mouseX <= 520) and (310 <= mouseY <= 350) and c4.matriz[0][1] == 0 and (jugador1Coloca or jugador2Coloca):
        ellipse(500,330,40,40)
          
    # Cuadrante 4 - 0,2
    if (540 <= mouseX <= 580) and (310 <= mouseY <= 350) and c4.matriz[0][2] == 0 and (jugador1Coloca or jugador2Coloca):
        ellipse(560,330,40,40)
        
    # Cuadrante 4 - 1,0
    if (420 <= mouseX <= 460) and (380 <= mouseY <= 420) and c4.matriz[1][0] == 0 and (jugador1Coloca or jugador2Coloca):
        ellipse(440,400,40,40)
        
    # Cuadrante 4 - 1,1
    if (480 <= mouseX <= 520) and (380 <= mouseY <= 420) and c4.matriz[1][1] == 0 and (jugador1Coloca or jugador2Coloca):
        ellipse(500,400,40,40)
        
    # Cuadrante 4 - 1,2
    if (540 <= mouseX <= 580) and (380 <= mouseY <= 420) and c4.matriz[1][2] == 0 and (jugador1Coloca or jugador2Coloca):
        ellipse(560,400,40,40)
        
    # Cuadrante 4 - 2,0
    if (420 <= mouseX <= 460) and (450 <= mouseY <= 490) and c4.matriz[2][0] == 0 and (jugador1Coloca or jugador2Coloca):
        ellipse(440,470,40,40)
        
    # Cuadrante 4 - 2,1
    if (480 <= mouseX <= 520) and (450 <= mouseY <= 490) and c4.matriz[2][1] == 0 and (jugador1Coloca or jugador2Coloca):
        ellipse(500,470,40,40)
        
    # Cuadrante 4 - 2,2
    if (540 <= mouseX <= 580) and (450 <= mouseY <= 490) and c4.matriz[2][0] == 0 and (jugador1Coloca or jugador2Coloca):
        ellipse(560,470,40,40)
    
    ## Elijiendo cuadrante para rotar
    # Cuadrante 1
    if (200 <= mouseX <= 400) and (100 <= mouseY <= 300) and (jugador1Rota or jugador2Rota):
        rect(200,100,200,200,15,0,0,0)
    
    # Cuadrante 2
    if (401 <= mouseX <= 600) and (100 <= mouseY <= 300) and (jugador1Rota or jugador2Rota):
        rect(400,100,200,200,0,15,0,0)
    
    # Cuadrante 3
    if (200 <= mouseX <= 400) and (301 <= mouseY <= 500) and (jugador1Rota or jugador2Rota):
        rect(200,300,200,200,0,0,0,15)
    
    # Cuadrante 4
    if (401 <= mouseX <= 600) and (301 <= mouseY <= 500) and (jugador1Rota or jugador2Rota):
        rect(400,300,200,200,0,0,15,0)
        
    ## Elejir direccion
    # Izquierda
    if (190 <= mouseX <= 310) and (620 <= mouseY <= 680) and (jugador1Direccion or jugador2Direccion):
        rectMode(CENTER)
        rect(width/2-150,650,120,60)
        
    # Derecha
    if (490 <= mouseX <= 610) and (620 <= mouseY <= 680) and (jugador1Direccion or jugador2Direccion):
        rectMode(CENTER)
        rect(width/2+150,650,120,60)
        
## Esta función contiene todas las posibles victorias,
## y termina el juego si el tablero está lleno y nadie 
## algún jugador consiguió tener 5 en raya o si hubo
## un empate.
## Entradas:
##      None
## Salidas:
##      Victoria o empate
## Restroccopmes:
##      None
def check():
    global jugador1Coloca, jugador1Rota, jugador1Direccion, jugador2Coloca, jugador2Rota, jugador2Direccion, c1, c2, c3, c4, jugador1Gana, jugador2Gana, empate
    
    # 0
    if c1.matriz[1][0] == c1.matriz[2][1] == c3.matriz[0][2] == c4.matriz[1][0] == c4.matriz[2][1] != 0:
        reset()
        if c1.matriz[1][0] == 1:
            jugador1Gana = True
        else:
            jugador2Gana = True
    
    # 1
    elif c1.matriz[0][1] == c1.matriz[1][2] == c2.matriz[2][0] == c4.matriz[0][1] == c4.matriz[1][2] != 0:
        reset()
        if c1.matriz[0][1] == 1:
            jugador1Gana = True
        else:
            jugador2Gana = True
    
    # 2
    elif c3.matriz[1][0] == c3.matriz[0][1] == c1.matriz[2][2] == c2.matriz[1][0] == c2.matriz[0][1] != 0:
        reset()
        if c3.matriz[1][0] == 1:
            jugador1Gana = True
        else:
            jugador2Gana = True
        
    # 3
    elif c3.matriz[2][1] == c3.matriz[1][2] == c4.matriz[0][0] == c2.matriz[2][1] == c2.matriz[1][2] != 0:
        reset()
        if c3.matriz[2][1] == 1:
            jugador1Gana = True
        else:
            jugador2Gana = True
            
    # 4
    elif c1.matriz[0][0] == c1.matriz[1][1] == c1.matriz[2][2] == c4.matriz[0][0] == c4.matriz[1][1] != 0:
        reset()
        if c1.matriz[0][0] == 1:
            jugador1Gana = True
        else:
            jugador2Gana = True
        
    # 5
    elif c1.matriz[1][1] == c1.matriz[2][2] == c4.matriz[0][0] == c4.matriz[1][1] == c4.matriz[2][2] != 0:
        reset()
        if c1.matriz[1][1] == 1:
            jugador1Gana = True
        else:
            jugador2Gana = True
            
    # 6
    elif c3.matriz[2][0] == c3.matriz[1][1] == c3.matriz[0][2] == c2.matriz[2][0] == c2.matriz[1][1] != 0:
        reset()
        if c3.matriz[2][0] == 1:
            jugador1Gana = True
        else:
            jugador2Gana = True
            
    # 7
    elif c3.matriz[1][1] == c3.matriz[0][2] == c2.matriz[2][0] == c2.matriz[1][1] == c2.matriz[0][2] != 0:
        reset()
        if c3.matriz[1][1] == 1:
            jugador1Gana = True
        else:
            jugador2Gana = True
        
    # 8
    elif c1.matriz[0][0] == c1.matriz[1][0] == c1.matriz[2][0] == c3.matriz[0][0] == c3.matriz[1][0] != 0:
        reset()
        if c1.matriz[0][0] == 1:
            jugador1Gana = True
        else:
            jugador2Gana = True
        
    # 9
    elif c1.matriz[1][0] == c1.matriz[2][0] == c3.matriz[0][0] == c3.matriz[1][0] == c3.matriz[2][0] != 0:
        reset()
        if c1.matriz[1][0] == 1:
            jugador1Gana = True
        else:
            jugador2Gana = True
            
    # 10
    elif c1.matriz[0][1] == c1.matriz[1][1] == c1.matriz[2][1] == c3.matriz[0][1] == c3.matriz[1][1] != 0:
        reset()
        if c1.matriz[0][1] == 1:
            jugador1Gana = True
        else:
            jugador2Gana = True
            
    # 11
    elif c1.matriz[1][1] == c1.matriz[2][1] == c3.matriz[0][1] == c3.matriz[1][1] == c3.matriz[2][1] != 0:
        reset()
        if c1.matriz[1][1] == 1:
            jugador1Gana = True
        else:
            jugador2Gana = True
            
    # 12
    elif c1.matriz[0][2] == c1.matriz[1][2] == c1.matriz[2][2] == c3.matriz[0][2] == c3.matriz[1][2] != 0:
        reset()
        if c1.matriz[0][2] == 1:
            jugador1Gana = True
        else:
            jugador2Gana = True
            
    # 13
    elif c1.matriz[1][2] == c1.matriz[2][2] == c3.matriz[0][2] == c3.matriz[1][2] == c3.matriz[2][2] != 0:
        reset()
        if c1.matriz[1][2] == 1:
            jugador1Gana = True
        else:
            jugador2Gana = True
            
    # 14
    elif c2.matriz[0][0] == c2.matriz[1][0] == c2.matriz[2][0] == c4.matriz[0][0] == c4.matriz[1][0] != 0:
        reset()
        if c2.matriz[0][0] == 1:
            jugador1Gana = True
        else:
            jugador2Gana = True
    
    # 15
    elif c2.matriz[1][0] == c2.matriz[2][0] == c4.matriz[0][0] == c4.matriz[1][0] == c4.matriz[2][0] != 0:
        reset()
        if c2.matriz[1][0] == 1:
            jugador1Gana = True
        else:
            jugador2Gana = True
            
    # 16
    elif c2.matriz[0][1] == c2.matriz[1][1] == c2.matriz[2][1] == c4.matriz[0][1] == c4.matriz[1][1] != 0:
        reset()
        if c2.matriz[0][1] == 1:
            jugador1Gana = True
        else:
            jugador2Gana = True
    
    # 17
    elif c2.matriz[1][1] == c2.matriz[2][1] == c4.matriz[0][1] == c4.matriz[1][1] == c4.matriz[2][1] != 0:
        reset()
        if c2.matriz[1][1] == 1:
            jugador1Gana = True
        else:
            jugador2Gana = True
            
    # 18
    elif c2.matriz[0][2] == c2.matriz[1][2] == c2.matriz[2][2] == c4.matriz[0][2] == c4.matriz[1][2] != 0:
        reset()
        if c2.matriz[0][2] == 1:
            jugador1Gana = True
        else:
            jugador2Gana = True
            
    # 19
    elif c2.matriz[1][2] == c2.matriz[2][2] == c4.matriz[0][2] == c4.matriz[1][2] == c4.matriz[2][2] != 0:
        reset()
        if c2.matriz[1][2] == 1:
            jugador1Gana = True
        else:
            jugador2Gana = True
            
    # 20
    elif c1.matriz[0][0] == c1.matriz[0][1] == c1.matriz[0][2] == c2.matriz[0][0] == c2.matriz[0][1] != 0:
        reset()
        if c1.matriz[0][0] == 1:
            jugador1Gana = True
        else:
            jugador2Gana = True
            
    # 21
    elif c1.matriz[0][1] == c1.matriz[0][2] == c2.matriz[0][0] == c2.matriz[0][1] == c2.matriz[0][2] != 0:
        reset()
        if c1.matriz[0][1] == 1:
            jugador1Gana = True
        else:
            jugador2Gana = True
            
    # 22
    elif c1.matriz[1][0] == c1.matriz[1][1] == c1.matriz[1][0] == c2.matriz[1][0] == c2.matriz[1][1] != 0:
        reset()
        if c1.matriz[1][0] == 1:
            jugador1Gana = True
        else:
            jugador2Gana = True
            
    # 23
    elif c1.matriz[1][1] == c1.matriz[1][2] == c2.matriz[1][0] == c2.matriz[1][1] == c2.matriz[1][2] != 0:
        reset()
        if c1.matriz[1][1] == 1:
            jugador1Gana = True
        else:
            jugador2Gana = True
            
    # 24
    elif c1.matriz[2][0] == c1.matriz[2][1] == c1.matriz[2][2] == c2.matriz[2][0] == c2.matriz[2][1] != 0:
        reset()
        if c1.matriz[2][0] == 1:
            jugador1Gana = True
        else:
            jugador2Gana = True
            
    # 25
    elif c1.matriz[2][1] == c1.matriz[2][2] == c2.matriz[2][0] == c2.matriz[2][1] == c2.matriz[2][2] != 0:
        reset()
        if c1.matriz[2][1] == 1:
            jugador1Gana = True
        else:
            jugador2Gana = True
        
    # 26
    elif c3.matriz[0][0] == c3.matriz[0][1] == c3.matriz[0][2] == c4.matriz[0][0] == c4.matriz[0][1] != 0:
        reset()
        if c3.matriz[0][0] == 1:
            jugador1Gana = True
        else:
            jugador2Gana = True
            
    # 27
    elif c3.matriz[0][1] == c3.matriz[0][2] == c4.matriz[0][0] == c4.matriz[0][1] == c4.matriz[0][2] != 0:
        reset()
        if c3.matriz[0][1] == 1:
            jugador1Gana = True
        else:
            jugador2Gana = True
            
    # 28
    elif c3.matriz[1][0] == c3.matriz[1][2] == c3.matriz[1][2] == c4.matriz[1][0] == c4.matriz[1][1] != 0:
        reset()
        if c3.matriz[1][0] == 1:
            jugador1Gana = True
        else:
            jugador2Gana = True
            
    # 29
    elif c3.matriz[1][1] == c3.matriz[1][2] == c4.matriz[1][0] == c4.matriz[1][1] == c4.matriz[1][2] != 0:
        reset()
        if c3.matriz[1][1] == 1:
            jugador1Gana = True
        else:
            jugador2Gana = True
            
    # 30
    elif c3.matriz[2][0] == c3.matriz[2][1] == c3.matriz[2][2] == c4.matriz[2][0] == c4.matriz[2][1] != 0:
        reset()
        if c3.matriz[2][0] == 1:
            jugador1Gana = True
        else:
            jugador2Gana = True
            
    # 31
    elif c3.matriz[2][1] == c3.matriz[2][2] == c4.matriz[2][0] == c4.matriz[2][1] == c4.matriz[2][2] != 0:
        reset()
        if c3.matriz[2][1] == 1:
            jugador1Gana = True
        else:
            jugador2Gana = True
    
    else:
        if lleno(c1.matriz) and lleno(c2.matriz) and lleno(c3.matriz) and lleno(c4.matriz):
            reset()
            empate = True
    
## Esta función contiene los procesos que se llevan a cabo
## en cada turno, colocar una ficha, elegir un cuadrante
## y rotar a la derecha o izquierda
## Entradas:
##      None
## Salidas:
##      Procesos del juego
## Restricciones:
##      None
def juego():
    
    global jugador1Coloca, jugador1Rota, jugador1Direccion, jugador2Coloca, jugador2Rota, jugador2Direccion, c1, c2, c3, c4, terminado, jugador1Gana, jugador2Gana, rotada
    
    ### Colocando una ficha ###
    if (675 <= mouseX <= 775) and (5 <= mouseY <= 55):
        reinicioJuego()
    
    if jugador1Coloca or jugador2Coloca:
        if (220 <= mouseX <= 260) and (110 <= mouseY <= 150):
            if jugador1Coloca:
                c1.matriz[0][0] = 1
                jugador1Coloca = False
                jugador1Rota = True
            else:
                c1.matriz[0][0] = 2 
                jugador2Coloca = False
                jugador2Rota = True
        
        elif (280 <= mouseX <= 320) and (110 <= mouseY <= 150):
            if jugador1Coloca:
                c1.matriz[0][1] = 1
                jugador1Coloca = False
                jugador1Rota = True
            else:
                c1.matriz[0][1] = 2 
                jugador2Coloca = False
                jugador2Rota = True
        
        elif (340 <= mouseX <= 380) and (110 <= mouseY <= 150):
            if jugador1Coloca:
                c1.matriz[0][2] = 1
                jugador1Coloca = False
                jugador1Rota = True
            else:
                c1.matriz[0][2] = 2 
                jugador2Coloca = False
                jugador2Rota = True
        
        elif (220 <= mouseX <= 260) and (180 <= mouseY <= 220):
            if jugador1Coloca:
                c1.matriz[1][0] = 1
                jugador1Coloca = False
                jugador1Rota = True
            else:
                c1.matriz[1][0] = 2 
                jugador2Coloca = False
                jugador2Rota = True
        
        elif (280 <= mouseX <= 320) and (180 <= mouseY <= 220):
            if jugador1Coloca:
                c1.matriz[1][1] = 1
                jugador1Coloca = False
                jugador1Rota = True
            else:
                c1.matriz[1][1] = 2 
                jugador2Coloca = False
                jugador2Rota = True
        
        elif (340 <= mouseX <= 380) and (180 <= mouseY <= 220):
            if jugador1Coloca:
                c1.matriz[1][2] = 1
                jugador1Coloca = False
                jugador1Rota = True
            else:
                c1.matriz[1][2] = 2 
                jugador2Coloca = False
                jugador2Rota = True
              
        elif (220 <= mouseX <= 260) and (250 <= mouseY <= 290):
            if jugador1Coloca:
                c1.matriz[2][0] = 1
                jugador1Coloca = False
                jugador1Rota = True
            else:
                c1.matriz[2][0] = 2 
                jugador2Coloca = False
                jugador2Rota = True
        
        elif (280 <= mouseX <= 320) and (250 <= mouseY <= 290):
            if jugador1Coloca:
                c1.matriz[2][1] = 1
                jugador1Coloca = False
                jugador1Rota = True
            else:
                c1.matriz[2][1] = 2 
                jugador2Coloca = False
                jugador2Rota = True
        
        elif (340 <= mouseX <= 380) and (250 <= mouseY <= 290):
            if jugador1Coloca:
                c1.matriz[2][2] = 1
                jugador1Coloca = False
                jugador1Rota = True
            else:
                c1.matriz[2][2] = 2 
                jugador2Coloca = False
                jugador2Rota = True
        
        elif (420 <= mouseX <= 460) and (110 <= mouseY <= 150):
            if jugador1Coloca:
                c2.matriz[0][0] = 1
                jugador1Coloca = False
                jugador1Rota = True
            else:
                c2.matriz[0][0] = 2 
                jugador2Coloca = False
                jugador2Rota = True
        
        elif (480 <= mouseX <= 520) and (110 <= mouseY <= 150):
            if jugador1Coloca:
                c2.matriz[0][1] = 1
                jugador1Coloca = False
                jugador1Rota = True
            else:
                c2.matriz[0][1] = 2 
                jugador2Coloca = False
                jugador2Rota = True
        
        elif (540 <= mouseX <= 580) and (110 <= mouseY <= 150):
            if jugador1Coloca:
                c2.matriz[0][2] = 1
                jugador1Coloca = False
                jugador1Rota = True
            else:
                c2.matriz[0][2] = 2 
                jugador2Coloca = False
                jugador2Rota = True
            
        elif (420 <= mouseX <= 460) and (180 <= mouseY <= 220):
            if jugador1Coloca:
                c2.matriz[1][0] = 1
                jugador1Coloca = False
                jugador1Rota = True
            else:
                c2.matriz[1][0] = 2 
                jugador2Coloca = False
                jugador2Rota = True
        
        elif (480 <= mouseX <= 520) and (180 <= mouseY <= 220):
            if jugador1Coloca:
                c2.matriz[1][1] = 1
                jugador1Coloca = False
                jugador1Rota = True
            else:
                c2.matriz[1][1] = 2 
                jugador2Coloca = False
                jugador2Rota = True
        
        elif (540 <= mouseX <= 580) and (180 <= mouseY <= 220):
            if jugador1Coloca:
                c2.matriz[1][2] = 1
                jugador1Coloca = False
                jugador1Rota = True
            else:
                c2.matriz[1][2] = 2 
                jugador2Coloca = False
                jugador2Rota = True
        
        elif (420 <= mouseX <= 460) and (250 <= mouseY <= 290):
            if jugador1Coloca:
                c2.matriz[2][0] = 1
                jugador1Coloca = False
                jugador1Rota = True
            else:
                c2.matriz[2][0] = 2 
                jugador2Coloca = False
                jugador2Rota = True
        
        elif (480 <= mouseX <= 520) and (250 <= mouseY <= 290):
            if jugador1Coloca:
                c2.matriz[2][1] = 1
                jugador1Coloca = False
                jugador1Rota = True
            else:
                c2.matriz[2][1] = 2 
                jugador2Coloca = False
                jugador2Rota = True
        
        elif (540 <= mouseX <= 580) and (250 <= mouseY <= 290):
            if jugador1Coloca:
                c2.matriz[2][2] = 1
                jugador1Coloca = False
                jugador1Rota = True
            else:
                c2.matriz[2][2] = 2 
                jugador2Coloca = False
                jugador2Rota = True
        
        elif (220 <= mouseX <= 260) and (310 <= mouseY <= 350):
            if jugador1Coloca:
                c3.matriz[0][0] = 1
                jugador1Coloca = False
                jugador1Rota = True
            else:
                c3.matriz[0][0] = 2 
                jugador2Coloca = False
                jugador2Rota = True
        
        elif (280 <= mouseX <= 320) and (310 <= mouseY <= 350):
            if jugador1Coloca:
                c3.matriz[0][1] = 1
                jugador1Coloca = False
                jugador1Rota = True
            else:
                c3.matriz[0][1] = 2 
                jugador2Coloca = False
                jugador2Rota = True
                
        elif (340 <= mouseX <= 380) and (310 <= mouseY <= 350):
            if jugador1Coloca:
                c3.matriz[0][2] = 1
                jugador1Coloca = False
                jugador1Rota = True
            else:
                c3.matriz[0][2] = 2 
                jugador2Coloca = False
                jugador2Rota = True
            
        elif (220 <= mouseX <= 260) and (380 <= mouseY <= 420):
            if jugador1Coloca:
                c3.matriz[1][0] = 1
                jugador1Coloca = False
                jugador1Rota = True
            else:
                c3.matriz[1][0] = 2 
                jugador2Coloca = False
                jugador2Rota = True
        
        elif (280 <= mouseX <= 320) and (380 <= mouseY <= 420):
            if jugador1Coloca:
                c3.matriz[1][1] = 1
                jugador1Coloca = False
                jugador1Rota = True
            else:
                c3.matriz[1][1] = 2 
                jugador2Coloca = False
                jugador2Rota = True
        
        elif (340 <= mouseX <= 380) and (380 <= mouseY <= 420):
            if jugador1Coloca:
                c3.matriz[1][2] = 1
                jugador1Coloca = False
                jugador1Rota = True
            else:
                c3.matriz[1][2] = 2 
                jugador2Coloca = False
                jugador2Rota = True
        
        elif (220 <= mouseX <= 260) and (450 <= mouseY <= 490):
            if jugador1Coloca:
                c3.matriz[2][0] = 1
                jugador1Coloca = False
                jugador1Rota = True
            else:
                c3.matriz[2][0] = 2 
                jugador2Coloca = False
                jugador2Rota = True
        
        elif (280 <= mouseX <= 320) and (450 <= mouseY <= 490):
            if jugador1Coloca:
                c3.matriz[2][1] = 1
                jugador1Coloca = False
                jugador1Rota = True
            else:
                c3.matriz[2][1] = 2 
                jugador2Coloca = False
                jugador2Rota = True
                
        elif (340 <= mouseX <= 380) and (450 <= mouseY <= 490):
            if jugador1Coloca:
                c3.matriz[2][2] = 1
                jugador1Coloca = False
                jugador1Rota = True
            else:
                c3.matriz[2][2] = 2 
                jugador2Coloca = False
                jugador2Rota = True
        
        elif (420 <= mouseX <= 460) and (310 <= mouseY <= 350):
            if jugador1Coloca:
                c4.matriz[0][0] = 1
                jugador1Coloca = False
                jugador1Rota = True
            else:
                c4.matriz[0][0] = 2 
                jugador2Coloca = False
                jugador2Rota = True
        
        elif (480 <= mouseX <= 520) and (310 <= mouseY <= 350):
            if jugador1Coloca:
                c4.matriz[0][1] = 1
                jugador1Coloca = False
                jugador1Rota = True
            else:
                c4.matriz[0][1] = 2 
                jugador2Coloca = False
                jugador2Rota = True
        
        elif (540 <= mouseX <= 580) and (310 <= mouseY <= 350):
            if jugador1Coloca:
                c4.matriz[0][2] = 1
                jugador1Coloca = False
                jugador1Rota = True
            else:
                c4.matriz[0][2] = 2 
                jugador2Coloca = False
                jugador2Rota = True
                
        elif (420 <= mouseX <= 460) and (380 <= mouseY <= 420):
            if jugador1Coloca:
                c4.matriz[1][0] = 1
                jugador1Coloca = False
                jugador1Rota = True
            else:
                c4.matriz[1][0] = 2 
                jugador2Coloca = False
                jugador2Rota = True  
                
        elif (480 <= mouseX <= 520) and (380 <= mouseY <= 420):
            if jugador1Coloca:
                c4.matriz[1][1] = 1
                jugador1Coloca = False
                jugador1Rota = True
            else:
                c4.matriz[1][1] = 2 
                jugador2Coloca = False
                jugador2Rota = True
                
        elif (540 <= mouseX <= 580) and (380 <= mouseY <= 420):
            if jugador1Coloca:
                c4.matriz[1][2] = 1
                jugador1Coloca = False
                jugador1Rota = True
            else:
                c4.matriz[1][2] = 2 
                jugador2Coloca = False
                jugador2Rota = True
            
        elif (420 <= mouseX <= 460) and (450 <= mouseY <= 490):
            if jugador1Coloca:
                c4.matriz[2][0] = 1
                jugador1Coloca = False
                jugador1Rota = True
            else:
                c4.matriz[2][0] = 2 
                jugador2Coloca = False
                jugador2Rota = True 
            
        elif (480 <= mouseX <= 520) and (450 <= mouseY <= 490):
            if jugador1Coloca:
                c4.matriz[2][1] = 1
                jugador1Coloca = False
                jugador1Rota = True
            else:
                c4.matriz[2][1] = 2 
                jugador2Coloca = False
                jugador2Rota = True
       
        elif (540 <= mouseX <= 580) and (450 <= mouseY <= 490):
            if jugador1Coloca:
                c4.matriz[2][2] = 1
                jugador1Coloca = False
                jugador1Rota = True
            else:
                c4.matriz[2][2] = 2 
                jugador2Coloca = False
                jugador2Rota = True  
        
        check()
                        
    ### Elijiendo un cuadrante para rotar ###                        
    elif jugador1Rota or jugador2Rota:
        if (200 <= mouseX <= 400) and (100 <= mouseY <= 300):
            rotada = 1
            if jugador1Rota:
                jugador1Rota = False
                jugador1Direccion = True
            else:
                jugador2Rota = False
                jugador2Direccion = True
        
        elif (401 <= mouseX <= 600) and (100 <= mouseY <= 300):
            rotada = 2
            if jugador1Rota:
                jugador1Rota = False
                jugador1Direccion = True
            else:
                jugador2Rota = False
                jugador2Direccion = True
        
        elif (200 <= mouseX <= 400) and (301 <= mouseY <= 500):
            rotada = 3
            if jugador1Rota:
                jugador1Rota = False
                jugador1Direccion = True
            else:
                jugador2Rota = False
                jugador2Direccion = True
        
        elif (401 <= mouseX <= 600) and (301 <= mouseY <= 500):
            rotada = 4
            if jugador1Rota:
                jugador1Rota = False
                jugador1Direccion = True
            else:
                jugador2Rota = False
                jugador2Direccion = True
        
        check()
            
    ### Rotar cuadrante ###
    elif jugador1Direccion or jugador2Direccion:
        if (190 <= mouseX <= 310) and (620 <= mouseY <= 680):
            if rotada == 1:
                c1.rotacionIzq()
                
            elif rotada == 2:
                c2.rotacionIzq()
            
                
            elif rotada == 3:
                c3.rotacionIzq()
                
            else:
                c4.rotacionIzq()
            
            if jugador1Direccion:
                jugador1Direccion = False
                jugador2Coloca = True
            
            else:
                jugador2Direccion = False
                jugador1Coloca = True
            
            
        
        elif (490 <= mouseX <= 610) and (620 <= mouseY <= 680):
            if rotada == 1:
                c1.rotacionDer()
                
            elif rotada == 2:
                c2.rotacionDer()
                
            elif rotada == 3:
                c3.rotacionDer()
                
            else:
                c4.rotacionDer()
            
            if jugador1Direccion:
                jugador1Direccion = False
                jugador2Coloca = True
            
            else:
                jugador2Direccion = False
                jugador1Coloca = True
        
        check()

## Esta función se utiliza cunado el juego se termina, ya sea
## que el jugador 1 gano, el jugador 2 gano o hubo un empate.
## Termina el juego cambiando  todas las variables de control
## del turno a False
## Entradas:
##       None
## Salidas:
##       Variables de control en False
## Restricciones:
##       None
def reset():
    global jugador1Coloca, jugador1Rota, jugador1Direccion, jugador2Coloca, jugador2Rota, jugador2Direccion
    jugador1Coloca = False
    jugador1Rota = False
    jugador1Direccion = False
    jugador2Coloca = False
    jugador2Rota = False
    jugador2Direccion = False

## Esta función revisa cada elemento de una matriz
## y retorna False si al menos un elemento es 0
## o en el contexto del juego, no tiene una ficha.
## Se utiliza en la funcion check() para verificar
## si hubo un empate
## Entradas:
##       una matriz
## Salidas:
##       True si una matriz está "llena"
##       False si al menos un elemento está "vacío"
## Restricciones:
##       None
def lleno(matriz):
    for fila in matriz:
        for columna in fila:
            if columna == 0:
                return False    
    return True

def reinicioJuego():
    global jugador1Coloca, jugador1Rota, jugador1Direccion, jugador2Coloca, jugador2Rota, jugador2Direccion, c1, c2, c3, c4, jugador1Gana, jugador2Gana, rotada
    
    jugador1Coloca = True
    jugador1Rota = False
    jugador1Direccion = False
    
    jugador2Coloca = False
    jugador2Rota = False
    jugador2Direccion = False
    
    jugador1Gana = False
    jugador2Gana = False
    
    empate = False
    
    rotada = 0
    
    c1 = Matriz(240,130)
    c2 = Matriz(440,130)
    c3 = Matriz(240,330)
    c4 = Matriz(440,330)