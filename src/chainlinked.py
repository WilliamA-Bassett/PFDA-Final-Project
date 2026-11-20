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
        self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.Vector2(1,0).rotate(0)

    def direct(self, angle):
        self.image = pygame.transform.rotate(self.image_default, angle)

    def move(self, angle):
        self.direction = pygame.Vector2(1,0).rotate(-(angle))
        self.pos += self.direction * TILESIZE
    
    def draw(self, screen):
        self.rect = self.image.get_rect(center=self.pos)
        screen.blit(self.image, self.pos)


class Collectable():

    def __init__(self, pos=(0,0), sprite_path="graphics\spr_collect_placeholder.png"):
        self.pos = pygame.Vector2(pos)
        self.image = pygame.image.load(sprite_path).convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.dead = False
    
    def draw(self, screen):
        if self.dead:
            return
        self.rect = self.image.get_rect(center=self.pos)
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
    turnbuffer = False

    collectable = Collectable((96, 96))

    while True:
        turnbuffer = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    is_fullscreen = not is_fullscreen
                    if is_fullscreen:
                        screen = pygame.display.set_mode(
                            resolution, pygame.SCALED | pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode(resolution, pygame.SCALED)
                
                if event.key == pygame.K_UP and angle != 270 and not turnbuffer:
                    angle = 90
                    turnbuffer = True
                if event.key == pygame.K_DOWN and angle != 90 and not turnbuffer:
                    angle = 270
                    turnbuffer = True
                if event.key == pygame.K_LEFT and angle != 0 and not turnbuffer:
                    angle = 180
                    turnbuffer = True
                if event.key == pygame.K_RIGHT and angle != 180 and not turnbuffer:
                    angle = 0
                    turnbuffer = True
                
        black = pygame.Color(0, 0, 0)
        screen.fill(black)

        player.direct(angle)
        player.move(angle)
        player.draw(screen)

        if collectable.rect.colliderect(player.rect):
            collectable.dead = True
        collectable.draw(screen)

        pygame.display.flip()
        clock.tick(8)


if __name__ == "__main__":
    main()