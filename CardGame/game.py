from battlefield import Battlefield
from turn import Turn
from display import display_game_state  # Import the display function
#we do not do any display print outside the display class every display should use display class

class Game:
    def __init__(self, players):
        self.players = players  # List of Player objects
        self.battlefield = Battlefield(3, 3)  # Renamed from Battlefield
        self.current_player_idx = 0
        self.round = 1
        self.is_game_over = False

    def start_game(self):
        print("Game started!")
        while not self.is_game_over:
            display_game_state(self, self.battlefield, self.players[0])  # Updated reference
            self.play_turn()
            self.check_winner()
            self.round += 1

    def play_turn(self):
        current_player = self.players[self.current_player_idx]
        turn = Turn(current_player, self)
        turn.start_turn()
        self.current_player_idx = (self.current_player_idx + 1) % len(self.players)

    def check_winner(self):
        # Check if any player has won (e.g., reduce opponent's HP to 0)
        for player in self.players:
            if player.hp <= 0:
                print(f"{player.name} has lost the game!")
                self.is_game_over = True

    def end_game(self):
        print("Game over!")