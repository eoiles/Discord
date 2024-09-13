# display.py
#we do not do any display print outside the display class every display should use display class

def draw_battlefield(battlefield):
    """
    Draw the battlefield (Monster Grid) in a grid format.
    Display HP of damaged monsters in yellow.
    """
    print("\n=== Battlefield ===")
    for y in range(battlefield.y_size):  
        for x in range(battlefield.x_size): 
            monster = battlefield.grid[y][x]  
            if monster:
                if monster.is_damaged_last_turn:
                    # Display damaged HP in yellow
                    print(f"[{monster.attack}|\033[93m{monster.hp}\033[0m]", end=" ")
                else:
                    print(f"[{monster.attack}|{monster.hp}]", end=" ")
            else:
                print("[   ]", end=" ")  # Empty cell
        print()
    print("====================\n")


def display_player_hand(player):
    """
    Display the player's hand of cards.
    Each card is listed by its name with an index for selection.
    """
    print("=== Player's Hand ===")
    if not player.hand:
        print("No cards available.")
    else:
        for idx, card in enumerate(player.hand):
            print(f"{idx + 1}. [ {card.name} ]")  # Simple card representation
    print("=====================\n")


def draw_submenu(player):
    """
    Display the submenu with player's name and available actions.
    """
    print("=== Submenu ===")
    print(f"Player: {player.name}")
    print("1. Play Card")
    print("2. Ready")
    print("3. View Card Details")
    print("=====================\n")


def display_turn(turn, battlefield):
    """
    Display the current state of the turn, including player name, card queue, and optional battlefield.
    """
    print(f"=== {turn.player.name}'s Turn ===")
    
    # Display card queue
    if turn.action_queue:
        print("Card Queue:")
        for idx, card in enumerate(turn.card_queue):
            print(f"{idx + 1}. {card.name}")
    else:
        print("No cards in the queue.")
    
    # Conditionally display battlefield
    if battlefield:
        draw_battlefield(battlefield)
    
    print("=====================\n")




def display_card_effect(card_effect_grid):
    """
    Display the effect of a card on the battlefield.
    Use red (-X) for damage.
    """
    print("\n=== Card Effect ===")
    for y in card_effect_grid:
        for effect in y:
            if effect is None:
                print("   ", end=" ")  # Keep the space for None
            else:
                print(f"\033[91m-{effect}\033[0m", end=" ")  # Display damage in red
        print()
    print("====================\n")