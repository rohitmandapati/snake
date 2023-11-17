import pygame
import sys
import time
from snake import SnakeHead, SnakeBody
from candy import Candy

pygame.init()

SCREENWIDTH = 475
SCREENHEIGHT = 475

screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))

from pygame.locals import (
    K_LEFT,
    K_RIGHT
)

def candyCheck(sn: SnakeHead, c: Candy ):
    if(sn.getX() == c.getX() and sn.getY() == c.getY()):
        del c
        c.shuffle()    

def keyCheck(): 
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # checking if key "A" was pressed
            if event.key == pygame.K_a:
                sn.turn((1,0,0))
                print("A")
            # checking if key "D" was pressed
            elif event.key == pygame.K_d:
                sn.turn((0,0,1))
                print("D")
            elif event.key == pygame.K_w:
                sn.turn((0,1,0))
                print("W")

c = Candy()
sn = SnakeHead()

COORDINATES = []
for i in range(0, 19):
    for j in range(0, 19):
        COORDINATES.append((i,j))

score = 0

running = True
while running:
    screen.fill((0,0,0))
    # pygame.Surface.fill()
    
    pygame.draw.rect(screen, (255,10,10), c.getRect())
    
    pygame.draw.rect(screen, (0,255,255), sn.getRect())
    sn.move()
        
    time.sleep(0.5)
    pygame.display.flip()
    
    if(not sn.collisionBoundCheck()):
        break
    keyCheck()
    candyCheck(sn, c)




pygame.quit()
sys.exit()