import pygame
import sys


WIDTH = 768
HEIGHT = 640
TILESIZE = 32


class Player():

    def __init__(self, pos, chain_length, sprite_path="graphics\spr_ball_placeholder.png"):
        self.pos = pygame.Vector2(pos)
        self.image_default = pygame.image.load(sprite_path).convert_alpha()
        self.image = self.image_default
        self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.Vector2(1,0).rotate(0)
        self.chain_length = chain_length + 1
        self.chains = []

    def draw(self, angle, screen):
        self.image = pygame.transform.rotate(self.image_default, angle)
        self.direction = pygame.Vector2(1,0).rotate(-(angle))
        self.pos += self.direction * TILESIZE
        self.rect = self.image.get_rect(center=self.pos)
        screen.blit(self.image, self.pos)

        chain = Chain(self.pos, self.chain_length, angle)
        self.chains.insert(0, chain)
        self._update_chains()
        for idx, chain in enumerate(self.chains):
            if idx != 0:
                chain.draw(screen)

    def _update_chains(self):
        for idx, chain in enumerate(self.chains):
            chain.update()
            if idx != 0:
                chain.check_collision(self)
            if chain.dead:
                del self.chains[idx]


class Collectable():

    def __init__(self, pos, sprite_path="graphics\spr_collect_placeholder.png"):
        self.pos = pygame.Vector2(pos)
        self.image = pygame.image.load(sprite_path).convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.dead = False
    
    def check_collision(self, player):
        if self.rect.colliderect(player.rect):
            player.chain_length = player.chain_length + 1
            self.dead = True

    def draw(self, screen):
        if self.dead:
            return
        self.rect = self.image.get_rect(center=self.pos)
        screen.blit(self.image, self.pos)


class Wall():

    def __init__(self, pos, sprite_path="graphics\spr_wall_placeholder.png"):
        self.pos = pygame.Vector2(pos)
        self.image = pygame.image.load(sprite_path).convert_alpha()
        self.rect = self.image.get_rect(center=pos)

    def check_collision(self, player):
        if self.rect.colliderect(player.rect):
            pygame.quit()
            sys.exit()

    def draw(self, screen):
        self.rect = self.image.get_rect(center=self.pos)
        screen.blit(self.image, self.pos)


class Chain():

    def __init__(self, pos, life, angle, sprite_path="graphics\spr_chain_placeholder.png"):
        self.pos = pygame.Vector2(pos)
        self.image = pygame.image.load(sprite_path).convert_alpha()
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect(center=pos)
        self.life = life
        self.dead = False

    def update(self):
        if self.life != 0:
            self.life = self.life - 1
        else:
            self.dead = True

    def check_collision(self, player):
        if self.rect.colliderect(player.rect):
            pygame.quit()
            sys.exit()

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

    player = Player((WIDTH//4, HEIGHT//2), 4)
    angle = 0
    turnbuffer = False

    collectable = Collectable((96, 96))
    wall = Wall((WIDTH//2, HEIGHT//2))

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

        player.draw(angle, screen)

        collectable.check_collision(player)
        collectable.draw(screen)
        wall.check_collision(player)
        wall.draw(screen)

        pygame.display.flip()
        clock.tick(8)


if __name__ == "__main__":
    main()