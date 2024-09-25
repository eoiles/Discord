import sys
import os
import unittest

# Add the parent directory of the 'tests' folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from battlefield import Battlefield

class TestBattlefield(unittest.TestCase):
    def test_load_level_by_name(self):
        # Load the level 1-1
        battlefield = Battlefield.load_level_by_name("1-1")

        # Check if the battlefield is not None
        self.assertIsNotNone(battlefield)

        # Check the size of the battlefield
        self.assertEqual(battlefield.x_size, 3)
        self.assertEqual(battlefield.y_size, 3)

        # Check the monsters on the battlefield
        expected_monsters = [
            ["Orc", "Goblin", "Empty"],
            ["Empty", "Dragon", "Slime"],
            ["Empty", "Slime", "Empty"]
        ]

        battlefield.display()

        # Get all monsters from the battlefield
        actual_monsters = [
            [battlefield.get_monster(x, y).name if battlefield.get_monster(x, y) else "Empty"
             for x in range(1, battlefield.x_size + 1)]
            for y in range(1, battlefield.y_size + 1)
        ]

        self.assertEqual(actual_monsters, expected_monsters)

# Run the tests
if __name__ == '__main__':
    unittest.main()