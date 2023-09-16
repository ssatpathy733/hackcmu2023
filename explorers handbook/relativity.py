import pygame
import sys
from events import EventHandler
from ui import UI, Menu
import math

# CONSTANTS
width = 1500
height = 844

train_x = (width * 0.1)
train_y = (height * 0.2)

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

flag = True

# scrolling mechanism
scroll = 0

# importing images
train = pygame.image.load("assets/train.png")


class relativity:
    def __init__(self) -> None:

        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        UI.init(self)
        self.clock = pygame.time.Clock()
        self.clock.tick(FPS)
        EventHandler()

        # draw scrolling background
        self.bg = pygame.image.load("assets/bg.png").convert()
        self.bg_width = self.bg.get_width()
        self.titles = math.ceil(width / self.bg_width)
        print(self.titles)

        # screen = self.screen

        self.menu = Menu(self)

    def run(self):
        self.running = True
        # self.screen.fill("black")
        for i in range(0, self.titles):
            bg = self.bg
            bg_width = self.bg_width
            screen = self.screen

            screen.blit(bg (i * bg_width, 0))
        # self.screen.blit(self.bg, (0, 0))

        while self.running:
            EventHandler.run()
            for e in EventHandler.events:
                if e.type == pygame.QUIT:
                    self.running = False

            self.menu.run()

            def add_train_at_location(x, y):
                self.screen.blit(train, (x, y))

            # self.screen.fill(BLACK)

            add_train_at_location(train_x, train_y)
            pygame.display.update()

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = relativity()
    game.run()
