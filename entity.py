import pygame.draw


def circle(screen, pos, color, size):
    rect = pygame.draw.circle(screen, color, pos, size)
    return rect
