import pygame
from typing import TYPE_CHECKING

import arsenal

#import arsenal

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import ShipArsenal


class Ship: 
    
    def __init__(self, game:'AlienInvasion', arsenal:'arsenal'):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()
        
        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.ship_w, self.settings.ship_h))
        
        #collision rectangle
        self.rect = self.image.get_rect()

        #center the ship at the buttom middle of the screen
        self.rect.midbottom = self.boundaries.midbottom #initial start of the project
        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)
        self.arsenal = arsenal



    def update(self): 
        #updating the postion of the ship
        self._update_ship_movement()
        self.arsenal.update_arsenal() 

    def _update_ship_movement(self):
        temp_speed = self.settings.ship_speed
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed

        self.rect.x = self.x#what the x position is will be placed  in rect position   

        

#ship should be able to draw itself
    def draw(self):
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)  #drawing unto the actual game(a rectangle)     

    def fire(self):
        return self.arsenal.fire_bullet()
