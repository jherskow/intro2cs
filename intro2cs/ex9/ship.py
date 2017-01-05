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

    # ===== Ship - class methods =======

    def __init__(self):
        """
        Initialize a new ship.
        """
        self._pos = helpers.get_random_pos()  # (x,y) tuple
        self._heading = Ship.STARTING_HEADING  # degrees
        self._health = Ship.DEFAULT_SHIP_LIVES
        self._speed = Ship.STARTING_SPEED

    def direction_change(self):
        """
        changes direction of the ship by 7 degrees or -7 degrees if
        left button is pressed or the right one accordingly
        """
        if Screen.is_left_pressed():
            self._heading += Ship.TURN_INCREMENT_LEFT

        elif Screen.is_right_pressed():
            self._heading += Ship.TURN_INCREMENT_RIGHT

    def radian_heading(self):
        """ docstring """
        return helpers.deg_to_radian(self._heading)

    def accelerate(self):
        """
        :return:
        """
        current_speed = self._speed
        cur_head_rad = self.radian_heading()
        new_x_speed = current_speed + math.cos(cur_head_rad)

        new_y_speed = current_speed + math.sin(cur_head_rad)

        self._speed = [new_x_speed,new_y_speed]

    def goto(self,pos):
        """
        :param pos:
        :return:
        """
        self._pos = pos