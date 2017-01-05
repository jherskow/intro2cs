"""########################################################################
# FILE : ship.py
# WRITER : Joshua Herskowitz , jherskow , 321658379
# WRITER : Rachel Zilberberg, rachelz , 314421876
# EXERCISE : intro2cs ex9 2016-2017
# DESCRIPTION: Functions making use of recursive logic.
#######################################################################"""

from screen import Screen
import helpers


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
        left button is pressed or the right one acordingly
        """
        if Screen.is_left_pressed():
            self._heading += Ship.TURN_INCREMENT_LEFT

        elif Screen.is_right_pressed():
            self._heading += Ship.TURN_INCREMENT_RIGHT

    def accelerate(self):
        """
        :return:
        """