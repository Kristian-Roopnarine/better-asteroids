import pygame
from asset_handler import load_asset
from player import Player

BACKGROUND_COLOR = "#0d001a"


class Game:
    def __init__(self, width, height):
        self.running = True
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.width = width
        self.height = height
        self.display_w = self.width / 3
        self.display_h = self.height / 3
        self.screen = pygame.display.set_mode((width, height), pygame.SCALED)
        self.display = pygame.Surface((self.display_w, self.display_h))
        self.assets = {"default_ship": load_asset("default_ship.png")}
        pygame.display.set_caption("New Space Game")

    def initialize_groups(self):
        # why does this not work?
        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        Player.contaiers = (updatable, drawable)
        return updatable, drawable

    def run(self):
        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        Player.containers = (updatable, drawable)
        player = Player(
            self.display_w / 2,
            self.display_h / 2,
            self.assets.get("default_ship"),
            # x min, y min, x max, y max
            boundary=[0, 0, self.display_w, self.display_h],
        )

        while self.running:
            self.screen.fill(BACKGROUND_COLOR)
            self.display.fill(BACKGROUND_COLOR)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()

            for u in updatable:
                u.update(self.dt)

            for d in drawable:
                d.draw(self.display)

            self.screen.blit(
                pygame.transform.scale(self.display, self.screen.get_size()), (0, 0)
            )
            pygame.display.flip()
            self.dt = self.clock.tick(60) / 1000
