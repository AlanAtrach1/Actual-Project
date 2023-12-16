
import pygame
import math
from random import randint
 
BLACK = (0, 0, 0)
 
class Ball(pygame.sprite.Sprite):    
    def __init__(self, color, wid, heig, x, y):
        super().__init__()
        
        #Making dimentions of ball and background transparent
        self.image = pygame.Surface([wid, heig])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Drawing ball (shaped as a square)
        pygame.draw.rect(self.image, color, [0, 0, wid, heig])
        self.rect = self.image.get_rect()
        
        #Initialize Properties
        self.velocity = [0, 0]
        self.start_x = x
        self.start_y = y
    
    #Allows for ball movement with every tick
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    #Changes velocity to values found in a later function
    def direction(self, x, y):
        self.velocity[0] = x
        self.velocity[1] = y
    
    #Bouncing off bricks
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)

    #Removes ball
    def die(self):
            self.kill()

    #Allows for triangulation from mouse curser to initial ball location
    def movement(self, vel):
        mx, my = pygame.mouse.get_pos()
        dx = mx - self.rect.x
        dy = my - self.rect.y
        angle = math.atan2(dx,dy)
        mvx = math.sin(angle)
        mvy = math.cos(angle)
        self.direction(mvx * vel, mvy * vel)

    #Restarts the ball to its initial position with a random x value
    def reset(self, randpos):
        self.rect.x = randint(5, randpos - 5)
        self.rect.y = self.start_y
        self.velocity = [0, 0]

    #Exponentially accelerating over time
    def speedup(self, time):
        self.velocity[0] *= (1.01 ** (time/2))
        self.velocity[1] *= (1.01 ** (time/2))









