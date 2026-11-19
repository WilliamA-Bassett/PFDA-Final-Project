import pygame
import sys


WIDTH = 768
HEIGHT = 640
TILESIZE = 32


class Player():

    def __init__(self, pos=(0,0), sprite_path="graphics\spr_ball_placeholder.png"):
        self.pos = pygame.Vector2(pos)
        self.image_default = pygame.image.load(sprite_path).convert_alpha()
        self.image = self.image_default
        self.speed = TILESIZE
        self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.Vector2(1,0).rotate(0)

    def direct(self, angle):
        self.image = pygame.transform.rotate(self.image_default, angle)
        self.rect = self.image.get_rect(center=self.pos)

    def move(self, angle):
        self.direction = pygame.Vector2(1,0).rotate(-(angle))
        self.pos += self.direction * self.speed
    
    def draw(self, screen):
        screen.blit(self.image, self.pos)


class Collectable():

    def __init__(self, pos=(0,0), sprite_path="graphics\spr_collect_placeholder.png"):
        self.pos = pygame.Vector2(pos)
        self.image = pygame.image.load(sprite_path).convert_alpha()

    def draw(self, screen):
        screen.blit(self.image, self.pos)


def main():
    pygame.init()
    pygame.display.set_caption("Chainlinked")
    clock = pygame.time.Clock()
    resolution = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(resolution, pygame.SCALED)
    is_fullscreen = False

    player = Player((0, HEIGHT//2))
    angle = 0

    collectable = Collectable()

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
            
            if keys[pygame.K_UP]:
                if angle != 270:
                    angle = 90
            if keys[pygame.K_DOWN]:
                if angle != 90:
                    angle = 270
            if keys[pygame.K_LEFT]:
                if angle != 0:
                    angle = 180
            if keys[pygame.K_RIGHT]:
                if angle != 180:
                    angle = 0
                
        black = pygame.Color(0, 0, 0)
        screen.fill(black)

        player.direct(angle)
        player.move(angle)
        player.draw(screen)

        collectable.pos = (96, 96)
        collectable.draw(screen)

        pygame.display.flip()
        clock.tick(8)


if __name__ == "__main__":
    main()