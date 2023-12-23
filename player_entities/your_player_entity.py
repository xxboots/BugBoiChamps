import config
import player_methods
import player_entities.base_player as base


class RenameMe(base.PlayerMob):
    def __init__(self, args):
        super().__init__(args)
        # define custom args here, idc how you do it, just don't change config.py to do it
        # unless it accepts everybody else's args too

    def move(self, screen, foods, mobs):
        # KEEP: set direction
        self.dir_x, self.dir_y = (
            player_methods.set_direction_main(self.dir_x, self.dir_y))

        # seek food ??

        # hunt players ??

        # KEEP: set velocity in direction
        self.velocity_x = self.dir_x * config.PLAYER_SPEED
        self.velocity_y = self.dir_y * config.PLAYER_SPEED

        # KEEP: update position
        self.x += self.velocity_x
        self.y += self.velocity_y

        # KEEP: generates new entities of your type when resources maxes are met
        if self.Resources % 10 == 0:
            self.generate_child(screen, mobs)

        return foods, mobs
