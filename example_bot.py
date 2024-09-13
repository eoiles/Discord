# This example requires the 'message_content' intent.

import discord # type: ignore

from discord.ext import commands # type: ignore


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

class MakeNumberChange(discord.ui.View):
    def __init__(self,inv:str):
        super().__init__()
        self.nbr = 0



    @discord.ui.button(label="add 1", style=discord.ButtonStyle.blurple)
    async def add1(self, interaction:discord.Interaction, button :discord.ui.Button):
        self.nbr+= 1

        self.nbrbtn.label=str(self.nbr)

        await interaction.response.edit_message(view=self)

    @discord.ui.button(label="0", style=discord.ButtonStyle.gray)
    async def nbrbtn(self, interaction: discord.Interaction, button: discord.ui.Button):
        pass  # This button is just for display and doesn't need to do anything
    
    @discord.ui.button(label="minus 1", style=discord.ButtonStyle.blurple)
    async def minus1(self, interaction:discord.Interaction, button :discord.ui.Button):
        self.nbr-= 1

        self.nbrbtn.label=str(self.nbr)

        await interaction.response.edit_message(view=self)

    @discord.ui.button(label='',emoji='<:LustThoughts:1210190946013024256>', style=discord.ButtonStyle.gray)
    async def img(self, interaction: discord.Interaction, button: discord.ui.Button):

        self.img.emoji="<:think:1204467342223081602>"

        

        await interaction.response.edit_message(view=self)

        monstergrid=MonsterGrid(3,3)
        cardlist=Cardlist(3,1)
        submenu=SubMenu(5,1)
        await interaction.channel.send(view=monstergrid)
        await interaction.channel.send(view=cardlist)
        await interaction.channel.send(view=submenu)


class MonsterGrid(discord.ui.View):
    def __init__(self, cols: int,rows:int):
        super().__init__()
        self.emojis = [
            "<:1_:1282725858724806727>",
            "<:2_:1282725868120051743>",
            "<:3_:1282725880468082749>",
            "<:4_:1282725886474453186>",
            "<:5_:1282725891956277279>",
            "<:6_:1282725896788115456>"
        ]

        self.buttons = []
        for y in range(rows):
            for x in range(cols):
                emoji = self.emojis[x % len(self.emojis)]
                custom_id = f"{x}-{y}"
                button = discord.ui.Button(label=f"{chr(0x1D7F6 + x)}|{chr(0x1D7F6 + y)}", emoji=emoji, style=discord.ButtonStyle.red, custom_id=custom_id, row=y)
                button.callback = self.toggle_color
                self.add_item(button)
                self.buttons.append(button)

    async def toggle_color(self, interaction: discord.Interaction):
        custom_id = interaction.data['custom_id']
        original_button = next((button for button in self.buttons if button.custom_id == custom_id), None)
        
        if original_button:
            if original_button.style == discord.ButtonStyle.red:
                original_button.style = discord.ButtonStyle.green
            else:
                original_button.style = discord.ButtonStyle.red
        else:
            print("Button not found")
        
        await interaction.response.edit_message(view=self)



class Cardlist(discord.ui.View):
    def __init__(self, cols: int,rows:int):
        super().__init__()
        self.emojis = [
            "<:1_:1282725858724806727>",
            "<:2_:1282725868120051743>",
            "<:3_:1282725880468082749>",
            "<:4_:1282725886474453186>",
            "<:5_:1282725891956277279>",
            "<:6_:1282725896788115456>"
        ]

        self.buttons = []
        for y in range(rows):
            for x in range(cols):
                emoji = self.emojis[x % len(self.emojis)]
                custom_id = f"{x}-{y}"
                button = discord.ui.Button(label=f"卡名", emoji=emoji, style=discord.ButtonStyle.grey, custom_id=custom_id, row=y)
                button.callback = self.toggle_color
                self.add_item(button)
                self.buttons.append(button)
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


class SubMenu(discord.ui.View):
    def __init__(self, cols: int,rows:int):
        super().__init__()
        self.emojis = [
            "<:1_:1282725858724806727>",
            "<:2_:1282725868120051743>",
            "<:3_:1282725880468082749>",
            "<:4_:1282725886474453186>",
            "<:5_:1282725891956277279>",
            "<:6_:1282725896788115456>"
        ]

        self.buttons = []
        for y in range(rows):
            for x in range(cols):
                emoji = self.emojis[x % len(self.emojis)]
                custom_id = f"{x}-{y}"
                button = discord.ui.Button(label=f"", emoji=emoji, style=discord.ButtonStyle.blurple, custom_id=custom_id, row=y)
                button.callback = self.toggle_color
                self.add_item(button)
                self.buttons.append(button)
        

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






@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        cngnbr=MakeNumberChange(str(123))
        
        await message.channel.send(view=cngnbr)
        


import logging

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# Assume client refers to a discord.Client subclass...



client.run('MTI4MjM3MDE4NjY2OTg1MDY5Nw.G35sZM.uQkuTQyiLnW5IvuovcnLI8UKHNOTyCyLpPXhrM',log_handler=handler,log_level=logging.DEBUG)
