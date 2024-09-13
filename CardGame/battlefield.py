from monster import Monster
#we do not do any display print outside the display class every display should use display class

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
    def add_monster(self, monster, x, y):
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


        



# Example usage:
# grid_2d = Battlefield(5, 5)  # Creates a 5x5 grid
# grid_2d.add_monster(Monster("Goblin"), 2, 3)  # Adds a monster at position (2, 3)
# print(grid_2d.get_monster(2, 3))  # Retrieves the monster at position (2, 3)
# grid_2d.remove_monster(2, 3)  # Removes the monster at position (2, 3)
# print(grid_2d.get_monster(2, 3))  # Should print None after removal