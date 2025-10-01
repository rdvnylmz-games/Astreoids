# todo: Implement multiple lives and respawning

import sys
import pygame
import pygame.freetype

from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from scoreboard import Scoreboard
from shot import Shot

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    Scoreboard.containers = (drawable)

    player_triangle = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroid_field = AsteroidField()
    score = Scoreboard((SCREEN_WIDTH / 2), 5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for obj in asteroids:
            if obj.collision_check(player_triangle):
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for bullet in shots:
                if bullet.collision_check(asteroid):
                    bullet.kill()
                    asteroid.split()
                    score.score_increase()

        screen.fill("black")

        for to_draw in drawable:
            to_draw.draw(screen)

        pygame.display.flip()

        dt = (clock.tick(60) / 1000)

if __name__ == "__main__":
    main()