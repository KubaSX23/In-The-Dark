import pygame
import time
import tkinter.filedialog

pygame.init()
window = pygame.display.set_mode((1380, 720))

def liniesiatki():
    blockSize = 25 
    for x in range(0, 1280, blockSize):
        for y in range(0, 720, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(window, (148,148,148), rect, 1)   
class Sciana:
    def __init__(self, x, y, szerokosc, wysokosc):
        
        self.x_cord = x
        self.y_cord = y
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.szerokosc, self.wysokosc)
 
    def __str__(self):
        return f"Sciana({self.x_cord},{self.y_cord},{self.szerokosc},{self.wysokosc}),"
 
    def draw(self):
        pygame.draw.rect(window, (0,0,0) , self.hitbox)
   
class Lawa:
    def __init__(self, x, y, szerokosc, wysokosc):
        
        self.x_cord = x
        self.y_cord = y
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.szerokosc, self.wysokosc)
 
    def __str__(self):
        return f"Lawa({self.x_cord},{self.y_cord},{self.szerokosc},{self.wysokosc}),"
 
    def draw(self):
        pygame.draw.rect(window, (255,0,0,) , self.hitbox)
    
item = 'sciana'

  
sciany = [
] 
lawy = [
]
 
scianaTrue = pygame.image.load('Textures\scianaSelect.png')
lavaTrue = pygame.image.load('Textures\lavaSelect.png')

pozycjasciana = 0
pozycjalava = 0
x = 0
y = 0
sizey = 25
sizex = 25
siatka = True
speed = 25
run = True

while run:
    
    time.sleep(0.05)
    pygame.time.Clock().tick(30)
    keys = pygame.key.get_pressed()
    window.fill((255,255,255))   
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:  
            run = False
  
    if keys[pygame.K_1]:
        item = 'sciana'
    if keys[pygame.K_2]:
        item = 'lawa'
    if keys[pygame.K_RIGHT] and not x == 1275:  
        x += speed
    if keys[pygame.K_LEFT] and not x == 0: 
        x -= speed
    if keys[pygame.K_UP] and not y == 0:  
        y -= speed
    if keys[pygame.K_DOWN]and not y == 700: 
        y += speed
    if keys[pygame.K_SPACE] and spacecheck == True:  
        spacecheck = False
        if item == 'sciana':
            sciany.insert(pozycjasciana, Sciana(x,y,sizex, sizey))
            print('-='*40)
            for sciana in sciany:
                print(sciana)
            for lawa in lawy:
                print(lawa)
            print('-='*40)
            pozycjasciana += 1   
        if item == 'lawa':
            sciany.insert(pozycjalava, Lawa(x,y,sizex,sizey))
            print('-='*40)
            for sciana in sciany:
                print(sciana)
            for lawa in lawy:
                print(lawa)
            print('-='*40)
            pozycjalava += 1  
    if not keys[pygame.K_SPACE]:
        spacecheck = True
              
    if keys[pygame.K_s]:
        sizey += 25

    
    if keys[pygame.K_w] and not sizey == 25:
        sizey -= 25


    if keys[pygame.K_d]:
        sizex += 25


    
    if keys[pygame.K_a] and not sizex == 25:
        sizex -= 25
    if keys[pygame.K_q]:
        if siatka == True:
            siatka = False
            print('siatka wylaczona')
        else:
            siatka = True
            print('siatka wlaczona')

    for sciana in sciany:
        sciana.draw()
    for lawa in lawy:
        lawa.draw()

    pygame.draw.rect(window, (255,255,0), (x, y, sizex, sizey), 6)
    if siatka == True:
        liniesiatki()
    pygame.draw.rect(window, (219, 222, 255), (1280, 0, 100, 720),)


    if item == 'sciana':
        window.blit(scianaTrue, (1290, 20))
    if not item == 'sciana':
        window.blit(lavaTrue, (1290, 20))
    pygame.display.update()



pygame.quit()
