import pygame

from constants import DEFAULT_PLAYER_SPEED, Y_VEC, X_VEC


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, sprite: pygame.Surface, move_speed=DEFAULT_PLAYER_SPEED):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        print(self.position)
        self.velocity = pygame.Vector2(0, 0)
        self.move_speed = move_speed
        self.original_image = sprite

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.move(dt, Y_VEC)

        if keys[pygame.K_s]:
            self.move(dt, -Y_VEC)

        if keys[pygame.K_a]:
            self.move(dt, -X_VEC)

        if keys[pygame.K_d]:
            self.move(dt, X_VEC)

    def move(self, dt: int, direction: pygame.Vector2):
        self.position += dt * direction * self.move_speed

    def draw(self, screen: pygame.Surface):
        screen.blit(self.original_image, self.position)
