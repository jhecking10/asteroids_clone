import pygame
from circleshape import CircleShape
from shot import Shot
from constants import *

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, delta_time):
        self.rotation += PLAYER_TURN_SPEED * delta_time

    def move(self, delta_time):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * delta_time

    def shoot(self):
            if self.shot_cooldown > 0:
                return
            else:
                shot_x, shot_y = self.position.x, self.position.y
                new_shot = Shot(shot_x, shot_y)
                direction = pygame.Vector2(0, 1)
                direction = direction.rotate(self.rotation)
                new_shot.velocity = direction * PLAYER_SHOOT_SPEED
                self.shot_cooldown = PLAYER_SHOOT_COOLDOWN

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def update(self, delta_time):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-delta_time)
        if keys[pygame.K_d]:
            self.rotate(delta_time)
        if keys[pygame.K_w]:
            self.move(delta_time)
        if keys[pygame.K_s]:
            self.move(-delta_time)
        if keys[pygame.K_SPACE]:
            self.shoot()
        self.shot_cooldown -= delta_time
