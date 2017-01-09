"""########################################################################
# FILE : asteroids_main.py
# WRITER : Joshua Herskowitz , jherskow , 321658379
# WRITER : Rachel Zilberberg, rachelz , 314421876
# EXERCISE : intro2cs ex9 2016-2017
# DESCRIPTION:
########################################################################"""
from screen import Screen
import sys
import ship
import asteroid
import random
import torpedo
import helpers
import math

DEFAULT_ASTEROIDS_NUM = 5
HIT_TITLE = 'Ouch!'
HIT_MSG = 'Please do not feed the asteroids.'
EXIT_TITLE = 'Quitters never win!'
EXIT_MSG = 'leaving so soon? :('
LOSS_TITLE = 'YOU LOSE'
LOSS_MSG = 'In Space.... No One Can Hear You Scream!'
WIN_TITLE = 'hhrhrhrrmmmmmmmm'
WIN_MSG = 'The Force Is Strong In This One'


class GameRunner:
    """ game runner"""
    # ===== GameRunner - class constants =====
    POINTS_L_ROCK = 20
    POINTS_M_ROCK = 50
    POINTS_S_ROCK = 100

    def __init__(self, asteroids_amnt):
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

    def move(self, thing):
        """moves an object that can move"""
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
        return None

    def move_all(self):
        """ moves all moveables on screen"""
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
            # print(str(self.ship))  # todo DEBUG this prints the thingy

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

    def _random_pos(self):
        """Returns a random [x,y] position on the board"""
        x = random.randint(Screen.SCREEN_MIN_X, Screen.SCREEN_MAX_X)
        y = random.randint(Screen.SCREEN_MIN_Y, Screen.SCREEN_MAX_Y)
        return [x, y]

    def _game_loop(self):
        """docstring"""
        if self._screen.is_left_pressed():
            self.ship.direction_change("left")
        if self._screen.is_right_pressed():
            self.ship.direction_change("right")
        if self._screen.is_up_pressed():
            self.ship.accelerate()
        if self._screen.is_space_pressed():
            self.add_torpedo()
        self.move_all()
        self.draw_all()
        self.check_asteroid_kills()
        self.check_ship_crash()
        self.manage_torpedoes()
        self.check_game_over()

    def add_asteroid(self):
        """docstring"""
        new_pos = self._random_pos()
        while new_pos == self.ship.get_pos():
            new_pos = self._random_pos()
        new_rock = asteroid.Asteroid(new_pos)
        self.asteroids.append(new_rock)
        self._screen.register_asteroid(new_rock, new_rock.get_size())

    def add_torpedo(self):
        """ docstring """
        pos = self.ship.get_pos()
        heading = self.ship.get_heading()
        speed = self.ship.get_speed()
        if len(self.torpedoes) < 15:
            new_torpedo = torpedo.Torpedo(pos, speed, heading)
            self.torpedoes.append(new_torpedo)
            self._screen.register_torpedo(new_torpedo)

    def check_ship_crash(self):
        """ docstring """
        # copy [:] list to prevent removal during iteration
        for rock in self.asteroids[:]:
            if rock.has_intersection(self.ship):
                if self.ship.get_health() != 0:
                    self.ship.lose_life()
                    self._screen.remove_life()
                self._screen.unregister_asteroid(rock)
                self.asteroids.remove(rock)
                self._screen.show_message(HIT_TITLE, HIT_MSG)

    def check_asteroid_kills(self):
        """ docstring """
        # copy [:] list to prevent removal during iteration
        for torp in self.torpedoes[:]:
            for rock in self.asteroids[:]:
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

    def check_game_over(self):
        """ docstring """
        if self.ship.get_health() == 0:
            self._screen.show_message(LOSS_TITLE, LOSS_MSG)
            self._screen.end_game()
            sys.exit(0)
        if self._screen.should_end():
            self._screen.show_message(EXIT_TITLE, EXIT_MSG)
            self._screen.end_game()
            sys.exit(0)
        if self.asteroids == []:
            self._screen.show_message(WIN_TITLE, WIN_MSG)
            self._screen.end_game()
            sys.exit(0)

    def award_points(self, points):
        """ docstring """
        self._score += points
        self._screen.set_score(self._score)

    def split_asteroid(self, rock, torp):
        """ docstring """
        if rock.get_size() > 1:
            new_pos = rock.get_pos()
            new_size = rock.get_size() - 1
            cur_x_speed_pow = rock.get_x_speed() ** 2
            cur_y_speed_pow = rock.get_y_speed() ** 2
            machane = math.sqrt(cur_x_speed_pow + cur_y_speed_pow)
            new_x_speed = (torp.get_x_speed() + rock.get_x_speed()) / machane
            new_y_speed = (torp.get_y_speed() + rock.get_y_speed()) / machane
            new_speed_i = [new_x_speed, new_y_speed]
            new_speed_ii = [-new_x_speed, -new_y_speed]
            rock_i = asteroid.Asteroid(new_pos, new_size, new_speed_i)
            rock_ii = asteroid.Asteroid(new_pos, new_size, new_speed_ii)
            self.asteroids += [rock_i, rock_ii]
            self._screen.register_asteroid(rock_i, rock_i.get_size())
            self._screen.register_asteroid(rock_ii, rock_ii.get_size())

    def manage_torpedoes(self):
        """docstring"""
        for missile in self.torpedoes:
            missile.reduce_dur()
            if missile.get_dur() == 0:
                self._screen.unregister_torpedo(missile)
                self.torpedoes.remove(missile)


def main(amnt):
    """ docstring """
    runner = GameRunner(amnt)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)