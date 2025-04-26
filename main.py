import sys

import pygame

# import Asteroid object from asteroid.py
from asteroid import Asteroid
from asteroidfield import AsteroidField

# import everything from the constants.py file
from constants import *

# import Player object from player.py
from player import Player
from shot import Shot


def main():
    pygame.init()  # initialize the pygame module

    # screen function creates a GUI window and sets it to the constants passed in
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create a clock object to control FPS
    clock = pygame.time.Clock()

    # create groups for screen management
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    # instantiate Player object
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    # set current delta time at 0
    dt = 0

    # set color hex code numbers
    black = 0, 0, 0

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for a in asteroids:
            if a.collides_with(player):
                print("Game Over!")
                sys.exit()

        for a in asteroids:
            for shot in shots:
                if a.collides_with(shot):
                    a.split()

        screen.fill(black)

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()

        # limit FPS to 60
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
