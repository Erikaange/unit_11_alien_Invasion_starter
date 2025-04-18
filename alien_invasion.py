# name: Lab13_Angeerika-1.py
# author: Angeerika
# comment:Alien invasion project where the ship fires bullet from the midleft of the screen
# date: 04/18/25



import sys
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from arsenal import ShipArsenal
#from alien import Alien
from alien_fleet import Alienfleet
from time import sleep

class AlienInvasion:

    """a class to manage the game mechanics of alien invasion"""

    def __init__(self):

        """initialize the game, settings, and game assets"""
        pygame.init()
        self.settings = Settings()
        self.game_stats = GameStats(self.settings.starting_ship_count)

        #set up the game window
        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
            )
        pygame.display.set_caption(self.settings.name)

        #load and scale the background image
        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, 
            (self.settings.screen_w, self.settings.screen_h)
            )

        # Initialize clock and game loop variables
        self.running = True
        self.clock = pygame.time.Clock()
        
        #initialize sound effect
        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.7)
        self.impact_sound = pygame.mixer.Sound(self.settings.impact_sound)
        self.impact_sound.set_volume(0.7)
        



        self.ship = Ship(self, ShipArsenal(self)) #initialize the ship with an arsenal
        self.alien_fleet = Alienfleet(self)
        self.alien_fleet.create_fleet() #creating the enemy on the game 13
        self.game_active = True
 
    def run_game(self):
        """main game loop: handles events and updates"""
       
        while self.running:
            self._check_events() #open different types
            if self.game_active: 
                self.ship.update() #update ship position
                self.alien_fleet.update_fleet() #updated the alien 13
                self._check_collisions()
            self._update_screen()  #draw updated screen
            self.clock.tick(self.settings.FPS) 

    def _check_collisions(self):
        """Handle collisions between ships, aliens, bullets, and screen edges."""
        
        if self.ship.check_collisions(self.alien_fleet.fleet): # Check for alien-ship collisions
            self._check_game_status()
        #check collisioms for aliens and bottom of screem
        if self.alien_fleet._check_fleet_bottom():
            self._check_game_status()

#check collisions of projectiles and aliens
        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal)
        if collisions:
            self.impact_sound.play()
            self.impact_sound.fadeout(500)
        if self.alien_fleet.check_destroyed_status():

            self._reset_level()
        
    def _check_game_status(self):
        """Respond to collisions: reduce lives or end game."""
        if self.game_stats.ships_left > 0:
            self.game_stats.ships_left -= 1  
            self._reset_level() 
            sleep(0.5)
        else:
            self.game_active = False
        
        
    def _reset_level(self): #decides what we want to do
        """Reset the level by clearing bullets and recreating the alien fleet."""
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty() 
        self.alien_fleet.create_fleet() 

    def _update_screen(self):
        """redraw the screen with updated elements"""
        self.screen.blit(self.bg, (0, 0)) 
        self.alien_fleet.draw()
        self.ship.draw()    
           
        pygame.display.flip()

    def _check_events(self):
        """check for the users input"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit() 
            elif event.type == pygame.KEYDOWN:  
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:   
                self._check_keyup_events(event)

    def _check_keyup_events(self, event): 
        """handle key release events to stop movement"""

        if event.key == pygame.K_RIGHT:  #if the key up was the up, not moving up) vice versa
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False 
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False    


    def _check_keydown_events(self, event):  
        """handle key press events to move the ship and fire """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True 
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True        
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(250)

                #play laser sound     
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()      




if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
