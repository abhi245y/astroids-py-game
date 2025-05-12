from circleshape import CircleShape
from constants import *
import pygame
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle  = random.uniform(20,50)
            velocity_plus = self.velocity.rotate(random_angle)
            velocity_minus = self.velocity.rotate(-random_angle)
            new_rad = self.radius - ASTEROID_MIN_RADIUS
            
            astroid_a = Asteroid(self.position.x, self.position.y, new_rad)
            astroid_b = Asteroid(self.position.x, self.position.y, new_rad)

            astroid_a.velocity = velocity_plus *1.2
            astroid_b.velocity = velocity_minus *1.2
            self.kill()