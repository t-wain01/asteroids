from circleshape import CircleShape
import pygame, random
from constants import *
from logger import log_event

class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            rotation = random.uniform(20, 50)
            ast1v = self.velocity.rotate(rotation)
            ast2v = self.velocity.rotate(rotation * -1)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid_1 = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid_2 = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid_1.velocity = ast1v * 1.2
            asteroid_2.velocity = ast2v * 1.2