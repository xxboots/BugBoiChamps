NUM_FOOD = 1000
NUM_PER_PLAYER = 1

PLAYER_SPEED = 0.3
MOVE_DIR_BIAS = 0.7
PROXIMITY_DISTANCE = 2

MAX_MOB_FINDER_DISTANCE = 4
MAX_FOOD_FINDER_DISTANCE = 10

WIDTH, HEIGHT = 1600, 900


def CREATE_MOBS(mob_class, args):
    return [mob_class(args) for _ in range(NUM_PER_PLAYER)]


def CONFIGURE_ALL_PLAYERS(args):
    mob_list = []
    i = 0
    while i < len(args):
        mob_class = args[i]
        mob_args = args[i + 1] + (mob_class,)
        mob_list.extend(CREATE_MOBS(mob_class, mob_args))
        i += 2
    return mob_list
