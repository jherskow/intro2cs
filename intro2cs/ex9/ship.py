"""########################################################################
# FILE : ship.py
# WRITER : Joshua Herskowitz , jherskow , 321658379
# WRITER : Rachel Zilberberg, rachelz , 314421876
# EXERCISE : intro2cs ex9 2016-2017
# DESCRIPTION: File containing class Ship.
#######################################################################"""
import helpers
import math
import copy


class Ship(helpers.Movable):
    """
    A class representing a Spaceship.
    """
    # ===== Ship - class constants =====
    DEFAULT_SHIP_LIVES = 3
    TURN_INCREMENT_LEFT = 7
    TURN_INCREMENT_RIGHT = -7
    STARTING_SPEED = [0.0, 0.0]
    STARTING_HEADING = 0
    RADIUS = 1
    LEFT = 'left'
    RIGHT = 'right'

    # ===== Ship - class methods =======

    def __init__(self, pos):
        """
        Initialize a new ship.
        :param pos: An [x,y] position on the board, in ints.
        """
        self._pos = pos
        self._heading = Ship.STARTING_HEADING
        self._health = Ship.DEFAULT_SHIP_LIVES
        self._speed = Ship.STARTING_SPEED
        self._radius = Ship.RADIUS

    def direction_change(self, direction):
        """
        Changes the direction of the ship by 7 degrees or -7 degrees if
        left or right keyboard arrow is pressed
        :param direction:
        """
        if direction == self.LEFT:
            self._heading += Ship.TURN_INCREMENT_LEFT
        elif direction == self.RIGHT:
            self._heading += Ship.TURN_INCREMENT_RIGHT
        self._heading %= 360

    def get_health(self):
        """ :return:  ship's lives, as an int """
        return copy.copy(self._health)

    def radian_heading(self):
        """ :return: the ships heading as radians """
        return helpers.deg_to_radian(self._heading)

    def accelerate(self):
        """
        Accelerates the ship's speed, according to the specified formula.
        """
        current_speed = self._speed
        cur_head_rad = self.radian_heading()
        new_x_speed = current_speed[0] + math.cos(cur_head_rad)

        new_y_speed = current_speed[1] + math.sin(cur_head_rad)

        self._speed = [new_x_speed, new_y_speed]

    def lose_life(self):
        """ removes a life from the ship"""
        self._health -= 1

    def draw_prep(self):
        """
        packages arguments for the draw ship() fuction
        :return: Tuple of arguments
        """
        return self._pos[0], self._pos[1], self._heading
