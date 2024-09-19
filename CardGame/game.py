from battlefield import Battlefield
from turn import Turn
from display import display_game_state

class Game:
    def __init__(self, players, battlefield_size=(3, 3)):
        """
        Initialize the game with a list of players and a customizable battlefield size.
        :param players: List of Player objects.
        :param battlefield_size: Tuple (x_size, y_size) for the battlefield grid.
        """
        self.players = players
        self.battlefield = Battlefield(*battlefield_size)  # Initialize the battlefield with provided size.
        self.current_player_idx = 0
        self.round = 1
        self.is_game_over = False

    def start(self):
        """
        Start the game and initialize any required setup.
        """
        print("Game started!")
        display_game_state(self)  # Display initial game state

    def play_turn(self):
        """
        Play a single turn in the game.
        """
        current_player = self.players[self.current_player_idx]
        print(f"Round {self.round}: {current_player.name}'s turn begins.")
        turn = Turn(current_player, self.battlefield)
        turn.start_turn()  # Handles actions for the current player's turn

        # Move to the next player
        self.current_player_idx = (self.current_player_idx + 1) % len(self.players)
        self.round += 1

    def add_monster_to_battlefield(self, monster, x, y):
        """
        Adds a monster to a specific position on the battlefield.
        :param monster: Monster object to add.
        :param x: X-coordinate on the battlefield.
        :param y: Y-coordinate on the battlefield.
        """
        self.battlefield.add_monster(monster, x, y)
        print(f"{monster.name} added to battlefield at position ({x}, {y})")

    def check_winner(self):
        """
        Check if all players have been defeated or if enemies have been defeated.
        """
        # Check if all players have 0 or less HP (team defeat)
        if self.is_player_all_dead(self.players):
            self.game_over = True
            return "Game Over - All players defeated!"
        
        # Check if all enemies are defeated (team victory)
        if self.is_monster_all_dead(self.battlefield.get_all_monsters()):
            self.game_over = True
            return "Victory - All enemies defeated!"
        
        return None  # No conclusion yet

    def is_player_all_dead(self, players):

        return all(player.hp <= 0 for player in self.players)

    def is_monster_all_dead(self, monsters):

        return all(monster.hp <= 0 for monster in monsters)
    

    def run_game_loop(self):
        """
        Main game loop to continue the game until a winner is determined.
        """
        while not self.is_game_over:
            self.play_turn()
            self.check_winner()
        self.end_game()

    def end_game(self):
        """
        End the game and display the final result.
        """
        print("Game over!")
        winner = [p for p in self.players if p.hp > 0]
        if winner:
            print(f"{winner[0].name} wins!")
        else:
            print("No winner, it's a draw!")
