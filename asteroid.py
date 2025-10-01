import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            2
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            vector = self.velocity.rotate(angle)
            neg_vector = self.velocity.rotate(angle * -1)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_one = Asteroid(self.position[0], self.position[1], new_radius)
            new_asteroid_two = Asteroid(self.position[0], self.position[1], new_radius)
            new_asteroid_one.velocity = vector
            new_asteroid_two.velocity = neg_vector
            new_asteroid_one.velocity *= 1.2
            new_asteroid_two.velocity *= 1.2