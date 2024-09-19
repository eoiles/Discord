#we do not do any display print outside the display class every display should use display class

class Card:
    def __init__(self, name, card_id, card_type, picture_url=None,description=None):
        self.name = name
        self.card_id = card_id
        self.card_type = card_type
        self.picture_url = picture_url
        self.description = description

    def __str__(self):
        return f"Card(name='{self.name}', card_id={self.card_id}, card_type='{self.card_type}')"

    def set_picture_url(self, url):
        self.picture_url = url

    def get_picture_url(self):
        return self.picture_url

    def play(self):
        """
        This is the play method that each card will implement.
        This method will be triggered when the resolve phase occurs.
        """
        raise NotImplementedError("This method should be overridden in subclasses.")


class Fireball(Card):
    def __init__(self):
        super().__init__("Fireball", card_id=1, card_type="spell")
        # Define the damage pattern for the Fireball
        self.effect_grid = [
            [0, 1, 0],
            [1, 2, 1],
            [0, 1, 0]
        ]

        self.description = "Deals damage to the monster that is in the cross pattern."

    def play(self, battlefield, x, y):
        """
        Play the Fireball card at the (x, y) position on the battlefield .
        The damage is applied to grid within the cross pattern.
        """
        for dx in range(-1, 2):  # Loop through -1, 0, 1 for both x and y offsets
            for dy in range(-1, 2):
                target_x, target_y = x + dx, y + dy
                if 1 <= target_x <= battlefield.x_size and 1 <= target_y <= battlefield.y_size:
                    monster = battlefield.get_monster(target_x, target_y)
                    if monster:
                        damage = self.effect_grid[dx + 1][dy + 1]
                        monster.take_damage(damage)
                        print(f"Dealt {damage} damage to monster at ({target_x}, {target_y})")