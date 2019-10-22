import pygame
import sys
import random
import time

from settings import Settings
from models.ship import Ship
from models.enemy import Enemy
from models.movetypes import MoveTypes
from models.bullet import Bullet


def checkEvent(screen, ship, settings, bullets, enemy, enemyBullets):
    if ship.health <= 0:
        screen.fill((0, 20, 0))
        loseFont = pygame.font.Font("fonts/OpenSans-Regular.ttf", 32)
        loseText = loseFont.render(
            'You Lose! Press space to exit', True, (57, 255, 20))
        loseTextRect = loseText.get_rect()
        loseTextRect.center = settings.getMidWH()
        screen.blit(loseText, loseTextRect)
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT) or (event.key == pygame.K_SPACE):
                    sys.exit()
    elif enemy.health <= 0:
        screen.fill((0, 20, 0))
        winFont = pygame.font.Font("fonts/OpenSans-Regular.ttf", 32)
        winText = winFont.render(
            'You Win! Press space to exit', True, (57, 255, 20))
        winTextRect = winText.get_rect()
        winTextRect.center = settings.getMidWH()
        screen.blit(winText, winTextRect)
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT) or (event.key == pygame.K_SPACE):
                    sys.exit()
    enemy.isMoving = random.choice([True, False])
    if time.time() - enemy.time >= settings.getBotResponseTime():
        enemy.time = time.time()
        enemy.moveDirection = random.choice(
            [MoveTypes.RIGHT, MoveTypes.LEFT, MoveTypes.UP, MoveTypes.DOWN])
        if random.choice([True, False]):
            enemyBullets.append(Bullet(screen, enemy, settings, True))
    # ship.isMoving = random.choice([True, False])
    # if time.time() - ship.time >= settings.getBotResponseTime():
    #     ship.time = time.time()
    #     ship.moveDirection = random.choice(
    #         [MoveTypes.RIGHT, MoveTypes.LEFT, MoveTypes.UP, MoveTypes.DOWN])
    #     if random.choice([True, False]):
    #         bullets.append(Bullet(screen, ship, settings, False))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.isMoving = True
                ship.moveDirection = MoveTypes.RIGHT
            elif event.key == pygame.K_LEFT:
                ship.isMoving = True
                ship.moveDirection = MoveTypes.LEFT
            elif event.key == pygame.K_UP:
                ship.isMoving = True
                ship.moveDirection = MoveTypes.UP
            elif event.key == pygame.K_DOWN:
                ship.isMoving = True
                ship.moveDirection = MoveTypes.DOWN
            elif event.key == pygame.K_SPACE:
                bullets.append(Bullet(screen, ship, settings, False))
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.isMoving = False
            elif event.key == pygame.K_LEFT:
                ship.isMoving = False
            elif event.key == pygame.K_UP:
                ship.isMoving = False
            elif event.key == pygame.K_DOWN:
                ship.isMoving = False


def updateScreen(settings, screen, ship, bullets, enemy, enemyBullets, health):
    screen.fill(settings.getColor())
    for index, bullet in enumerate(bullets):
        if bullet.checkHit(ship, enemy):
            bullets.pop(index)
        bullet.blitme()
    for index, bullet in enumerate(enemyBullets):
        if bullet.checkHit(ship, enemy):
            enemyBullets.pop(index)
        bullet.blitme()
    healthText = health.render(
        f"Your Health: {ship.health} | Enemy's Health: {enemy.health}", True, (57, 255, 20))
    healthRect = healthText.get_rect()
    screen.blit(healthText, healthRect)
    ship.blitme()
    enemy.update()
    enemy.blitme()


def main():
    pygame.init()
    mainScreenSettings = Settings(800, 600, (0, 0, 0), 2, 0.20)
    mainScreen = pygame.display.set_mode(mainScreenSettings.getWH())
    pygame.display.set_caption("Ship Yeeter 9000")
    playerShip = Ship(mainScreen)
    enemyShip = Enemy(mainScreen)
    health = pygame.font.Font("fonts/OpenSans-Regular.ttf", 16)
    bullets = []
    enemyBullets = []
    while True:
        checkEvent(mainScreen, playerShip,
                   mainScreenSettings, bullets, enemyShip, enemyBullets)
        playerShip.update()
        for index, bullet in enumerate(bullets):
            bullet.update()
            if bullet.getPosY() <= mainScreen.get_rect().top:
                bullets.pop(index)
        for index, bullet in enumerate(enemyBullets):
            bullet.update()
            if bullet.getPosY() >= mainScreen.get_rect().bottom:
                enemyBullets.pop(index)
        updateScreen(mainScreenSettings, mainScreen,
                     playerShip, bullets, enemyShip, enemyBullets, health)
        pygame.display.flip()


main()
