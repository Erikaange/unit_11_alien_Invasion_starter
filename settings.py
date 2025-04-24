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
        self.difficulty_scale = 1.1


        #screen settings
        self.ship_file = Path.cwd() / 'Assets'/ 'images'/ 'ship2(no bg).png'
        self.ship_w = 40
        self.ship_h = 60
        
        #bullet settings
        self.bullet_file = Path.cwd() / 'Assets'/ 'images'/ 'laserBlast.png'
        self.laser_sound = Path.cwd() / 'Assets'/ 'sound'/ 'laser.mp3'
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'impactSound.mp3'


        #alien settings
        self.alien_file = Path.cwd() /'Assets' / 'images' / 'spider.png'
        self.alien_w = 40
        self.alien_h = 30
        self.fleet_direction = -1
        self.alien_bounce_speed = 1.0
        self.alien_bounce_range = 30

        self.button_w = 200
        self.button_h = 50
        self.button_color = (0, 135, 50) #you can pick any color you want

        self.text_color = (255, 255, 255)
        self.button_font_size = 48
        self.HUD_font_size = 20
        self.font_file = Path.cwd() /'Assets' / 'Fonts' /'Silkscreen'/ 'Caveat-Regular.ttf'

    def initialize_dynamic_settings(self):
        self.ship_speed = 5
        self.starting_ship_count = 3

        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_speed =7
        self.bullet_amount = 100

        self.fleet_speed = 2 #sets the fleet speed
        self.fleet_drop_speed = 40 # the amount we are dropping out

    def increase_difficulty(self):
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale




        