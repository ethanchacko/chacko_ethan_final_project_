#  This file was created by: Ethan Chacko

# Sources:
# content from kids can code: http://kidscancode.org/blog/
# Create a Pong Game in Python - Pygame – GeeksforGeeks
# Mr.Cozort(Cris Cozort)
# My Father(Chacko, Antony) 

import pygame as pg
from settings import *

# Creating the Player Class
class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        # Setting how big the Player Sprite will be
        self.image = pg.Surface((100,10))
        # What color they will be
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        

        # This is determining the position of the Sprite
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 20 

        # Setting the intial speed to 0
        self.speedx = 0


    def update(self):
        self.speedx = 0 
        keystate = pg.key.get_pressed()
        # Controls
        if keystate[pg.K_a]:
            # Decides how fast we want the Player to go
            self.speedx = -10
        if keystate[pg.K_d]:
            self.speedx = 10
        self.rect.x += self.speedx

        # Limiting the Sprite so it can't go off screen
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

        if self.rect.left < 0:
            self.rect.left = 0 


# Creating the Computer Class
class Computer(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        # Setting how big the Player Sprite will be
        self.image = pg.Surface((100,10))
        # What color they will be
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
       

        # This is determining the position of the Sprite
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 690 

        # Setting the intial speed to 0
        self.speedx = 0


    def update(self):
        self.speedx = 0 
        keystate = pg.key.get_pressed()
        # Controls
        if keystate[pg.K_LEFT]:
            # Decides how fast we want the Player to go
            self.speedx = -10
        if keystate[pg.K_RIGHT]:
            self.speedx = 10
        self.rect.x += self.speedx

        # Limiting the Sprite so it can't go off screen
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

        if self.rect.left < 0:
            self.rect.left = 0

# Creating the Ball class
class Ball(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        # Sets how big the ball is
        self.image = pg.Surface((11, 11))
        # Sets the Color of the Ball
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

        # Determines where the Ball will be in the beggining
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT / 2

        # Determines the intial speed of the Ball
        self.speedx = 5
        self.speedy = 2.5


    
    def update(self):
        
        # Allows the ball to move
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Restricts the ball within the parameter of the screem 
        # Unlike the players, this makes the ball reflect of the sides of the screen, as we multiply it's speedx by -1, essentially reflecting it 
        if self.rect.right > WIDTH:
            self.speedx *= -1

        if self.rect.left < 0:
            self.speedx *= -1

       
   
                   






    