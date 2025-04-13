import pygame
from typing import TYPE_CHECKING

import arsenal

#import arsenal

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import ShipArsenal


class Ship: 
    
    def __init__(self, game:'AlienInvasion', arsenal:'arsenal'):
        """Initialize the ship and set its starting position.
        
        Args:
            game (AlienInvasion): The game instance, providing settings and screen access.
            arsenal (ShipArsenal): The ship's weapon system (handles bullets).
        """

        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()
        
        self.image = pygame.image.load(self.settings.ship_file) #load image
        self.image = pygame.transform.scale(self.image, 
            (self.settings.ship_w, self.settings.ship_h))
        self.image = pygame.transform.rotate(self.image, -90) # change the direction of the ship
        
        #collision rectangle for the ship
        self.rect = self.image.get_rect()

        
        #this is where i will change the position of the ship
        self._center_ship()
        self.moving_up = False
        self.moving_down = False
        self.arsenal = arsenal

    def _center_ship(self):
        self.rect.midleft = self.boundaries.midleft #psotion ship at the middle left of the screen
        self.y = float(self.rect.y)
        



    def update(self): 
        #updating the postion of the ship
        self._update_ship_movement()
        self.arsenal.update_arsenal() 

    def _update_ship_movement(self):
        temp_speed = self.settings.ship_speed
        if self.moving_up and self.rect.top > self.boundaries.top:
            self.y -= temp_speed
        if self.moving_down and self.rect.bottom < self.boundaries.bottom:
            self.y += temp_speed

        self.rect.y = self.y #what the y position is will be placed  in rect position   

        

#ship should be able to draw itself
    def draw(self):
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)  #drawing unto the actual game(a rectangle)     

    def fire(self):
        return self.arsenal.fire_bullet()
    
    def check_collisions(self, other_group): #check if we are colliding with any sprite
        if pygame.sprite.spritecollideany(self, other_group):
            self._center_ship() #if it has collision you center the ship
            return True
        return False