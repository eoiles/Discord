from display import draw_player_hand
from display import draw_turn
from action import Action


class Turn:
    def __init__(self, player, battlefield):
        """
        Initialize the Turn object.
        :param player: The player whose turn it is.
        :param game: The current game instance.
        """
        self.player = player
        self.battlefield = battlefield
        self.action_queue = []  # Queue to hold selected cards for this turn

    def display(self):
        draw_turn(self, self.battlefield)
        draw_player_hand(self.player)

    def start_turn(self):
        print(f"{self.player.name}'s turn begins.")
    
        self.player.draw_card()

        self.wait_for_player_input()
        self.execute_action_queue()

        self.display()

        self.reset_battlefield_monster_stats()


    def wait_for_player_input(self):
        """
        Interpret player input and add the corresponding action to the action queue.
        Input format: '<card_index> -> <x>,<y>'
        Example: '1->2,2' means cast the 1st card in hand at position 2nd cols and 3rd rows.
        """

        while True:  # Loop until valid input is provided

                # Prompt the user for input
            player_input = input("Enter action (e.g., '1->2,2' for casting 1st card to position 2nd cols and 3rd rows): ")

            #player choose to pass
            if player_input == "pass":
                break
            
            # Split the input into card index and position
            card_part, pos_part = player_input.split('->')
            card_index = int(card_part.strip()) - 1  # Convert to 0-based index
            x,y = map(int, pos_part.strip().split(','))  # Get y and xumn

            # Check if the card index is valid
            if card_index < 0 or card_index >= len(self.player.hand):
                raise ValueError("Invalid card selection.")

            # Check if the position is within valid boundaries
            if not (1 <= y <= self.battlefield.y_size) or not (1 <= x <= self.battlefield.x_size):
                raise ValueError("Invalid position on the battlefield.")

            # Get the card from the player's hand
            card = self.player.hand[card_index]

            # Add the action to the action queue
            action = Action(self.player, card, (x, y))
            self.action_queue.append(action)
            print(f"Added action: Cast {card.name} at position ({x}, {y}).")

            #quit loop if valid input
            break
            



    
    def execute_action_queue(self):
        """
        Execute all actions in the action queue.
        """
        if not self.action_queue:
            print("No actions to execute.")
        else:
            print(f"Executing {len(self.action_queue)} actions...")
            while self.action_queue:
                action = self.action_queue.pop(0)
                action.execute(self.battlefield)



    def ready(self):
        """
        Resolve all cards in the card queue.
        """
        if not self.card_queue:
            print("No cards to resolve.")
        else:
            print(f"Resolving {len(self.card_queue)} cards...")
            while self.card_queue:
                card = self.card_queue.pop(0)
                self.cast_card(card)


    def view_card_details(self):
        """
        Allow the player to view detailed information about the cards in their hand.
        """
        if not self.player.hand:
            print("No cards in hand.")
        else:
            for card in self.player.hand:
                print(f"{card}")


    #reset battlefield monster stats after every turn
    def reset_battlefield_monster_stats(self):
        
        #reset monster damaged last turn
        for monster in self.battlefield.get_all_monsters():
           monster.reset_stats()