import pygame


class Button:
    def __init__(self, x, y, image, scale):
        img_width = image.get_width()
        img_height = image.get_height()
        self.image = pygame.transform.scale(image, (int(img_width * scale), int(img_height * scale)))
        # has some collision functions
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, screen):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked????
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
            self.clicked = True
            action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action