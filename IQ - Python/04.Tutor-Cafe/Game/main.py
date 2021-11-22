#importacion de la libreria pygame
import pygame

# -------------------------------------------------------------------------------
#inicializacion de pygame
pygame.init()

#creacion de la ventana del juego
screen = pygame.display.set_mode((800,600)) #(ancho, alto)

#cargar imagenes:
#cargar imagen de fondo
background = pygame.image.load("fondo.png")

#cargar la imagen de nuestra nave:
playerImg = pygame.image.load("player.png")
#posicionar la nave en la ventana del juego:
playerX = 370 #ancho
playerY = 480 #alto
playerX_change = 0 #con esto vamos a mover al jugador, en el eje de las X


#cargar balas:
bulletImg = pygame.image.load("bala32PX.png") #cargar imagen de la bala
bulletX = 0 #0 poruqe la bala se va a mover solo verticalmente
bulletY = 480 #empieza desde el mismo alto o posicion del jugador, desde ahi sale la bala
#parametros para mover a la bala
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready" #estamos listos para disparar

#cargar imagen de la explosion
boomImg = pygame.image.load("boom.png")

#cargamos el icono para la ventana -----------------------------------
pygame.display.set_caption("Invasores espaciales")
icon = pygame.image.load("nave.png")
pygame.display.set_icon(icon)
#---------------------------------------------------------------------

#uso de funciones ----------------------------------------------------
def player(x,y):
    screen.blit(playerImg, (x,y)) #mostrar en pantalla a nuestra nave con .blit()

def fired_bullet(x,y):
    global bullet_state
    bullet_state = "fire" #esto persistente de disparo para nuestra bala
    screen.blit(bulletImg, (x+16, y+10)) #dibujamos la bala para que parezca que sale de la nave espacial


# --------------------------------------------------------------------


#Logica del juego
running = True
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
                    #TODO: cargar sonido de disparo (2)
                    bulletX = playerX #alineamos la bala a la misma posicion de nuestra nave
                    fired_bullet(playerX, bulletY)

        if event.type == pygame.KEYUP:
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

    #...

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
    pygame.display.update() #refresca la pantalla (imagen de fondo se queda como congelada)