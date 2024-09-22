from io import BytesIO
import re
import discord
import requests


class PlayerMenu(discord.ui.View):
    def __init__(self):
        super().__init__()

        self.user = None
        self.guild = None

        # Button for showing the user's avatar
        self.user_portrait = discord.ui.Button(
            label="玩家信息",
            style=discord.ButtonStyle.secondary
        )
        self.user_portrait.callback = self.show_avatar
        self.add_item(self.user_portrait)

    async def show_avatar(self, interaction: discord.Interaction):
        """Handle the button click and show the user's avatar as a custom emoji."""

        # Defer the interaction to give yourself more time
        await interaction.response.defer()  # This sends an "acknowledgment" response

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
        self.user_portrait.label = f"{self.user.name}'s Avatar"

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

    async def toggle_color(self, interaction: discord.Interaction):
        custom_id = interaction.data['custom_id']
        original_button = next((button for button in self.buttons if button.custom_id == custom_id), None)
        
        if original_button:
            if original_button.style == discord.ButtonStyle.grey:
                original_button.style = discord.ButtonStyle.blurple
            else:
                original_button.style = discord.ButtonStyle.grey
        else:
            print("Button not found")
        
        await interaction.response.edit_message(view=self)