"""########################################################################
# FILE : game.py
# WRITER : Joshua Herskowitz , jherskow , 321658379
# EXERCISE : intro2cs ex8 2016-2017
# DESCRIPTION: --------------------------------------------------
########################################################################"""

############################################################
# Imports
############################################################
import game_helper as gh

############################################################
# Constants
############################################################
GAME_STATUS_ONGOING = 'game on'
GAME_STATUS_ENDED = 'game over'

############################################################
# Class definition
############################################################


class Bomb:
    """
    A class representing a bomb.
    A bomb is composed of a location, and a timer.
    """

    def __init__(self, pos):
        """

        :param pos:
        """
        self._pos = pos
        self._time_left = 3

    def update(self):
        """ Lowers timer by one """
        self._time_left -= 1

    def pos(self):
        """ returns position """
        return self._pos

    def reset(self):
        """ resets timer to 3 """
        self._time_left = 3


class Game:
    """
    A class representing a battleship game.
    A game is composed of ships that are moving on a square board and a user
    which tries to guess the locations of the ships by guessing their
    coordinates.
    """

    def __init__(self, board_size, ships):
        """
        Initialize a new Game object.
        :param board_size: Length of the side of the game-board.
        :param ships: A list of ships (of type Ship) that participate in the
            game.
        """
        self._ships = ships
        self._board_size = board_size
        self._bombs = []

    def __play_one_round(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. The logic defined by this function must be implemented
        but if you wish to do so in another function (or some other functions)
        it is ok.

        The function runs one round of the game :
            1. Get user coordinate choice for bombing.
            2. Move all game's ships.
            3. Update all ships and bombs.
            4. Report to the user the result of current round (number of hits and
             terminated ships)
        :return:
            (some constant you may want implement which represents) Game status :
            GAME_STATUS_ONGOING if there are still ships on the board or
            GAME_STATUS_ENDED otherwise.
        """
        target = gh.get_target(self._board_size)
        if target not in self._bombs:
            new_bomb = Bomb(target)
            self._bombs.append(new_bomb)
        else:
            for bomb in self._bombs:
                if bomb.pos == target:
                    bomb.reset()
        hit_count = 0
        kill_count = 0
        exploded_bombs = []
        for ship in self._ships:
            ship.move()
        for ship in self._ships:
            for bomb in self._bombs:
                if ship.hit(bomb.pos):
                    hit_count += 1
                    exploded_bombs.append(bomb)
                    if ship._terminated:
                        self._ships.remove(ship)
                        kill_count += 1
        for bomb in self._bombs:
            if bomb in exploded_bombs:
                self._bombs.remove(bomb)
            else:
                bomb.update()
        gh.report_turn(hit_count, kill_count)
        if self._ships != []:
            return GAME_STATUS_ONGOING
        else:
            return GAME_STATUS_ENDED

    def __repr__(self):
        """
        Return a string representation of the board's game.
        :return: A tuple converted to string (that is, for a tuple x return
            str(x)). The tuple should contain (maintain
        the following order):
            1. Board's size.
            2. A dictionary of the bombs found on the board, mapping their
                coordinates to the number of remaining turns:
                 {(pos_x, pos_y) : remaining turns}
                For example :
                 {(0, 1) : 2, (3, 2) : 1}
            3. A list of the ships found on the board (each ship should be
                represented by its __repr__ string).
        """
        pass

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        pass

############################################################
# An example usage of the game
############################################################
if __name__ == "__main__":
    game = Game(5, gh.initialize_ship_list(4, 2))
    game.play()
