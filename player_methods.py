import config
import random
import particles


def set_direction_main(previous_direction_x, previous_direction_y):
    random_offset_x = random.uniform(-1, 1)
    random_offset_y = random.uniform(-1, 1)

    chosen_direction_x = (random_offset_x * (1 - config.MOVE_DIR_BIAS)) + (previous_direction_x * config.MOVE_DIR_BIAS)
    chosen_direction_y = (random_offset_y * (1 - config.MOVE_DIR_BIAS)) + (previous_direction_y * config.MOVE_DIR_BIAS)

    magnitude = (chosen_direction_x ** 2 + chosen_direction_y ** 2) ** 0.5
    if magnitude > 0:
        chosen_direction_x /= magnitude
        chosen_direction_y /= magnitude

    return chosen_direction_x, chosen_direction_y


def force_direction_on_border(self):
    near_border = False
    if self.x < config.BORDER_MARGIN:
        self.dir_x = 1
        near_border = True
    elif self.y > config.WIDTH - config.BORDER_MARGIN:
        self.dir_x = -1
        near_border = True

    if self.y < config.BORDER_MARGIN:
        self.dir_y = 1
        near_border = True
    elif self.y > config.HEIGHT - config.BORDER_MARGIN:
        self.dir_y = -1
        near_border = True

    return self.dir_x, self.dir_y, near_border


def set_velocity(velocity, pos, spawn_pos, leave_spawn, resources):
    if resources >= 30:
        acceleration = 0.03
    elif resources >= 20:
        acceleration = 0.02
    else:
        acceleration = 0.01

    if pos >= config.HEIGHT - 5:
        velocity = -abs(velocity)
    elif pos <= 5:
        velocity = abs(velocity)
    else:
        if spawn_pos - leave_spawn <= pos <= spawn_pos + leave_spawn:
            velocity -= acceleration
        elif random.random() < config.MOVE_DIR_BIAS:
            direction = set_direction_main(velocity)
            velocity += direction * acceleration * abs(velocity)

    velocity = max(-config.PLAYER_SPEED, min(config.PLAYER_SPEED, velocity))
    return velocity


def find_food(player, foods):
    nearest_food = None
    min_distance = config.MAX_FOOD_FINDER_DISTANCE

    if foods:
        for food in foods:
            distance = ((food.x - player.x) ** 2 + (food.y - player.y) ** 2) ** 0.5

            if distance < min_distance:
                nearest_food = food
                min_distance = distance

    return nearest_food


def try_kill(player_a, player_b, mobs):
    if player_b and abs(player_b.x - player_a.x) < player_b.radius and abs(
            player_b.y - player_a.y) < player_b.radius:
        player_a_resource, mob_to_remove, player_b_resource = FIGHT(player_a, player_b)
        if mob_to_remove:
            if player_a_resource:
                player_a.Resources += player_a_resource * config.EAT_PLAYER_RESOURCE_MOD
                player_a.SpawnResources += player_a_resource
                player_a.radius += ((config.EAT_PLAYER_MOD * player_b.radius)
                                    + (config.EAT_PLAYER_RESOURCE_MOD * player_b.Resources))
            else:
                player_a.Resources = 0
                player_a.SpawnResources = 0
                player_a.radius = 0
            if player_b_resource:
                player_b.Resources += player_b_resource * config.EAT_PLAYER_RESOURCE_MOD
                player_b.SpawnResources += player_b_resource
                player_b.radius += ((config.EAT_PLAYER_MOD * player_a.radius)
                                    + (config.EAT_PLAYER_RESOURCE_MOD * player_a.Resources))
            particles.particles.add_particles(mob_to_remove.x, mob_to_remove.y)
            mobs.remove(mob_to_remove)

    return mobs, player_a.Resources, player_a.SpawnResources, player_a.radius


def find_mobs(player, mobs, my_player_entity_type):
    nearest_mob = None
    min_distance = config.MAX_MOB_FINDER_DISTANCE

    for mob in mobs:
        if not isinstance(mob, my_player_entity_type):
            distance = ((mob.x - player.x) ** 2 + (mob.y - player.y) ** 2) ** 0.5

            if distance < min_distance:
                nearest_mob = mob
                min_distance = distance

    return nearest_mob, mobs


def FIGHT(player_a, player_b):
    print("<---------  Uh oh!  ------------>")
    if player_a.Resources < player_b.Resources:
        print(player_a.Resources, ' vs ', player_b.Resources)
        print(player_a.sub_class, "loses to ", player_b.sub_class)
        return player_a.radius * config.EAT_PLAYER_MOD, player_a, 0
    elif player_b.Resources < player_a.Resources:
        print(player_a.Resources, ' vs ', player_b.Resources)
        print(player_b.sub_class, "loses to ", player_a.sub_class)
        return 0, player_b, player_b.radius * config.EAT_PLAYER_MOD
    elif player_b.Resources == player_a.Resources:
        p_loser = random.choice([player_b, player_a])
        print(player_a.Resources, ' vs ', player_b.Resources)
        print(p_loser.sub_class, " loses to unknown enemy due to a push")
        return 0, p_loser, 0
    else:
        pass
