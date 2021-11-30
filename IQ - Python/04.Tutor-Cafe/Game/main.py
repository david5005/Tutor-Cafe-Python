#importacion de la libreria pygame
import pygame
import random
import math
from pygame import mixer
# -------------------------------------------------------------------------------
#inicializacion de pygame
pygame.init()

#creacion de la ventana del juego
screen = pygame.display.set_mode((800,600)) #(ancho, alto)

#cargar imagenes:
#cargar imagen de fondo
background = pygame.image.load("fondo.png")

#cargar sonido de fondo
mixer.music.load("background.wav") #cargamos la musica de fondo
mixer.music.play(-1) #se repite automaticamente con -1

#cargar la imagen de nuestra nave:
playerImg = pygame.image.load("player.png")
#posicionar la nave en la ventana del juego:
playerX = 370 #ancho
playerY = 480 #alto
playerX_change = 0 #con esto vamos a mover al jugador, en el eje de las X


#Enemigo UFO
#cargamos la misma imagen en distintos indices, que hacen referencia a "distintos"
#enemigos
enemyImg = [] # juanito(x,y), pedrito(x,y), luisito, ...
enemyX = [] #posiciones aleatorias para x
enemyY = [] #posiciones aleatorias para y
enemyX_change = [] #valores para el desplazamiento en X
enemyY_change = [] #vamlores para el desplazamiento en Y
#definimos el numero de enemigos que deseamos
num_of_enemies = 6
for i in range(num_of_enemies): #aplicar propiedades a cada enemigo (i)
    enemyImg.append(pygame.image.load("ufo.png")) #cargamos los enemigos al arreglo
    enemyX.append(random.randint(0, 735)) #posicion aleatoria en el eje X
    enemyY.append(random.randint(50, 150)) # posicion aleatoria en el eje Y
    enemyX_change.append(3) #desplazamiento en x para simular el movimiento
    enemyY_change.append(40) #desplazamiento en y para simular el movimiento


#cargar balas:
bulletImg = pygame.image.load("bala32PX.png") #cargar imagen de la bala
bulletX = 0 #0 porque la bala se va a mover solo verticalmente
bulletY = 480 #empieza desde el mismo alto o posicion del jugador, desde ahi sale la bala
#parametros para mover a la bala
bulletX_change = 0
bulletY_change = 10 #saltos que da la bala (movimiento)
bullet_state = "ready" #estamos listos para disparar, el estado actual

#cargar imagen de la explosion
boomImg = pygame.image.load("boom.png")

#cargamos el icono para la ventana -----------------------------------
pygame.display.set_caption("Invasores espaciales") #colocamos el titulo de la ventana
icon = pygame.image.load("nave.png") #cargamos el icono
pygame.display.set_icon(icon) #colocamos el icono
#---------------------------------------------------------------------

#uso de funciones ----------------------------------------------------
#logica para la puntuacion:
score_value = 0
font = pygame.font.Font("Herrington Font - Spotty.ttf", 32)
textX = 10
textY = 10
def show_score(x,y):
    texto = "                David Torres"
    score = font.render("Mijin's Score: " + str(score_value) + texto, True, (255,255,255)) #(texto, mostrar en pantalla, color)
    screen.blit(score, (x,y))
#-----------------------------------
#mostramos el mensaje del fin del juego
game_over_font = pygame.font.Font("Herrington Font - Spotty.ttf", 64)
def game_over_text():
    over_text = game_over_font.render("Perdiste Guambra", True, (255,255,255))
    screen.blit(over_text, (100,250))
#-----------------------------------
#logica para mostrar a la nave
def player(x,y):
    screen.blit(playerImg, (x,y)) #mostrar en pantalla a nuestra nave con .blit()
#logica para mostrar al enemigo
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x,y)) #mostramos al enemigo segun i, en pantalla con sus coordenadas
#logica para disparar
def fired_bullet(x,y):
    global bullet_state
    bullet_state = "fire" #esto persistente de disparo para nuestra bala
    screen.blit(bulletImg, (x+16, y+10)) #dibujamos la bala para que parezca que sale de la nave espacial

#utilizacion para calcular la distancia entre dos puntos
#Raiz((x2-x1)^2 + (y2-y1)^2)
def isCollision(enemyX, enemyY, bulletX, bulletY): #(enemigo(X,Y), bala(X,Y))
    #aplicacion de la formula
    distance = math.sqrt((math.pow(enemyX-bulletX, 2) + (math.pow(enemyY-bulletY, 2))))
    if distance < 27: # existe una colision
        screen.blit(boomImg,(enemyX, enemyY)) # hace boom en la posicion de nuestro enemigo
        return True #colision ha ocurrido
    else:
        return False #la colision no ha ocurrido

# -------------------------------------------------------------------------------------


#Logica del juego
running = True #para un loop infinito
while running:
    #cambiamos el color de fondo de la pantalla con RGB - red, green, blue
    screen.fill((0,0,0))
    screen.blit(background,(0,0)) #cargar imagen de fondo, (esquina izquierda, esquina izquierda arriba)

    #Recorrer todos los eventos (escuchar alguna accion)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #comprobar si se presionó el botón de cerrar
            running = False         #terminar el juego, cerrar la ventana

        if event.type == pygame.KEYDOWN: #si presionamos una tecla:
            if event.key == pygame.K_LEFT: #ha presionado la tecla izquierda?
                #mover la nave a la izquierda
                playerX_change = -5    # mover a la izquierda (-)...0...(+)
            if event.key == pygame.K_RIGHT:
                #mover la nave a la derecha
                playerX_change = 5  # mover a la derecha (-)...0...(+)
            if event.key == pygame.K_SPACE:
                #disparar
                if bullet_state == "ready":

                    bullet_Sound = mixer.Sound("laser.wav")
                    bullet_Sound.play()

                    bulletX = playerX #alineamos la bala a la misma posicion de nuestra nave
                    fired_bullet(playerX, bulletY)

        if event.type == pygame.KEYUP: #soltar la tecla
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0 #freno

    #MOVIMIENTOS

    #MOVIMIENTO DE LA NAVE (JUGADOR)-------------------------------------------------------
    playerX += playerX_change
    #controlar que la nave llegue al borde sea izquierdo o derecho
    # (0) ----------------------------------------------------------------- (736)
    if playerX <= 0:
        playerX = 0 #para que ya no salga del borde izquierdo
    if playerX >= 736:
        playerX = 736 # para que ya no salga del borde derecho
    #------------------------------------------------------------------------

    # MOVIMIENTO DEL ENEMIGO -------------------------------------------------------------
    for i in range(num_of_enemies): #evaluamos para cada enemigo del arreglo
        #Game over, fin del juego
        if enemyY[i] > 440: # EN Y: si uno de los enemigos llega a la posicion Y, cerca de la nave
            for j in range(num_of_enemies): #desaparecer a todos los enemigos
                enemyY[j] = 2000

            game_over_text()

            break; #rompemos el proceso
        enemyX[i] += enemyX_change[i] #el desplazamiento
        #controlamos al enemigo para que llegue solo al margen izquierdo o derecho
        #la imagen del enemigo tiene 64px, el ancho de la ventana es de 800
        if enemyX[i] <= 0: #cuando llegue al borde izquierdo, debe realizar un cambio vertical hacia abajo
            enemyX_change[i] = 3
            enemyY[i] += enemyY_change[i] #truco, para que el enemigo avance, cambio vertical hacia abajo
        elif enemyX[i] >= 736:  #cuando el enemigo llega al borde derecho
            enemyX_change[i] = -3
            enemyY[i] += enemyY_change[i] #ocurre el cambio vertical hacia abajo

        #colision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision: #si la colision esta dada
            #damos play al sonido de la colision:
            explosion_Sound = mixer.Sound("explosion.wav")
            explosion_Sound.play() #con esto suena la explosion
            bulletY = 480 #la bala regresa a la posicion de la nave
            bullet_state = "ready" #estamos listos para disparar
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)


    #MOVIMIENTO DE LA BALA -------------------------------------------------------------
    """
        (0)
        .
        .
        .
        (480)
    """
    if bulletY <= 0: #si la bala ya ha llegado a la parte superior, osea a la posicion 0, entonces
        bulletY = 480 #debe regresar a la posicion de la nave en Y
        bullet_state = "ready"
    if bullet_state == "fire":
        fired_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    #----------------------------------------------------------------------------------

    player(playerX, playerY) #funcion que dibuja a la nave en la pantalla
    show_score(textX, textY) #mostrar nuestra puntuacion

    pygame.display.update() #refrescar la pantalla (imagen de fondo se queda como congelada)