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
import helpers

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
        self.ship = ship.Ship(pos=self._random_pos())
        for rock in range(asteroids_amnt):
            self.add_asteroid()

    def move(self, thing):
        """moves an object that can move"""
        x_speed, y_speed = thing._speed[0], thing._speed[1]
        old_x, old_y = thing._pos[0], thing._pos[1]
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
        for torpedo in self.torpedoes:
            self.move(torpedo)
        self.move(self.ship)

    def draw_all(self):
        """draws all objects on screen"""
        for rock in self.asteroids:
            self._screen.draw_asteroid(rock, *rock._pos)
        self._screen.draw_ship(*self.ship.draw_prep())
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
        self.move_all()
        self.draw_all()
        if self._screen.is_left_pressed():
            self.ship.direction_change("left")
        if self._screen.is_right_pressed():
            self.ship.direction_change("right")
        if self._screen.is_up_pressed():
            self.ship.accelerate()

    def add_asteroid(self):
        """docstring"""
        new_asteroid = asteroid.Asteroid(self._random_pos())
        self.asteroids.append(new_asteroid)
        self._screen.register_asteroid(new_asteroid, new_asteroid._size)


def main(amnt):
    """ docstring """
    runner = GameRunner(amnt)
    runner.run()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
