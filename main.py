import pygame
import sys
import food
import config
from player_entities import madison
from player_entities import example_player_entity
import colors

pygame.init()
SCREEN = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption("BUG-BOI CHAMPS")
pygame.display.set_icon(pygame.image.load("Assets/bugboi.png"))
clock = pygame.time.Clock()

# spawn entities
FOODS = list()
FOOD = food.INIT_FOOD(SCREEN, FOODS)

args = [
    madison.BigBoi, (colors.BLUE, 2),
    example_player_entity.TEST, (colors.RED, 2)
]

MOBS = config.CONFIGURE_ALL_PLAYERS(args)
for mob in MOBS:
    mob.spawn(SCREEN)


def handle_close():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


# game
while True:
    handle_close()
    SCREEN.fill(colors.BLACK)

    # Create copies of FOODS and MOBS
    foods_copy = FOODS[:]
    mobs_copy = MOBS[:]

    if not foods_copy:
        pass

    for f in foods_copy:
        f.draw(SCREEN)

    for m in mobs_copy:
        m.move(SCREEN, foods_copy, mobs_copy)

    for m in mobs_copy:
        m.draw(SCREEN)

    pygame.display.update()
    clock.tick(120)

    # Update the original FOODS and MOBS lists if needed
    FOODS[:] = foods_copy
    MOBS[:] = mobs_copy
