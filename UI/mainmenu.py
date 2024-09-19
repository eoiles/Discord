import discord
from UI.dungeon import DungeonMenu

class MainMenu(discord.ui.View):
    def __init__(self):
        super().__init__()
        # Add buttons manually and link them to specific callbacks
        buttons = [
            discord.ui.Button(label="Deck", style=discord.ButtonStyle.primary, custom_id="deck",row=1),
            discord.ui.Button(label="Store", style=discord.ButtonStyle.primary, custom_id="store",row=1),
            discord.ui.Button(label="地下城", style=discord.ButtonStyle.primary, custom_id="dungeon",row=2),
            discord.ui.Button(label="Market", style=discord.ButtonStyle.primary, custom_id="market",row=2),
            discord.ui.Button(label="Blacksmith", style=discord.ButtonStyle.primary, custom_id="blacksmith",row=3),
            discord.ui.Button(label="Stats", style=discord.ButtonStyle.primary, custom_id="stats",row=3),
            discord.ui.Button(label="Exit", style=discord.ButtonStyle.danger, custom_id="exit"),
        ]

        for button in buttons:
            button.callback = self.handle_button_click  # Assign handle_button_click as the callback
            self.add_item(button)

    async def handle_button_click(self, interaction: discord.Interaction):
        custom_id = interaction.data['custom_id']
        print(f"Button clicked with custom_id: {custom_id}")

        # Handle button-specific logic
        if custom_id == "deck":
            await self.show_deck(interaction)
        elif custom_id == "store":
            await self.show_store(interaction)
        elif custom_id == "dungeon":
            await self.show_dungeon(interaction)
        # other button handling...

    async def show_deck(self, interaction: discord.Interaction):
        # Logic for showing the deck
        await interaction.response.send_message("Displaying Deck", ephemeral=True)

    async def show_store(self, interaction: discord.Interaction):
        # Logic for showing the store
        await interaction.response.send_message("Displaying Store", ephemeral=True)

    async def show_dungeon(self, interaction: discord.Interaction):
        dungeon_menu = DungeonMenu(main_menu=self)
        await interaction.response.edit_message(content="Dungeon Menu", view=dungeon_menu)

class SubMenu(discord.ui.View):
    def __init__(self, title: str, main_menu: MainMenu):
        super().__init__()
        self.title = title
        self.main_menu = main_menu
        back_button = discord.ui.Button(label="Back", style=discord.ButtonStyle.secondary, custom_id="back")
        back_button.callback = self.back_to_main_menu  # Assign the callback for the "Back" button
        self.add_item(back_button)

    async def back_to_main_menu(self, interaction: discord.Interaction):
        await interaction.response.edit_message(content="Main Menu", view=self.main_menu)