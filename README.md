# Discord Card Game Bot

Welcome to the **Discord Card Game Bot**! This project is a card-based RPG adventure where players can duel, explore dungeons, and strategize with a variety of cards and monsters on a dynamic battlefield. Built for use in a Discord server, the bot offers immersive gameplay that combines strategic depth, card mechanics, and RPG features.

## Table of Contents
1. Features
2. [How to Set Up](#how-to-set-up)
3. [How to Play](#how-to-play)
4. [Game Mechanics](#game-mechanics)
    - [Monster Grid](#monster-grid)
    - [Card Mechanics](#card-mechanics)
    - [Example Gameplay](#example-gameplay)
    - [RPG Features](#rpg-features)
5. [Future Considerations](#future-considerations)
6. Contributing
7. License

## Features
- **Multiplayer Card-Based Combat**: Engage in duels or dungeon raids using unique cards that feature attacks, spells, and monster summons.
- **RPG Elements**: Manage your deck, earn rewards, and upgrade cards in the store or blacksmith.
- **3x3 Monster Grid**: Deploy monsters and strategize your battlefield placement.
- **Dungeon Mode**: Team up with others to conquer dungeons and earn rewards.
- **Market System**: Trade cards with other players and expand your collection.

## How to Set Up
To get started, follow these steps to install and run the Discord bot:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/discord-card-game-bot.git
    cd discord-card-game-bot
    ```

2. **Install Dependencies**:
    Ensure you have Python 3.x installed, then run:
    ```bash
    pip install -r requirements.txt
    ```

3. **Create a Discord Bot**:
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications), create a new application, and generate a bot token.
   - Add your bot to your server.

4. **Configure the Bot**:
    - In the root folder, create a `.env` file with the following:
    ```bash
    DISCORD_TOKEN=your-bot-token-here
    ```

5. **Run the Bot**:
    ```bash
    python main.py
    ```

## How to Play

### 1. Basic Commands
- **Start a Game**: `!startgame` — Begin a new card game match.
- **Join a Game**: `!joingame` — Join an active game lobby.
- **Play a Card**: `!play [card_name]` — Play a card from your hand.

### 2. Game Flow
Players take turns drawing cards and playing them on a 3x3 monster grid. The game ends when one player's health drops to 0.

### 3. Commands Overview:
- `!draw`: Draw a card from your deck.
- `!play [card_name]`: Play a card from your hand.
- `!attack [position]`: Attack a monster on the battlefield.
- `!endturn`: End your turn.

## Game Mechanics

### Monster Grid
The battlefield is a 3x3 grid where monsters are deployed:
- Each slot holds one monster.
- Monsters have attack and defense stats (e.g., 3/3 for 3 attack and 3 defense).

### Card Mechanics
Cards are central to the game and come in various types:
- **Monsters**: Summon creatures to the grid that can attack and defend.
- **Spells**: Cast spells that affect the battlefield or enemy creatures.
- Example card: **Fireball**:
    - The Fireball deals damage in a cross pattern:
    ```
    010
    121
    010
    ```
    - The player can choose the cast location, dealing damage to adjacent slots.

### Example Gameplay
- **Turn 1**: Player 1 casts a **Fireball** at position (1,1). The center of the Fireball hits the grid, dealing 2 damage, while adjacent positions take 1 damage.
- **Turn 2**: Player 2 summons a **Dragon** with 3/3 stats at position (2,2).

### RPG Features
The bot also includes RPG-like features that enhance the gameplay:
- **Deck Management**: Players can view and organize their deck of cards.
- **Dungeon Mode**: Players can enter dungeons, face monster challenges, and earn rare cards.
- **Store**: Purchase new cards and upgrades using in-game currency.
- **Blacksmith**: Upgrade existing cards with collected resources.
- **Market**: A trading system for players to exchange cards.

## Future Considerations
The project has a roadmap for future development:
- **Mana System**: Introduce mana costs for playing cards to add resource management.
- **More Card Effects**: Design complex damage patterns and unique card abilities.
- **Expanded Store**: Implement rarity systems for cards and player-to-player trading.
- **Multiplayer Modes**: Add more modes such as cooperative dungeons and player duels.

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue for discussion. Please ensure your code adheres to the style guide and is well-documented.

### Steps to Contribute:
1. Fork the repository.
2. Create a new branch for your feature or bugfix:
    ```bash
    git checkout -b feature/new-feature
    ```
3. Commit your changes:
    ```bash
    git commit -m "Add new feature"
    ```
4. Push to your forked repository and open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

---

Enjoy your adventure in the world of cards, and may you build the ultimate deck!