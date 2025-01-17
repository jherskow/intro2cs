"""########################################################################
# FILE : ship.py
# WRITER : Joshua Herskowitz , jherskow , 321658379
# EXERCISE : intro2cs ex8 2016-2017
# DESCRIPTION: Implements the ship class, for use in game.py
########################################################################"""


#########################################################
# Imports
############################################################
import ship_helper as h
import copy as c


############################################################
# Helper class
############################################################


class Direction:
    """
    Class representing a direction in 2D world.
    You may not change the name of any of the constants (UP, DOWN, LEFT,
     RIGHT, NOT_MOVING, VERTICAL, HORIZONTAL, ALL_DIRECTIONS), but other
     implementations are for you to carry out.
    """
    UP = 'The Jig'
    DOWN = 'trisomy 21'
    LEFT = 'dov_khanin'
    RIGHT = "naftali_bennet"

    NOT_MOVING = 'carrie_fisher_:('

    VERTICAL = (UP, DOWN)
    HORIZONTAL = (LEFT, RIGHT)

    ALL_DIRECTIONS = (UP, DOWN, LEFT, RIGHT)

############################################################
# Class definition
############################################################


class Ship:
    """
    A class representing a ship in Battleship game.
    A ship is 1-dimensional object that could be laid in either horizontal
    or vertical alignment. A ship sails on its vertical\horizontal axis
    back and forth until reaching the board's boarders and then changes its
    direction to the opposite (left <--> right, up <--> down).
    If a ship is hit in one of its coordinates,
    it ceases its movement in all future turns.
    A ship that had all her coordinates hit is considered terminated.
    """

    def __init__(self, pos, length, direction, board_size):
        """
        A constructor for a Ship object
        :param pos: A tuple representing The ship's head's (x, y) position
        :param length: Ship's length
        :param direction: Initial direction in which the ship is sailing
        :param board_size: Board size in which the ship is sailing
        """
        self._pos = list(pos)
        self._length = length
        self._direction = direction
        self._board_size = board_size
        self._damaged_cell_list = []
        self._coordinate_list = []
        self.__update_coordinates()
        self._terminated = False

    def __repr__(self):
        """
        Return a string representation of the ship.
        :return: A tuple converted to string (that is, for a tuple x return
            str(x)).
        The tuple's content should be (in the exact following order):
            1. A list of all the ship's coordinates.
            2. A list of all the ship's hit coordinates.
            3. Last sailing direction.
            4. The size of the board in which the ship is located.
        """
        cord_list = self._coordinate_list
        hit_cord_list = self._damaged_cell_list
        direction = h.direction_repr_str(Direction, self._direction)
        board_size = self._board_size
        repr_tuple = cord_list, hit_cord_list, direction, board_size
        return str(repr_tuple)

    def move(self):
        """
        Make the ship move one board unit.
        Movement is in the current sailing direction, unless such movement
        would take the ship outside of the board, in which case the ship
        switches direction and sails one board unit in the new direction.
        :return: A direction object of the new movement direction.
        """
        if self._direction == Direction.NOT_MOVING:
            return self._direction
        elif self._direction == Direction.RIGHT:
            if self._length + self._pos[0] >= self._board_size:
                self._direction = Direction.LEFT
        elif self._direction == Direction.LEFT:
            if self._pos[0] == 0:
                self._direction = Direction.RIGHT
        elif self._direction == Direction.DOWN:
            if self._length + self._pos[1] >= self._board_size:
                self._direction = Direction.UP
        elif self._direction == Direction.UP:
            if self._pos[1] == 0:
                self._direction = Direction.DOWN
        return self.sail()

    def sail(self):
        """sail one unit in ship's direction"""
        if self._direction == Direction.RIGHT:
            self._pos[0] += 1
        elif self._direction == Direction.LEFT:
            self._pos[0] -= 1
        elif self._direction == Direction.DOWN:
            self._pos[1] += 1
        elif self._direction == Direction.UP:
            self._pos[1] -= 1
        self.__update_coordinates()
        return self._direction

    def hit(self, pos):
        """
        Inform the ship that a bomb hit a specific coordinate. The ship
         updates its state accordingly.
        If one of the ship's body's coordinate is hit, the ship does not
         move in future turns. If all ship's body's coordinate are hit, the
         ship is terminated and removed from the board.
        :param pos: A tuple representing the (x, y) position of the hit.
        :return: True if the bomb generated a new hit in the ship, False
         otherwise.
        """
        hit = False
        if self.__contains__(pos) and pos not in self._damaged_cell_list:
            self._damaged_cell_list.append(pos)
            self._direction = Direction.NOT_MOVING
            hit = True
            if self.terminated():
                self._terminated = True
        return hit

    def terminated(self):
        """
        :return: True if all ship's coordinates were hit in previous turns,
         False otherwise.
        """
        if len(self._damaged_cell_list) == self._length:
            return True
        else:
            return False

    def __contains__(self, pos):
        """
        Check whether the ship is found in a specific coordinate.
        :param pos: A tuple representing the coordinate for check.
        :return: True if one of the ship's coordinates is found in the
         given (x, y) coordinate, False otherwise.
        """
        if pos in self._coordinate_list:
            return True
        else:
            return False

    def __update_coordinates(self):
        """
        Update ship's current coordinates on board.
        :return: A list of (x, y) tuples representing the ship's current
        occupying coordinates.
        """
        coordinate_list = []
        if self._direction in Direction.HORIZONTAL:
            for i in range(self._length):
                coordinate_list.append((self._pos[0] + i, self._pos[1]))
        elif self._direction in Direction.VERTICAL:
            for i in range(self._length):
                coordinate_list.append((self._pos[0], self._pos[1] + i))
        self._coordinate_list = coordinate_list

    def coordinates(self):
        """
        Return ship's current coordinates on board.
        :return: A list of (x, y) tuples representing the ship's current
        occupying coordinates.
        """
        cord_list = c.deepcopy(self._coordinate_list)
        return cord_list

    def damaged_cells(self):
        """
        Return the ship's hit positions.
        :return: A list of tuples representing the (x, y) coordinates of a
         ship which were hit in past turns (If there are no hit coordinates
         -return an empty list). There is no importance to the order of the
         values in the returned list.
        """
        cell_list = c.deepcopy(self._damaged_cell_list)
        return cell_list

    def direction(self):
        """
        Return the ship's current sailing direction.
        :return: One of the constants of Direction class :
         [UP, DOWN, LEFT, RIGHT] according to current sailing direction or
         NOT_MOVING if the ship is hit and not moving.
        """
        return self._direction

    def cell_status(self, pos):
        """
        Return the status of the given coordinate (hit\not) in current ship
        :param pos: A tuple representing the coordinate to query.
        :return:
            if the given coordinate is not hit : False
            if the given coordinate is hit : True
            if the coordinate is not part of the ship's body : None 
        """
        if self.__contains__(pos):
            if pos in self._damaged_cell_list:
                return True
            else:
                return False
        else:
            return None
