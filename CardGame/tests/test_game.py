import sys
import os
import unittest

# Add the parent directory of the 'tests' folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game import Game
from player import Player
from monster import Monster
from card import Fireball
from battlefield import Battlefield

class TestGame(unittest.TestCase):
    
    def setUp(self):
        """
        Set up the game environment before each test.
        """
        # Create players
        self.player1 = Player(name="Player1", hp=10)
        self.player2 = Player(name="Player2", hp=10)

        # Manually add a Fireball card to player1's hand for testing purposes
        fireball = Fireball()  # Create the Fireball card
        self.player1.hand.append(fireball)  # Add Fireball to player1's hand

        # Initialize the game with a 3x3 battlefield
        self.game = Game(players=[self.player1, self.player2], battlefield_size=(3, 3))

        """
        Test adding monsters to the battlefield manually.
        """
        self.goblin = Monster(name="Goblin", hp=5, attack=2)  # Create a goblin monster
        self.orc = Monster(name="Orc", hp=8, attack=3)        # Create an orc monster

        # Add monsters to the battlefield at specific positions
        self.game.add_monster_to_battlefield(self.goblin, 1, 1)
        self.game.add_monster_to_battlefield(self.orc, 2, 2)

        # Start the game
        self.game.start()


    def test_initialize_game(self):
        """
        Test that the game initializes correctly with two players and a battlefield.
        """
        self.assertEqual(len(self.game.players), 2)
        self.assertEqual((self.game.battlefield.x_size,self.game.battlefield.y_size), (3, 3))
        self.assertEqual(self.game.players[0].hp, 10)
        self.assertEqual(self.game.players[1].hp, 10)
        """
        Test that player1 has the Fireball card in their hand.
        """
        self.assertEqual(len(self.player1.hand), 1)
        self.assertIsInstance(self.player1.hand[0], Fireball)  # E


    def test_monster_on_battlefield(self):


        """
        Test if the monsters are correctly placed on the battlefield.
        """
        # Check if the goblin and orc are at the correct positions
        self.assertEqual(self.game.battlefield.get_monster(1, 1), self.goblin)
        self.assertEqual(self.game.battlefield.get_monster(2, 2), self.orc)

    def test_play_turn(self):

        # Simulate turns
        self.game.play_turn()  # Player 1's turn
        self.game.play_turn()  # Player 2's turn

        # Check if the round number has advanced
        self.assertEqual(self.game.round, 3)

        # Test player switching after a turn
        self.assertEqual(self.game.players[self.game.current_player_idx].name, "Player1")

    def test_game_over(self):
        """
        Test that the game correctly ends when all players' HP reaches 0.
        """
        # Set all players' HP to 0 to simulate defeat
        self.player1.hp = 0
        self.player2.hp = 0

        result = self.game.check_winner()

        # Assert that the game is over and returns the correct message
        self.assertTrue(self.game.is_player_all_dead(self.game.players))
        self.assertEqual(result, "Game Over - All players defeated!")

if __name__ == "__main__":
    unittest.main()