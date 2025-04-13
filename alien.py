import pygame
from pygame.sprite import Sprite #import sprite from bullet grouping
from typing import TYPE_CHECKING #import type check for better IDE

if TYPE_CHECKING:
    from alien_fleet import AlienFleet


class Alien(Sprite):
    def __init__(self, fleet: 'AlienFleet', x: float, y: float):
        """Create a bullet object at the ship's position.
        
        Args:
            game (AlienInvasion): The game instance, providing settings and screen access.
        """
        super().__init__()
        self.fleet = fleet
        self.screen = fleet.game.screen #passing the screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings    

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.alien_w, self.settings.alien_h))
        self.image = pygame.transform.flip(self.image, True, False)   #fliped the image of the enemy to look at the ship 13     
 
        # Position the bullet at the midright side of the ship
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x #just added this updating the values to change

        #self.rect.midright = game.ship.rect.midright #should be midright to change the dir of the bullet
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)#13

    def update(self):
        #self.x += self.settings.bullet_speed
        #self.rect.x = self.x
        temp_speed = self.settings.fleet_speed#13

        
        self.x += temp_speed * self.fleet.fleet_direction
        self.rect.x = self.x #update the rectangle 13
        self.rect.y = self.y 

    def check_edges(self): #to make sure the alien stays in the rectangle
        return (self.rect.right >= self.boundaries.right or
                self.rect.left <= self.boundaries.left)

  
    def draw_alien(self):
        self.screen.blit(self.image, self.rect)


        
        