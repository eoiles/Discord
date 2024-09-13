## Game Idea

### 1. Monster Grid
- The game features a 3x3 monster grid.
- Each slot in the grid can hold a monster.
- grid are similar to Hearthstone minions, having attack and defense stats (e.g., 3/3 for 3 attack and 3 defense).

### 2. Card Mechanics
- Players have cards they can play, but for now, no mana cost is implemented.
- Example card: **Fireball**.
  - The Fireball deals damage in a cross pattern on the grid.
  - The pattern looks like this:
    ```
    010
    121
    010
    ```
  - The numbers represent the damage dealt to the corresponding grid positions.
  - The player can choose the cast location of the center of the card (represented by the "2" in the pattern).
  
### 3. Example Gameplay
- Player 1 casts a Fireball at location (1,1) on the grid. This means the Fireball's center (2 damage) hits the first y, first column grid slot.
- The adjacent grid slots are affected by 1 damage as per the Fireball's damage pattern.

### Future Considerations
- Add mana cost for cards.
- Design other card effects and damage patterns.
- Implement more complex grid and monster interactions.