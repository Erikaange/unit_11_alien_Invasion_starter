from pathlib import Path
class Settings:
    """a class to store all alien invasion settings
    """
    def __init__(self): #screen settings

        """initialize the game static settings"""
        
        self.name: str = "Alien Invasion"
        self.screen_w = 1000
        self.screen_h = 600
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'


        #screen settings
        self.ship_file = Path.cwd() / 'Assets'/ 'images'/ 'ship2(no bg).png'
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 5
        self.starting_ship_count = 3
        
        #bullet settings
        self.bullet_file = Path.cwd() / 'Assets'/ 'images'/ 'laserBlast.png'
        self.laser_sound = Path.cwd() / 'Assets'/ 'sound'/ 'laser.mp3'
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'impactSound.mp3'
        self.bullet_speed =7
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_amount = 100


        #alien settings
        self.alien_file = Path.cwd() /'Assets' / 'images' / 'spider.png'
        self.alien_w = 60
        self.alien_h = 20
        self.fleet_speed = 3 #sets the fleet speed
        self.fleet_direction = 1
        self.fleet_drop_speed = 40 # the amount we are dropping out
    