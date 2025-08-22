import circleshape
import pygame
from constants import *
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            self.position,
            self.radius,
            width=2
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        new_pos = self.position
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        outward_angle = random.uniform(20, 50)
        new_velo1 = self.velocity.rotate(outward_angle) * 1.2
        new_aster1 = Asteroid(new_pos.x, new_pos.y, new_rad)
        new_aster1.velocity = new_velo1
        new_velo2 = self.velocity.rotate(-1 * outward_angle) * 1.2
        new_aster2 = Asteroid(new_pos.x, new_pos.y, new_rad)
        new_aster2.velocity = new_velo2