import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.update(dt)
        # this is the same as below but passing actual RGB values 
        # screen.fill((0,0,0))
        screen.fill("black")
        player.draw(screen)
        # flip is basically a blit from the backbuffer to the front buffer
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()
