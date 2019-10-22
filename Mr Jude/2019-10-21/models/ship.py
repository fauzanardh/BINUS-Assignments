import pygame
import time

from models.movetypes import MoveTypes


class Ship:
    def __init__(self, screen):
        self.screen = screen
        self.health = 100
        self.image = pygame.image.load('images/ships/ship1.png')
        self.rect = self.image.get_rect()
        self.screenRect = self.screen.get_rect()
        self.isMoving = False
        self.moveDirection = MoveTypes.RIGHT
        self.time = time.time()
        self.rect.centerx = self.screenRect.centerx
        self.rect.bottom = self.screenRect.bottom-25

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.isMoving:
            self.move(self.moveDirection)

    def move(self, moveType):
        if moveType == MoveTypes.UP:
            if (self.rect.top - 1 >= self.screenRect.top) ^ (self.rect.top <= self.screenRect.centery*1.25):
                self.rect.centery -= 1
        elif moveType == MoveTypes.DOWN:
            if self.rect.bottom + 1 <= self.screenRect.bottom:
                self.rect.centery += 1
        elif moveType == MoveTypes.RIGHT:
            if self.rect.right + 1 <= self.screenRect.right:
                self.rect.centerx += 1
        elif moveType == MoveTypes.LEFT:
            if self.rect.left - 1 >= self.screenRect.left:
                self.rect.centerx -= 1
