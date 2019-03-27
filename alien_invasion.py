from ship import Ship
import pygame
from pygame.sprite import Group

from settings import Settings
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings=Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship=Ship(ai_settings,screen)
    bullets=Group()

    pygame.display.set_caption("Alien Invasion")
    bg_color=(230,230,230)

    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings,screen,ship,bullets)

run_game()
