from deck import Deck
from card import Card

class Player:
    def __init__(self, name="Player", hp=30, mana=0, hand_limit=5):
        self.name = name  # Add the name attribute
        self.hp = hp
        self.mana = mana
        self.hand_limit = hand_limit
        self.hand = []  # This will hold the player's hand of cards
        self.deck = Deck()  # Add a deck for the player

    def draw_card(self, num_cards=1):
        """Draw a specified number of cards from the deck."""
        if len(self.hand) + num_cards > self.hand_limit:
            print("Cannot draw more cards than hand limit.")
            return

        for _ in range(num_cards):
            drawn_card = self.deck.draw_card()
            if drawn_card:
                self.hand.append(drawn_card)
                print(f"Player drew: {drawn_card}")
            else:
                print("No card drawn, deck is empty.")
                break

    def play_card(self, card):
        if card in self.hand:
            self.hand.remove(card)
            print(f"Player played: {card}")
        else:
            print(f"Card {card} is not in hand.")

    def select_card(self):
        """Allow the player to select a card from their hand."""
        if not self.hand:
            print("No cards in hand to select.")
            return None
        
        print("Your hand:")
        for idx, card in enumerate(self.hand, start=1):
            print(f"{idx}. {card}")
        
        choice = int(input("Select a card by number: ")) - 1
        if 0 <= choice < len(self.hand):
            return self.hand[choice]
        else:
            print("Invalid selection.")
            return None

    def add_card_to_deck(self, card):
        """Method to add a card to the player's deck."""
        self.deck.add_card(card)

    def __str__(self):
        return (f'Player Stats: HP = {self.hp}, Mana = {self.mana}, '
                f'Hand Limit = {self.hand_limit}, Cards in Hand = {len(self.hand)}, '
                f'Cards in Deck = {len(self.deck.cards)}')

    def __repr__(self):
        return self.__str__()

# Example Usage
if __name__ == "__main__":
    player = Player()
    card1 = Card(name="Dragon", card_id=1, card_type="Monster")
    card2 = Card(name="Fireball", card_id=2, card_type="Spell")
    
    player.add_card_to_deck(card1)
    player.add_card_to_deck(card2)
    
    player.draw_card()
    player.draw_card()
    
    print(player)
    player.play_card(card1)
    print(player)