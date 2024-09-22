class Monster:
    def __init__(self, name, attack, hp):
        self.name = name
        self.attack = attack
        self.hp = hp
        self.is_damaged_last_turn = False  # New attribute to track if monster was damaged 

        #store icon of each monsters
        self.emoji='<:LustThoughts:1210190946013024256>'

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