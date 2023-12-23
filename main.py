import colors
import config
import food
import pygame
import sys
import game_obj
import particles

from player_entities import example_player_entity, example_player_entity2, mad

pygame.init()
SCREEN = pygame.display.set_mode((config.WIDTH, config.HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("BUG-BOI CHAMPS")
pygame.display.set_icon(pygame.image.load("Assets/bugboi.png"))
clock = pygame.time.Clock()
ticker = 0

# setup game
players = [
    game_obj.PLAYER(mad.BigBoi, colors.BLUE, 2.5),
    game_obj.PLAYER(example_player_entity.TEST, colors.RED, 2.5),
    game_obj.PLAYER(example_player_entity2.TEST2, colors.ORANGE, 2.5)
]

GAME = game_obj.GAME(players, food.INIT_FOOD(SCREEN, [], config.NUM_FOOD))
GAME.init_players()
GAME.spawn_players(SCREEN)


def event_loop():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


# game
food_added = False
ticks = 0
flash = False

while True:
    ticks += 0.25

    event_loop()

    if flash:
        SCREEN.fill(colors.RED)
        flash = False
    else:
        SCREEN.fill(colors.BLACK)

        if particles.particles:
            particles.particles.emit(SCREEN)

        # Create copies of FOODS and MOBS
        foods_copy = GAME.food[:]
        mobs_copy = GAME.mobs[:]

        if foods_copy:
            for f in foods_copy:
                f.draw(SCREEN)

        if mobs_copy:
            for m in mobs_copy:
                # pygame.time.delay(1)
                if m in GAME.mobs:
                    if m.Resources < 10:
                        m.Resources -= 0.0005
                        m.radius = int(m.Resources / 2)
                    elif m.radius >= 5:
                        m.Resources -= 0.00005

                    if m.Resources > 40:
                        m.radius -= 0.00001
                    elif m.Resources > 15:
                        m.radius -= 0.00005
                    elif m.radius > 3:
                        m.radius -= 0.0001

                    if m.Resources <= 0 or m.radius == 0:
                        print("<---------  Wooooooooooooooooooooooooooooow...  ------------>")
                        print(m.sub_class, " starved to death...")
                        flash = True
                        particles.particles.add_particles(m.x, m.y)
                        GAME.spawn_big_cheese(m.x, m.y)
                        GAME.mobs.remove(m)
                    else:
                        GAME.food, GAME.mobs = m.move(SCREEN, GAME.food, GAME.mobs)

        foods_copy, mobs_copy = GAME.food[:], GAME.mobs[:]

        if mobs_copy:
            for m in mobs_copy:
                m.draw(SCREEN)

        if ticks % 100 == 0:
            GAME.spawn_more_food(SCREEN, 15)
            ticks = 0

        if len(GAME.food) <= config.NUM_FOOD / 3 and not food_added:
            GAME.spawn_more_food(SCREEN, 500)
            food_added = True
            config.PROXIMITY_DISTANCE += 4

    clock.tick(120)
    pygame.display.update()
