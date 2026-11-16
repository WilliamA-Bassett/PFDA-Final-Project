import pygame
import sys


def main():
    pygame.init()
    pygame.display.set_caption("Chainlinked")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution, pygame.SCALED)
    is_fullscreen = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_just_pressed()
            if keys[pygame.K_ESCAPE]:
                is_fullscreen = not is_fullscreen
                if is_fullscreen:
                    screen = pygame.display.set_mode(resolution, pygame.SCALED | pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode(resolution, pygame.SCALED)
        black = pygame.Color(0, 0, 0)
        screen.fill(black)
        pygame.display.flip()
        dt = clock.tick(12)


if __name__ == "__main__":
    main()