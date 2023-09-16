import pygame


class Button:
    def __init__(self, x, y, image, scale):
        img_width = image.get_width()
        img_height = image.get_height()
        self.image = pygame.transform.scale(image, (int(img_width * scale), int(img_height * scale)))
        # has some collision functions
        self.rect = self.image.get_rect()
        #self.rect.topleft = (x, y)
        #self.rect.center = (x, y)
        self.clicked = False

    def isClicked(self, pos):
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        action = False
        # get mouse position
        #pos = pygame.mouse.get_pos()

        # check mouseover and clicked????
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
            self.clicked = True
            action = True

        return action
    """
    action = False
        # get mouse position
        #pos = pygame.mouse.get_pos()

        # check mouseover and clicked????
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
            self.clicked = True
            action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
            
        return action 
    """
    def draw(self, screen, x, y):
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
             # draw button on screen
        screen.blit(self.image, (x, y))