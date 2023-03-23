import pygame
import random
import time

#Initializing pygame
pygame.init()

# Screen
W_wd = 1000
W_ht = 700
game_Window = pygame.display.set_mode((W_wd, W_ht))
bg_i = pygame.image.load('Snake_Vegan.png')
bg_i = pygame.transform.scale(bg_i, (W_wd, W_ht)).convert_alpha()

# Defining Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
cyan = (0, 255, 244)
yellow = (247, 255, 0)

# Game Title
pygame.display.set_caption('Vegan Snakes')
pygame.display.update()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_on_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    game_Window.blit(screen_text, [x,y])

def snake_form(game_Window, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(game_Window, color, [x, y, snake_size, snake_size ])

def template():
    exit_Game = False
    while not exit_Game:
        game_Window.blit(bg_i, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    exit_Game = True    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
            
        pygame.display.update()
        clock.tick(20)