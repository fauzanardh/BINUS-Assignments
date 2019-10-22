import pygame
import sys


def checkEvent():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def updateScreen(screen):
