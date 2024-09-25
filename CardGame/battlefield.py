from monster import Monster
#we do not do any display print outside the display class every display should use display class
import json

from display import draw_battlefield

class Battlefield:
    '''
    the coordinates start from 1, not 0

    1,1    1,2     1,3
    2,1    2,2     2,3
    3,1    3,2     3,3
    '''


    def __init__(self, x_size, y_size):
        self.x_size = x_size  # x represents the x coordinate
        self.y_size = y_size  # y represents the y coordinate
        self.grid = [[None for _ in range(x_size)] for _ in range(y_size)]  # Initialize the grid

    # add_monster(x, y) means adding a monster to the specified column (x) and row (y)
    def add_monster(self, monster : Monster, x, y):
        # Adjusting for 1-based index
        if 1 <= x <= self.x_size and 1 <= y <= self.y_size:
            self.grid[y-1][x-1] = monster  # Adjust for 0-based grid
        else:
            raise ValueError("Position out of bounds")

    # Remove a monster at a specific position (x, y)
    def remove_monster(self, x, y):
        # Adjusting for 1-based index
        if 1 <= x <= self.x_size and 1 <= y <= self.y_size:
            self.grid[y-1][x-1] = None  # Adjust for 0-based grid
        else:
            raise ValueError("Position out of bounds")

    # Get the monster at a specific position (x, y)
    def get_monster(self, x, y):
        # Adjusting for 1-based index
        if 1 <= x <= self.x_size and 1 <= y <= self.y_size:
            return self.grid[y-1][x-1]  # Adjust for 0-based grid
        else:
            raise ValueError("Position out of bounds")

    # Method to iterate over all grid in the battlefield
    def get_all_monsters(self):
        for row in self.grid:
            for monster in row:
                if monster:
                    yield monster


    
    @staticmethod
    def load_level_by_name(level_name):
        # Load the levels from the JSON file
        with open('CardGame/levels.json', 'r') as file:
            levels_data = json.load(file)

        # Iterate over each level in the JSON data
        for level_data in levels_data:
            if level_data['Name'] == level_name:
                battlefield_grid = level_data['Battlefield']

                # Create a new Battlefield object
                battlefield = Battlefield(x_size=len(battlefield_grid[0]), y_size=len(battlefield_grid))

                # Populate the battlefield with monsters
                for y, row in enumerate(battlefield_grid):
                    for x, monster_name in enumerate(row):
                        if monster_name.strip().lower() == "empty":  # Skip entries marked as "empty"
                            continue
                        monster = Monster.load_monster_by_name(monster_name)
                        if monster:
                            battlefield.add_monster(monster, x + 1, y + 1)  # Adjust for 1-based index

                # Return the battlefield object
                return battlefield

        # If no matching level is found, return None or raise an exception
        return None
    

    def display(self):
        draw_battlefield(self)


        



# Example usage:
# grid_2d = Battlefield(5, 5)  # Creates a 5x5 grid
# grid_2d.add_monster(Monster("Goblin"), 2, 3)  # Adds a monster at position (2, 3)
# print(grid_2d.get_monster(2, 3))  # Retrieves the monster at position (2, 3)
# grid_2d.remove_monster(2, 3)  # Removes the monster at position (2, 3)
# print(grid_2d.get_monster(2, 3))  # Should print None after removal