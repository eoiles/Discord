import asyncio
import discord
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from CardGame.battlefield import Battlefield
from CardGame.monster import Monster
from UI.playermenu import PlayerMenu
from UI.battlefield import Battlefield
from CardGame.game import Game

class DungeonMenu(discord.ui.View):
    def __init__(self, main_menu):
        super().__init__()
        self.main_menu = main_menu
        self.title = "Dungeon Menu"
        self.nbr = 0
        self.task = None  # Background task

        self.components=[]

        #placeholder for game
        self.game=None

        self.battlefield : Battlefield 
        self.player1menu :PlayerMenu
        self.player2menu :PlayerMenu

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
    async def map_name(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Start the counter task when the button is clicked
        pass
    
    
    #we start the game here
    @discord.ui.button(label='进入',emoji='<:LustThoughts:1210190946013024256>', style=discord.ButtonStyle.gray)
    async def start(self, interaction: discord.Interaction, button: discord.ui.Button):

        

        await interaction.response.edit_message(view=self)

        
        self.game = Game()


        self.game.load_level("1-1")



        self.battlefield = Battlefield(self.game,dungeon = self)
        self.battlefield_view = await interaction.channel.send(view=self.battlefield)

        self.player1menu = PlayerMenu(self.game,dungeon = self)
        self.player1menu_view = await interaction.channel.send(view=self.player1menu)

        self.player2menu = PlayerMenu(self.game,dungeon = self)
        self.player2menu_view = await interaction.channel.send(view=self.player2menu)

        self.components.extend([self.battlefield,self.player1menu,self.player2menu])






        
        

