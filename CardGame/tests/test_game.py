import sys
import os
import unittest

# Add the parent directory of the 'tests' folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game import Game
from player import Player
from CardGame.monster import Monster
from card import Fireball
from battlefield import Battlefield

class TestGame(unittest.TestCase):

    def setUp(self):
        # Setup code without game turn execution
        self.player1 = Player(name="Player1", hp=10)
        fireball = Fireball()
        self.player1.hand.append(fireball)
        self.game = Game(players=[self.player1], battlefield_size=(3, 3))
        self.game.load_level("1-1")  # Load the level, but don't play turn yet

    def test_player1_turn(self):
        # Call play_turn() only in this specific test
        self.game.start()
        self.game.play_turn()

    def test_initialize_game(self):
    # Initialization-related checks without running a turn
        self.assertEqual(len(self.game.players), 1)
        self.assertEqual((self.game.battlefield.x_size, self.game.battlefield.y_size), (3, 3))
        self.assertEqual(self.game.players[0].hp, 10)
        self.assertEqual(len(self.player1.hand), 1)
        self.assertIsInstance(self.player1.hand[0], Fireball)




if __name__ == "__main__":
    unittest.main()