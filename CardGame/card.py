#we do not do any display print outside the display class every display should use display class

class Card:
    def __init__(self, name, card_id, card_type, emoji=None,description=None):
        self.name = name
        self.card_id = card_id
        self.card_type = card_type
        self.emoji = None
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
    
def get_predefined_card(card_id):
    predefined_cards = {
        1: Fireball(),
        2: TheDeath(),
        3: Blizzard(),
        4: Heal(),
        5: Lightning()
    }

    return predefined_cards.get(card_id, None)

'''

            "<:1_:1282725858724806727>",
            "<:2_:1282725868120051743>",
            "<:3_:1282725880468082749>",
            "<:4_:1282725886474453186>",
            "<:5_:1282725891956277279>",
            "<:6_:1282725896788115456>"


'''

class Fireball(Card):
    def __init__(self):
        super().__init__("火球", card_id=1, card_type="spell")
        # Define the damage pattern for the Fireball
        self.effect_grid = [
            [0, 1, 0],
            [1, 2, 1],
            [0, 1, 0]
        ]

        self.emoji="<:1_:1282725858724806727>"

        self.description = "对目标怪物造成AOE溅射伤害。"

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


'''
TheDeath
Instantly kills a single target monster on the battlefield.
'''

class TheDeath(Card):
    def __init__(self):
        super().__init__("死亡", card_id=2, card_type="spell")

        self.emoji="<:2_:1282725868120051743>"

        self.description = "瞬间消灭战场上指定位置的单个目标怪物。"

    def play(self, battlefield, x, y):
        """
        Play 'TheDeath' card, which instantly kills a single target monster at the specified position on the battlefield.
        :param battlefield: The battlefield object.
        :param x: X-coordinate of the target monster on the battlefield.
        :param y: Y-coordinate of the target monster on the battlefield.
        """
        monster = battlefield.get_monster(x, y)  # Get monster at the specified position
        if monster:
            # Set monster's HP to 0 (kill the monster)

            monster.hp = 0
            print(f"{monster.name} at position ({x}, {y}) has been killed by TheDeath.")
        else:
            print(f"No monster found at position ({x}, {y}).")

'''
Blizzard
Deals 1 damage to each monster on the battlefield.
'''
class Blizzard(Card):
    def __init__(self):
        super().__init__("暴雪", card_id=3, card_type="spell")
        self.emoji="<:3_:1282725880468082749>"
        self.description = "对战场上的所有怪物造成 1 点伤害。"

    def play(self, battlefield):
        """
        Play the 'Blizzard' card, which deals 1 damage to every monster on the battlefield.
        """
        all_monsters = battlefield.get_all_monsters()
        if not all_monsters:
            print("No monsters on the battlefield.")
            return

        for monster in all_monsters:
            monster.take_damage(1)  # Deal 1 damage to each monster
            print(f"{monster.name} takes 1 damage from Blizzard.")

'''
Heal
Resotre player hp for 6.
'''
class Heal(Card):
    def __init__(self):
        super().__init__("治疗", card_id=4, card_type="spell")
        self.emoji="<:4_:1282725886474453186>"
        self.description = "为玩家恢复 6 点生命值。"

    def play(self, player):
        """
        Play the 'Heal' card, which restores 6 HP to the player.
        """
        if player.hp < player.max_hp:
            restored_hp = min(6, player.max_hp - player.hp)
            player.hp += restored_hp
            print(f"{player.name} restored {restored_hp} HP using Heal.")
        else:
            print(f"{player.name} already has full HP.")



'''
Lightning
Deals 3 damage in a column

0 3 0
0 3 0
0 3 0

'''

class Lightning(Card):
    def __init__(self):
        super().__init__("雷电", card_id=5, card_type="spell")
        # Define the damage pattern for Lightning
        self.effect_grid = [
            [0, 3, 0],
            [0, 3, 0],
            [0, 3, 0]
        ]

        self.emoji="<:5_:1282725891956277279>"

        self.description = "对一列中的每个目标造成 3 点伤害。"

    def play(self, battlefield, x, y):
        """
        Play the Lightning card at the (x, y) position on the battlefield.
        The damage is applied in a vertical line (column).
        """
        for dx in range(-1, 2):  # Loop through -1, 0, 1 for row offsets
            target_x, target_y = x + dx, y
            if 1 <= target_x <= battlefield.x_size:
                monster = battlefield.get_monster(target_x, target_y)
                if monster:
                    damage = self.effect_grid[dx + 1][1]
                    monster.take_damage(damage)
                    print(f"Dealt {damage} damage to monster at ({target_x}, {target_y})")