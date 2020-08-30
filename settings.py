# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 15:24:11 2020

@author: Cathig
"""
class Settings:
    """A class to store all settings for Rain."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (25, 25, 85)

        # Raindrop settings
        self.raindrop_speed = 2.0