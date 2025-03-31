import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Ship: 
    
    def __init__(self, game:'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        
        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.ship_w, self.settings.ship_h))
        
        #collision rectangle
        self.rect = self.image.get_rect()

        #center the ship at the buttom middle of the screen
        self.rect.midbottom = self.screen_rect.midbottom #initial start of the project


#ship should be able to drwaw itself
    def draw(self):
        self.screen.blit(self.image, self.rect)  #drawing unto the actual game(a rectangle)     

