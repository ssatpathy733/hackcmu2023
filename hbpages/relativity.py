import pygame
import sys
from hbpages.events import EventHandler
from hbpages.ui import UI, Menu
from button.button import Button
import math

width = 1500
height = 844
train_x = (width * 0.1)
train_y = (height * 0.35)

WHITE = (255,255,255)
BLACK = (0,0,0)

flag = True


# characters
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
        self.titles = math.ceil(width / self.bg_width)
        print(self.titles)

        # screen = self.screen

        # button to return to handbook page
        hb_img = pygame.image.load('button/hb_button.png').convert_alpha()
        self.hb_button = Button(0, 0, hb_img, 0.1)
        self.menu = Menu(self)

    def run(self):
        self.running = True
        while self.running:
            EventHandler.run()
            for e in EventHandler.events:
                if e.type == pygame.QUIT:
                    self.running = False

            self.menu.run()

            pygame.display.update()
            self.clock.tick(60)

            def add_train_at_location(x, y):
                self.screen.blit(character, (x, y))

            # self.screen.fill(BLACK)

            add_train_at_location(train_x, train_y)
            pygame.display.update()

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = relativity()
    game.run()


