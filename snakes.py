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

# Game Loop
def gameloop():
    ## Game specific variables
    exit_Game = False
    game_Over = False
    apple_x = random.randint(100, W_wd-100)
    apple_y = random.randint(100, W_ht-100)
    fps = 20
    snake_size = 20

    #snakey_1
    snake_1_x = 250
    snake_1_y = 125
    vel_1_x = 0
    vel_1_y = 0
    score_1 = 0
    snake_1_list = []
    snake_1_len = 1

    #snakey_2
    snake_2_x = 750
    snake_2_y = 125
    vel_2_x = 0
    vel_2_y = 0
    score_2 = 0
    snake_2_list = []
    snake_2_len = 1

    while not exit_Game:
            if game_Over:
                game_Window.fill(black)
                if snake_1_x < 0 or snake_1_x > W_wd or snake_1_y < 0 or snake_1_y > W_ht:
                    text_on_screen('Player 2 Won !!', white, 350, 250)
                    text_on_screen('Press ENTER to play again', white, 250, 300)
                    game_Over = True
                if snake_2_x < 0 or snake_2_x > W_wd or snake_2_y < 0 or snake_2_y > W_ht:
                    text_on_screen('Player 1 Won !!', white, 350, 250)
                    text_on_screen('Press ENTER to play again', white, 250, 300)
                    game_Over = True
                if head_1 in snake_1_list[:-1]:
                    text_on_screen('Player 2 Won !!', white, 350, 250)
                    text_on_screen('Press ENTER to play again', white, 250, 300)
                    game_Over = True
                if head_2 in snake_2_list[:-1]:
                    text_on_screen('Player 1 Won !!', white, 350, 250)
                    text_on_screen('Press ENTER to play again', white, 250, 300)
                    game_Over = True
            
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_Game = True
                        
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            template()
            else:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit_Game = True
                        if event.type == pygame.KEYDOWN:
                            #snakey_1
                            if event.key == pygame.K_d:
                                vel_1_x = 7
                                vel_1_y = 0
                            if event.key == pygame.K_a:
                                vel_1_x = -7
                                vel_1_y = 0
                            if event.key == pygame.K_w:
                                vel_1_y = -7
                                vel_1_x = 0
                            if event.key == pygame.K_s:
                                vel_1_y = 7
                                vel_1_x = 0
                            #snakey_2
                            if event.key == pygame.K_RIGHT:
                                vel_2_x = 7
                                vel_2_y = 0
                            if event.key == pygame.K_LEFT:
                                vel_2_x = -7
                                vel_2_y = 0
                            if event.key == pygame.K_UP:
                                vel_2_y = -7
                                vel_2_x = 0
                            if event.key == pygame.K_DOWN:
                                vel_2_y = 7
                                vel_2_x = 0
                            
                            #Continue playing
                    if event.key == pygame.K_RETURN:
                        gameloop()
                        
            #snakey_1 movement       
            snake_1_x += vel_1_x
            snake_1_y += vel_1_y
            
            #snakey_2 movement
            snake_2_x += vel_2_x
            snake_2_y += vel_2_y 

            #Scoring, length increment, Apple generator        
            if abs(snake_1_x-apple_x)<18 and abs(snake_1_y-apple_y)<18:
                score_1 += 1
                snake_1_len += 10
                apple_x = random.randint(100, W_wd-100)
                apple_y = random.randint(100, W_ht-100)
            if abs(snake_2_x-apple_x)<18 and abs(snake_2_y-apple_y)<18:
                score_2 += 1
                snake_2_len += 10
                apple_x = random.randint(100, W_wd-100)
                apple_y = random.randint(100, W_ht-100)
                        
            game_Window.fill(black) 
            text_on_screen('Score I: '+str(score_1), white, 10, 10)
            text_on_screen('Score II: '+str(score_2), white, 800, 10)
            pygame.draw.circle(game_Window, red, [apple_x, apple_y], 10)

            #Managing length
            head_1 = []
            head_1.append(snake_1_x)
            head_1.append(snake_1_y)
            snake_1_list.append(head_1)
            
            head_2 = []
            head_2.append(snake_2_x)
            head_2.append(snake_2_y)
            snake_2_list.append(head_2)
            
            if len(snake_1_list) > snake_1_len:
                del snake_1_list[0]   
            if len(snake_2_list) > snake_2_len:
                del snake_2_list[0]


            #Snakey collision    
            if snake_1_x < 0 or snake_1_x > W_wd or snake_1_y < 0 or snake_1_y > W_ht:
                game_Over = True
            if snake_2_x < 0 or snake_2_x > W_wd or snake_2_y < 0 or snake_2_y > W_ht:
                game_Over = True
            if head_1 in snake_1_list[:-1]:
                game_Over = True
            if head_2 in snake_2_list[:-1]:
                game_Over = True
            
            #Results
            if score_1 == 7:
                game_Window.fill(black)
                time.sleep(1)
                text_on_screen('Player 1 WON !!', white, 350, 250)
                text_on_screen('Press ENTER to play again', white, 250, 300)
                del snake_2_list[:]
                del snake_1_list[:]
            elif score_2 == 7:
                game_Window.fill(black)
                time.sleep(1)
                text_on_screen('Player 2 WON !!', white, 350, 250)
                text_on_screen('Press ENTER to play again', white, 250, 300)
                del snake_2_list[:]
                del snake_1_list[:]
                  
            #Calling vegan_snakes    
            snake_form(game_Window, cyan, snake_1_list, snake_size)
            snake_form(game_Window, yellow, snake_2_list, snake_size)
        
    pygame.display.update()
    clock.tick(fps)
        
    pygame.quit()
    quit()
template()
