import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)
        self.shot_radius = SHOT_RADIUS

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.shot_radius, 2)

    def update(self, delta_time):
        self.position += self.velocity * delta_time