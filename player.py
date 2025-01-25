from typing import List
import pygame

from constants import DEFAULT_PLAYER_SPEED, Y_VEC, X_VEC


class Player(pygame.sprite.Sprite):
    def __init__(
        self,
        x,
        y,
        sprite: pygame.Surface,
        move_speed=DEFAULT_PLAYER_SPEED,
        boundary=None | List[int],
    ):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.move_speed = move_speed
        self.original_image = sprite
        self.rect = self.original_image.get_rect()
        self.boundary = boundary

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if self.position.y <= self.boundary[1]:
                return
            self.move(dt, Y_VEC)

        if keys[pygame.K_s]:
            if self.position.y >= self.boundary[3] - self.rect.height:
                return
            self.move(dt, -Y_VEC)

        if keys[pygame.K_a]:
            if self.position.x <= self.boundary[0]:
                return
            self.move(dt, -X_VEC)

        if keys[pygame.K_d]:
            if self.position.x >= self.boundary[2] - self.rect.width:
                return
            self.move(dt, X_VEC)

    def move(self, dt: int, direction: pygame.Vector2):
        self.position += dt * direction * self.move_speed

    def draw(self, screen: pygame.Surface):
        screen.blit(self.original_image, self.position)
