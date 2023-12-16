
import pygame

WHITE = (255,255,255)
BLACK = (0, 0, 0)

class Button():
    def __init__(self, color, x, y, widt, heigh, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = widt
        self.height = heigh
        self.text = text

    #Function to summon button
    def draw(self, win, fontsize, outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.Font(None, fontsize)
            text = font.render(self.text, 1, WHITE)
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    #Function to identify if mouse is hovering over button
    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True           
        return False


        
#This section of the code is not mine. It is used for a trivial application that isn't necessary for the function of the game. The code's implementation to this program was done by me.