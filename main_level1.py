#initialize the screen
import pygame, math, sys, level2, time
from pygame.locals import *


def level1():
    pygame.init()
    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption('NEED FOR SPEED' )
    back_g = pygame.image.load('image/bgLV1.png')
    pygame.display.set_caption('NEED FOR SPEED LV1')
    
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
        CONNERy=[]

        def __init__(self, image, position):
            pygame.sprite.Sprite.__init__(self)
            self.src_image = pygame.image.load(image)
            self.position = position
            self.speed = self.direction = 0
            
        
        def update(self, deltat):
            #SIMULATION
            self.speed =1
       

            LineX=[1068]
            LineY=[560,357]
           

            x, y = (self.position)
            rad = self.direction * math.pi / 180
            if (x<LineX[0] and y==LineY[0]):  #line 1
                self.direction = 0 
                x += self.speed
            elif (x == LineX[0] and y > LineY[1] and y<=LineY[0]): #line 2
                self.direction = 90
                y += -self.speed
            elif (x >= 347 and x<= 1069 and y==357 ): #line 3
                self.direction =180
                x += -self.speed
            elif (x == 346 and y>=216 and y <= 357 ): #line 4 
                self.direction =90
                y += -self.speed
            elif (x>=345 and x <= 1135 and y==215): #line 5    
                self.direction =0
                x += self.speed
            elif (x == 1136 and y>=30 and y <= 217 ): #line 6     
                self.direction =90
                y += -self.speed
            elif (x >= 79 and x<= 1136 and y==29 ): #line 7            
                self.direction =180
                x += -self.speed
            elif (x == 78 and y<300 and y>=29 ): #line 8
                self.direction =270
                y+= self.speed
            #U-TURN 
            elif ( x>=78 and  x<= 125 and y == 300 ): 
                self.direction=0  
                x+= self.speed
            elif (x == 126 and y >= 79 and y <= 300  ): 
                self.direction=90 
                y+= -self.speed
            #U-TURN 
            elif (x <= 1097 and x>= 125 and y == 78): #line 8
                self.direction=0 
                x+= self.speed
            elif (x== 1098 and y< 173 and y>=78): #line 7
                self.direction=270 
                y+= self.speed 
            elif (x<= 1098 and x>280 and y==173): #line 6
                self.direction=180 
                x+= -self.speed
            elif (x == 280 and y <420 and y >= 173 ): #line 5
                self.direction=270 
                y+= self.speed
            elif (x>=280 and x<1018 and y==420 ): #line 4
                self.direction=0 
                x+= self.speed
            elif (x==1018 and y>=420 and y<498): #line 3
                self.direction=270 
                y+= self.speed
            elif (x <= 1018 and x > 120 and y==498): #line 2
                self.direction=180 
                x+= -self.speed
            #U-turn 
            elif (x==120 and y>= 498 and y < 560): 
                self.direction=270 
                y+= self.speed
            elif (x>=120 and x<1068 and y==560):
                self.direction=0 
                x+= self.speed
            #U-turn 



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
        normal = pygame.image.load('image/tree.png')
        def __init__(self, position):
            super(Wall_H, self).__init__()
            self.rect = pygame.Rect(self.normal.get_rect())
            self.rect.center = position
            self.image = self.normal
    
    class Wall_W(pygame.sprite.Sprite):
        normal = pygame.image.load('image/wall.png')
        def __init__(self, position):
            super(Wall_W, self).__init__()
            self.rect = pygame.Rect(self.normal.get_rect())
            self.rect.center = position
            self.image = self.normal
    
    # class Car_Ai(pygame.sprite.Sprite):
    #     normal = pygame.image.load('image/yellowcarRIGHT.png')
    #     def __init__(self, position):
    #         super(Car_Ai, self).__init__()
    #         self.rect = pygame.Rect(self.normal.get_rect())
    #         self.rect.center = position
    #         self.image = self.normal
   
    
    
    pads = [
        Wall_H((13,325)),
        Wall_H((13,100)),
        Wall_H((40,325)),
        Wall_W((35,0)),
        Wall_W((100,0)),
        Wall_W((250,0)),
        Wall_W((400,0)),
        Wall_W((600,0)),
        Wall_W((800,0)),
        Wall_W((1080,0)),
        Wall_H((1187,100)),
        Wall_H((1187,300)),
        Wall_H((1187,500)),
        Wall_H((1160,400)),
        Wall_H((1160,600)),
        Wall_H((1133,400)),
        Wall_H((1133,600)),
        Wall_W((220,598)),
        Wall_W((500,598)),
        Wall_W((700,598)),
        Wall_W((980,598)),
        Wall_W((150,450)),
        Wall_W((450,450)),
        Wall_W((700,450)),
        Wall_W((800,450)),
        Wall_W((220,475)),
        Wall_W((500,475)),
        Wall_W((800,475)),
        Wall_W((330,120)),
        Wall_W((600,120)),
        Wall_W((850,120)),
        Wall_W((570,320)),
        Wall_W((820,320)),
        Wall_W((970,320)),
        Wall_W((970,270)),
        Wall_H((170,280)),
        Wall_H((200,280)),
        Wall_H((230,280)),
        Wall_W((670,270)),
        Wall_W((570,270)),
        Wall_W((520,295)),
        Wall_W((820,295)),
        Wall_W((970,295)),
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

    trophies = [Trophy((90,399))]
    trophy_group = pygame.sprite.RenderPlain(*trophies)

    # CREATE A CAR AND RUN
 

    car = CarSprite("image/driveCar/redcar.png", (40, 540))
    car_group = pygame.sprite.RenderPlain(car)


    Car_Ai = [CarAI('image/cars/police.png' , (500, 560)),
                CarAI('image/cars/white.png' , (1098, 80)) ,
                CarAI('image/cars/police.png' , (120, 300)),
                CarAI('image/cars/orangeCar.png' , (280, 175)),
                CarAI('image/cars/f1.png' , (345, 215)),
                CarAI('image/cars/cas.png' , (1100, 29 )),
                CarAI('image/cars/ca.png' , (1018, 421))
            ]  
    cars_group = pygame.sprite.RenderPlain(*Car_Ai)
   

    #THE GAME LOOP
    while 1:
        #USER INPUT
        t1 = time.time()
        dt = t1-t0
        
        
        deltat = clock.tick(30)   #fram Rate
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    pygame.display.update()
                    pygame.display.flip()
            if not hasattr(event, 'key'): continue
            down = event.type == KEYDOWN 
            #SST MOVE CAR
            if win_condition == None: 
                if event.key == K_RIGHT: car.k_right = down * -5 
                elif event.key == K_LEFT: car.k_left = down * 5
                elif event.key == K_UP: car.k_up = down * 1
                elif event.key == K_DOWN: car.k_down = down * -1
                elif event.key == K_SPACE: car.k_down = down*-1
                elif event.key == K_ESCAPE: sys.exit(0) # quit the game

            elif win_condition == True and event.key == K_SPACE:
                pygame.mixer.music.load('music/Baby Shark [8 Bit Tribute to Pinkfong The Washington Nationals] - 8 Bit Universe.mp3')
                pygame.mixer.music.set_volume((0.1))
                pygame.mixer.music.play(loops=100, start=0.0)
                level2.level2()
            elif win_condition == False and event.key == K_SPACE: 
                level1()
                t0 = t1
            elif event.key == K_ESCAPE: sys.exit(0)    
    
        #COUNTDOWN TIMER
        #SET TIME TO LEVEL 1
        setTIME = 5900
        seconds = round((setTIME - dt),2)
        if win_condition == None:
            timer_text = font.render(str(seconds), True, (255,255,0))
            if seconds <= 0:
                win_condition = False
                timer_text = font.render(" Over Time !!!", True, (255,0,0))
                loss_text = win_font.render('Time Out !!! Press Space To Retry', True, (255,0,0))
            
    
        #RENDERING
        
        car_group.update(deltat)
        cars_group.update(deltat)
        collisions = pygame.sprite.groupcollide(car_group, pad_group, False, False, collided = None)
        if collisions != {}:
            win_condition = False
            timer_text = font.render("Crash!", True, (255,0,0))
            car.image = pygame.image.load('image/collision.png')
            loss_text = win_font.render('Press Space To Retry', True, (255,0,0))
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
            pygame.mixer.music.load('music/Teenage Mutant Ninja Turtles Theme Song (8 Bit Remix Cover Version) - 8 Bit Universe.mp3')
            pygame.mixer.music.set_volume((0.3978141))    
            pygame.mixer.music.play(loops=10, start=0.0)
            win_text = win_font.render('You are Finish !! Press Space to next Level ', True, (0,255,0))  #Press Space to Advance
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
        
        cars_group.update(cars_collisions)
        cars_group.draw(screen)


        car_group.draw(screen)
        # car_ai.draw(screen)
        trophy_group.draw(screen)
        #Counter Render
        screen.blit(timer_text, (20,60))
        screen.blit(win_text, (250, 500))
        screen.blit(loss_text, (400, 500)) # (X,Y)
        pygame.display.flip()


