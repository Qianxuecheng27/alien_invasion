import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """represent single alien"""

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #load alien image and set rect distribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #initial every alien appear at left-top conner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #save where is the alien
        self.x = float(self.rect.x)

    def blitme(self):
        """draw alien at right place"""
        self.screen.blit(self.image, self.rect)