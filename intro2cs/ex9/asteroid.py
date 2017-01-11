"""########################################################################
# FILE : asteroid.py
# WRITER : Joshua Herskowitz , jherskow , 321658379
# WRITER : Rachel Zilberberg, rachelz , 314421876
# EXERCISE : intro2cs ex9 2016-2017
# DESCRIPTION: File containing class Asteroid and related constants.
#######################################################################"""
import helpers
import math

# these constants need to be available before the initialization.
DEFAULT_SIZE = 3
RAND_SPEED = 'random'


class Asteroid(helpers.Movable):
    """
    An asteroid
    """
    # ===== Asteroid - class constants =====
    SIZE_L = 3
    SIZE_M = 2
    SIZE_S = 1
    SIZE_MODIFIER = 10
    SIZE_NORMALIZER = 5

    # ===== Asteroid - class methods =======

    def __init__(self, pos, size=DEFAULT_SIZE, speed=RAND_SPEED):
        """
        Initialises a new asteroid.
        :param pos: [x,y] list representing cartesian coordinates.
        :param size: size of the asteroid - default 3
        """
        self._size = size
        if speed == RAND_SPEED:
            speed = helpers.random_speed()
        self._speed = speed
        self._pos = pos
        radius = size * Asteroid.SIZE_MODIFIER - Asteroid.SIZE_NORMALIZER
        self._radius = radius

    def has_intersection(self, obj):
        """ checks if asteroid has collided with something"""
        x_diff = self.get_x_pos() - obj.get_x_pos()
        x_diff_pow = x_diff ** 2
        y_diff = self.get_y_pos() - obj.get_y_pos()
        y_diff_pow = y_diff ** 2
        distance = math.sqrt(x_diff_pow + y_diff_pow)
        if distance <= self._radius + obj.get_radius():
            return True
        else:
            return False
