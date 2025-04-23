import pygame.font

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Button:
    def __init__(self, game, msg):
       self.game = game
       self.screen = game.screen
       self.boundaries = game.screen.get_rect()
       self.settings = game.settings

       self.font = pygame.font.Font(self.settings.font_file, self.settings.button_font_size)
       self.rect = pygame.Rect(0,0, self.settings.buttom_w, self.settings.button_h) #centers the messahe at the mid center of the screen
       self.rect.center = self.boundaries.center
       self._prep_msg(msg)

    def _prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.settings.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center #centering the button


    def draw(self):#make sur the button has been clicked
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def check_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)    