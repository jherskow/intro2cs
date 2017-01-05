# 			------------- useful things for us to use -------------

# im working on this:

""" =================vIM WORKING ON THIS THISv======================"""
""" =================^IM WORKING ON THIS THIS^======================"""

# look at this:

""""ISSUE / QUESTION ?""""

"""########################################################################
# FILE : helpers.py
# WRITER : Joshua Herskowitz , jherskow , 321658379
# WRITER : Rachel Zilberberg, rachelz , 314421876                          # FILE : helpers.py
# EXERCISE : intro2cs ex9 2016-2017
# DESCRIPTION:
#######################################################################"""
import math

# ============ helper functions ===========================================

# ===== constants =====
STRAIT_DEG = 180
PI = math.pi()


# ===== Space_objects methods =========

def deg_to_radian(degs):
    """converts degrees to radians"""
    return (deg * PI) / STRAIT_DEG


def get_random_pos():
    """returns a random pos lol wut did u think """


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

"""<<<<< updateddddd"""


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
        """updateddddd"""

    """
    :return:
    """
    return helpers.deg_to_radian(self._heading)


def accelerate(self):
    """
    :return:
    """
    current_speed = self._speed
    cur_head_rad = self.radian_heading()
    new_x_speed = current_speed + math.cos(cur_head_rad)

    new_y_speed = current_speed + math.sin(cur_head_rad)
    self._speed = [new_x_speed, new_y_speed]

    def goto(self, pos):
        """
        :param pos:
        :return:
        """

    self._pos = pos
    """till here"""


"""########################################################################
# FILE : asteroid.py
# WRITER : Joshua Herskowitz , jherskow , 321658379
# WRITER : Rachel Zilberberg, rachelz , 314421876                          # FILE : asteroid.py
# EXERCISE : intro2cs ex9 2016-2017
# DESCRIPTION:
#######################################################################"""


class Asteroid:
    """
    An asteroid
    """

    # ===== Asteroid - class constants =====


    # ===== Asteroid - class methods =======
    def __init__(self, pos, speed, heading, size):
        """
        Initialize a new asteroid
        """
        self._size = size  # int
        self._speed =  # [x,y] list reperesenting sped in each axis
        self._pos = pos  # (x,y) tuple
        self._heading = heading  # int? float? ***not (x,y) tuple?***

        def goto(self,
                 pos):                                                          """<<<<<<<<<<<<<<<<<<<"""

        """
        :param pos:
        :return:
        """
        self._pos = pos
        """<<<<<<<<<<<<<<<<<<<<<<<<<<"""


"""########################################################################
# FILE : torpedo.py
# WRITER : Joshua Herskowitz , jherskow , 321658379
# WRITER : Rachel Zilberberg, rachelz , 314421876                          # FILE : torpedo.py
# EXERCISE : intro2cs ex9 2016-2017
# DESCRIPTION:
#######################################################################"""


class Torpedo:
    """
    A class representing a n object on the board
    """

    def __init__(self, pos, speed, heading):
        """
        Initialize a new torpedo
        """
        self._size = size
        self._pos = pos  # (x,y) tuple
        self._heading = heading
        self._duration  ######## figure out
        self._speed =  # [x,y] list reperesenting sped in each axis
        # figure out initial speed setting

    def reduce_dur():
        """
        when a loop has passed reduce from current duration
        """

        self._duration -= 1

        def goto(self,
                 pos):                                                      """<<<<<<<<<<<<<<<<<<<<"""

        """
        :param pos:
        :return:
        """
        self._pos = pos
        """<<<<<<<<<<<<<<<<<<<<"""


"""########################################################################
# FILE : asteroids_main.py
# WRITER : Joshua Herskowitz , jherskow , 321658379
# WRITER : Rachel Zilberberg, rachelz , 314421876
# EXERCISE : intro2cs ex9 2016-2017
# DESCRIPTION:
#######################################################################"""
from screen import Screen
import sys
import math, ship, helpers, asteroid, torpedo

DEFAULT_ASTEROIDS_NUM = 5


class GameRunner:
    """ a """

    def __init__(self, asteroids_amnt):
        self._screen = Screen()
        self.screen_max_x = Screen.SCREEN_MAX_X
        self.screen_max_y = Screen.SCREEN_MAX_Y
        self.screen_min_x = Screen.SCREEN_MIN_X
        self.screen_min_y = Screen.SCREEN_MIN_Y
        self.torpedoes = []
        self.asteroids = []  # todfo
        self.ship = ship.Ship()

    def move(self, thing):
        """moves all movables on board"""

        return None

    def run(self):
        """a"""
        self._do_loop()
        self._screen.start_screen()

    def _do_loop(self):
        # You don't need to change this method!
        self._game_loop()

        # Set the timer to go off again
        self._screen.update()
        self._screen.ontimer(self._do_loop, 5)

    def _game_loop(self):
        """
        Your code goes here!
        """
        pass


# ===== Space_objects - class  methods =========
def move(self, space_thingy)  # space thingy must have thig
    """
    moves an object's position coordinates
  """


def main(amnt):
    """a """
    runner = GameRunner(amnt)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)

"""########################################################################
# FILE : asteroids_main.py
# WRITER : Joshua Herskowitz , jherskow , 321658379
# WRITER : Rachel Zilberberg, rachelz , 314421876
# EXERCISE : intro2cs ex9 2016-2017
# DESCRIPTION:
########################################################################"""
"""" added and starded game loop"""

from screen import Screen
import sys
from ship import Ship

DEFAULT_ASTEROIDS_NUM = 5


class GameRunner:
    """ game runner"""

    def __init__(self, asteroids_amnt):
        self._screen = Screen()
        self.screen_max_x = Screen.SCREEN_MAX_X
        self.screen_max_y = Screen.SCREEN_MAX_Y
        self.screen_min_x = Screen.SCREEN_MIN_X
        self.screen_min_y = Screen.SCREEN_MIN_Y
        self.torpedoes = []
        self.asteroids = []
        self.ship = ship.Ship()
        self.movables = self.torpedoes + self.asteroids + [self.ship]

    def move(self):
        """moves all movables on board"""
        for thing in self.movables:
            new_x, new_y = 0, 0
            x_speed, y_speed = thing.speed[0], thing.speed[1]
            old_x, old_y = thing.pos[0], thing.pos[1]
            min_x, min_y = self.screen_min_x, self.screen_min_y
            max_x, max_y = self.screen_max_x, self.screen_max_y
            delta_x = max_x - min_x
            delta_y = max_y - min_y
            new_x = (x_speed + old_x - min_x) % delta_x + min_x
            new_y = (y_speed + old_y - min_y) % delta_y + min_y
            new_pos = (new_x, new_y)
            thing.goto(new_pos)
        return None

    def run(self):
        """ docstring """
        self._do_loop()
        self._screen.start_screen()

    def _do_loop(self):
        # You don't need to change this method!
        self._game_loop()

        # Set the timer to go off again
        self._screen.update()
        self._screen.ontimer(self._do_loop, 5)

    def _game_loop(self):
        """
        Your code goes here!
        """
        if Screen.is_left_pressed() or Screen.is_right_pressed():
            self.ship.direction_change()

        if Screen.is_up_pressed():
            self.ship.accelerate()


def main(amnt):
    """ docstring """
    runner = GameRunner(amnt)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)


