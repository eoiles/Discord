'''
The Action class represents a player's move during the game.
Currently, it models playing a card to a specific position on the battlefield.
Actions are stored in a turn's action queue and resolved one by one.

Example:
Player 1 casts a fireball at position (2, 2).

We represent this as:
    Action(player, card, position)

The Action class is primarily used as a data structure to store and represent each move.
'''

class Action:
    def __init__(self, player, card, position):
        """
        Initialize the Action object.
        
        :param player: The player performing the action.
        :param card: The card being played.
        :param position: The position on the battlefield where the card is played.
        """
        self.player = player
        self.card = card
        self.position = position

    def execute(self, battlefield):
        """
        Execute the action by applying the card's effects to the specified position on the battlefield.
        
        Some card does not requires position to be specified.

        We use the play method of the card to apply the effects.
        """

        if self.position is not None:
            self.card.play(battlefield, self.position[0], self.position[1])
        else:
            self.card.play(battlefield)
        

    def __repr__(self):
        """
        String representation of the Action object.
        """
        return f"Action(player={self.player.name}, card={self.card}, position={self.position})"


