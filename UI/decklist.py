import asyncio
import discord

from player_profile.player_profile_manager import PlayerProfileManager

from CardGame.card import Card

async def show_deck(interaction: discord.Interaction):
    # Logic for showing the deck
    await interaction.response.edit_message(content="Displaying Deck", view=Decklist())



class Decklist(discord.ui.View):
    def __init__(self):
        super().__init__()
        
        # Add initial buttons (View Deck, Edit Deck, Back to Main Menu)
        self.view_deck_button = discord.ui.Button(label="查看卡组", style=discord.ButtonStyle.primary, custom_id="view_deck")
        self.view_deck_button.callback = self.view_deck
        self.add_item(self.view_deck_button)

        self.edit_deck_button = discord.ui.Button(label="Edit Deck", style=discord.ButtonStyle.primary, custom_id="edit_deck")
        self.add_item(self.edit_deck_button)

        self.back_button = discord.ui.Button(label="返回主菜单", style=discord.ButtonStyle.secondary)
        self.back_button.callback = self.back_to_main_menu
        self.add_item(self.back_button)

        self.ephemeral_message_ids = {}  # Store message IDs by user

    async def view_deck(self, interaction: discord.Interaction):
        """
        Display the player's deck with buttons for each card, and a "Back" button to return to the previous menu.
        """
        player_name = "player1"
        player = PlayerProfileManager.load_profile(player_name)

        # Create a button for each card in the player's deck
        buttons = []
        for card in player.deck:
            card_button = discord.ui.Button(
                label=card.name,
                emoji=card.emoji,
                style=discord.ButtonStyle.primary,
                custom_id=f"card_{card.card_id}"
            )
            card_button.callback = lambda interaction, card=card: self.show_card_details(interaction, card)
            buttons.append(card_button)

        # Create a new view with the deck buttons
        deck_view = discord.ui.View()

        for button in buttons:
            deck_view.add_item(button)

        # Add a "Back" button to the deck view to return to the initial menu
        back_to_decklist_button = discord.ui.Button(label="返回卡组", style=discord.ButtonStyle.secondary)
        back_to_decklist_button.callback = self.back_to_decklist
        deck_view.add_item(back_to_decklist_button)

        # Update the message with the deck buttons
        await interaction.response.edit_message(content="Here is your deck:", view=deck_view)

    async def back_to_decklist(self, interaction: discord.Interaction):
        """
        Restore the initial decklist view (with 'View Deck' and 'Edit Deck' buttons).
        """
        # Create a new view with the initial buttons
        await interaction.response.edit_message(content="Decklist Menu", view=self)

    async def back_to_main_menu(self, interaction: discord.Interaction):
        """
        Navigate back to the main menu.
        """
        await interaction.response.edit_message(content="Main Menu", view=None)

    '''
        When a card button is clicked, display the card details.
        Use ephemeral messages to show card details, visible only to the user.
        Only one ephemeral message will be used for displaying the card details.
    '''
    
    async def show_card_details(self, interaction: discord.Interaction, card: Card):
        """
        Display the card details in an ephemeral message, editing the previous message if it exists.
        """
        content = f"{card.emoji} {card.name}\n{card.description}"

        # Check if interaction is done or defer it
        if not interaction.response.is_done():
            await interaction.response.defer(ephemeral=True)

        user_id = interaction.user.id  # Get the user's ID

        # If this is the first time for this user, send a new ephemeral message
        if user_id not in self.ephemeral_message_ids:
            message = await interaction.followup.send(
                content=content,
                ephemeral=True  # Makes the message visible only to the user
            )
            if message:  # Make sure message is not None
                self.ephemeral_message_ids[user_id] = message.id  # Store the message ID for this user
        else:
            # Edit the existing ephemeral message for this user
            await interaction.followup.edit_message(
                message_id=self.ephemeral_message_ids[user_id],
                content=content
            )