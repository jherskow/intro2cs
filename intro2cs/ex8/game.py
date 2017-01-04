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
import copy

############################################################
# Constants
############################################################
GAME_STATUS_ONGOING = 'game on'
GAME_STATUS_ENDED = 'game over'

############################################################
# Class definition
############################################################


class Game:
    """
    A class representing a battleship game.
    A game is composed of ships that are moving on a square board and a user
    which tries to guess the locations of the ships by guessing their
    coordinates.
    """
    BOMB_FUSE = 3
    BOMB_POS = 0
    BOMB_TIMER = 1

    def __init__(self, board_size, ships):
        """
        Initialize a new Game object.
        :param board_size: Length of the side of the game-board.
        :param ships: A list of ships (of type Ship) that participate in the
            game.
        """
        self._ships = ships
        self._board_size = board_size
        self._bombs = {}
        self._last_turn_hits = []

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
        target = gh.get_target(self._board_size)                             # todo place bomb func
        if target not in self._bombs:
            bomb = {target: Game.BOMB_FUSE}
            self._bombs.update(bomb)
        else:
            for bomb in self._bombs:
                if bomb == target:
                    self._bombs[bomb] = Game.BOMB_FUSE
        turn_hit_count = 0
        turn_kill_count = 0
        turn_exploded_bombs = []
        for ship in self._ships:
            ship.move()
        for ship in self._ships:                                            # todo check hits func
            for bomb in self._bombs:
                if ship.hit(bomb):
                    turn_hit_count += 1
                    self._last_turn_hits.append(bomb)
                    turn_exploded_bombs.append(bomb)
                    if ship.terminated():
                        self._ships.remove(ship)
                        turn_kill_count += 1
        for bomb in turn_exploded_bombs:                                    # todo refresh bombs func
            self._bombs.__delitem__(bomb)
        for bomb in self._bombs:
                self._bombs[bomb] -= 1
                if self._bombs[bomb] == 0:
                    self._bombs.__delitem__(bomb)

        gh.report_turn(turn_hit_count, turn_kill_count)

        if self._ships is not []:                                           # todo game status func
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
        board_size = self._board_size
        bomb_dict = {bomb[0]: bomb[1] for bomb in self._bombs}
        ship_list = [str(ship) for ship in self._ships]
        repr_tuple = (board_size, bomb_dict, ship_list)
        return str(repr_tuple)

    def board_prep(self):
        """A"""
        board_length = self._board_size
        hit_ships = []
        for ship in self._ships:
            if ship.damaged_cells != []:
                hit_ships += ship.damaged_cells()
        bombs = copy.deepcopy(self._bombs)
        hits = []
        if self._last_turn_hits != []:
            hits = self._last_turn_hits
        ship_cords = []
        for ship in self._ships:
            ship_cords += ship.coordinates()
        if hit_ships != []:
            for pos in hit_ships:
                if pos in ship_cords:
                    ship_cords.remove(pos)
        return board_length, hits, bombs, hit_ships, ship_cords

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        gh.report_legend()
        board_length, hits, bombs, hit_ships, ships = self.board_prep()
        print(gh.board_to_string(board_length, hits, bombs, hit_ships, ships))
        while self.__play_one_round() != GAME_STATUS_ENDED:
            board_length, hits, bombs, hit_ships, ships = self.board_prep()
            print(gh.board_to_string(board_length, hits, bombs, hit_ships,
                                     ships))
        return None


############################################################
# An example usage of the game
############################################################
if __name__ == "__main__":
    game = Game(5, gh.initialize_ship_list(4, 2))
    game.play()
