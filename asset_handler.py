import pygame
import os


def load_asset(file_name: str) -> pygame.Surface:
    return pygame.image.load(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets", file_name)
    ).convert_alpha()
