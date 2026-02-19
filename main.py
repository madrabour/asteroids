import pygame, sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS, LINE_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    fps_clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

 
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    af1 = AsteroidField()

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for drawling in drawable:
            drawling.draw(screen)
        updatable.update(dt)
        for asti in asteroids:
            if asti.collides_with(player1):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asti.collides_with(shot):
                    log_event("asteroid_shot")
                    #asti.kill()
                    asti.split()
                    shot.kill()


        """
        for asti in asteroids:
            for shot in shots:
                if asti.collides_with(shot):
                    log_event("asteroid_shot")
                    asti.kill()
                    shot.kill()
        """
        
        pygame.display.flip()
        
        last_call_time = fps_clock.tick(60)
        dt = last_call_time / 1000


if __name__ == "__main__":
    main()

