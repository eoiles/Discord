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