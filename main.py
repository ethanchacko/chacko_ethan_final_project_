# This file was created by: Ethan Chacko
# Title: Pong()

# Sources:
# content from kids can code: http://kidscancode.org/blog/
# Create a Pong Game in Python - Pygame – GeeksforGeeks
# Mr.Cozort(Cris Cozort)
# My Father(Chacko, Antony) 


# Goals:
# I want to make the game modular (Completed: Arguably the most important)
# Fixing the glitching(Completed)
# Adding Variables to make the game more interesting:
    # Made the Ball Accelerate upon each time it collides with one of the players(Completed)
    # Making the Player be able to choose where the want to hit the ball(Not yet)
    # Have the Computer also decides where is hits the Ball(Not Yet)
    # Change the color palet and look of the game(Not Yet: In its current state I feel like Black and White is best)
# Change the game from Pong to Tennis:(Not Yet)
    # Change the screen dimensions
    # Make a tennis court
    # Make it so that the ball can be hit out of bounds




# import libraries and modules
import pygame as pg 
from settings import *
from sprites import *

# Making the Game class
class Game:
    def __init__(self):
        # Initializing pygame, and creating the window, and setting window parameters
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Tennis Game")
        self.clock = pg.time.Clock()
        self.running = True

    # The things that should occur when a new window(game) is made
    def new(self):
        # Making a Sprite group that will contain all the Sprite(Player, Computer, Ball)
        self.all_sprites = pg.sprite.Group()
        # Making a group that will contain the players(Player, Computer)
        self.all_players = pg.sprite.Group()

        self.player = Player()
        self.computer = Computer()
        self.ball = Ball()

        # Adding these Sprites to their groups
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.computer)
        self.all_sprites.add(self.ball)
        self.all_players.add(self.player)
        self.all_players.add(self.computer)
        g.run()
    # What should occur when the game is running
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

    # Allowing for the Player and Computer to collide with the ball
    def collisions(self):
         hits = pg.sprite.spritecollide(self.ball, self.all_players, False)
         # When the os detects a collision has occured between the Ball and one of the players, the ball will reflect of them
         if hits:
            # By putting -1, the object will just reflect, but if you put more, then each time the ball collides with either one of the players(Player, Computer) it will increase it's speed
            self.ball.speedy *= -1.2

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                # If pg.Quit occurs, stop running
                if self.playing:
                    self.playing = False
                self.running = False
    
    
    def draw(self):
        # Draw 
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # Once everything is drawn, we display it
        pg.display.flip()



g = Game()
while g.running:
    g.new()


pg.quit()






