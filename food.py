import entity
import config
import random
import colors


def INIT_FOOD(screen, foodarr):
    i = 0
    while i < config.NUM_FOOD:
        food = Food(colors.GREEN)
        foodarr.append(food)
        food.spawn()
        food.draw(screen)
        i += 1
    return foodarr


def spawn_food(count, screen):
    food = Food(colors.GREEN)

    i = 0
    while i < count:
        food.spawn()
        food.draw(screen)
        i += 1


class Food(object):
    def __init__(self, color):
        self.y = None
        self.x = None
        self.alive = True
        self.color = color
        self.radius = 2

    def spawn(self):
        self.x = random.randrange(0, config.WIDTH, 1)
        self.y = random.randrange(0, config.HEIGHT, 1)

    def draw(self, screen):
        entity.circle(screen, (self.x, self.y), self.color, self.radius)

    def move(self):
        pass
