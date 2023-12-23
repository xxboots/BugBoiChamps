NUM_FOOD = 1000
NUM_PER_PLAYER = 5
INITIAL_RESOURCE = 5

PLAYER_SPEED = 0.3
EATPLAYER = 3
MOVE_DIR_BIAS = 0.7
PROXIMITY_DISTANCE = 4

MAX_MOB_FINDER_DISTANCE = 25
MAX_FOOD_FINDER_DISTANCE = 30

WIDTH, HEIGHT = 1600, 900


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


class GAME(object):
    def __init__(self, players, food):
        self.players = players
        self.mobs = []
        self.food = food

    def init_players(self):
        for player in self.players:
            mob_class = player.type
            mob_args = (player.color, player.size) + (mob_class,)
            self.mobs.extend([mob_class(mob_args) for _ in range(NUM_PER_PLAYER)])

    def spawn_players(self, screen):
        for mob in self.mobs:
            mob.spawn(screen)