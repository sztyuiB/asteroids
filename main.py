import pygame
from constants import *
import player
import circleshape

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    ply = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, (0, 0, 0))
        ply.update(dt)
        ply.draw(screen)
        
        
        pygame.display.flip()

        #this should happen after everything
        clock.tick(60)
        dt = int(clock.get_time()) / 1000


if __name__ == "__main__":
    main()
