import pygame
# naming system:
# from directory.fileName import className
from button.button import Button
from hbpages.relativity import Relativity
#        scr_width, scr_height = 1500, 844

class HandbookMenu:
    def __init__(self, width, height):
        pygame.init()
        # visuals
        self.screen = pygame.display.set_mode((width, height))
        self.font = pygame.font.SysFont("comicsans", 40)
        self.text_col = (255, 255, 255)

        # import images for buttons
        # MAKE SURE FILE PATH NAMES ARE CORRECT
        self.rel_img = pygame.image.load('button/rel_button.png').convert_alpha()
        self.mainmen_img = pygame.image.load('button/mainmen_button.png').convert_alpha()

        # make buttons
        self.rel_button = Button(width/2, 250, self.rel_img, 0.2)
        self.mainmen_button = Button(width/2, 500, self.mainmen_img, 0.2)

    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))
"""
    def run(self):
        run = True
        pygame.display.set_caption("Explorer's Handbook")

        while run:
            self.screen.fill((52, 78, 91))

            # special relativity
            if self.rel_button.draw(self.screen, (self.screen.get_width())/2, 250):
                hb_page = Relativity()
                hb_page.run()

            if self.mainmen_button.draw(self.screen, (self.screen.get_width())/2, 500):
                print("vroom vroom main menu")
                # return to main menu
                #run = False
            # event handler

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        hb_open = True
                if event.type == pygame.QUIT:
                    run = False
            #

            pygame.display.update()


#game = HandbookMenu(1500, 844)
#game.run()
"""