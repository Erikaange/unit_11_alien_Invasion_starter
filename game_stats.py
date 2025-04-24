# from pathlib import Path
import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class GameStats():
    def __init__(self, game: 'AlienInvasion'):
        """
        Initializes the game statistics including loading saved high scores and resetting 
        the current game stats (score, level, lives).

        :param game: An instance of the AlienInvasion game. The game object provides access 
                     to game settings, which are necessary for initializing stats.
        """
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.init_saved_scores()  # Load high score from file
        self.reset_stats()        # Reset current game stats

    def init_saved_scores(self):
        """
    Initializes the high score by attempting to load it from a saved file. If the file
    doesn't exist, is too small, or is corrupted, it will create a new file with a default 
    high score of 0.

    The method checks if the score file exists and contains meaningful data (based on file size),
    then reads and loads the high score from the file. If any issues are encountered, it resets 
    the high score to 0 and saves the default value.

    This method ensures that the high score is loaded and available for use in the game.
    """
        self.path = self.settings.scores_file

        # Check if score file exists and contains meaningful data
        if self.path.exists() and self.path.stat().__sizeof__() > 80:  # <-- 80 bytes? Possibly unreliable check
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.hi_score = scores.get('hi_score', 0)
        else:
            self.hi_score = 0
            self.save_scores()  # Save default high score if file is missing or too small

    def save_scores(self):
        """
    Saves the current high score to a file in JSON format. This allows the high score 
    to persist between game sessions.

    If the file cannot be found, it prints an error message. This method ensures that
    the high score is stored safely for future access.
    """
        scores = {
            'hi_score': self.hi_score
        }
        contents = json.dumps(scores, indent=4)
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f'File not found: {e}')  # <-- Consider handling other I/O exceptions too

    def reset_stats(self):
        """
    Resets the game statistics to their initial values at the start of a new game.
    This includes the number of ships left (lives), the player's score, and the current level.
    """
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1

    def update(self, collisions):
        """Updates the current game statistics based on events such as alien collisions."""
        self._update_score(collisions)
        self._update_max_score()
        self._update_hi_score()

    def _update_max_score(self):
        """
    Updates the maximum score for the current game session.
    If the player's current score exceeds the recorded max score,
    the max score is updated.
    """
        if self.score > self.max_score:
            self.max_score = self.score 

    def _update_hi_score(self):
        """
    Updates the all-time high score if the current score exceeds it.
    This value is persistent and will be saved to disk.
    """
        if self.score > self.hi_score:
            self.hi_score = self.score

    def _update_score(self, collisions):
        """
    Increases the player's score based on collisions with aliens.
    """
        for alien in collisions.values():
            self.score += self.settings.alien_points


    def update_level(self):
        """
    Increases the game level by 1. Typically called when the player clears all aliens 
    and progresses to the next wave or stage.
    """
        self.level += 1
