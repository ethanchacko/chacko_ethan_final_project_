#  This file was created by: Ethan Chacko

import pygame as pg
from settings import *


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((100,10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        # save this for the BALLL

        # This is determining the position of the Sprite
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 20 

        self.speedx = 0


    def update(self):
        self.speedx = 0 
        keystate = pg.key.get_pressed()
        if keystate[pg.K_a]:
            self.speedx = -20
        if keystate[pg.K_d]:
            self.speedx = 20
        self.rect.x += self.speedx

        # Limiting the Sprite so it can't go off screen
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

        if self.rect.left < 0:
            self.rect.left = 0 



class Computer(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((100,10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        # save this for the BALLL

        # This is determining the position of the Sprite
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 690 

        self.speedx = 0


    def update(self):
        self.speedx = 0 
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT]:
            self.speedx = -20
        if keystate[pg.K_RIGHT]:
            self.speedx = 20
        self.rect.x += self.speedx

        # Limiting the Sprite so it can't go off screen
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

        if self.rect.left < 0:
            self.rect.left = 0


class Ball(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((15, 15))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT / 2

        self.speedx = 5
        self.speedy = 2.5


    
    def update(self):
        
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.right > WIDTH:
            self.speedx *= -1

        if self.rect.left < 0:
            self.speedx *= -1

        # hits = pg.sprite.spritecollide(self.player, self.ball, False)
        # if hits:
        #     self.speedy *= -1

 
    def collsion(self):
        pass

        # if self.rect.y >= WIDTH:
        #     self.speedx *= -1
        
        # if self.rect.y <= 0:
        #     self.speedx *= -1
   
                   






    