# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 15:09:30 2020

@author: Cathig
"""
import sys
import pygame
from random import randint
from settings import Settings
from raindrop import Raindrop

class Rain:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        # Set the window size and title bar text
        # Windowed
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        # Full screen
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Rainstorm")

        self.raindrops = pygame.sprite.Group()

        self._create_rain()

    def _create_rain(self):
        """Create the storm of raindrops."""
        # Create raindrop and find the number of raindrops in a row.
        # Spacing between each raindrop is equal to one raindrop width
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        available_space_x = self.settings.screen_width - (2 * raindrop_width)
        number_raindrops_x = available_space_x // (2 * raindrop_width)

        # Determine the number of rows of raindrops that fit if spaced evenly.
        available_space_y = self.settings.screen_height
        number_raindrops_y = available_space_y // (2 * raindrop_height)

        # Determine the number of raindrops to create.
        number_raindrops = number_raindrops_x * number_raindrops_y

        # Create the first raindrops.
        for raindrop_number in range(number_raindrops):
            self._create_raindrop(raindrop_number)

    def _create_raindrop(self, raindrop_number):
        #Create a raindrop and place it in the game surface.
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        raindrop.x = (randint(0, self.settings.screen_width - raindrop_width))
        raindrop.rect.x = raindrop.x
        raindrop.rect.y = randint(0, (self.settings.screen_height -
                                      raindrop_height))
        self.raindrops.add(raindrop)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_raindrops()
            self._update_screen()

    def _update_raindrops(self):
        """Update the positions of all raindrops in the storm."""
        # Move raindrops down
        for raindrop in self.raindrops.sprites():
            raindrop.rect.y += int(self.settings.raindrop_speed)
        # Get rid of raindrops that have disappeared.
        for raindrop in self.raindrops.sprites():
            if raindrop.rect.top >=self.settings.screen_height:
                raindrop.rect.y = randint((-1 * raindrop.rect.height), 0)
                raindrop.rect.x = randint(0, (self.settings.screen_width
                                              - raindrop.rect.width))
        # print(len(self.raindrops)) # test raindrop removal

    def _check_events(self):
        """Respond to key presses and mouse events."""
        # Gracefully exit when 'X' or alt+F4 close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN
                                             and event.key == pygame.K_q):
                pygame.quit()
                # sys.exit() - in text, but does not close gracefully

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)
        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    rs = Rain()
    rs.run_game()