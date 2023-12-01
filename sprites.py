# This file was created by: Ethan Chacko 


import pygame as pg
from pygame.sprite import Sprite

from pygame.math import Vector2 as vec
import os
from settings import *
from main import *



font20 = pg.font.Font('freesansbold.ttf', 20)
# Setting the basic parameters of the screen
screen = pg.display.set_mode((WIDTH, HEIGHT))

# Creating the Player class

class Player: 
    # Defining the Player
    def __init__(self, posx, posy, width, height, speed, color):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.rect = pg.Rect(posx, posy, width, height)
        # Object that is shown on the screen
        self.rect = pg.draw.rect(screen, self.color, self.rect)
 
    # Used to display the object on the screen
    def display(self):
        self.show = pg.draw.rect(screen, self.color, self.rect)

    # Defining the state of the object
    def update(self, xvel):
        self.posx = self.posx + self.speed*xvel
 
        # Restricting the Player so that it can't travel out of bounds
        if self.posx <= 0:
            self.posx = 0
      
        elif self.posx + self.height >= WIDTH:
            self.posx = WIDTH-self.width
 
        # Updating the rect with the new values
        self.rect = (self.posx, self.posy, self.width, self.height)

# Used to render the score on to the screen
    def displayScore(self, text, score, x, y, color):
        text = font20.render(text+str(score), True, color)
        textRect = text.get_rect()
        textRect.center = (x, y)
 
        screen.blit(text, textRect)
 
    def getRect(self):
        return self.rect
    
# Creating the Computer Class
# Artifical Stupidity :)

class Computer: 
    # Defining the Computer
    def __init__(self, posx, posy, width, height, speed, color):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.rect = pg.Rect(posx, posy, width, height)
        # Object that is shown on the screen
        self.rect = pg.draw.rect(screen, self.color, self.rect)
 
    # Used to display the object on the screen
    def display(self):
        self.show = pg.draw.rect(screen, self.color, self.rect)

    # Defining the state of the object
    def update(self, xvel, ball):
        if self.posx < ball.posx:
            xvel += 1
        if self.posx > ball.posx:
            xvel -= 1
        self.posx = self.posx + self.speed*xvel
 
        # Restricting the Computer so that it can't exceed the boundries
        if self.posx <= 0:
            self.posx = 0
        
        elif self.posx + self.height >= WIDTH:
            self.posx = WIDTH-self.width
 
        # Updating the rect with the new values
        self.rect = (self.posx, self.posy, self.width, self.height)

# Used to render the score on to the screen
    def displayScore(self, text, score, x, y, color):
        text = font20.render(text+str(score), True, color)
        textRect = text.get_rect()
        textRect.center = (x, y)
 
        screen.blit(text, textRect)
 
    def getRect(self):
        return self.rect
    
#Creating the Ball class
class Ball:
    def __init__(self, posx, posy, radius, speed, color):
        self.posx = posx
        self.posy = posy
        self.radius = radius
        self.speed = speed
        self.color = color
        self.xvel = 1
        self.yvel = -1
        self.ball = pg.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)
        self.firstTime = 1
 
    def display(self):
        self.ball = pg.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)
    
    def update(self):
        self.posx += self.speed*self.xvel
        self.posy += self.speed*self.yvel

        # Making the ball bounce/reflect of the walls
        if self.posx <= 0 or self.posx >= WIDTH:
            self.xvel *= -1

        # Making sure that the program adustss the score when someone scores
        if self.posy <= 0 and self.firstTime:
            self.firstTime = 0
            return 1
        elif self.posy >= HEIGHT and self.firstTime:
            self.firstTime = 0
            return -1
        else:
            return 0
        

# Used to reset the position of the ball to the center of the screen
    def reset(self):
        self.posx = WIDTH//2
        self.posy = HEIGHT//2
        self.yvel *= -1
        self.firstTime = 1
 
    # Used to reflect the ball along the Y-axis
    def hit(self):
        self.yvel *= -1
 
    def getRect(self):
        return self.ball