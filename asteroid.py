import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        pygame.draw.circle(screen, "white", self.position, radius, 2)
        self.position += self.velocity * dt