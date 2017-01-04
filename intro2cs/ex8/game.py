"""########################################################################
# FILE : game.py
# WRITER : Joshua Herskowitz , jherskow , 321658379
# EXERCISE : intro2cs ex8 2016-2017
# DESCRIPTION: The main runner file for the game
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
        self._last_turn_kills = 0

    def update_bombs(self):
        """updates bomb fuses"""
        for bomb in self._bombs:
            self._bombs[bomb] -= 1

    def place_bomb(self):
        """
        allows a user to place a bomb on the board.
        if the bomb exists, will restart the fuse.
        """
        target = gh.get_target(self._board_size)
        if target not in self._bombs:
            bomb = {target: Game.BOMB_FUSE}
            self._bombs.update(bomb)
        else:
            for bomb in self._bombs:
                if bomb == target:
                    self._bombs[bomb] = Game.BOMB_FUSE
        return None

    def move_ships(self):
        """moves ships, if they are still moving"""
        for ship in self._ships:
            ship.move()
        return None

    def do_hits(self):
        """checks each bomb and ship for collisions, and updates as needed"""
        for ship in self._ships:
            for bomb in self._bombs:
                if ship.hit(bomb):
                    self._last_turn_hits.append(bomb)
                    if ship.terminated():
                        self._ships.remove(ship)
                        self._last_turn_kills += 1
        return None

    def cleanup_bombs(self):
        """remove old or exploded bombs from the game"""
        bombs_to_remove = []
        for bomb in self._bombs:
            if bomb in self._last_turn_hits or self._bombs[bomb] == 0:
                bombs_to_remove.append(bomb)
        for bomb in bombs_to_remove:
            self._bombs.__delitem__(bomb)
        return None

    def print_board(self):
        """prints current board, using board_to_string"""
        board_length, hits, bombs, hit_ships, ships = self.board_print_prep()
        print(gh.board_to_string(board_length, hits, bombs, hit_ships, ships))
        return None

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
        self._last_turn_hits = []
        self._last_turn_kills = 0
        self.update_bombs()
        self.place_bomb()
        self.move_ships()
        self.do_hits()
        self.cleanup_bombs()
        gh.report_turn(len(self._last_turn_hits), self._last_turn_kills)
        if self._ships is not []:
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

    def board_print_prep(self):
        """Prepares variables in format compatible with gh.board_to_string"""
        board_length = self._board_size
        hit_ships = []
        for ship in self._ships:
            if ship.damaged_cells is not []:
                hit_ships += ship.damaged_cells()
        bombs = copy.deepcopy(self._bombs)
        hits = []
        if self._last_turn_hits is not []:
            hits = self._last_turn_hits
        ship_cords = []
        for ship in self._ships:
            ship_cords += ship.coordinates()
        if hit_ships is not []:
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
        board_length, hits, bombs, hit_ships, ships = self.board_print_prep()
        print(gh.board_to_string(board_length, hits, bombs, hit_ships, ships))
        while self.__play_one_round() != GAME_STATUS_ENDED:
            self.print_board()
            print(self._ships)
        gh.report_gameover()
        return 0


############################################################
# An example usage of the game
############################################################
if __name__ == "__main__":
    game = Game(5, gh.initialize_ship_list(4, 2))
    game.play()
