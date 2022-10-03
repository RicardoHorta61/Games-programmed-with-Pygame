import sys
import random
import pygame

pygame.init()

x = 1280
y = 720

screen = pygame.display.set_mode((x,y))
pygame.display.set_caption('Ping-Pong Circle')
play_img = pygame.image.load('Textures/play.png').convert_alpha()
exit_img = pygame.image.load('Textures/exit.png').convert_alpha()
bar_1 = pygame.image.load('Textures/bar1.png').convert_alpha()
bar_2 = pygame.image.load('Textures/bar2.png').convert_alpha()


#---POINTS-----------------------------------------------------------------#
text_color = (255, 255, 255)
font = pygame.font.SysFont('arialblack', 40)
font_menu = pygame.font.SysFont('arialblack', 20)

def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))

#--------------------------------------------------------------------------#

#---BUTTON-----------------------------------------------------------------#
class button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
    
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action
#--------------------------------------------------------------------------#

#--------------------------------------------------------------------------#
play_button = button(480, 160, play_img, 1.3)
exit_button = button(480, 360, exit_img, 1.3)
bar1, bar2 = button(1200, 160, bar_1, 0.5), button(100, 360, bar_2, 0.5)
player_1 = pygame.image.load('Textures/bar1.png').convert_alpha()
player_1 = pygame.transform.scale(player_1, (20, 150))
player_2 = pygame.image.load('Textures/bar2.png').convert_alpha()
player_2 = pygame.transform.scale(player_2, (20, 150))
ball = pygame.image.load('Textures/white_circle.png').convert_alpha()
ball = pygame.transform.scale(ball, (25, 25))
player_1_rect, player_2_rect, ball_rect = player_1.get_rect(), player_2.get_rect(), ball.get_rect()
bg_game = pygame.image.load('Textures/bg_game.jpg').convert_alpha()
bg_game = pygame.transform.scale(bg_game, (1280, 720))
#--------------------------------------------------------------------------#

#---GAME-------------------------------------------------------------------#
def game_1vs1():
    running = True
    pos_player_1_x, pos_player_1_y = 1170, 310
    pos_player_2_x, pos_player_2_y = 110, 310
    pos_ball_x, pos_ball_y = 300, 100 
    x_speed, y_speed = 1, 1
    player_1_points = 0
    player_2_points = 0
    while running:
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            menu()
        if key[pygame.K_UP] and pos_player_1_y > 1:
            pos_player_1_y -= 1
        if key[pygame.K_DOWN] and pos_player_1_y < 570:
            pos_player_1_y += 1
        if key[pygame.K_w] and pos_player_2_y > 1:
            pos_player_2_y -= 1
        if key[pygame.K_s] and pos_player_2_y < 570:
            pos_player_2_y += 1

        #ball logic
        pos_ball_x += x_speed
        pos_ball_y += y_speed 
        if pos_ball_y >= y:
            y_speed = -1
        if pos_ball_y <= 0:
            y_speed = 1
        if pos_ball_x == 0:
            player_2_points += 1
            pos_ball_x, pos_ball_y = x/2, y/2
            x_speed, y_speed = random.choice ([1, -1]), random.choice ([1, -1])
        if pos_ball_x == x:
            player_1_points += 1
            pos_ball_x, pos_ball_y = x/2, y/2
            x_speed, y_speed = random.choice ([1, -1]), random.choice ([1, -1])
        if player_1_rect.colliderect(ball_rect):
             y_speed = random.choice ([1, -1])
             x_speed = -1
        if player_2_rect.colliderect(ball_rect):
             y_speed = random.choice ([1, -1])
             x_speed = 1

        player_1_rect.x = pos_player_1_x
        player_1_rect.y = pos_player_1_y

        player_2_rect.x = pos_player_2_x
        player_2_rect.y = pos_player_2_y

        ball_rect.x = pos_ball_x
        ball_rect.y = pos_ball_y

        screen.blit(bg_game, (0, 0))
        screen.blit(ball, (pos_ball_x, pos_ball_y))
        screen.blit(player_1, (pos_player_1_x, pos_player_1_y))
        screen.blit(player_2, (pos_player_2_x, pos_player_2_y))

        draw_text(f'{player_1_points} | {player_2_points}', font,text_color, 600, 100) 
        draw_text('Click SPACE to go back to Menu', font_menu, text_color, 460, 670) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
        pygame.display.update()
#--------------------------------------------------------------------------#

#---MENU-------------------------------------------------------------------#
def menu():
    menu_running = True
    while menu_running:
        screen.fill((10, 10, 0))
        if play_button.draw(): 
            game_1vs1()
        if exit_button.draw():
            menu_running = False
            sys.exit()
        bar1.draw() 
        bar2.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
#--------------------------------------------------------------------------#

#---MENU INICIAL-----------------------------------------------------------#
run = True
while run:
    screen.fill((10, 10, 0))
    if play_button.draw(): 
        game_1vs1()
    if exit_button.draw():
        run = False
    bar1.draw()
    bar2.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
#--------------------------------------------------------------------------#