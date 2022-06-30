import pygame
import time
from .constants import *

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")


def main():
    clock = pygame.time.Clock()

    while True:
        clock.tick(FPS)
        pygame.display.update()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        display.fill(BLACK)


main()