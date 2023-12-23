import random

import config
import food
from config import NUM_PER_PLAYER, INITIAL_RESOURCE


class GAME(object):
    mobs = []

    def __init__(self, players, foods):
        self.players = players
        self.mobs = []
        self.food = []
        self.food = foods

    def init_players(self):
        for player in self.players:
            mob_class = player.type
            mob_args = (player.color, player.size) + (mob_class,)
            self.mobs.extend([mob_class(mob_args) for _ in range(NUM_PER_PLAYER)])

    def spawn_players(self, screen):
        for mob in self.mobs:
            mob.spawn(screen)

    def get_mobs(self):
        return self.mobs

    def spawn_more_food(self, screen, count):
        self.food = food.INIT_FOOD(screen, self.food, count)

    def spawn_big_cheese(self, x, y):
        i = 0
        while i < 4:
            int_x = int(x) + 60
            # if int_x <= config.WIDTH:
            #     int_x = config.WIDTH - 120
            # if int_x >= config.WIDTH:
            #     int_x = 120

            rx = random.randint(int_x - 60, int_x + 60)

            int_y = int(y) + 60
            # if int_y <= config.HEIGHT:
            #     int_y = config.HEIGHT - 120
            # if int_y >= config.HEIGHT:
            #     int_y = 120

            ry = random.randint(int_y - 60, int_y + 60)

            resource_value = random.randint(25, 75)
            self.food.append(food.cheese(resource_value, rx, ry))
            i += 1


class PLAYER(object):
    def __init__(self, mob_type, color, size):
        self.type = mob_type
        self.color = color
        self.size = size
        self.resources = INITIAL_RESOURCE
        self.mobs = NUM_PER_PLAYER

    def update_count(self, count):
        self.mobs = count

    def update_resources(self, count):
        self.resources = count
