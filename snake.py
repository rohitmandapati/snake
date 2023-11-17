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
        self.heading = [0, 1, 0, 0] 
    
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
            self.loca[0] -= 1
        elif self.heading == [1, 0, 0, 0]:
            self.loca[1] -= 1
    
    def turn(self, n):
        if n == (1, 0, 0): 
            temp = self.heading[0]
            self.heading.pop(0)
            self.heading.append(temp)
        elif n == (0, 0, 1):
            print(self.heading)
            temp = self.heading[3]
            self.heading.pop(3)            
            print(self.heading)
            self.heading.insert(0, temp)
            print(self.heading)
            
    def collisionBoundCheck(self):
        if( 0 <= self.getX() <= 18 and 
           0 <= self.getY() <= 18):
            return True
        else: return False
    

class SnakeBody():
    loca = []
    
    def __init__(self, x, y):
        self.loca[0] = x
        self.loca[1] = y
    
    