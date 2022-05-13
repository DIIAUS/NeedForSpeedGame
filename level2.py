#initialize the screen
import pygame, math, sys, level3, time
from pygame.locals import *



def level2():
    pygame.init()
    
    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption('NEED FOR SPEED' )
    back_g = pygame.image.load('image/lv2.png')
    pygame.display.set_caption('NEED FOR SPEED LV2')
    
    #GAME CLOCK
    clock = pygame.time.Clock()
    font = pygame.font.Font('font/Pixel.ttf', 40)
    win_font = pygame.font.Font(None, 50)
    win_condition = None
    win_text = font.render('', True, (0, 255, 0))
    loss_text = font.render('', True, (255, 0, 0))
    t0 = time.time()

    class CarAI(pygame.sprite.Sprite):
        MAX_FORWARD_SPEED = 10
        MAX_REVERSE_SPEED = 10
        ACCELERATION = 2
        TURN_SPEED = 10
        
        def __init__(self, image, position):
            pygame.sprite.Sprite.__init__(self)
            self.src_image = pygame.image.load(image)
            self.position = position
            self.speed = self.direction = 0
            
        
        def update(self, deltat):
            #SIMULATION
            self.speed =1
           

            LineX=[46,220,1112,301,999]
            LineY=[455,45,471,325,105,158]
           

            x, y = (self.position)
            rad = self.direction * math.pi / 180
            if (x==LineX[0] and y<=LineY[0] and y>LineY[1]):  #line 1
                self.direction = 90 
                y += -self.speed
            elif (x>=LineX[0] and x<LineX[1] and y == LineY[1]):
                self.direction = 0
                x += self.speed
            elif (x==LineX[1] and y>=LineY[1] and y<LineY[2]):
                self.direction = 270
                y += self.speed
            elif (x>=LineX[1] and x<LineX[2] and y==LineY[2]):
                self.direction = 0
                x += self.speed
            elif (x==LineX[2] and y<=LineY[2] and y>LineY[3]):
                self.direction = 90
                y += -self.speed
            elif (x<= LineX[2]  and x>LineX[3] and y==LineY[3]):
                self.direction = 180
                x += -self.speed
            elif (x==LineX[3] and y<=LineY[3] and y>LineY[4]):
                self.direction = 90
                y += -self.speed
            elif (x>=LineX[3] and x<LineX[4] and y==LineY[4]):
                self.direction = 0
                x += self.speed
            #U-Turn
            elif(x==LineX[4] and y>=LineY[4] and y<LineY[5]):
                self.direction = 270
                y += self.speed
            #U-Turn
            elif ( x<=LineX[4] and x>355  and y==LineY[5]):
                self.direction = 180
                x += -self.speed
            elif (x==355 and y>=158 and y<272):
                self.direction = 90
                y += self.speed
            elif (x>=355 and x< 1169 and y==272):
                self.direction = 0
                x += self.speed
            elif (x==1169 and y>=272 and y<524):
                self.direction = 270
                y += self.speed
            elif (x<=1169 and x>176 and y == 524):
                self.direction = 180
                x += -self.speed
            elif (x==176 and y<=524 and y>88 ):
                self.direction = 90
                y += -self.speed
            elif (x<= 176 and x>94 and y==88):
                self.direction = 180
                x += -self.speed
            elif (x==94 and y>=88 and y<455):
                self.direction = 270
                y += self.speed
            #U-Turn
            elif (x<=94 and x>46 and y==455):
                self.direction = 180
                x += -self.speed
            

            self.position = (x, y)
            self.image = pygame.transform.rotate(self.src_image, self.direction)
            self.rect = self.image.get_rect()
            self.rect.center = self.position
    



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
        normal = pygame.image.load('image/padlv3_H.png')
        def __init__(self, position):
            super(Wall_H, self).__init__()
            self.rect = pygame.Rect(self.normal.get_rect())
            self.rect.center = position
            self.image = self.normal
    
    class Wall_W(pygame.sprite.Sprite):
        normal = pygame.image.load('image/padlv3_W.png')
        def __init__(self, position):
            super(Wall_W, self).__init__()
            self.rect = pygame.Rect(self.normal.get_rect())
            self.rect.center = position
            self.image = self.normal
    
    
    pads = [
        Wall_H((10,535)),
        Wall_H((10,412)),
        Wall_H((10,296)),
        Wall_H((10,177)),
        Wall_H((10,62)),

        Wall_H((1197,535)),
        Wall_H((1197,412)),
        Wall_H((1197,296)),
        Wall_H((1197,177)),
        Wall_H((1197,62)),

        
        Wall_H((129,296)),
        Wall_H((129,419)),
        Wall_H((129,536)),
        Wall_H((129,192)),
        
        Wall_H((266,72)),
        Wall_H((266,198)),
        Wall_H((266,317)),

        Wall_W((397,359)),
        Wall_W((557,359)),
        Wall_W((760,359)),
        Wall_W((918,359)),

        Wall_W((384,392)),
        Wall_W((587,392)),
        Wall_W((790,392)),
        Wall_W((963,392)),

        Wall_W((952,433)),
        Wall_W((792,433)),
        Wall_W((598,433)),
        Wall_W((460,433)),

        Wall_W((250,560)),
        Wall_W((449,560)),
        Wall_W((653,560)),
        Wall_W((858,560)),
        Wall_W((1061,560)),
        Wall_W((264,579)),
        Wall_W((464,579)),
        Wall_W((666,579)),
        Wall_W((868,579)),
        Wall_W((1075,579)),

        Wall_W((122,-5)),
        Wall_W((320,-5)),
        Wall_W((523,-5)),
        Wall_W((727,-5)),
        Wall_W((933,-5)),
        Wall_W((112,-5)),

        Wall_W((392,30)),
        Wall_W((602,30)),
        Wall_W((814,30)),
        Wall_W((1024,30)),

        Wall_W((392,61)),
        Wall_W((602,61)),
        Wall_W((814,61)),
        Wall_W((1024,61)),

        Wall_W((533,196)),
        Wall_W((712,196)),
        Wall_W((927,196)),
        Wall_W((1139,196)),

        Wall_W((500,226)),
        Wall_W((712,226)),
        Wall_W((927,227)),
        Wall_W((1139,226)),
        ]
     
    pad_group = pygame.sprite.RenderPlain(*pads)


    class Trophy(pygame.sprite.Sprite):
        def __init__(self, position):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('image/trophy.png')
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = position
        def draw(self, screen):
            screen.blit(self.image, self.rect)

    trophies = [Trophy((1124,109))]
    trophy_group = pygame.sprite.RenderPlain(*trophies)

    # CREATE A CAR AND RUN
    #rect = screen.get_rect()
    car = CarSprite("image/driveCar/yellowcar.png", (67, 560))
    car_group = pygame.sprite.RenderPlain(car)

    Car_Ai = [CarAI('image/cars/police.png' , (176,88)),
    CarAI('image/cars/ca.png' , (999,158)),
    CarAI('image/cars/cas.png' , (46,455)),
    CarAI('image/cars/f1.png' , (220,45)),
    CarAI('image/cars/f1.png' , (1112,471)),
    CarAI('image/cars/white.png' , (301,325))]  
    cars_group = pygame.sprite.RenderPlain(*Car_Ai)

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
                elif event.key == K_UP: car.k_up = down * 2
                elif event.key == K_DOWN: car.k_down = down * -1
                elif event.key == K_SPACE: car.k_down = down * -1
                elif event.key == K_ESCAPE: sys.exit(0) # quit the game

            elif win_condition == True and event.key == K_SPACE:
                pygame.mixer.music.load('music/OnlyMP3.to - Never Gonna Give You Up (8 Bit Remix Cover Version) [Tribute to Rick Astley] - 8 Bit Universe.mp3')
                pygame.mixer.music.set_volume((0.3978141))
                pygame.mixer.music.play(loops=10, start=0.0)
                level3.level3()
            elif win_condition == False and event.key == K_SPACE: 
                level2()
                t0 = t1
            elif event.key == K_ESCAPE: sys.exit(0)    
    
        #COUNTDOWN TIMER
        seconds = round((350 - dt),2)
        if win_condition == None:
            timer_text = font.render(str(seconds), True, (255,255,0))
            if seconds <= 0:
                win_condition = False
                timer_text = font.render("Time!", True, (255,0,0))
                loss_text = win_font.render('Press Space to Retry', True, (255,0,0))
            
    
        #RENDERING
        
        car_group.update(deltat)
        cars_group.update(deltat)
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
        
        cars_collisions = pygame.sprite.groupcollide(car_group, cars_group, False, False, collided = None)
        if cars_collisions != {}:
            win_condition = False
            timer_text = font.render("Crash!", True, (255,0,0))
            car.image = pygame.image.load('image/collision.png')
            loss_text = win_font.render('Press Space To Retry', True, (255,0,0))
            seconds = 0
            car.MAX_FORWARD_SPEED = 0 
            car.MAX_REVERSE_SPEED = 0
            car.k_right = 0
            car.k_left = 0    
               
        
        
        
        screen.blit(back_g,(0,0))
        pad_group.update(collisions)
        pad_group.draw(screen)
        car_group.draw(screen)

        cars_group.update(cars_collisions)
        cars_group.draw(screen)

        trophy_group.draw(screen)
        #Counter Render
        screen.blit(timer_text, (20,60))
        screen.blit(win_text, (400, 500))
        screen.blit(loss_text, (400, 500))
        pygame.display.flip()


