import sys
import os
import unittest

# Add the parent directory of the 'tests' folder to sys.path
sys.path.append(os.path.abspath('.'))

from CardGame.game import Game
from CardGame.player import Player
from CardGame.monster import Monster
from CardGame.card import Fireball
from CardGame.battlefield import Battlefield


class TestGame(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # Setup code without game turn execution
        print(111111111111111111111111111111111111111111111111111)



    def test_player1_turn(self):
        # Call play_turn() only in this specific test
        print(2222222222222222222222222222222222222222222222222222)


    def test_initialize_game(self):
    # Initialization-related checks without running a turn

        print(2222222222222222222222222222222222222222222222222222)




if __name__ == "__main__":
    print(100000000000000000000000000000000000)

    print(f"Script name: {__name__}")
    print(f"Arguments: {sys.argv}")
    unittest.main()