# deck.py

import random
from card import Card  # Import the Card class from card.py

class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        if isinstance(card, Card):  # Check if card is an instance of Card
            self.cards.append(card)
            print(f"Added {card} to the deck.")
        else:
            print(f"Cannot add {card} to deck. Expected instance of Card.")

    def remove_card(self, card):
        if card in self.cards:
            self.cards.remove(card)
            print(f"Removed {card} from the deck.")
        else:
            print(f"{card} is not in the deck.")

    def shuffle(self):
        random.shuffle(self.cards)
        print("Deck shuffled.")

    def draw_card(self):
        if len(self.cards) > 0:
            drawn_card = self.cards.pop(0)
            print(f"Drew {drawn_card} from the deck.")
            return drawn_card
        else:
            print("Deck is empty.")
            return None

    def __str__(self):
        return f"Deck with {len(self.cards)} cards"

    def __repr__(self):
        return self.__str__()

# Example Usage
if __name__ == "__main__":
    deck = Deck()
    card1 = Card(name="Dragon", card_id=1, card_type="Monster")
    card2 = Card(name="Fireball", card_id=2, card_type="Spell")
    
    deck.add_card(card1)
    deck.add_card(card2)
    
    deck.shuffle()
    
    print(deck.draw_card())
    print(deck)