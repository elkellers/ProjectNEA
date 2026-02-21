import pygame
import button


pygame.init()

#screen size
screen_width = 1280
screen_height = 720

#screen definition
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game")

background_image = pygame.image.load("background.png")

#game variables
playing = False
menu_state = "main"


#text
font = pygame.font.SysFont(None, 50, bold = False, italic = False)
text_col = (255, 255, 255)

#main button images
play_img = pygame.image.load("play_button.png").convert_alpha()
settings_img = pygame.image.load("settings_button.png").convert_alpha()
quit_img = pygame.image.load("quit_button.png").convert_alpha()

#settings button images


#create main buttons
play_button = button.Button(456, 194, play_img, 1)
settings_button = button.Button(456, 318, settings_img, 1)
quit_button = button.Button(456, 442, quit_img, 1)

#create settings buttons


#text definition
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))



#game loop
