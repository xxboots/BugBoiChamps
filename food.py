import pygame

import entity
import config
import random
import colors


def INIT_FOOD(screen, foodarr, num):
    i = 0
    while i < num:
        food = Food(colors.GREEN)
        foodarr.append(food)
        food.spawn()
        food.draw(screen)
        i += 1
    return foodarr


def cheese(resource_value, x, y):
    food = Food(colors.WHITE)
    food.x = int(x)
    food.y = int(y)
    food.radius = random.randint(3, 12)
    food.resource = resource_value
    return food


class Food(object):
    def __init__(self, color):
        self.y = None
        self.x = None
        self.alive = True
        self.color = color
        self.radius = 2
        self.resource = config.FOOD_VALUE

    def spawn(self):
        self.x = random.randrange(config.BORDER_MARGIN, config.WIDTH - config.BORDER_MARGIN, 1)
        self.y = random.randrange(config.BORDER_MARGIN, config.HEIGHT - config.BORDER_MARGIN, 1)

    def draw(self, screen):
        entity.circle(screen, (self.x, self.y), self.color, self.radius)

    def move(self):
        pass
