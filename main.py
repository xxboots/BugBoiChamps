import colors
import config
import food
import pygame
import sys

from player_entities import example_player_entity, example_player_entity2
from player_entities import mad

pygame.init()
SCREEN = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption("BUG-BOI CHAMPS")
pygame.display.set_icon(pygame.image.load("Assets/bugboi.png"))
clock = pygame.time.Clock()
ticker = 0

# setup game
players = [
    config.PLAYER(mad.BigBoi, colors.BLUE, 2),
    config.PLAYER(example_player_entity.TEST, colors.RED, 2),
    config.PLAYER(example_player_entity2.TEST2, colors.ORANGE, 5)
]
GAME = config.GAME(players, food.INIT_FOOD(SCREEN, []))
GAME.init_players()
GAME.spawn_players(SCREEN)


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
    foods_copy = GAME.food[:]
    mobs_copy = GAME.mobs[:]

    if not foods_copy:
        pass

    for f in foods_copy:
        f.draw(SCREEN)

    for m in mobs_copy:
        m.move(SCREEN, foods_copy, mobs_copy)

    for m in mobs_copy:
        m.draw(SCREEN)

    pygame.display.update()
    # clock.tick(120)
    # ticker += 1
    # if ticker % 1000 == 0:
    #     if config.PLAYER_SPEED <= 1:
    #         config.PLAYER_SPEED += 0.01
    #     if config.PROXIMITY_DISTANCE <= 20:
    #         config.PROXIMITY_DISTANCE += 0.1
    #     if config.EATPLAYER <= 1:
    #         config.EATPLAYER += 0.0005

    # Update the original FOODS and MOBS lists if needed
    GAME.food[:] = foods_copy
    GAME.mobs[:] = mobs_copy
