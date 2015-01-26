import pygame
from pygame.locals import *

import os

from twisted.internet.task import LoopingCall
from twisted.internet import reactor

pygame.init()

screen = pygame.display.set_mode((1920, 1080), 0, 32)


cwd = os.getcwd()
futura = pygame.font.Font(os.path.join(cwd, '..', '..', 'assets', 'fonts', 'futura', 'FuturaLT.ttf'), 32)


def draw_label(text, position, font, color='white'):
    text_label = font.render(text, 1, color)
    screen.blit(text_label, position)

def display_tick():
    screen.fill([51, 51, 51])
    
    user = '420blazeit'

    draw_label(user, [15, 1035], futura, [255, 255, 255])
    width = futura.size(user)[0]

    draw_label("some inane comment", [24 + width, 1035], futura, [119, 119, 119])
    pygame.display.flip()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        display_tick()


if __name__ == "__main__":
    main()