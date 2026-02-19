import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS, LINE_WIDTH
from logger import log_state
import player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    fps_clock = pygame.time.Clock()
    dt = 0
    
    player1 = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        player1.draw(screen)
        
        pygame.display.flip()
        
        last_call_time = fps_clock.tick(60)
        dt = last_call_time / 1000


if __name__ == "__main__":
    main()

