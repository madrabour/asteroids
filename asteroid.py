import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_angle = random.uniform(20, 50)
        #print(f"na: {new_angle}")
        #rotated_vector = unit_vector.rotate(self.rotation)
        rotated_vector_p = self.velocity.rotate(new_angle)
        rotated_vector_m = self.velocity.rotate(-1*new_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_aster_p = Asteroid(self.position.x, self.position.y, new_radius)
        new_aster_m = Asteroid(self.position.x, self.position.y, new_radius)
        new_aster_p.velocity = rotated_vector_p * 1.2
        new_aster_m.velocity = rotated_vector_m * 1.2
        #print(f"sv {self.velocity}, pv: {new_aster_p.velocity}, mv: {new_aster_m.velocity}")
