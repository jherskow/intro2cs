"""########################################################################
# FILE : asteroids_main.py
# WRITER : Joshua Herskowitz , jherskow , 321658379
# WRITER : Rachel Zilberberg, rachelz , 314421876
# EXERCISE : intro2cs ex9 2016-2017
# DESCRIPTION: File containing main game Class, and related constants.
########################################################################"""
# ============================ IMPORTS  ===================================
from screen import Screen
import sys
import ship
import asteroid
import random
import torpedo
import math

# ============================ CONSTANTS  =================================
DEFAULT_ASTEROIDS_NUM = 5

# === Message text ====
HIT_TITLE = 'Ouch!'
HIT_MSG = 'Please do not feed the asteroids.'
EXIT_TITLE = 'Quitters never win!'
EXIT_MSG = 'leaving so soon? :('
LOSS_TITLE = 'YOU LOSE'
LOSS_MSG = 'In Space.... No One Can Hear You Scream!'
WIN_TITLE = 'YOU WON'
WIN_MSG = 'The Force Is Strong In You.'
PERFECT_TITLE = '!!!!! PERFECT GAME !!!!!!!!'
PERFECT_MSG = 'Fantastic Job!\nYou cleared the asteroid field, with no ' \
              'damage taken! \n Your\'e ready for the Kessel run!'

# ============================ Game Runner  ===============================


class GameRunner:
    """
    game runner
    !!stuff
    !! stuff
    """
    # ===== GameRunner - class constants =====
    POINTS_L_ROCK = 20
    POINTS_M_ROCK = 50
    POINTS_S_ROCK = 100

    def __init__(self, asteroids_amnt):
        """

        :param asteroids_amnt:
        """
        self._screen = Screen()
        self.screen_max_x = Screen.SCREEN_MAX_X
        self.screen_max_y = Screen.SCREEN_MAX_Y
        self.screen_min_x = Screen.SCREEN_MIN_X
        self.screen_min_y = Screen.SCREEN_MIN_Y
        self.torpedoes = []
        self.asteroids = []
        self._score = 0
        self.ship = ship.Ship(pos=self._random_pos())
        for rock in range(asteroids_amnt):
            self.add_asteroid()

    # ===== MAIN GAME FUNCTIONS ==============================

    def run(self):
        """ calls the first game loop and starts the screen"""
        self._do_loop()
        self._screen.start_screen()

    def _do_loop(self):
        """ runs one game loop, and updates the screen"""
        # You don't need to change this method!
        self._game_loop()

        # Set the timer to go off again
        self._screen.update()
        self._screen.ontimer(self._do_loop, 5)

    def _game_loop(self):
        """
        The main loop that implements the gameplay.
        A game round proceeds as follows:
        1. Adjust heading and go to warp x.
        2. Fire photon torpedoes.
        3. Make it so. (move and redraw objects accordingly)
        4. Damage report. (check for collisons of all sorts)
        5. Munition check. (remove old torpedos)
            (otherwise they might hit you, due to newton's first law)
        6. Orders Captain! (See if the fight should continue)
        """
        self.ship_input()
        self.move_all()
        self.draw_all()
        self.check_asteroid_kills()
        self.check_ship_crash()
        self.manage_torpedoes()
        self.check_game_over()

    # ===================   GAME LOOP SUB - FUNCTIONS  ====================

    def ship_input(self):
        """ checks for ship input from user"""
        if self._screen.is_left_pressed():
            self.ship.direction_change(self.ship.LEFT)
        if self._screen.is_right_pressed():
            self.ship.direction_change(self.ship.RIGHT)
        if self._screen.is_up_pressed():
            self.ship.accelerate()
        if self._screen.is_space_pressed():
            self.add_torpedo()

    def move_all(self):
        """
        moves all moveables on screen
        """
        for rock in self.asteroids:
            self.move(rock)
        for missile in self.torpedoes:
            self.move(missile)
        self.move(self.ship)

    def draw_all(self):
        """draws all objects on screen"""
        for rock in self.asteroids:
            self._screen.draw_asteroid(rock, *rock.get_pos())
        self._screen.draw_ship(*self.ship.draw_prep())
        for missile in self.torpedoes:
            x = missile.get_x_pos()
            y = missile.get_y_pos()
            heading = missile.get_heading()
            self._screen.draw_torpedo(missile, x, y, heading)

    def check_asteroid_kills(self):
        """
        Checks for torpedo hits on asteroids,
        and updates the game accordingly
        """
        for rock in self.asteroids:
            for torp in self.torpedoes:
                if rock.has_intersection(torp):
                    if rock.get_size() == asteroid.Asteroid.SIZE_L:
                        self.split_asteroid(rock, torp)
                        self.award_points(self.POINTS_L_ROCK)
                    elif rock.get_size() == asteroid.Asteroid.SIZE_M:
                        self.split_asteroid(rock, torp)
                        self.award_points(self.POINTS_M_ROCK)
                    elif rock.get_size() == asteroid.Asteroid.SIZE_S:
                        self.award_points(self.POINTS_S_ROCK)
                    self._screen.unregister_asteroid(rock)
                    self.asteroids.remove(rock)
                    self._screen.unregister_torpedo(torp)
                    self.torpedoes.remove(torp)
                    # make sure torpedo can hit only once
                    break

    def check_ship_crash(self):
        """ checks if there is a collision between our
        ship and an asteroid on the screen """
        for rock in self.asteroids:
            if rock.has_intersection(self.ship):
                if self.ship.get_health() != 0:
                    self.ship.lose_life()
                    self._screen.remove_life()
                self._screen.unregister_asteroid(rock)
                self.asteroids.remove(rock)
                self._screen.show_message(HIT_TITLE, HIT_MSG)

    def manage_torpedoes(self):
        """
        Counts down each torpedo's duration timer.
        Removes torpedos whose timers have reached zero.
        """
        for missile in self.torpedoes:
            missile.reduce_dur()
            if missile.get_dur() == 0:
                self._screen.unregister_torpedo(missile)
                self.torpedoes.remove(missile)

    def check_game_over(self):
        """
        Checks if the game is over:
        - If the ship's lives are over
        - If there are no more asteroids
        - If the player pressed quit or q
        """
        # check if ship is destroyed.
        if self.ship.get_health() == 0:
            self._screen.show_message(LOSS_TITLE, LOSS_MSG)
            self._screen.end_game()
            sys.exit(0)
        # check if quit was pressed
        if self._screen.should_end():
            self._screen.show_message(EXIT_TITLE, EXIT_MSG)
            self._screen.end_game()
            sys.exit(0)
        # victory
        if self.asteroids == []:
            # check for a perfect game.
            if self.ship.get_health() == 3:
                self._screen.show_message(PERFECT_TITLE, PERFECT_MSG)
            # regular victory
            else:
                self._screen.show_message(WIN_TITLE, WIN_MSG)
            self._screen.end_game()
            sys.exit(0)

    # ===================   GAME LOOP SUB-SUB-FUNCTIONS  ==================

    def move(self, thing):
        """
        Moves an object, according to a formula.
        :param thing: an object of parent class Moveable
        """
        x_speed, y_speed = thing.get_x_speed(), thing.get_y_speed()
        old_x, old_y = thing.get_x_pos(), thing.get_y_pos()
        min_x, min_y = self.screen_min_x, self.screen_min_y
        max_x, max_y = self.screen_max_x, self.screen_max_y
        delta_x = max_x - min_x
        delta_y = max_y - min_y
        new_x = (x_speed + old_x - min_x) % delta_x + min_x
        new_y = (y_speed + old_y - min_y) % delta_y + min_y
        new_pos = (new_x, new_y)
        thing.goto(new_pos)

    def add_asteroid(self):
        """
        Creates a new asteroid in a random position (not the ship's),
        adds it to the asteroid list,
        and registers it so it would appear on the sceen
        """
        new_pos = self._random_pos()
        # loop until the position is not identical to the ship's.
        while new_pos == self.ship.get_pos():
            new_pos = self._random_pos()
        new_rock = asteroid.Asteroid(new_pos)
        self.asteroids.append(new_rock)
        self._screen.register_asteroid(new_rock, new_rock.get_size())

    def add_torpedo(self):
        """
        Creates a new torpedo with the ship's position as it's initial one,
        uses the ship's current heading and speed as it's own constants.
        Adds it to the torpedoes list if the list is not full
        (there are no more than 15 torpedoes in the game at the same time)
        and registers it so it would appear on the sceen
        """
        pos = self.ship.get_pos()
        heading = self.ship.get_heading()
        speed = self.ship.get_speed()
        if len(self.torpedoes) < 15:
            new_torpedo = torpedo.Torpedo(pos, speed, heading)
            self.torpedoes.append(new_torpedo)
            self._screen.register_torpedo(new_torpedo)

    def split_asteroid(self, rock, torp):
        """
        When a larger asteroid is hit by a torpedo
        the asteroid is split into 2 smaller ones.
        The new speed of each is given by a specific formula.
        And is dependant on the speed of the torpedo.
        :param rock: an Asteroid object
        :param torp:  a Torpedo object
        """
        new_pos = rock.get_pos()
        new_size = rock.get_size() - 1
        cur_x_speed_pow = rock.get_x_speed() ** 2
        cur_y_speed_pow = rock.get_y_speed() ** 2
        divisor = math.sqrt(cur_x_speed_pow + cur_y_speed_pow)
        new_x_speed = (torp.get_x_speed() + rock.get_x_speed()) / divisor
        new_y_speed = (torp.get_y_speed() + rock.get_y_speed()) / divisor
        new_speed_i = [new_x_speed, new_y_speed]
        new_speed_ii = [-new_x_speed, -new_y_speed]
        rock_i = asteroid.Asteroid(new_pos, new_size, new_speed_i)
        rock_ii = asteroid.Asteroid(new_pos, new_size, new_speed_ii)
        self.asteroids += [rock_i, rock_ii]
        # new asteroids need to be drawn immediately.
        # waiting until the next draw_all() causes
        # unexpected behaviour in Screen.
        self._screen.register_asteroid(rock_i, rock_i.get_size())
        self._screen.draw_asteroid(rock_i, *rock_i.get_pos())
        self._screen.register_asteroid(rock_ii, rock_ii.get_size())
        self._screen.draw_asteroid(rock_ii, *rock_ii.get_pos())

    def award_points(self, points):
        """
        Adds a given amount of points (int)
        to the player, and update the screen.
        :param points: int of points.
        """
        self._score += points
        self._screen.set_score(self._score)

    def _random_pos(self):
        """:return a random [x,y] position on the board"""
        x = random.randint(Screen.SCREEN_MIN_X, Screen.SCREEN_MAX_X)
        y = random.randint(Screen.SCREEN_MIN_Y, Screen.SCREEN_MAX_Y)
        return [x, y]


def main(amnt):
    """
    main function to start the game
    :param amnt: # of asteroids
    """
    runner = GameRunner(amnt)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
