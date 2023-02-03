"""
    game.py
    -------

    This module contains the Game class that implements the actual game mechanics as well as
    the __main__ construct to make the game runnable.
"""

# sphinx-apidoc --full --force --implicit-namespaces -a --separate -o docs gamedemo
# sphinx-autobuild docs docs/_build/html --open-browser

__author__ = "Reindert-Jan Ekker"

import os
import random
import sys
#sys.path.insert(0, os.path.abspath('..'))
from player import Player
from weapons import Sword, FireBreath


def my_function(my_arg, my_other_arg):
    """A function just for me.

    :param my_arg: The first of my arguments.
    :param my_other_arg: The second of my arguments.

    :returns: A message (just for me, of course).
    """


class MyClass():
    def foo(self):
        print('foo')

    def bar(self):
        """This method does the same as

        :py:func:`gamedemo.game.Player.take_hit`

        """

        print('foo')


class Game:
    def __init__(self, player1, player2):
        self.p1 = player1
        self.p2 = player2

    def run(self):
        print(self.p1)
        print(self.p2)
        while self.p1.is_alive and self.p2.is_alive:
            if random.choice([True, False]):
                attacker = self.p1
                defender = self.p2
            else:
                attacker = self.p2
                defender = self.p1
            dmg, sound = attacker.weapon.attack()
            print(attacker.name, "attacks:", sound)
            print(attacker.name, "did", dmg, "damage")
            defender.take_hit(dmg)
        print(attacker.name, "won with", attacker.health, "health left")


if __name__ == "__main__":
    random.seed()
    g = Game(Player("The Knight", Sword()), Player("The Dragon", FireBreath()))
    sys.path.insert(0, os.path.abspath('..'))
    print(f"{sys.path=}")
    g.run()
