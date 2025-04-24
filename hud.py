import pygame.font
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class HUD:

    def __init__(self, game):
        """
    Initializes the HUD for the game. This includes setting up
    font rendering, screen dimensions, and initial score/level/life display setup.
    """
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.bounderies = game.screen.get_rect()
        self.game_stats = game.game_stats
        self.font = pygame.font.Font(self.settings.font_file,
                                     self.settings.HUD_font_size)
        self.padding = 20
        self._setup_life_image()# Prepare initial score display
        self.update_scores()# Set up the player life indicator image (e.g. small ship icons)
        self.update_level()# Prepare the initial level display

    def _setup_life_image(self):
        """
    Loads and prepares the player's life (ship) image used to display remaining lives on the HUD.
    The image is scaled to the configured width and height, and its rect is stored for layout use.
    """
    # Load the ship image used to represent player lives
        self.life_image = pygame.image.load(self.settings.ship_file)
        self.life_image = pygame.transform.scale(self.life_image, 
                                                 (self.settings.ship_w, self.settings.ship_h))    
        self.life_rect = self.life_image.get_rect()


    def update_scores(self):
        """
    Updates all score-related HUD elements: current score, session max score, and high score.
    This method is a wrapper that calls the individual update methods.
    """
        self._update_score()
        self._update_max_score()
        self._update_hi_score()

    def _update_score(self):
        """
        Renders the current score as a text image and positions it on the screen.
        The score is right-aligned near the top-right corner of the screen, below the max score.
        """
        score_str = f'Score: {self.game_stats.score: ,.0f}'
        self.score_image = self.font.render(score_str, True,
                                             self.settings.text_color, None)    
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.bounderies.right - self.padding
        self.score_rect.top = self.score_rect.bottom + self.padding

    def _update_max_score(self):
        """
    Renders the session's maximum score as a text image and positions it at the top-right
    corner of the screen. This is typically displayed above the current score.
    """
        max_score_str = f'Max-Score: {self.game_stats.max_score: ,.0f}'
        self.max_score_image = self.font.render(max_score_str, True,
                                             self.settings.text_color, None)    
        self.max_score_rect = self.max_score_image.get_rect()
        self.max_score_rect.right = self.bounderies.right - self.padding
        self.max_score_rect.top = self.padding

    def _update_hi_score(self):
        """
    Renders the all-time high score as a text image and positions it near the top-center
    of the screen. This gives prominence to the player's best-ever performance.
    """
        hi_score_str = f'hi-Score: {self.game_stats.hi_score:,.0f}'
        self.hi_score_image = self.font.render(hi_score_str, True,
                                             self.settings.text_color, None)    
        self.hi_score_rect = self.hi_score_image.get_rect()
        self.hi_score_rect.right = self.bounderies.right - self.padding
        self.hi_score_rect.midtop = (self.bounderies.centerx, self.padding)

    def update_level(self):
        """
            Renders the current level number as a text image and places it near the top-left
            corner of the screen, just below the life indicator icons.
            """
        level_str = f'Level: {self.game_stats.level: ,.0f}'
        self.level_image = self.font.render(level_str, True,
                                             self.settings.text_color, None)    
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.padding
        self.level_rect.top = self.life_rect.bottom + self.padding    

    def _draw_lives(self):
        """
            Draws small ship icons on the screen to visually represent how many lives the player has left.
            Each life is drawn using the preloaded ship image, spaced out with padding.
            """
        current_x = self.padding
        current_y = self.padding
        for _ in range(self.game_stats.ships_left):
            self.screen.blit(self.life_image, (current_x, current_y))  
            current_x += self.life_rect.width + self.padding

    def draw(self):
        """ draws all elements on the screen"""
        # Draw each score and level image in its designated position
        self.screen.blit(self.hi_score_image, self.hi_score_rect)
        self.screen.blit(self.max_score_image, self.max_score_rect)
        self.screen.blit(self.score_image, self.score_rect)  
        self.screen.blit(self.level_image, self.level_rect) 
        self._draw_lives()  

