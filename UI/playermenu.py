from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from UI.dungeon import DungeonMenu


from io import BytesIO
import re
import discord
import requests
from CardGame.game import Game
from player_profile.player_profile_manager import PlayerProfileManager
from CardGame.player import Player
import asyncio
from CardGame.card import Card
import random




class CardButton(discord.ui.Button):
    def __init__(self,card, **kwargs):
        super().__init__(**kwargs)
        self.selected = False  # Custom attribute

        self.card=card

        self.callback = self.on_card_pressed


    async def on_card_pressed(self, interaction: discord.Interaction):
        """Handle the button click and show the card details."""
        
        # Set this button to selected and change its style
        self.selected = True
        self.style = discord.ButtonStyle.green  # Change to green

        # Reset other buttons in the parent view
        #only 1,2,3 is card button, 0 is player por
        for item in self.view.children[1:4]:
            if isinstance(item, CardButton) and item != self:
                item.selected = False
                self.view.selected_card_button = self
                item.style = discord.ButtonStyle.blurple  # Change back to blue

        # Update the view

        await self.show_card_details(interaction)

        await interaction.message.edit(view=self.view)

        



    async def show_card_details(self, interaction: discord.Interaction):
        """
        Display the card details in an ephemeral message, editing the previous message if it exists.
        """
        content = f"{self.card.emoji} {self.card.name}\n{self.card.description}"
        

        # Check if interaction is done or defer it
        if not interaction.response.is_done():
            await interaction.response.defer(ephemeral=True)

        user_id = interaction.user.id  # Get the user's ID

        # If this is the first time for this user, send a new ephemeral message
        if user_id not in self.view.ephemeral_message_ids:
            message = await interaction.followup.send(
                content=content,
                ephemeral=True  # Makes the message visible only to the user
            )
            if message:  # Make sure message is not None
                self.view.ephemeral_message_ids[user_id] = message.id  # Store the message ID for this user
        else:
            # Edit the existing ephemeral message for this user
            await interaction.followup.edit_message(
                message_id=self.view.ephemeral_message_ids[user_id],
                content=content
            )



class PlayerMenu(discord.ui.View):
    
    def __init__(self,game: Game,dungeon : 'DungeonMenu'):
        
        super().__init__()

        self.dungeon = dungeon

        self.ephemeral_message_ids = {}  # Store message IDs by user

        self.user = None
        self.guild = None

        self.game = game

        self.selected_card_button : CardButton

        # Button for showing the user's avatar
        self.user_portrait = discord.ui.Button(
            label="加入",
            style=discord.ButtonStyle.secondary,
            row=2
        )
        self.user_portrait.callback = self.join_game
        self.add_item(self.user_portrait)


    #the place for 3 cards of player hand
    async def card_buttons(self, x:int):
        return self.children[x]



    async def join_game(self, interaction: discord.Interaction):
        """Join the game and show the user's avatar and hp and mana and ready button."""

        
        self.user_portrait.label = "Loading..."
        await interaction.response.edit_message(view=self)

        player = PlayerProfileManager.load_profile('Player1')
        assert isinstance(player, Player)

        self.game.add_player(player)
        self.game.start()

        # Create tasks for the two coroutines
        hand = asyncio.create_task(self.show_player_hand(player, interaction))
        avatar = asyncio.create_task(self.show_avatar(interaction))
        status = asyncio.create_task(self.show_player_status(player, interaction))

        # Run the tasks in parallel
        await asyncio.gather(hand, avatar,status)

    #display the hp and ready button.
    async def show_player_status(self, player: Player, interaction: discord.Interaction):
        """Display the player's HP and the "Ready" button."""

        # Create the HP label
        hp_label = discord.ui.Button(label=f"HP: {player.hp}", 
                                     disabled=True,
                                     style=discord.ButtonStyle.grey,
                                     row=2)
        self.add_item(hp_label)

        # Create the "Ready" label
        ready_label = discord.ui.Button(label="准备", 
                                        style=discord.ButtonStyle.primary,
                                        row=2)
        ready_label.callback = self.on_ready

        self.add_item(ready_label)

        # Edit the original message with the updated view
        await interaction.message.edit(view=self)

    
    async def on_ready(self, interaction: discord.Interaction):
        """Handle the "Ready" button click.
            Check and get selected card and selected monster.
            add to game action queue.
            then resolve.
        """

        monster_button =self.dungeon.battlefield.selected_monster_button
        card_button =self.selected_card_button
        
        if monster_button and card_button:
            position = monster_button.position
            card = card_button.card

            self.game.add_player_action(self.user, card, *position)

            self.game.next_turn()

            await self.dungeon.battlefield.update(self.dungeon.battlefield_view)

        

        await interaction.response.edit_message(view=self)


    
    async def show_player_hand(self, player: Player, interaction: discord.Interaction):
        """Load player.hand and display as up to 4 buttons."""


        hand = player.hand

        if len(hand) == 0:
            await interaction.response.send_message("No cards in hand.")
            return

        # Update or add buttons
        for i in range(1,4):
            if i <= 3:
                if i <= len(hand):
                    card = hand[i - 1]
                    if i < len(self.children):
                        #the 0 index button is player portrait, do not modify it
                        # the 1 2 3 index button is the card button
                        button = self.children[i]
                        button.label = f"{card.name}{random.randint(1, 3)}"
                        button.emoji = card.emoji
                    else:
                        
                        #use modified button class

                        button = CardButton(
                            card=card,
                            style=discord.ButtonStyle.primary,
                            label= f"{card.name}{random.randint(1, 3)}",
                            emoji=card.emoji,
                            row=(i - 1) // 3 + 1
                        )


                        self.add_item(button)


        await interaction.message.edit(view=self)

    async def show_avatar(self, interaction: discord.Interaction):
        """Handle the button click and show the user's avatar as a custom emoji."""



        self.user = interaction.user
        self.guild = interaction.guild


        avatar_data = await self.download_avatar()
        if not avatar_data:
            await interaction.response.send_message("Failed to download avatar.")
            return

        # Use a fixed name for the emoji
        emoji_name = "player1portrait"

        # Check if an emoji with this name already exists and delete it
        existing_emoji = discord.utils.get(self.guild.emojis, name=emoji_name)
        if existing_emoji:
            try:
                await existing_emoji.delete(reason="Updating player portrait")
            except discord.HTTPException as e:
                await interaction.response.send_message(f"Failed to delete existing emoji: {e}")
                return

        # Upload the new emoji
        new_emoji = await self.upload_custom_emoji(avatar_data, name=emoji_name)
        if not new_emoji:
            await interaction.response.send_message("Failed to upload avatar as emoji.")
            return

        # Update the button label and emoji
        self.user_portrait.label = f"{self.user.name}"

        self.user_portrait.emoji = new_emoji

        # Update the interaction message to reflect changes
        await interaction.message.edit(view=self)

    async def download_avatar(self):
        """Download the user's avatar and return it as a BytesIO object."""
        avatar_url = str(self.user.avatar.url)
        response = requests.get(avatar_url)
        if response.status_code == 200:
            return BytesIO(response.content)
        return None

    async def upload_custom_emoji(self, image_data: BytesIO, name: str):
        """Upload the user's avatar as a custom emoji in the guild."""
        try:
            emoji = await self.guild.create_custom_emoji(name=name, image=image_data.getvalue())
            return emoji
        except discord.HTTPException as e:
            print(f"Failed to upload emoji: {e}")
            return None
