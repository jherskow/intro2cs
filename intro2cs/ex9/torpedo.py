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


class Torpedo:
    """
    A class representing a n object on the board
    """

    def __init__(self, pos, speed, heading):
        """
        Initialize a new torpedo
        """
        self._size = 3  # todo get random size
        self._pos = pos
        self._heading = heading
        self._duration = DEAFULT_DUR
        self._speed = self.tor_speed(speed, helpers.deg_to_radian(heading))

    def reduce_dur(self):
        """
        when a loop has passed reduce from current duration
        """
        self._duration -= 1

    def get_dur(self):
        return copy.copy(self._duration)

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

    def tor_speed(self, speed, cur_hed_rad):
        new_x_speed = speed[0] + (AXXL_CONST * math.cos(cur_hed_rad))
        new_y_speed = speed[1] + (AXXL_CONST * math.sin(cur_hed_rad))
        return [new_x_speed, new_y_speed]

    def get_radius(self):
        return copy.copy(self._radius)

    def goto(self, pos):
        """
        :param pos:
        :return:
        """
        self._pos = pos