import random
import pygame

class Candy:
    
    def __init__(self):
        xPos = random.randint(0, 18)
        yPos = random.randint(0, 18)
        self.loca = [xPos, yPos]
    
    def getX(self):
        return self.loca[0]
   
    def getY(self):
        return self.loca[1]
    
    def getRect(self):
        vertTopLeftX = self.getX() * 25
        vertTopLeftY = self.getY() * 25
        
        return pygame.Rect(vertTopLeftX, vertTopLeftY, 25, 25)
    
    def shuffle(self):
        pass
        

    
    