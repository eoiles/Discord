import sys
import os


# Add the parent directory of the 'tests' folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from battlefield import Battlefield
from monster import Monster
from player import Player
from card import Fireball

from turn import Turn
from display import draw_turn,draw_card_effect

def test_turn_with_fireball():
    # Create a 3x3 monster grid and add grid
    battlefield = Battlefield(3, 3)
    goblin = Monster("Goblin", hp=5, attack=2)
    orc = Monster("Orc", hp=8, attack=3)
    orc1 = Monster("Orc", hp=8, attack=3)
    slime = Monster("Slime", hp=3, attack=1)
    slime1 = Monster("Slime", hp=3, attack=1)
    slime2 = Monster("Slime", hp=3, attack=1)
    slime3 = Monster("Slime", hp=3, attack=1)
    battlefield.add_monster(goblin, 2, 1)  # top middle
    battlefield.add_monster(orc, 2, 2)     # center monster
    battlefield.add_monster(orc1, 3, 3)
    battlefield.add_monster(slime, 1, 1)
    battlefield.add_monster(slime1, 1, 2)
    battlefield.add_monster(slime2, 2, 3)
    battlefield.add_monster(slime3, 3, 2)

    # Create player
    player1 = Player(name="Player1", hp=10)
    player1.hand = [Fireball()]  # Add Fireball to player's hand

    # Create a turn instance for Player1
    turn = Turn(player1, battlefield)

    

    #turn 1
    print(f"{turn.player.name}'s turn begins.")
        #display turn state
    turn.display()

    draw_card_effect(Fireball().effect_grid)

    turn.wait_for_player_input()
    turn.execute_action_queue()
    turn.display()
    turn.reset_battlefield_monster_stats()






    #turn 2
    print(f"{turn.player.name}'s turn begins.")
        #display turn state
    turn.display()

    turn.wait_for_player_input()
    turn.execute_action_queue()
    turn.display()
    turn.reset_battlefield_monster_stats()




    # Test cleanup or additional checks if necessary

# Run the test
test_turn_with_fireball()

