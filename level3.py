#initialize the screen
import pygame, math, sys, level4, time
from pygame.locals import *



def level3():
    pygame.init()
    
    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption('NEED FOR SPEED' )
    back_g = pygame.image.load('image/lv3.png')
    pygame.display.set_caption('NEED FOR SPEED LV3')
    
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
           

            x, y = (self.position)
            rad = self.direction * math.pi / 180
            if (x==82 and y<= 472 and y>63):  #line 1
                self.direction = 90 
                y += -self.speed
            elif (y==63 and x>=82 and x<207):  #line 1
                self.direction = 0 
                x += self.speed
            elif (x==207 and y>=63 and y<534):  #line 1
                self.direction = 270 
                y += self.speed
            elif (y==534 and x>=207 and x<435):  #line 1
                self.direction = 0 
                x += self.speed
            elif (x==435 and y<=534 and y>66):  #line 1
                self.direction = 90 
                y += -self.speed
            elif (y==66 and x>=435 and x<590):  #line 1
                self.direction = 0 
                x += self.speed
            elif (x==590  and y>=66 and y<550):  #line 1
                self.direction = 270 
                y += self.speed
            elif (y==550 and x>=590 and x<1167):  #line 1
                self.direction = 0 
                x += self.speed
            elif (x==1167 and y<= 550 and y>51):  #line 1
                self.direction = 90 
                y += -self.speed
            elif (y==51 and x<= 1167 and x>741):  #line 1
                self.direction = 180 
                x += -self.speed
            elif (x==741 and y>=51 and y<217):  #line 1
                self.direction = 270 
                y += self.speed
            #U-turn
            elif (y==217 and x>=741 and x<782):  #line 1
                self.direction = 0
                x += self.speed
            #U-turn
            elif (x==782 and y<=217 and y>82):  #line 1
                self.direction = 90 
                y += -self.speed
            elif (y==82 and x>=782 and x<1137):  #line 1
                self.direction = 180 
                x += self.speed
            elif (x==1137 and y>=82 and y<507):  #line 1
                self.direction = 270 
                y += self.speed
            elif (y==507 and x<=1137 and x>621):
                self.direction = 180 
                x += -self.speed
            elif (x==621 and y<=507 and y>34):  #line 1
                self.direction = 90 
                y += -self.speed
            elif (y==34  and x<=621 and x>400):
                self.direction = 180 
                x += -self.speed
            elif (x==400 and y>=34 and y<506):  #line 1
                self.direction = 270 
                y += self.speed
            elif (y==506 and x<=400 and x>240):
                self.direction = 180
                x += -self.speed
            elif (x==240 and y<=506 and y>23):  #line 1
                self.direction = 90 
                y += -self.speed
            elif (y==23 and x<=240 and x>40):
                self.direction = 180
                x += -self.speed
            elif (x==40 and y>=23 and y<472):  #line 1
                self.direction = 270
                y += self.speed
            #U-turn
            elif (y==472 and x>=40 and x<82):  #line 1
                self.direction = 0 
                x += self.speed
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
            Wall_H((11,61)),
        Wall_H((11,174)),
        Wall_H((11,286)),
        Wall_H((11,399)),
        Wall_H((11,538)),
        Wall_H((1203,33)),
        Wall_H((1203,142)),
        Wall_H((1203,257)),
        Wall_H((1203,372)),
        Wall_H((1203,507)),
        Wall_H((1203,200)),
        Wall_H((1203,318)),
        Wall_H((857,222)),
        Wall_H((857,330)),
        Wall_H((831,225)),
        Wall_H((831,330)),
        
        Wall_H((681,-2)),
        Wall_H((681,105)),
        Wall_H((681,222)),
        Wall_H((681,334)),
        Wall_H((657,392)),
        Wall_H((657,281)),
        Wall_H((657,169)),
        Wall_H((307,410)),
        Wall_H((307,299)),
        Wall_H((307,180)),
        Wall_H((307,65)),
        Wall_H((333,372)),
        Wall_H((333,302)),
        Wall_H((333,178)),
        Wall_H((333,65)),
        Wall_H((362,302)),
        Wall_H((362,181)),
        Wall_H((362,65)),
        Wall_H((483,510)),
        Wall_H((483,399)),
        Wall_H((483,286)),
        #Wall_H((483,172)),
        Wall_H((507,510)),
        Wall_H((507,399)),
        Wall_H((507,286)),
        Wall_H((507,172)),
        Wall_H((537,510)),
        Wall_H((537,399)),
        Wall_H((507,286)),
        Wall_H((507,172)),
        Wall_H((537,510)),
        Wall_H((537,399)),
        Wall_H((537,286)),
        #Wall_H((537,172)),

        Wall_W((763,408)),
        Wall_W((969,408)),
        Wall_W((777,582)),
        Wall_W((991,438)),
        Wall_W((789,470)),
        Wall_W((993,470)),
        Wall_W((975,363)),
        Wall_W((975,316)),
        Wall_W((975,276)),
        Wall_W((975,234)),
        Wall_W((975,195)),
        Wall_W((916,147)),
        Wall_W((992,150)),
        
        Wall_W((871,10)),
        Wall_W((1082,10)),
        Wall_W((678,-5)),
        Wall_W((495,-10)),
        Wall_W((294,-10)),
        Wall_W((99,-10)),
        Wall_W((212,578)),
        Wall_W((412,581)),
        Wall_W((633,582)),
       
        Wall_W((978,583)),
        Wall_W((1125,582)),

        Wall_H((276,200)),
        Wall_H((276,316)),
        Wall_H((169,186)),
        Wall_H((169,278)),
        Wall_H((169,392)),
        Wall_H((169,504)),
        Wall_H((142,162)),
        Wall_H((142,278)),
        Wall_H((142,392)),
        Wall_H((142,504)),
        Wall_H((115,186)),
        Wall_H((115,277)),
        Wall_H((115,392)),
        Wall_H((115,504)),

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

    trophies = [Trophy((740,270))]
    trophy_group = pygame.sprite.RenderPlain(*trophies)

    # CREATE A CAR AND RUN
    #rect = screen.get_rect()
    car = CarSprite("image/driveCar/f1.png", (47, 533))
    car_group = pygame.sprite.RenderPlain(car)

    Car_Ai = [CarAI('image/yellowcarRIGHT.png' , (40,472)),
              CarAI('image/cars/f1.png' , (741,217)),]  
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
                if event.key == K_RIGHT: car.k_right = down * -5 ; print("Turn Right")
                elif event.key == K_LEFT: car.k_left = down * 5 ; print("Turn Left")
                elif event.key == K_UP: car.k_up = down * 1  ; print("UP")
                elif event.key == K_DOWN: car.k_down = down * -1  ; print("Down")
                elif event.key == K_ESCAPE: sys.exit(0) # quit the game
            elif win_condition == True and event.key == K_SPACE:
                pygame.mixer.music.load('music/Ghostbusters [8 Bit Tribute to Ray Parker Jr.] - 8 Bit Universe.mp3')
                pygame.mixer.music.set_volume((0.3978141))
                pygame.mixer.music.play(loops=10, start=0.0)
                level4.level4()
            elif win_condition == False and event.key == K_SPACE: 
                level3()
                t0 = t1
            elif event.key == K_ESCAPE: sys.exit(0)    
    
        #COUNTDOWN TIMER
        seconds = round((300 - dt),2)
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


