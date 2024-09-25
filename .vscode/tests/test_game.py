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

from player_profile.player_profile_manager import PlayerProfileManager


class TestGame(unittest.TestCase):


    @classmethod
    def setUpClass(self):
        # Setup code without game turn execution

        self.game = Game()

        self.game.load_level('1-1')

        player = PlayerProfileManager.load_profile('Player1')

        self.game.add_player(player)

        self.player1 = self.game.players[0]


        self.player1.draw_card()
        self.player1.draw_card()
        self.player1.draw_card()


    def test_player1_turn(self):
        # Call play_turn() only in this specific test

        self.game.start()
        self.game.play_turn()

    def test_initialize_game(self):
    # Initialization-related checks without running a turn

        self.assertEqual(len(self.game.players), 1)
        self.assertEqual((self.game.battlefield.x_size, self.game.battlefield.y_size), (3, 3))
        self.assertEqual(self.game.players[0].hp, 30)
        self.assertEqual(len(self.player1.hand), 3)
        self.assertIsInstance(self.player1.hand[0], Fireball)




if __name__ == "__main__":
    print(100000000000000000000000000000000000)

    print(f"Script name: {__name__}")
    print(f"Arguments: {sys.argv}")
    unittest.main()