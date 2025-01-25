import pygame
from asset_handler import load_asset

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

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
            self.screen.fill(BACKGROUND_COLOR)
            self.display.fill(BACKGROUND_COLOR)
            self.display.blit(
                self.assets.get("default_ship"),
                (self.display_w / 2, self.display_h / 2),
            )
            self.screen.blit(
                pygame.transform.scale(self.display, self.screen.get_size()), (0, 0)
            )
            pygame.display.flip()
            self.dt = self.clock.tick(60) / 1000
