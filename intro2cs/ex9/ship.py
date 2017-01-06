"""########################################################################
# FILE : ship.py
# WRITER : Joshua Herskowitz , jherskow , 321658379
# WRITER : Rachel Zilberberg, rachelz , 314421876                          # FILE : ship.py
# EXERCISE : intro2cs ex9 2016-2017
# DESCRIPTION:
#######################################################################"""
from screen import Screen
import helpers
import math
import copy


class Ship:
    """
    A ship
    """
    # ===== Ship - class constants =====
    DEFAULT_SHIP_LIVES = 3  # figure out how to do this
    TURN_INCREMENT_LEFT = 7  # degrees
    TURN_INCREMENT_RIGHT = -7  # degrees
    STARTING_SPEED = [0, 0]  # no speed
    STARTING_HEADING = 0  # no speed
    RADIUS = 1

    # ===== Ship - class methods =======

    def __init__(self, pos):
        """
        Initialize a new ship.
        """
        self._pos = pos
        self._heading = Ship.STARTING_HEADING
        self._health = Ship.DEFAULT_SHIP_LIVES
        self._speed = Ship.STARTING_SPEED
        self._radius = Ship.RADIUS

    def direction_change(self, dir):
        """
        changes direction of the ship by 7 degrees or -7 degrees if
        left button is pressed or the right one accordingly
        """
        if dir == "left":
            self._heading += Ship.TURN_INCREMENT_LEFT

        elif dir == "right":
            self._heading += Ship.TURN_INCREMENT_RIGHT
        self._heading %= 360

    def get_heading(self):
        return copy.copy(self._heading)

    def get_speed(self):
        return copy.copy(self._speed)

    def get_pos(self):
        return copy.copy(self._pos)

    def get_x_pos(self):
        return copy.copy(self._pos[0])

    def get_y_pos(self):
        return copy.copy(self._pos[1])

    def get_x_speed(self):
        return copy.copy(self._speed[0])

    def get_y_speed(self):
        return copy.copy(self._speed[1])

    def get_radius(self):
        return copy.copy(self._radius)
    
    def radian_heading(self):
        """ docstring """
        return helpers.deg_to_radian(self._heading)

    def accelerate(self):
        """
        :return:
        """
        current_speed = self._speed
        cur_head_rad = self.radian_heading()
        new_x_speed = current_speed[0] + math.cos(cur_head_rad)

        new_y_speed = current_speed[1] + math.sin(cur_head_rad)

        self._speed = [new_x_speed, new_y_speed]

    def __repr__(self):   # todo remove this debug shiiit
        """aa"""
        speed = self._speed
        pos = self._pos
        heading = self._heading
        return str((int(10*(speed[0])), int(10*(speed[1])), (int(pos[0]), int(pos[1])), heading))

    def goto(self, pos):
        """
        :param pos:
        :return:
        """
        self._pos = pos
        return None

    def draw_prep(self):
        """preps info for draw ship"""
        return self._pos[0], self._pos[1], self._heading
