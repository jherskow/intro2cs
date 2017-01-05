"""########################################################################
# FILE : asteroid.py
# WRITER : Joshua Herskowitz , jherskow , 321658379
# WRITER : Rachel Zilberberg, rachelz , 314421876
# EXERCISE : intro2cs ex9 2016-2017
# DESCRIPTION:
#######################################################################"""
import helpers

ASTEROID_SIZE = 3


class Asteroid:
    """
    An asteroid
    """
    # ===== Asteroid - class constants =====

    # ===== Asteroid - class methods =======

    def __init__(self, pos, speed, heading):
        """
        Initialize a new asteroid
        """
        self._size = ASTEROID_SIZE
        self._speed = speed  # [x,y] list representing speed in each axis
        self._pos = pos  # (x,y) tuple
        self._heading = heading  # int deg

    def goto(self, pos):
        """ docstring """
        self._pos = pos
