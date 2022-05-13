#initialize the screen
import pygame, math, sys, time,end
from pygame.locals import *



def level4():
    pygame.init()
    
    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption('NEED FOR SPEED' )
    back_g = pygame.image.load('image/lv4.png')
    pygame.display.set_caption('NEED FOR SPEED LV4')
    
    #GAME CLOCK
    clock = pygame.time.Clock()
    font = pygame.font.Font('font/Pixel.ttf', 40)
    win_font = pygame.font.Font(None, 50)
    win_condition = None
    win_text = font.render('', True, (0, 255, 0))
    loss_text = font.render('', True, (255, 0, 0))
    t0 = time.time()
    



    class CarSprite(pygame.sprite.Sprite):
        MAX_FORWARD_SPEED = 10
        MAX_REVERSE_SPEED = 10
        ACCELERATION = 2
        TURN_SPEED = 10

        def __init__(self, image, position):
            pygame.sprite.Sprite.__init__(self)
            self.src_image = pygame.image.load(image)
            self.position = position
            self.speed = self.direction = 0
            self.k_left = self.k_right = self.k_down = self.k_up = 0
        
        def update(self, deltat):
            #SIMULATION
            self.speed += (self.k_up + self.k_down)
            if self.speed > self.MAX_FORWARD_SPEED:
                self.speed = self.MAX_FORWARD_SPEED
            if self.speed < -self.MAX_REVERSE_SPEED:
                self.speed = -self.MAX_REVERSE_SPEED
            self.direction += (self.k_right + self.k_left)
            x, y = (self.position)
            rad = self.direction * math.pi / 180
            x += -self.speed*math.sin(rad)
            y += -self.speed*math.cos(rad)
            self.position = (x, y)
            self.image = pygame.transform.rotate(self.src_image, self.direction)
            self.rect = self.image.get_rect()
            self.rect.center = self.position

    class Wall_H(pygame.sprite.Sprite):
        normal = pygame.image.load('image/padlv4_H_P.png')
        def __init__(self, position):
            super(Wall_H, self).__init__()
            self.rect = pygame.Rect(self.normal.get_rect())
            self.rect.center = position
            self.image = self.normal
    
    class Wall_W(pygame.sprite.Sprite):
        normal = pygame.image.load('image/padlv4_W_P.png')
        def __init__(self, position):
            super(Wall_W, self).__init__()
            self.rect = pygame.Rect(self.normal.get_rect())
            self.rect.center = position
            self.image = self.normal
    
    
    pads = [
         Wall_H((151,174)),
        Wall_H((197,175)),
        Wall_W((298,130)),
        Wall_H((151,300)),
        Wall_H((194,298)),
        Wall_H((151,424)),
        Wall_H((577,172)),
        Wall_H((195,424)),
        Wall_H((615,171)),
        Wall_H((544,284)),
        Wall_H((604,290)),
        Wall_H((955,547)),
        Wall_H((1001,542)),
        Wall_H((1051,542)),
        Wall_H((752,372)),
        Wall_H((797,374)),
        Wall_H((754,241)),
        Wall_H((801,244)),
        Wall_H((757,111)),
        Wall_H((804,114)),
        Wall_H((758,-12)),
        Wall_H((798,-15)),
        Wall_H((17,100)),
        Wall_H((15,248)),
        Wall_H((17,384)),
        Wall_H((15,511)),
        Wall_H((1187,91)),
        Wall_H((1190,217)),
        Wall_H((1187,345)),
        Wall_H((1185,472)),
        Wall_H((1188,598)),

        Wall_W((70,-10)),
        Wall_W((258,-10)),
        Wall_W((438,-10)),
        Wall_W((632,-10)),
        Wall_W((921,-10)),
        Wall_W((1115,-10)),
        Wall_W((470,137)),
        Wall_W((432,204)),
        Wall_W((428,255)),
        Wall_W((427,312)),
        Wall_W((322,457)),
        Wall_W((522,458)),
        Wall_W((734,455)),
        Wall_W((994,132)),
        Wall_W((994,284)),
        Wall_W((994,337)),
        Wall_W((994,387)),
        Wall_W((994,451)),
        Wall_W((88,587)),
        Wall_W((270,591)),
        Wall_W((455,592)),
        Wall_W((641,591)),
        Wall_W((828,588)),]
     
    pad_group = pygame.sprite.RenderPlain(*pads)

    class Trophy(pygame.sprite.Sprite):
        def __init__(self, position):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('image/trophy.png')
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = position
        def draw(self, screen):
            screen.blit(self.image, self.rect)

    trophies = [Trophy((270,180))]
    trophy_group = pygame.sprite.RenderPlain(*trophies)

    # CREATE A CAR AND RUN
    #rect = screen.get_rect()
    car = CarSprite("image/driveCar/police.png", (1123, 562))
    car_group = pygame.sprite.RenderPlain(car)

    #THE GAME LOOP
    while 1:
        #USER INPUT
        t1 = time.time()
        dt = t1-t0
        
        
        deltat = clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    pygame.display.update()
                    pygame.display.flip()
            if not hasattr(event, 'key'): continue
            down = event.type == KEYDOWN 
            if win_condition == None: 
                if event.key == K_RIGHT: car.k_right = down * -5 
                elif event.key == K_LEFT: car.k_left = down * 5
                elif event.key == K_UP: car.k_up = down * 1
                elif event.key == K_DOWN: car.k_down = down * -1 
                elif event.key == K_ESCAPE: sys.exit(0) # quit the game
            elif win_condition == True and event.key == K_SPACE:
                pygame.mixer.music.load('music/Gryyfin.mp3')
                pygame.mixer.music.set_volume((0.3978141))
                pygame.mixer.music.play(loops=20, start=0.0)
                end.end_game()
            elif win_condition == False and event.key == K_SPACE: 
                level4()
                t0 = t1
            elif event.key == K_ESCAPE: sys.exit(0)    
    
        #COUNTDOWN TIMER
        seconds = round((500 - dt),2)
        if win_condition == None:
            timer_text = font.render(str(seconds), True, (255,255,0))
            if seconds <= 0:
                win_condition = False
                timer_text = font.render("Time!", True, (255,0,0))
                loss_text = win_font.render('Press Space to Retry', True, (255,0,0))
            
    
        #RENDERING
        
        car_group.update(deltat)
        collisions = pygame.sprite.groupcollide(car_group, pad_group, False, False, collided = None)
        if collisions != {}:
            win_condition = False
            timer_text = font.render("Crash!", True, (255,0,0))
            car.image = pygame.image.load('image/collision.png')
            loss_text = win_font.render('Press Space to Retry', True, (255,0,0))
            seconds = 0
            car.MAX_FORWARD_SPEED = 0
            car.MAX_REVERSE_SPEED = 0
            car.k_right = 0
            car.k_left = 0

        trophy_collision = pygame.sprite.groupcollide(car_group, trophy_group, False, True)
        if trophy_collision != {}:
            seconds = seconds
            timer_text = font.render("Finished!", True, (0,255,0))
            win_condition = True
            car.MAX_FORWARD_SPEED = 0
            car.MAX_REVERSE_SPEED = 0

            pygame.mixer.music.load('music/Super Mario Bob-omb Battlefield Theme (8 Bit Remix Cover Version) [Tribute to NES].mp3')
            pygame.mixer.music.set_volume((0.3978141))
            pygame.mixer.music.play(loops=10, start=0.0)
          
            win_text = win_font.render('Press Space to Advance', True, (0,255,0))
            if win_condition == True:
                car.k_right = -5
               
        
        
        
        screen.blit(back_g,(0,0))
        pad_group.update(collisions)
        pad_group.draw(screen)
        car_group.draw(screen)
        trophy_group.draw(screen)
        #Counter Render
        screen.blit(timer_text, (20,60))
        screen.blit(win_text, (400, 500))
        screen.blit(loss_text, (400, 500))
        pygame.display.flip()


