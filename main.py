import pygame
from constants import *
import player
import asteroid
import asteroidfield
import sys
import shot

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    score = 0

    updateables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    player.Player.containers = (updateables, drawables)
    asteroid.Asteroid.containers = (updateables, drawables, asteroids)
    asteroidfield.AsteroidField.containers = (updateables)
    shot.Shot.containers = (updateables, drawables, shots)

    ply = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asfield = asteroidfield.AsteroidField()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, (0, 0, 0))
        updateables.update(dt)
        for unit in drawables:
            unit.draw(screen)

        for aster in asteroids:
            if aster.collosion(ply):
                print("Game over!")
                print(score)
                sys.exit()

        for aster in asteroids:
            for blt in shots:
                if aster.collosion(blt):
                    aster.split()
                    blt.kill()
                    score += 1
        
        
        pygame.display.flip()

        #this should happen after everything
        clock.tick(60)
        dt = int(clock.get_time()) / 1000


if __name__ == "__main__":
    main()
