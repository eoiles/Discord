import sys
import os
import pytest

# Add the parent directory of the 'tests' folder (cardgame main folder) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import from modules in the cardgame folder
from battlefield import Battlefield
from monster import Monster
from card import Fireball

def test_fireball_card():
    # Create a 3x3 monster grid
    grid = Battlefield(3, 3)

    # Add grid at different positions
    goblin = Monster("Goblin", hp=5, attack=2)
    orc = Monster("Orc", hp=8, attack=3)
    grid.add_monster(goblin, 1, 1)  # center monster
    grid.add_monster(orc, 0, 1)     # adjacent monster

    # Create a Fireball card
    fireball = Fireball()

    # Play the Fireball card at the center (1, 1)
    fireball.play(grid, 1, 1)

    # Check the HP of the grid after Fireball damage
    assert goblin.hp == 3  # center takes 2 damage
    assert orc.hp == 7     # adjacent takes 1 damage

    # Check no other monster is affected
    assert grid.get_monster(0, 0) is None
    assert grid.get_monster(2, 2) is None