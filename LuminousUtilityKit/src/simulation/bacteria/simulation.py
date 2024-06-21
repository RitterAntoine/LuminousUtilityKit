import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"

import pygame
import sys
from random import randint
from LuminousUtilityKit.src.simulation.bacteria.bacteria import Bacteria

def bacteria_simulation():
    pygame.init()

    screen = pygame.display.set_mode((1000, 800))
    clock = pygame.time.Clock()

    num_bacteria = 10
    radius = 10
    bacteria_list = [
        Bacteria(randint(radius, 1000 - radius), randint(radius, 800 - radius), 'green', radius, 0, 0)
        for _ in range(num_bacteria)
    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for i in range(num_bacteria):
            for j in range(i + 1, num_bacteria):
                bacteria_list[i].attract(bacteria_list[j])

        screen.fill((0, 0, 0))

        for bacteria in bacteria_list:
            bacteria.draw(screen)

        pygame.display.flip()
        clock.tick(20)

if __name__ == "__main__":
    bacteria_simulation()
