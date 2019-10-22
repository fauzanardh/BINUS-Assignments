import pygame
from pygame.sprite import Sprite


class Bullet:
    def __init__(self, screen, ship, settings, isEnemy):
        self.screen = screen
        self.ship = ship
        self.speed_factor = settings.getBulletSpeedFactor()
        self.image = pygame.image.load('images/bullets/bullet1.png')
        self.rect = self.image.get_rect()
        self.isEnemy = isEnemy
        self.rect.centerx = ship.rect.centerx
        if self.isEnemy:
            self.rect.centery = ship.rect.bottom
        else:
            self.rect.centery = ship.rect.top

    def update(self):
        if self.isEnemy:
            self.rect.y += self.speed_factor
        else:
            self.rect.y -= self.speed_factor

    def checkHit(self, ship, enemy):
        if self.isEnemy:
            if ((self.rect.y >= ship.rect.top) and (self.rect.y <= ship.rect.bottom)) and ((self.rect.x >= ship.rect.left) and (self.rect.x <= ship.rect.right)):
                ship.health -= 10
                return True
        else:
            if ((self.rect.y >= enemy.rect.top) and (self.rect.y <= enemy.rect.bottom)) and ((self.rect.x >= enemy.rect.left) and (self.rect.x <= enemy.rect.right)):
                enemy.health -= 10
                return True
        return False

    def getPosY(self):
        return self.rect.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
