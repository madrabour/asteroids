import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass


    def collides_with(self, other):
        dist = self.position.distance_to(other.position)
        #print(f"dist: {dist}, sr: {self.radius}, or: {other.radius}")
        if self.radius + other.radius > dist:
            #print(f"Tdist: {dist}, sr: {self.radius}, or: {other.radius}")
            return True
        else:
            #print(f"Fdist: {dist}, sr: {self.radius}, or: {other.radius}")
            return False
    