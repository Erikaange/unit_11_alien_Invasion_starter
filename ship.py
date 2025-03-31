import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Ship: 
    
    def __init__(self, game:'AlienInvasion'):
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



    def update(self): 
        #updating the postion of the ship
        temp_speed = self.settings.ship_speed
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed

        self.rect.x = self.x #what the x position is will be placed  in rect position       
        

#ship should be able to draw itself
    def draw(self):
        self.screen.blit(self.image, self.rect)  #drawing unto the actual game(a rectangle)     

