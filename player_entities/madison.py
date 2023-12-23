import config
import player_methods
import player_entities.base_player as base

leave_spawn_if_in_pxl_range = 5


class BigBoi(base.PlayerMob):
    def __init__(self, args):
        super().__init__(args)

    def move(self, screen, foods, mobs):
        # set direction
        self.dir_x, self.dir_y = (
            player_methods.set_direction_main(self.dir_x, self.dir_y))

        # seek food
        where_food = object
        if self.Omnivore or self.Vegan:
            foods, where_food = self.seek_food(foods)

        # hunt players
        found_mob = object
        if self.Omnivore or self.Carnivore:
            mobs, found_mob = self.hunt(mobs)

        # handle findings
        if self.Omnivore:
            self.vegan_or_not(where_food, found_mob)
        if self.Vegan:
            self.veg_out(where_food)
        if self.Carnivore:
            self.flesh_out(found_mob)

        # set velocity in direction
        self.velocity_x = self.dir_x * config.PLAYER_SPEED
        self.velocity_y = self.dir_y * config.PLAYER_SPEED

        # update position
        self.x += self.velocity_x
        self.y += self.velocity_y

        if self.Resources % 10 == 0:
            self.generate_child(screen, mobs)

        return foods, mobs

    def hunt(self, mobs):
        found_mob = player_methods.find_mobs(self, mobs, BigBoi)
        if found_mob and abs(found_mob.x - self.x) < found_mob.radius and abs(
                found_mob.y - self.y) < found_mob.radius:
            mobs.remove(found_mob)
            self.Resources += 1

        return mobs, found_mob

    def go_for_kill(self, mob):
        if not isinstance(mob, BigBoi):
            distance_to_mob = ((mob.x - self.x) ** 2 + (mob.y - self.y) ** 2) ** 0.5
            if distance_to_mob < config.PROXIMITY_DISTANCE:
                self.dir_x *= 1.05
                self.dir_y *= 1.05

    def seek_food(self, foods):
        where_food = player_methods.find_food(self, foods)
        if where_food:
            if abs(where_food.x - self.x) < where_food.radius and abs(where_food.y - self.y) < where_food.radius:
                foods.remove(where_food)
                self.Resources += 1

        return foods, where_food

    def vegan_or_not(self, where_food, found_mob):
        if where_food and found_mob:
            if ((self.x - found_mob.x) + (self.y - found_mob.y)) < ((self.x - where_food.x) + (self.y - where_food.y)):
                self.dir_x = 1 if found_mob.x > self.x else -1 if found_mob.x < self.x else 0
                self.dir_y = 1 if found_mob.y > self.y else -1 if found_mob.y < self.y else 0
                self.go_for_kill(found_mob)
            else:
                self.dir_x = 1 if where_food.x > self.x else -1 if where_food.x < self.x else 0
                self.dir_y = 1 if where_food.y > self.y else -1 if where_food.y < self.y else 0
        elif where_food:
            self.veg_out(where_food)
        elif found_mob:
            self.flesh_out(found_mob)
            self.go_for_kill(found_mob)

    def veg_out(self, where_food):
        if where_food:
            self.dir_x = 1 if where_food.x > self.x else -1 if where_food.x < self.x else 0
            self.dir_y = 1 if where_food.y > self.y else -1 if where_food.y < self.y else 0

    def flesh_out(self, found_mob):
        if found_mob:
            self.dir_x = 1 if found_mob.x > self.x else -1 if found_mob.x < self.x else 0
            self.dir_y = 1 if found_mob.y > self.y else -1 if found_mob.y < self.y else 0

