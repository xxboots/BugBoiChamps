import config
import random


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


def set_direction(direction, axis_len):
    if direction > axis_len:
        return 1
    if direction < 0:
        return -1
    return direction


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
        elif random.random() < config.PLAYER_DIRECTION_WEIGHT:
            direction = set_direction_main(velocity)
            velocity += direction * acceleration * abs(velocity)

    velocity = max(-config.PLAYER_SPEED, min(config.PLAYER_SPEED, velocity))
    return velocity


def find_food(player, foods):
    nearest_food = None
    min_distance = config.MAX_FOOD_FINDER_DISTANCE

    for food in foods:
        distance = ((food.x - player.x) ** 2 + (food.y - player.y) ** 2) ** 0.5

        if distance < min_distance:
            nearest_food = food
            min_distance = distance

    return nearest_food


def find_mobs(player, mobs, my_player_entity_type):
    nearest_mob = None
    min_distance = config.MAX_MOB_FINDER_DISTANCE

    for mob in mobs:
        if not isinstance(mob, my_player_entity_type):
            distance = ((mob.x - player.x) ** 2 + (mob.y - player.y) ** 2) ** 0.5

            if distance < min_distance:
                nearest_mob = mob
                min_distance = distance

    return nearest_mob
