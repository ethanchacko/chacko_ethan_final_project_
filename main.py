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
import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint
from settings import *
from sprites import *


class Game:
    pg.init()

    def main():
        pg.display.set_caption("Tennis")
        # Used to adjust the frame rate
        clock = pg.time.Clock()
        running = True
 
        # Defining the objects
        p1 = Player(220, 50, 100, 10, 10, WHITE)
        p2 = Computer(320, 650, 100, 10, 10, WHITE)
        ball = Ball(WIDTH//2, HEIGHT//2, 7, 7, WHITE)

        listOfPlayers = [p1, p2]

        # Used to render the score on to the screen

    
        
        # Initial parameters of the Player and Computer
        p1Score, p2Score = 0, 0
        p1xvel, p2xvel = 0, 0
    
        while running:
            screen.fill(BLACK)

        # Event handling
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        p2xvel = -1
                    if event.key == pg.K_RIGHT:
                        p2xvel = 1
                    if event.key == pg.K_a:
                        p1xvel = -1
                    if event.key == pg.K_d:
                        p1xvel = 1
                if event.type == pg.KEYUP:
                    if event.key == pg.K_RIGHT or event.key == pg.K_LEFT:
                        p2xvel = 0
                    if event.key == pg.K_d or event.key == pg.K_a:
                        p1xvel = 0

            # Collision detection
            for p in listOfPlayers:
                if pg.Rect.colliderect(ball.getRect(), p.getRect()):
                    ball.hit()
    
            # Updating the objects
            p1.update(p1xvel)
            p2.update(p2xvel, ball)
            point = ball.update()

            # -1 -> The Player has scored
            # +1 -> The Computer has scored
            #  0 -> None of them scored
            if point == -1:
                p1Score += 1
            elif point == 1:
                p2Score += 1
    
            # Reseting the Ball when someone scores a point
            if point:   
                ball.reset()
    
            # Displaying the objects on the screen
            p1.display()
            p2.display()
            ball.display()
    
            # Displaying the scores of the players
            p1.displayScore("Player : ", p1Score, 100, 20, WHITE)
            p2.displayScore("Computer : ", p2Score, WIDTH-100, 20, WHITE)
    
            pg.display.update()
            # Adjusting the frame rate
            clock.tick(FPS)
                        

    if __name__ == "__main__":
        main()
        pg.quit()
