import os
import json

class PlayerProfileManager:
    def __init__(self, player):
        self.player = player

    def save_profile(self, filename):
        """Saves the player's profile to a JSON file in the profiles folder."""
        os.makedirs('player_profile/profiles', exist_ok=True)  # Create the folder if it doesn't exist
        filepath = os.path.join('player_profile/profiles', filename)
        
        profile_data = {
            "player_id": self.player.player_id,
            "name": self.player.name,
            "hp": self.player.hp,
            "mana": self.player.mana,
            "hand_limit": self.player.hand_limit,
            "deck": [card.to_dict() for card in self.player.deck_manager.deck],
            "hand": [card.to_dict() for card in self.player.deck_manager.hand],
            "win_count": self.player.win_count,
            "loss_count": self.player.loss_count,
        }
        
        with open(filepath, 'w') as f:
            json.dump(profile_data, f, indent=4)
        print(f"Profile saved to {filepath}.")

    def load_profile(self, filename):
        """Loads a player's profile from a JSON file in the profiles folder."""
        filepath = os.path.join('player_profile/profiles', filename)
        
        with open(filepath, 'r') as f:
            profile_data = json.load(f)
        
        self.player.player_id = profile_data["player_id"]
        self.player.name = profile_data["name"]
        self.player.hp = profile_data["hp"]
        self.player.mana = profile_data["mana"]
        self.player.hand_limit = profile_data["hand_limit"]
        self.player.deck_manager.deck = [Card.from_dict(card) for card in profile_data["deck"]]
        self.player.deck_manager.hand = [Card.from_dict(card) for card in profile_data["hand"]]
        self.player.win_count = profile_data["win_count"]
        self.player.loss_count = profile_data["loss_count"]
        
        print(f"Profile loaded from {filepath}.")

    def update_stats(self, hp=None, mana=None, win_count=None, loss_count=None):
        """Updates player stats like HP, mana, wins, and losses."""
        if hp is not None:
            self.player.hp = hp
        if mana is not None:
            self.player.mana = mana
        if win_count is not None:
            self.player.win_count = win_count
        if loss_count is not None:
            self.player.loss_count = loss_count


if __name__ == "__main__":
    player = Player()
    player_profile_manager = PlayerProfileManager(player)
    player_profile_manager.save_profile('player_profile.json')
    player_profile_manager.load_profile('player_profile.json')
# Example usage:
# player_profile_manager = PlayerProfileManager(player)
# player_profile_manager.save_profile('player_profile.json')
# player_profile_manager.load_profile('player_profile.json')