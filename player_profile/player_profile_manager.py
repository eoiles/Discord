
import json
from CardGame.player import Player
from CardGame.card import Card
from CardGame.deck import Deck
# player_profile_manager.py

from CardGame.card import get_predefined_card

class PlayerProfileManager:
    @staticmethod
    def load_profile(player_name):
        """
        Load a player's profile from a JSON file and return a Player instance.
        """
        profile_file_path = f'player_profile/profiles/{player_name}.profile'  # Adjust the file path as needed
        with open(profile_file_path, 'r') as file:
            data = json.load(file)

        # Create the Player instance
        player = Player(
            name=data["name"],
            hp=data["hp"],
            mana=data["mana"],
            hand_limit=data["hand_limit"]
        )

        # Load the player's deck using predefined cards
        deck = Deck()
        for card_data in data["deck"]:
            card = get_predefined_card(card_data["card_id"])
            if card:
                deck.add_card(card)
            else:
                print(f"Card with id {card_data['card_id']} not found.")

        player.deck = deck


        assert isinstance(player, Player)

        return player