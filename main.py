# This file was created by: Ethan Chacko
# Sources: 

# Title: Tennis Simulator
# test git

# Goals:
# I want to make the game modular
# Making the Player be able to choose where the want to hit the ball
# Have the Computer also decides where is hits the Ball
# Change the color palet and look of the game
# Change the game from Pong to Tennis:
    # Change the screen dimensions
    # Make a tennis court
    # Make it so that the ball can be hit out of bounds




# import libraries and modules
#This file was made by: Ethan Chacko
# content from kids can code: http://kidscancode.org/blog/

import pygame as pg 
from settings import *
from sprites import *

class Game:
    def __init__(self):
        # Initializing pygame, and creating the window, and setting window parameters
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Tennis Game")
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.all_players = pg.sprite.Group()
        self.player = Player()
        self.computer = Computer()
        self.ball = Ball()
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.computer)
        self.all_sprites.add(self.ball)
        self.all_players.add(self.player)
        self.all_players.add(self.computer)
        g.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
    
            self.update()
            self.draw()

    def update(self):
        # Update 
    
        self.all_sprites.update()
        self.collisions()

        
    def collisions(self):
         hits = pg.sprite.spritecollide(self.ball, self.all_players, False)
         if hits:
            self.ball.speedy *= -1.5

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
    
    
    def draw(self):
         # Draw 
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # Once everything is drawn, Flip the Display
        pg.display.flip()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()






