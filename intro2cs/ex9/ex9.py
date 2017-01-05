"""########################################################################
# FILE : ex9.py
# WRITER : Joshua Herskowitz , jherskow , 321658379
# WRITER : Rachel Zilberberg, rachelz , 314421876
# EXERCISE : intro2cs ex9 2016-2017
# DESCRIPTION: Functions making use of recursive logic.
#######################################################################"""
""" ======================vIM WORKING ON THIS THISv==========================="""
""" ======================^IM WORKING ON THIS THIS^==========================="""

# ============ helper functions =====================================
def deg_to_radian(degs):



# ============ Main Class ===========================================
class Space_Object:
    """
    A class representing a n object on the borard
    """
    # ===== Space_objects - class constants =======
    UPPER_BORDER
    LOWER_BORDER
    RIGHT_BORDER
    LEFT_BORDER
    # ===== Space_objects - class  methods =========
    def move(self,)
    	"""
        moves an object's position coordinates
        """


    def


    class Ship:
      """
      A ship
      """
      # ===== Ship - class constants =====
      DEFAULT_SHIP_LIVES = 3  # figure out how to do this
      TURN_INCREMENT = 7 # degrees

      # ===== Ship - class methods =======

      def __init__(self, pos, speed, heading):
        """
        Initialize a new ship.
        """
        self._pos = pos #(x,y) tuple
        self._heading = heading
        self._health = DEFAULT_SHIP_LIVES
        self._speed = # [x,y] list reperesenting sped in each axis
        self._
        self._


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
        self._size = size  #int
        self._speed = # [x,y] list reperesenting sped in each axis
        self._pos = pos  #(x,y) tuple
        self._heading = heading  #int? float? ***not (x,y) tuple?***

    class Torpedo:
      """
      A class representing a n object on the board
      """
      def __init__(self, pos, speed, heading):
        """
        Initialize a new torpedo
        """
        self._size = size
        self._pos = pos #(x,y) tuple
        self._heading = heading
        self._duration     ######## figure out
        self._speed = # [x,y] list reperesenting sped in each axis
                      # figure out initial speed setting

      def reduce_dur():
        """
        when a loop has passed reduce from current duration
        """

        self._duration -= 1









