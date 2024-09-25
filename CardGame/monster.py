
import json

class Monster:
    def __init__(self, name, attack, hp, emoji='<:transparent:1286823572244922461>'):
        self.name = name
        self.attack = attack
        self.hp = hp
        self.is_damaged_last_turn = False  # New attribute to track if monster was damaged 

        #store icon of each monsters
        self.emoji=emoji
    


    def to_corpse(self):
        """
        Transforms the monster into a corpse.
        Typically, this means setting its HP to 0 and possibly
        changing its status or type to indicate it's a corpse.
        """
        self.hp = 0  # Make sure the HP is set to 0
        self.name = "Corpse"  # Optionally rename the monster
        print(f"{self.name} is now a corpse.")

    @staticmethod
    def load_monster_by_name(name):
        """
        Load a monster by its name from the 'monsters.json' file.
        :param name: The name of the monster to load.
        :return: A Monster instance or None if the monster is not found.
        """
        with open('CardGame/monsters.json', 'r') as file:
            monsters = json.load(file)

        for monster_data in monsters:
            if monster_data['name'].lower() == name.lower():
                return Monster(
                    name=monster_data['name'],
                    attack=monster_data['attack'],
                    hp=monster_data['hp'],
                    emoji=monster_data['emoji']
                )
        
        print(f"Monster with name '{name}' not found.")
        return None

    #actually eq need to check all attributes, not just listed
    def __eq__(self, other):
        if not isinstance(other, Monster):
            return NotImplemented
        return (self.name == other.name and
                self.hp == other.hp and
                self.attack == other.attack)

    def get_attack(self):
        return self.attack

    def get_hp(self):
        return self.hp

    def take_damage(self, damage):
        self.hp -= damage

        if damage > 0:
            self.is_damaged_last_turn = True

        print(f"{self.name} took {damage} damage, remaining HP: {self.hp}")
        if self.hp <= 0:
            self.to_corpse()  # Turn the monster into a corpse
            print(f"{self.name} has been defeated!")

    def is_alive(self):
        return self.hp > 0

    def reset_damage_status(self):
            """Resets the 'damaged_last_turn' flag at the start of a new turn."""
            self.is_damaged_last_turn = False

    def reset_stats(self):
        self.is_damaged_last_turn = False

# Example usage:
# monster1 = Monster("Imp", 1, 1)
# monster2 = Monster("Dragon", 3, 5)