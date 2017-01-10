"""########################################################################
# FILE : torpedo.py
# WRITER : Joshua Herskowitz , jherskow , 321658379
# WRITER : Rachel Zilberberg, rachelz , 314421876
# EXERCISE : intro2cs ex9 2016-2017
# DESCRIPTION:
#######################################################################"""
import helpers
import math
import copy

DEAFULT_DUR = 200
AXXL_CONST = 2


class Torpedo(helpers.Movable):
    """
    A class representing an object on the board
    """

    def __init__(self, pos, speed, heading):
        """
        Initialize a new torpedo
        """
        self._pos = pos
        self._heading = heading
        self._duration = DEAFULT_DUR
        self._speed = self.tor_speed(speed, helpers.deg_to_radian(heading))
        self._radius = 4  # todo magic number

    def reduce_dur(self):
        """
        when a loop has passed reduce from current duration
        """
        self._duration -= 1

    def get_dur(self):
        """ returns the torpedo's current loop duration """
        return copy.copy(self._duration)

    def tor_speed(self, speed, cur_hed_rad):
        """ calculates torpedo's initial speed"""
        new_x_speed = speed[0] + (AXXL_CONST * math.cos(cur_hed_rad))
        new_y_speed = speed[1] + (AXXL_CONST * math.sin(cur_hed_rad))
        return [new_x_speed, new_y_speed]
