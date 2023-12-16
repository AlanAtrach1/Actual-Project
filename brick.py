
import pygame
from random import randint

BLACK = (0,0,0)
 
class Brick(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        #Making dimentions of brick and background transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Drawing Brick
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()



