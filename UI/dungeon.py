import asyncio
import discord

class DungeonMenu(discord.ui.View):
    def __init__(self, main_menu):
        super().__init__()
        self.main_menu = main_menu
        self.title = "Dungeon Menu"
        self.nbr = 0
        self.task = None  # Background task

        self.components=[]

        # Add a "Back to Main" button
        back_button = discord.ui.Button(label="返回主菜单", style=discord.ButtonStyle.secondary)
        back_button.callback = self.back_to_main_menu  # Set callback to back_to_main_menu
        self.add_item(back_button)  # Add the button to the view

    async def back_to_main_menu(self, interaction: discord.Interaction):

        await asyncio.gather(
        interaction.response.edit_message(content="Main Menu", view=self.main_menu),
        *(msg.delete() for msg in self.components)
    )
        
        



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

        msg1 = await interaction.channel.send(view=monstergrid)
        msg2 = await interaction.channel.send(view=cardlist)
        msg3 = await interaction.channel.send(view=carddetail)
        msg4 = await interaction.channel.send(view=submenu)

        self.components.extend([msg1, msg2, msg3, msg4])


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