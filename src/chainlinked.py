import pygame
import sys


WIDTH = 800
HEIGHT = 600


class Player():

    def __init__(self, pos=(0,0), sprite_path="graphics\spr_ball_placeholder.png"):
        self.pos = pygame.Vector2(pos)
        self.image = pygame.image.load(sprite_path).convert_alpha()
        self.speed = 1.0
        self.rect = self.image.get_rect(center=pos)
        self.angle = 0

    def draw(self, screen):
        screen.blit(self.image, self.pos)


def main():
    pygame.init()
    pygame.display.set_caption("Chainlinked")
    clock = pygame.time.Clock()
    dt = 0
    resolution = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(resolution, pygame.SCALED)
    is_fullscreen = False

    player = Player((WIDTH//2, HEIGHT//2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_just_pressed()
            if keys[pygame.K_ESCAPE]:
                is_fullscreen = not is_fullscreen
                if is_fullscreen:
                    screen = pygame.display.set_mode(
                        resolution, pygame.SCALED | pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode(resolution, pygame.SCALED)
        black = pygame.Color(0, 0, 0)
        screen.fill(black)

        player.draw(screen)

        pygame.display.flip()
        dt = clock.tick(12)


if __name__ == "__main__":
    main()