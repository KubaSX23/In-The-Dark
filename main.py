import pygame





pygame.init()
menuselect = 1
window = pygame.display.set_caption('Gra')
window = pygame.display.set_mode((1280, 720))


#libraries
icon = pygame.image.load('Textures\icon.ico').convert_alpha()
bgmenu = pygame.image.load('Textures\menubg.png').convert_alpha()
playbutton = pygame.image.load('Textures\playbutton.png').convert_alpha()
playbuttonselect = pygame.image.load('Textures\playbuttonselect.png').convert_alpha()
settingsbutton = pygame.image.load('Textures\settingsbutton.png').convert_alpha()
settingsbuttonselect = pygame.image.load('Textures\settingsbuttonselect.png').convert_alpha()
menubutton = pygame.image.load('Textures\menubutton.png').convert_alpha()
menubuttonselect = pygame.image.load('Textures\menubuttonselect.png').convert_alpha()
GameName = pygame.image.load('Textures\GameName.png').convert_alpha()



pygame.display.set_icon(icon)
level = 1

pygame.mixer.init()
pygame.mixer.music.load("Audio\loopmusic.mp3") 
pygame.mixer.music.play(-1,0.0)




class Physic:
    def __init__(self, x, y, szerokosc, wysokosc, przyspieszenie, MAX_SPEED):
        self.level = level
        self.x_cord = x  
        self.y_cord = y  
        self.predkosc_poziomu = 0  
        self.predkosc_pionu = 0  
        self.przyspieszenie = przyspieszenie  
        self.MAX_SPEED = MAX_SPEED  
        self.szerokosc = szerokosc  
        self.wysokosc = wysokosc  
        self.poprzednie_x = x
        self.poprzednie_y = y
        self.jumping = False  
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.szerokosc, self.wysokosc)

    def physic_tick(self, sciany, lawy):
        self.predkosc_pionu += 0.4
        self.x_cord += self.predkosc_poziomu
        self.y_cord += self.predkosc_pionu
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.szerokosc, self.wysokosc)  
        for sciana in sciany:
            if sciana.hitbox.colliderect(self.hitbox):
                 
                if self.x_cord + self.szerokosc >= sciana.x_cord + 1 > self.poprzednie_x + self.szerokosc:  #z lewej
                    self.x_cord = self.poprzednie_x
                    self.predkosc_poziomu = 0
                    
                if self.x_cord <= sciana.x_cord + sciana.szerokosc - 1 < self.poprzednie_x:   #z prawej
                    self.x_cord = self.poprzednie_x
                    self.predkosc_poziomu = 0
 
                if self.y_cord + self.wysokosc >= sciana.y_cord + 1 > self.poprzednie_y + self.wysokosc:   #z góry
                    self.y_cord = self.poprzednie_y
                    self.predkosc_pionu = 0
                    self.jumping = False

                if self.y_cord >= sciana.y_cord < self.poprzednie_y:  #z dołu
                    self.y_cord = self.poprzednie_y 
                    self.predkosc_pionu = 0

                    
        for lawa in lawy:
            if lawa.hitbox.colliderect(self.hitbox):
                pygame.mixer.Channel(1).play(pygame.mixer.Sound("Audio\dead.mp3"))
                self.x_cord = 1
                self.y_cord = 640
                self.poprzednie_x = 1
                self.poprzednie_y = 655
                
        if self.y_cord > 1000:
            self.x_cord = 1
            self.y_cord = 655
            self.poprzednie_x = 1
            self.poprzednie_y = 655
            pygame.mixer.Channel(1).play(pygame.mixer.Sound("Audio\dead.mp3")) 
        
        if self.x_cord >= 1275:
            self.level += 1
            self.x_cord = 1
            self.y_cord = 655
            self.poprzednie_x = 1
            self.poprzednie_y = 655
            pygame.mixer.Channel(1).play(pygame.mixer.Sound("Audio\succes.mp3"))



        if self.x_cord < 0:
            self.x_cord = 1       
   
        self.poprzednie_x = self.x_cord
        self.poprzednie_y = self.y_cord
                
                        
class Player(Physic):
    def __init__(self):
        self.image = pygame.image.load("Textures\postac1.png").convert_alpha()
        self.Sterowanie = 'wsad'
        pygame.mixer.init()
        szerokosc = self.image.get_width() 
        wysokosc = self.image.get_height() 
        super().__init__(1, 655, szerokosc, wysokosc, 0.125, 3)

    def tick(self, keys, sciany, lawy):
        self.physic_tick(sciany, lawy)
        
        if keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_d]:
            self.Sterowanie = 0

        if keys[pygame.K_UP] or keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
            self.Sterowanie = 1

        if self.Sterowanie == 0:
            if keys[pygame.K_a] and self.predkosc_poziomu > self.MAX_SPEED * -1:
                self.image = pygame.image.load("Textures\postac2.png").convert_alpha() 
                self.predkosc_poziomu -= self.przyspieszenie

            if keys[pygame.K_d] and self.predkosc_poziomu < self.MAX_SPEED:
                self.image = pygame.image.load("Textures\postac1.png").convert_alpha()
                self.predkosc_poziomu += self.przyspieszenie

            if keys[pygame.K_w] and self.jumping is False:
                self.predkosc_pionu -= 10
                self.jumping = True

            if not (keys[pygame.K_d] or keys[pygame.K_a]):
                if self.predkosc_poziomu > 0:
                    self.predkosc_poziomu -= self.przyspieszenie
                elif self.predkosc_poziomu < 0:
                    self.predkosc_poziomu += self.przyspieszenie

        if self.Sterowanie == 1:
            if keys[pygame.K_LEFT] and self.predkosc_poziomu > self.MAX_SPEED * -1:
                self.image = pygame.image.load("Textures\postac2.png").convert_alpha() 
                self.predkosc_poziomu -= self.przyspieszenie

            if keys[pygame.K_RIGHT] and self.predkosc_poziomu < self.MAX_SPEED:
                self.image = pygame.image.load("Textures\postac1.png").convert_alpha()
                self.predkosc_poziomu += self.przyspieszenie

            if keys[pygame.K_UP] and self.jumping is False:
                self.predkosc_pionu -= 10
                self.jumping = True

            if not (keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]):
                if self.predkosc_poziomu > 0:
                    self.predkosc_poziomu -= self.przyspieszenie
                elif self.predkosc_poziomu < 0:
                    self.predkosc_poziomu += self.przyspieszenie
                              

        
        
            
  
    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))
        pygame.mixer.init()


class Sciana:
    def __init__(self, x, y, szerokosc, wysokosc):
        self.x_cord = x
        self.y_cord = y
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.szerokosc, self.wysokosc)

    def draw(self, win):
        pygame.draw.rect(win, (0,0,0) , self.hitbox)


class Lawa:
    def __init__(self, x, y, szerokosc, wysokosc):
        self.x_cord = x
        self.y_cord = y
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.szerokosc, self.wysokosc)

    def draw(self, win):
        pygame.draw.rect(win, (255,0,0) , self.hitbox, )




def main():
    gamestart = False
    run = True
    player = Player()
    clock = 0
    czcionka = pygame.font.SysFont('Comic Sans', 40)
    background = pygame.image.load("Textures\Tlo.png").convert_alpha()
 


    sciany = [
        Sciana(0, 695, 620, 25),
        Sciana(600, 620, 25, 100),
        Sciana(800, 695, 620, 25),
        ]
    lawy = [
        Lawa(270, 695, 70, 25),
    ]



    while run:
        transition = True
        leveltext = czcionka.render('  Level: ' + (str(player.level)), False, (0, 0, 0))
        clock += pygame.time.Clock().tick(130) * 100
        keys = pygame.key.get_pressed()
        player.tick(keys, sciany, lawy)
        window.blit(background, (0, 0))  
        window.blit(leveltext, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                run = False
        mouseposx = pygame.mouse.get_pos()[0]
        mouseposy = pygame.mouse.get_pos()[1]
    
        #MENU
        if gamestart == False:
            window.blit(bgmenu, (0,0))
            window.blit(GameName, (240,25)) 
            #PLAY BUTTON
            if mouseposx >= 530 and mouseposx <= 730 and mouseposy >= 270 and mouseposy <= 370:
                window.blit(playbuttonselect, (530,265)) 
                if pygame.mouse.get_pressed()[0]:                                                 
                    gamestart = True
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("Audio\clickbutton.wav"))
            else:
                window.blit(playbutton, (540,270)) 



            #SETTINGS BUTTON
            if mouseposx >= 530 and mouseposx <= 730 and mouseposy >= 375 and mouseposy <= 475:
                window.blit(settingsbuttonselect, (530,385)) 
                if pygame.mouse.get_pressed()[0]:
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("Audio\clickbutton.wav"))
            else:
                window.blit(settingsbutton, (540,390)) 

        #GAME
        if gamestart == True:
            player.draw()
            for sciana in sciany:
                sciana.draw(window)
            for lawa in lawy:
                lawa.draw(window)
            #MENU BUTTON
            if mouseposx >= 1200 and mouseposx <= 1280 and mouseposy >= 0 and mouseposy <= 70:
                window.blit(menubuttonselect, (1200,5)) 
                if pygame.mouse.get_pressed()[0]:
                    pygame.mixer.Channel(1).play(pygame.mixer.Sound("Audio\clickbutton.wav"))
                    gamestart = False

            else:
                window.blit(menubutton, (1200,5)) 


        
        #LEVELE:





        #arg 1-x 2-y 3-szerokosc 4-wysokosc
        if player.level == 2:
            sciany = [
                Sciana(0, 695, 620, 25),
                Sciana(50, 490, 25, 100),
                Sciana(600, 600, 25, 200),
                Sciana(50, 570, 470, 25),
                Sciana(200, 410, 470, 25),
                Sciana(800, 410, 670, 25),
                ]

            lawy = [   
                Lawa(625, 695, 800, 25), 
                ]
        
        if player.level == 3:
            sciany = [
                Sciana(0, 695, 620, 25),
                Sciana(0, 420, 870, 25),
                Sciana(0, 320, 270, 25),
                Sciana(270, 220, 1270, 25),
                Sciana(600, 620, 25, 100),
                Sciana(750, 620, 25, 100),
                Sciana(900, 620, 25, 100),
                Sciana(1050, 620, 320, 25),
                Sciana(1255, 245, 25, 375),
                Sciana(1150, 520, 220, 25),
                Sciana(1000, 420, 150, 25),
            ]
            lawy = [
                Lawa(625, 695, 125, 25),
                Lawa(775, 695, 125, 25),
                Lawa(925, 695, 999, 25),
                ]
        
        if player.level == 4:
            sciany = [
                Sciana(0, 695, 620, 25),
                Sciana(600, 620, 25, 100),
                Sciana(800, 220, 25, 500),
                Sciana(0, 520, 500, 25),
                Sciana(400, 410, 200, 25),
                Sciana(0, 445, 25, 75),
                Sciana(0, 300, 500, 25),
                Sciana(400, 200, 425, 25),
                Sciana(950, 195, 25, 525),
                Sciana(1100, 195, 25, 525),
                Sciana(1100, 195, 500, 25),
                Sciana(600, 205, 25, 230),
                ]

            lawy = [
                Lawa(625, 695, 175, 25),
                Lawa(825, 695, 125, 25),
                Lawa(975, 695, 125, 25),

            ]

        if player.level == 5:
            sciany = [
                Sciana(0,700,225,25),
                Sciana(225,625,25,100),
                Sciana(0,575,125,25),
                Sciana(0,500,25,100),
                Sciana(100,400,25,75),
                Sciana(100,400,75,25),
                Sciana(250,475,75,25),
                Sciana(300,425,25,75),
                Sciana(400,350,25,75),
                Sciana(400,350,75,25),
                Sciana(550,350,75,25),
                Sciana(700,350,75,25),
                Sciana(750,300,25,75),
                Sciana(775,700,125,25),
                Sciana(875,625,25,125),
                Sciana(1025,625,150,25),
                Sciana(1150,550,25,100),
                Sciana(1150,550,150,25),
                ]

            lawy = [
                ]
        if player.level == 6:
            sciany = [
                Sciana(0,700,325,25),
                Sciana(300,625, 25,100),
                Sciana(0,525,225,25),
                Sciana(300,425,25,75),
                Sciana(575,425,75,25),
                Sciana(625,375,25,75),
                Sciana(650,700,200,25),
                Sciana(825,625,25,125),
                Sciana(650,575,25,150),
                Sciana(650,550,100,25),
                Sciana(875,550,100,25),
                Sciana(950,475,25,100),
                Sciana(1000,400,75,25),
                Sciana(1050,275,25,150),
                Sciana(875,325,75,25),
                Sciana(1150,275,150,25),
                Sciana(450,425,75,25),
                Sciana(300,425,100,25),
                ]

            lawy = [
                Lawa(400,425,50,25),
                Lawa(525,425,50,25),
                ]
        if player.level == 7:
            sciany = [


                ]

            lawy = [


                ]
        

        pygame.mixer.init()
        pygame.display.update()
        
       

if __name__ == "__main__":
    main()