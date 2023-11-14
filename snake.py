import pygame

class SnakeHead:
    
    # Directions
    # [UP, RIGHT, DOWN, LEFT]
    
    # Grid coordinates
    # {
    #   0 1 2 3 4 5 6 7 8
    #   1
    #   2
    #   3
    #   4
    #   5
    #   6
    #   7
    #   8 
    # }
    
    heading = []
    loca = []
    
    def __init__(self):
        self.loca = [0, 0]
        self.heading = [0, 0, 1, 0] 
    
    def getX(self):
        return self.loca[0]
    
    def getY(self):
        return self.loca[1]
    
    def getRect(self):
        vertTopLeftX = self.getX() * 25
        vertTopLeftY = self.getY() * 25
        
        return pygame.Rect(vertTopLeftX, vertTopLeftY, 25, 25)
    
    def move(self):
        if self.heading == [0, 1, 0, 0]:
            self.loca[0] += 1
        elif self.heading == [0, 0, 1, 0]:
            self.loca[1] += 1
        elif self.heading == [0, 0, 0, 1]:
            self.loca = [self.getX() - 1, self.getY()]
        elif self.heading == [1, 0, 0, 0]:
            self.loca = [self.getX(), self.getY() + 1]
    
    def turnLeft(self):
        temp = self.heading[0]
        self.heading.pop(0)
        self.heading.append(temp)
    
    def turnRight(self):
        temp = self.heading.pop(3)
        self.heading.insert(temp, 0)
        
        
