import pygame
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    

class Alienfleet:
    """Manages the fleet of aliens, including creation, positioning, movement, and collisions."""


    def __init__(self, game: 'AlienInvasion'): 
        """Initialize the alien fleet and set starting direction and speed"""
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = -1 
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_fleet()  # Build the fleet at game start
         
        

    def create_fleet(self):
        """Calculate how many aliens fit and create a rectangle-style fleet."""
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_w
        screen_h = self.settings.screen_h


        #calculate the fleet size/how many aliens we can fit on the screen
        fleet_w, fleet_h = self.calculate_fleet_size(alien_w, screen_w, alien_h, screen_h) 
        x_offset, y_offset = self.calculate_offsets(alien_w, alien_h, screen_w, fleet_w, fleet_h)

                # Actually create the fleet based on size and position
        self._create_rectangle_fleet(alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset)

    def _create_rectangle_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
        """Create a rectangular grid of aliens with optional spacing logic."""
        for row in range(fleet_h):
            for col in range(fleet_w):
                # Vertical placement along the right side
                current_y = alien_h * row + y_offset

            # Place aliens on the right edge, moving leftward
                current_x = self.settings.screen_w - alien_w - x_offset - (col * alien_h)  # Right side, no movement

                if col % 2 == 0 or row % 2 == 0: #taking out every even number of alien
                    continue
                self._create_alien(current_x, current_y)

    def calculate_offsets(self, alien_w, alien_h, screen_w, fleet_w, fleet_h):
        """Center the alien fleet horizontally and vertically on the screen."""
        half_screen = screen_w//2
        fleet_horizontal_space = fleet_w * alien_w
        x_offset = int((half_screen - fleet_horizontal_space)//2)
        
        screen_h = self.settings.screen_h
        fleet_vertical_space = fleet_h * alien_h
        y_offset = int((screen_h-fleet_vertical_space)//2)
        return x_offset,y_offset


    def calculate_fleet_size(self, alien_w, screen_w, alien_h, screen_h):
        """Determine how many aliens can fit horizontally and vertically."""
        fleet_w = (screen_w//alien_w) #horizontal columns
        fleet_h = (screen_h//alien_h) #vertical rows

        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w -= 2 

        if fleet_h % 2 == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2         

        return int(fleet_w), int(fleet_h) 
    




    def _create_alien(self, current_x: int, current_y: int):
        """Create a single alien at a specified position and add it to the fleet."""
        new_alien = Alien(self, current_x, current_y)  

        self.fleet.add(new_alien)

    def _check_fleek_edges(self):
        """Check if any alien hits top or bottom edge, and reverse direction if so."""
        alien: Alien
        for alien in self.fleet:
            if alien.check_edges(): #make sure is checks the edge of the fleet
                
                self.fleet_y_dir *= -1
               
                break #makes it to bounce back and forth
               
                # pass


    def _drop_alien_fleet(self):
        """Drop the entire fleet down vertically."""
        for alien in self.fleet:
            alien.y += self.fleet_drop_speed *3


    def update_fleet(self):
        """Update the fleet's movement and bounce behavior."""
        self._check_fleek_edges()
        self.fleet.update()  # Calls each Alien's update method

    def draw(self):
        alien: 'Alien' #type int of the variable
        for alien in self.fleet:
            alien.draw_alien()   #the alien can draw itself 

    def check_collisions(self, other_group):
        """
        Check for bullet collisions with aliens.
        Returns True if any collision occurred (alien and bullet both disappear).
        """
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)        
    
    def _check_fleet_bottom(self):
        """
        Check if any alien has reached the bottom of the screen.
        Used to end game if alien touches the bottom.
        """
        alien: Alien
        for alien in self.fleet:
            if alien.rect.bottom >= self.settings.screen_h: #i will change the dir to left 
                return True
        return False

    def check_destroyed_status(self):
        """Return True if all aliens are destroyed (fleet is empty)."""
        return not self.fleet




    
       


