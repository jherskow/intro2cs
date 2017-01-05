"""########################################################################
# FILE : torpedo.py
# WRITER : Joshua Herskowitz , jherskow , 321658379
# WRITER : Rachel Zilberberg, rachelz , 314421876
# EXERCISE : intro2cs ex9 2016-2017
# DESCRIPTION:
#######################################################################"""
import helpers


class Torpedo:
    """
    A class representing a n object on the board
    """

    def __init__(self, pos, speed, heading):
        """
        Initialize a new torpedo
        """
        self._size = 3  # todo get random size
        self._pos = helpers.random_int_range()
        self._heading = heading
        self._duration = 16   # todo =figure out
        self._speed = [0, 0]  # todo get random speed

    def reduce_dur(self):
        """
        when a loop has passed reduce from current duration
        """
        self._duration -= 1

    def goto(self, pos):
        """
        :param pos:
        :return:
        """
        self._pos = pos
