import pygame

class Button():

    def __init__(self, x, y, image, scale):

        #size
        width = image.get_width()
        height = image.get_height()

        #scale 
        self.image = pygame.transform.scale(image, (int(width * scale)), int(height * scale))

        #image area
        self.rect = self.image.get_rect()

        self.rect.topleft = (x , y)
        
        #clicked definition
        self.clicked = False

    def draw_button(self, screen):

        #action definition
        action = False

        #mouse position
        position = pygame.mouse.get_pos()

        #mouse action
        if self.rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

		#draw image
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action        