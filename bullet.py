import pygame
from pygame.sprite import Sprite #import sprite from bullet grouping
from typing import TYPE_CHECKING #import type check for better IDE

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Bullet(Sprite):
    def __init__(self, game: 'AlienInvasion'):
        """Create a bullet object at the ship's position.
        
        Args:
            game (AlienInvasion): The game instance, providing settings and screen access.
        """
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings    

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.bullet_w, self.settings.bullet_h))
        self.image = pygame.transform.rotate(self.image, -90)   #rotate the image dir of the bullet     
 
        # Position the bullet at the midright side of the ship
        self.rect = self.image.get_rect()
        self.rect.midright = game.ship.rect.midright #should be midright to change the dir of the bullet
        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.bullet_speed
        self.rect.x = self.x
  
    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)

        
        