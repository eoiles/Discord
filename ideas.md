## Game Idea

### 1. Monster Grid
- The game features a 3x3 monster grid.
- Each slot in the grid can hold a monster.
- Monsters are similar to Hearthstone minions, having attack and defense stats (e.g., 3/3 for 3 attack and 3 defense).

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
- Player 1 casts a Fireball at location (1,1) on the grid. This means the Fireball's center (2 damage) hits the first row, first column grid slot.
- The adjacent grid slots are affected by 1 damage as per the Fireball's damage pattern.

### 4. RPG Features
This is a card-based RPG with various menus and gameplay systems that expand the experience beyond just battles:

#### Main Player Menu
- **Deck**: View and manage the player's deck of cards.
- **Store**: Purchase new cards, items, or upgrades for the deck using in-game currency.
- **Dungeon**: Enter dungeons where players face monsters and challenges to earn rewards like cards and resources.
- **Market**: A trading system where players can exchange cards or items with other players.
- **Blacksmith**: A system where players can upgrade their cards or create new cards using resources collected in dungeons.
- **Stats**: View player stats such as HP, mana, gold, and inventory.

### 5. Future Considerations
- Add mana cost for cards.
- Design other card effects and damage patterns.
- Implement more complex grid and monster interactions.
- Expand the store and market mechanics with rarity systems and player-to-player trading.
- Add a multiplayer mode for duels and cooperative dungeon raids.