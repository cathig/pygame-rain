# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 19:19:08 2020

@author: Cathig
"""
import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """A class to represent a single raindrop in the storm."""

    def __init__(self, ai_game):
        """Initialize the raindrop and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the raindrop image and set is rec attribute.
        self.image = pygame.image.load('images/raindrop.png')
        self.rect = self.image.get_rect()

        # Start each new raindrop near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the raindrops exact vertical position.
        self.y = float(self.rect.y)