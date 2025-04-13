import pygame
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    

class Alienfleet:


    def __init__(self, game: 'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_fleet()

    def create_fleet(self):
        alien_w = self.settings.alien_w
        screen_w = self.settings.screen_w

        #calculate the fleet size/how many aliens we can fit on the screen
        fleet_w = self.calculate_fleet_size(alien_w, screen_w) 

        fleet_horizontal_space = fleet_w * alien_w
        x_offset = int((screen_w - fleet_horizontal_space)//2)

        for col in range(fleet_w):
            current_x = alien_w * col + x_offset
            self._create_alien(current_x, 10)


    def calculate_fleet_size(self, alien_w, screen_w):
        fleet_w = (screen_w//alien_w)

        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w -= 2   
        return fleet_w  
    def _create_alien(self, current_x: int, current_y: int):
        new_alien = Alien(self, current_x, current_y)  

        self.fleet.add(new_alien)

    def draw(self):
        alien: 'Alien' #type int of the variable
        for alien in self.fleet:
            alien.draw_alien()   #the alien can draw itself 





    
       


