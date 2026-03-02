import pygame
import button

class Menu:

    def __init__(self, screen):
        
        self.screen = screen

        self.playing = False

        self.menu_state = "main"

        #images
        self.background_image = pygame.image.load("images/background.png")
        self.background_image = pygame.transform.scale(self.background_image, (self.screen.get_width(), self.screen.get_height()))
        
        self.play_img = pygame.image.load("images/play_button.png").convert_alpha()
        self.quit_img = pygame.image.load("images/quit_button.png").convert_alpha()

        play_width = self.play_img.get_width()
        play_height = self.play_img.get_height()

        self.settings_img = pygame.image.load("images/settings_button.png").convert_alpha()
        self.settings_img = pygame.transform.scale(self.settings_img, (play_width, play_height))
        
        #buttons
        self.play_button = button.Button(456, 194, self.play_img, 1)
        self.settings_button = button.Button(456, 318, self.settings_img, 1)
        self.quit_button = button.Button(456, 442, self.quit_img, 1)

        #font
        self.font = pygame.font.SysFont(None, 50, bold = False, italic = False)
        self.text_col = (255, 255, 255)

    def draw_text(self, text, x, y):
        img = self.font.render(text, True, self.text_col)
        self.screen.blit(img, (x, y))

    def update(self):
        self.screen.blit(self.background_image, (0, 0))

        if self.menu_state == "main":
            if self.play_button.draw(self.screen):
                self.playing = True

            if self.settings_button.draw(self.screen):
                self.menu_state = "settings"

            if self.quit_button.draw(self.screen):
                pygame.quit()
                exit()
            
            if self.play_button.draw(self.screen):
                self.menu_state = "playing"

        elif self.menu_state == "settings":
            self.draw_text("Settings Menu", 500, 200)
        
