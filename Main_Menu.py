from tracemalloc import stop
import pygame, math, sys, time, end, main_level1,level2,level3,level4
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption('NEED FOR SPEED for Computer Graphics 64')

pygame.mixer.music.load('music/BelieveONE PIECE 8bit0002.mp3')
pygame.mixer.music.set_volume((0.3978141))
pygame.mixer.music.play(loops=10, start=1 , fade_ms=3 )


#Start Game
while 1:
    for event in pygame.event.get():
            
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    pygame.display.update()
                    pygame.display.flip()    
                if not hasattr(event, 'key'): continue
                if event.key == K_SPACE: 
                    pygame.mixer.music.load('music/ONE PIECE 8bit00001.mp3')
                    pygame.mixer.music.set_volume((0.3978141))
                    pygame.mixer.music.play(loops=10, start=1 )
                    main_level1.level1()
                    # level3.level3()
                    # pygame.mixer.music.load('music/Gryyfin.mp3')
                    # pygame.mixer.music.set_volume((0.5978141))
                    # pygame.mixer.music.play(loops=20, start=0.0)
                    # end.end_game()
                elif event.key == K_ESCAPE: sys.exit(0)  
                

    img = pygame.image.load("image/nfs.png")
    screen.blit(img,(0,0))
    pygame.display.flip()
