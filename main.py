# this allows us to use the codr from
# the opne-source  pygame library
# through this file
import pygame
from constants import *

BLACK = (0, 0, 0)


def main():
    pygame.init()
    print("Starting Asteroids!")
    print('Screen width:', SCREEN_WIDTH)
    print('Screen height:', SCREEN_HEIGHT)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(BLACK)
        pygame.display.flip()


if __name__ == "__main__":
    main()
