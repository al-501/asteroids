from constants import *
import pygame
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x,y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0,1).rotate(rotation)
        self.velocity *= PLAYER_SHOOT_SPEED