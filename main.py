import pygame
import time
from snake import SnakeHead

pygame.init()

SCREENWIDTH = 475
SCREENHEIGHT = 475

screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))

from pygame.locals import (
    K_LEFT,
    K_RIGHT
)

sn = SnakeHead()

running = True
while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    # pygame.Surface.fill()
    sn.move()
    pygame.draw.rect(screen, (0,255,255), sn.getRect())
    
    time.sleep(0.5)
    
    pygame.display.flip()
    
pygame.quit()