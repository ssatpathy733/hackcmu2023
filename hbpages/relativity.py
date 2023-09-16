import pygame
import sys
from hbpages.events import EventHandler
from hbpages.ui import UI, Menu
from button.button import Button
import math

width = 1500
height = 844
train_x = (width * 0.1)
train_y = (height * 0.3)

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

flag = True

# importing images
train = pygame.image.load("hbpages/assets/train.png")


class relativity:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        UI.init(self)
        self.clock = pygame.time.Clock()
        EventHandler()

        # draw scrolling background
        self.bg = pygame.image.load("assets/bg.png").convert()
        self.bg_width = self.bg.get_width()
        self.tiles = math.ceil(width / self.bg_width) + 1
        self.scroll = 0

        # button to return to handbook page
        hb_img = pygame.image.load('button/hb_button.png').convert_alpha()
        self.hb_button = Button(0, 0, hb_img, 0.1)
        self.menu = Menu(self)

    def run(self):
        self.running = True
        # self.screen.fill("black")
        while self.running:
            EventHandler.run()

            # scrolling mechanism
            self.screen.blit(self.bg, (0,0))
            self.clock.tick(FPS)
            for i in range(0, self.tiles):
                self.screen.blit(self.bg, (i * self.bg_width + self.scroll, 0))

            # scroll background
            # self.scroll -= self.menu.change_scrolling_speed()
            self.menu.scroll_mech()
            # rest scroll
            if abs(self.scroll) > self.bg_width:
                self.scroll = 0


            for e in EventHandler.events:
                if e.type == pygame.QUIT:
                    self.running = False

            self.menu.run()

            # adding the train
            def add_train_at_location(x, y):
                self.screen.blit(train, (x, y))
            add_train_at_location(train_x, train_y)

            pygame.display.update()



        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = relativity()
    game.run()
