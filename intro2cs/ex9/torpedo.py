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


class Torpedo(helpers.Movable):
    """
    A class representing a Torpedo on the board.
    """
    # ===== Torpedo - class constants =====
    DEAFULT_DUR = 200
    ACEL_CONST = 2
    RADIUS = 4

    # ===== Torpedo - class methods =======

    def __init__(self, pos, speed, heading):
        """
        Initializes a new torpedo.
        :param pos: An [x,y] position on the board, in ints.
        :param speed: An [x,y] of floats representing speed in each axis.
        :param heading: a compass heading in degrees.
        """
        self._pos = pos
        self._heading = heading
        self._duration = Torpedo.DEAFULT_DUR
        self._speed = self.tor_speed(speed, helpers.deg_to_radian(heading))
        self._radius = Torpedo.RADIUS

    def reduce_dur(self):
        """
        Reduces the torpedo's duration by one.
        """
        self._duration -= 1

    def get_dur(self):
        """ :return: the torpedo's current loop duration """
        return copy.copy(self._duration)

    def tor_speed(self, speed, radians):
        """
        Calculates a new torpedo's initial speed.
        :param speed: an [x,y] speed, from the firing ship.
        :param radians: A direction in radians.
        :return: speed as [x,y] list.
        """
        new_x_speed = speed[0] + (Torpedo.ACEL_CONST * math.cos(radians))
        new_y_speed = speed[1] + (Torpedo.ACEL_CONST * math.sin(radians))
        return [new_x_speed, new_y_speed]
