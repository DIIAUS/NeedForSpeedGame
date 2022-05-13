import pygame, sys, math
from pygame.locals import *


def end_game():
    while 1:
        pygame.init()
        screen = pygame.display.set_mode((1200, 600))
        win_font = pygame.font.Font('font/PressStart.ttf',25)
        name_font = pygame.font.Font('font/PressStart.ttf',18)
        
        win_text = win_font.render('Congratulations! Thanks for Play This Game!', True, (219, 222, 23))
        screen.blit(win_text, (100, 200))
        name_text = name_font.render('Dev by Nathan Butta 6130300425', True, (249, 249, 249))
        name_text2 = name_font.render('For Computer Graphics 03603481-60', True, (249, 249, 249))
       
        screen.blit(name_text, (100, 400))
        screen.blit(name_text2, (100, 500))
  
        

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
                pygame.display.update()
                pygame.display.flip()    
            # if event.key == K_ESCAPE: sys.exit(0) # quit the game

