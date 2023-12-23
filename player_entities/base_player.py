import random
import colors
import config
import entity


class PlayerMob(object):
    def __init__(self, args):
        self.initial_args = args
        self.Alive = True
        self.Resources = 5
        self.SpawnResources = self.Resources
        self.Carnivore = False
        self.Vegan = False
        self.Omnivore = True

        self.spawn_x = None
        self.spawn_y = None

        self.x = None
        self.y = None

        self.last_x = None
        self.last_y = None

        self.velocity_x = 0
        self.velocity_y = 0

        self.dir_x = random.randint(0, 1)
        self.dir_y = random.randint(0, 1)

        if len(args) >= 2:
            self.color, self.initial_radius = args[:2]
            self.sub_class = args[-1]
        else:
            self.color, self.initial_radius = colors.BLUE, 2
            self.sub_class = PlayerMob

        self.radius = self.initial_radius

    # THIS IS REQUIRED
    def spawn(self, screen):
        if not self.spawn_x:
            self.spawn_x = random.randrange(config.BORDER_MARGIN, config.WIDTH - config.BORDER_MARGIN, 1)
        self.x = self.spawn_x
        self.last_x = self.x

        if not self.spawn_y:
            self.spawn_y = random.randrange(config.BORDER_MARGIN, config.HEIGHT - config.BORDER_MARGIN, 1)

        self.y = self.spawn_y
        self.last_y = self.y
        self.draw(screen)

    # THIS IS REQUIRED
    def draw(self, screen):
        if self.SpawnResources == 10 and self.radius <= config.MAX_PLAYER_SIZE:
            self.radius += 0.01
        entity.circle(screen, (self.x, self.y), self.color, self.radius)

    # THIS IS REQUIRED
    def generate_child(self, screen, mobs):
        if self.SpawnResources >= 10:
            num_children = self.SpawnResources // 10
            if num_children > 0:
                new_mob = self.sub_class(self.initial_args)
                # Offset the child's spawn location by a few pixels
                offset_x = random.randint(-5, 5)  # Adjust the offset as needed
                offset_y = random.randint(-5, 5)  # Adjust the offset as needed
                new_mob.spawn_x = self.x + offset_x
                new_mob.spawn_y = self.y + offset_y
                new_mob.spawn(screen)
                mobs.append(new_mob)
                self.SpawnResources %= 10  # Reduce resources by the amount used to create one child
