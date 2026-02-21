import pygame
import button

class Menu:

    def __init__(self, screen):
        
        self.screen = screen

        self.playing = False
        self.menu_state = "main"