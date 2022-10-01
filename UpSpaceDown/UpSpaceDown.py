#----------------------------------------------------------------------------------------------#
import pygame
import random
#----------------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------------#
no_juego = True 
puntos = 1
x = 1280
y = 720
puntos_x = 50
puntos_y = 50
#----------------------------------------------------------------------------------------------#
pantalla = pygame.display.set_mode((x,y))       #crear una vista sencilla
pygame.display.set_caption('mi juego de Python')

antecedentes = pygame.image.load('Textures/espacio.png').convert_alpha() #añadir una pantalla
antecedentes = pygame.transform.scale(antecedentes, (x, y))
#----------------------------------------------------------------------------------------------#

#---Crear lo jugador, el enemigo y el misil----------------------------------------------------# 
jugador = pygame.image.load('Textures/nave_espacial.png').convert_alpha()
jugador = pygame.transform.scale(jugador, (100, 100))

enemigo = pygame.image.load('Textures/nave_espacial_enemigo.png').convert_alpha()
enemigo = pygame.transform.scale(enemigo, (100, 100))

misil = pygame.image.load('Textures/misil.png').convert_alpha()
misil = pygame.transform.scale(misil, (40, 40))
misil = pygame.transform.rotate(misil, -45)

pos_jugador_x = 100 #posiciones iniciales
pos_jugador_y = 360

pos_enemigo_x = 100
pos_enemigo_y = 300

vel_misil_x = 0 
pos_misil_x = 120
pos_misil_y = 380

motivado = False
#----------------------------------------------------------------------------------------------#

#---añadir hitboxes----------------------------------------------------------------------------#
jugador_rect = jugador.get_rect()
enemigo_rect = enemigo.get_rect()
misil_rect = misil.get_rect()
#----------------------------------------------------------------------------------------------# 

#---función de generación----------------------------------------------------------------------#
def generar_enemigo():
    x = 1350
    y = random.randint(1,620)
    return [x,y] 
#----------------------------------------------------------------------------------------------# 
#---función de generación de misil-------------------------------------------------------------#
def generar_misil():
    motivado = False
    generar_misil_x = pos_jugador_x + 20
    generar_misil_y = pos_jugador_y + 20
    vel_misil_x = 0
    return [generar_misil_x, generar_misil_y, motivado, vel_misil_x]
#----------------------------------------------------------------------------------------------# 
#---función de colisiones----------------------------------------------------------------------#
def colisiones():
    global puntos
    if jugador_rect.colliderect(enemigo_rect) or enemigo_rect.x == 50:
        puntos -= 1
        return True
    elif misil_rect.colliderect(enemigo_rect):
        puntos += 1
        return True
    else:
        return False
#----------------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------------#
while no_juego:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            no_juego = False
        if puntos == -1:
            no_juego = False
    
    pantalla.blit(antecedentes, (0, 0))
    
    rel_x = x % antecedentes.get_rect().width
    pantalla.blit(antecedentes, (rel_x - antecedentes.get_rect().width, 0))
    if rel_x < 1280:
        pantalla.blit(antecedentes, (rel_x, 0))
    
    #llaves-----------------#
    llave = pygame.key.get_pressed()
    if llave[pygame.K_UP] and pos_jugador_y > 1:
        pos_jugador_y -= 1
        if not motivado:
            pos_misil_y -= 1
    if llave[pygame.K_DOWN] and pos_jugador_y < 620:
        pos_jugador_y += 1
        if not motivado:
            pos_misil_y += 1
    if llave[pygame.K_SPACE]:
        motivado = True
        vel_misil_x = 2
    #Generación-------------# 
    if pos_enemigo_x == -50 or colisiones():
        pos_enemigo_x = generar_enemigo()[0]
        pos_enemigo_y = generar_enemigo()[1]

    if pos_misil_x == 1300:
        pos_misil_x, pos_misil_y, motivado, vel_misil_x = generar_misil()
    #movimiento-------------#
    x-= 0.5
    
    pos_enemigo_x -= 1

    pos_misil_x += vel_misil_x

    jugador_rect.x = pos_jugador_x
    jugador_rect.y = pos_jugador_y

    enemigo_rect.x = pos_enemigo_x
    enemigo_rect.y = pos_enemigo_y

    misil_rect.x = pos_misil_x
    misil_rect.y = pos_misil_y
    #Hitboxes---------------#
    
    #Jugador/enemigo--------#
    pantalla.blit(misil, (pos_misil_x, pos_misil_y))
    pantalla.blit(jugador, (pos_jugador_x, pos_jugador_y))
    pantalla.blit(enemigo, (pos_enemigo_x, pos_enemigo_y))

    pygame.display.update()
#----------------------------------------------------------------------------------------------#