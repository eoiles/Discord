# This example requires the 'message_content' intent.

import asyncio

import discord # type: ignore

from discord.ext import commands # type: ignore
from discord.ext import tasks


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

class MakeNumberChange(discord.ui.View):
    def __init__(self,inv:str):
        super().__init__()
        self.nbr = 0
        self.task = None  # Background task

    @discord.ui.button(label="Start Counter", style=discord.ButtonStyle.gray)
    async def start_counter(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Start the counter task when the button is clicked
        print(f"Type of interaction: {type(interaction)}")
        if self.task is None or self.task.done():
            self.task = asyncio.create_task(self.update_counter(interaction, button))

        #i need to resonse the interaction otherwise discord will think no response is an error
        await interaction.response.defer()

    async def update_counter(self, interaction: discord.Interaction, button: discord.ui.Button):
        for i in range(1000):
            await asyncio.sleep(1)  # Wait 1 second
            self.nbr += 1
            button.label = str(self.nbr)
            await interaction.message.edit(view=self)  # Edit the message with the updated button


    @discord.ui.button(label="幽暗森林", style=discord.ButtonStyle.gray)
    async def start_counter(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Start the counter task when the button is clicked
        pass
    

    @discord.ui.button(label='进入',emoji='<:LustThoughts:1210190946013024256>', style=discord.ButtonStyle.gray)
    async def img(self, interaction: discord.Interaction, button: discord.ui.Button):

        self.img.emoji="<:think:1204467342223081602>"

        

        await interaction.response.edit_message(view=self)

        monstergrid=Battlefield(3,3)
        cardlist=Cardlist(3,1)
        carddetail = CardDetail() 
        submenu=SubMenu(5,1)
        await interaction.channel.send(view=monstergrid)
        await interaction.channel.send(view=cardlist)
        await interaction.channel.send(view=carddetail)
        await interaction.channel.send(view=submenu)


class Battlefield(discord.ui.View):
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
                button = discord.ui.Button(label=f"卡名{x}", emoji=emoji, style=discord.ButtonStyle.grey, custom_id=custom_id, row=y)
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


class CardDetail(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.button=discord.ui.Button(label=f"火球术在命中目标后会产生爆炸,影响范围内的所有敌人", emoji= "<:6_:1282725896788115456>", style=discord.ButtonStyle.grey, custom_id='custom_id')

        self.add_item(self.button)
        
        
        

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
