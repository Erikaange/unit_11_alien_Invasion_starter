import pygame
from pygame.sprite import Sprite #import sprite from bullet grouping
from typing import TYPE_CHECKING #import type check for better IDE

if TYPE_CHECKING:
    from alien_fleet import AlienFleet


class Alien(Sprite):
    def __init__(self, fleet: 'AlienFleet', x: float, y: float):
        """
        Initialize the alien and set its starting position.

        Args:
            fleet (AlienFleet): The fleet that this alien belongs to.
            x (float): Initial horizontal position.
            y (float): Initial vertical position.
        """
        super().__init__()
        self.fleet = fleet
        self.screen = fleet.game.screen #passing the screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings    

         # Load and transform the alien image
        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.alien_w, self.settings.alien_h))
        
        self.image = pygame.transform.rotate(self.image, -90)

        # Set the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x 

        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.move_up = False

        # Bouncing control
        self.original_y = y
        self.bounce_dir = 1  # 1 = down, -1 = up
        self.bounce_range = self.settings.alien_bounce_range 
    def update(self):
        """Update the alien's position both horizontally and with bounce effect."""
        temp_speed = self.settings.fleet_speed
    
        self.x += temp_speed * self.fleet.fleet_direction
        self.rect.x = self.x 
        
        
        
        
        # Vertical bounce movement
        self.y += self.settings.alien_bounce_speed * self.bounce_dir
        self.rect.y = self.y 

        if abs(self.y - self.original_y) >= self.settings.alien_bounce_range:
            self.bounce_dir *= -1  
      


    def check_edges(self): #to make sure the alien stays in the rectangle
        """
        Check if the alien has hit the top or bottom edge of the screen.

        Returns:
            bool: True if alien hits top or bottom edge, else False.
        """
        return (self.rect.top <= self.boundaries.top or
                self.rect.bottom >= self.boundaries.bottom)

  
    def draw_alien(self):
        self.screen.blit(self.image, self.rect) #was self.rect i changed


        
        