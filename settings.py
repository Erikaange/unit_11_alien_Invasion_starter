from pathlib import Path
class Settings:

    def __init__(self):
        self.name: str = "Alien Invasion"
        self.screen_w = 1000
        self.screen_h = 600
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'

        self.ship_file = Path.cwd() / 'Assets'/ 'images'/ 'ship2(no bg).png'
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 5