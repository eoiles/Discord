

from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from UI.dungeon import DungeonMenu

import discord

from CardGame.game import Game
from CardGame.monster import Monster

class Battlefield(discord.ui.View):
    def __init__(self, game: Game,dungeon : DungeonMenu):
        super().__init__()

        self.buttons = []

        self.game=game

        self.dungeon = dungeon
        self.selected_monster_button :MonsterButton
        
        self.battlefield = game.battlefield




        for y in range(self.battlefield.y_size):
            for x in range(self.battlefield.x_size):
                monster = self.battlefield.grid[y][x]

                #if there is monster draw monster
                if monster:

                    print(monster,Monster)
                    assert isinstance(monster, Monster)
                    if not monster.is_alive():


                        emoji='<:transparent:1286823572244922461>'

                        custom_id = f"{x}-{y}"
                        label = "．x．"

                        button = MonsterButton(monster=monster, 
                                               label=label, 
                                               emoji=emoji, 
                                               style=discord.ButtonStyle.grey, 
                                               custom_id=custom_id, 
                                               row=y)

                    else:
                        emoji = monster.emoji
                        
                        custom_id = f"{x}-{y}"

                        def to_fullwidth(number: int) -> str:
                            translation_table = str.maketrans("0123456789", "０１２３４５６７８９")
                            return str(number).translate(translation_table)

                        # Example usage in your code
                        label = f"{to_fullwidth(monster.attack)}|{to_fullwidth(monster.hp)}"

                        button = MonsterButton(monster=monster, 
                                               label=label, 
                                               emoji=emoji, 
                                               style=discord.ButtonStyle.red, 
                                               custom_id=custom_id, 
                                               row=y)
                #magic:"ᅠᅠᅠ"
                #if no monster keep grid :
                elif monster is None:
                    emoji='<:transparent:1286823572244922461>'

                    custom_id = f"{x}-{y}"
                    label = "．.．"

                    button = MonsterButton(monster=monster, 
                                           label=label, 
                                           emoji=emoji, 
                                           style=discord.ButtonStyle.grey, 
                                           custom_id=custom_id, 
                                           row=y)

                
                self.add_item(button)
                self.buttons.append(button)

    async def update(self,message: discord.Message):

        for y in range(self.battlefield.y_size):
            for x in range(self.battlefield.x_size):
                monster = self.battlefield.grid[y][x]
                button = self.buttons[y * self.battlefield.x_size + x]


                def to_fullwidth(number: int) -> str:
                    translation_table = str.maketrans("0123456789", "０１２３４５６７８９")
                    return str(number).translate(translation_table)

                if monster:
                    if not monster.is_alive():
                        emoji = '<:transparent:1286823572244922461>'
                        label = '．x．'
                        style = discord.ButtonStyle.grey
                    else:
                        emoji = monster.emoji
                        label = f"{to_fullwidth(monster.attack)}|{to_fullwidth(monster.hp)}"
                        style = discord.ButtonStyle.red
                else:
                    emoji = '<:transparent:1286823572244922461>'
                    label = '．.．'
                    style = discord.ButtonStyle.grey

                button.monster = monster
                button.emoji = emoji
                button.label = label
                button.style = style

        await message.edit(view=self)



class MonsterButton(discord.ui.Button):
    def __init__(self, monster, **kwargs):
        custom_id = kwargs.get('custom_id')
        super().__init__(**kwargs)
        self.monster = monster
        self.base_style = kwargs.get('style', discord.ButtonStyle.gray)
        self.selected = False


        #translate 0 based to 1 based index
        self.position = tuple(map(lambda x: int(x) + 1, custom_id.split('-')))

        self.callback = self.on_monster_pressed

    async def on_monster_pressed(self, interaction: discord.Interaction):
        # Reset other MonsterButtons in the parent view
        for item in self.view.children:
            if isinstance(item, MonsterButton) and item != self:
                item.selected = False
                item.style = item.base_style

        # Toggle the selected state of this MonsterButton
        self.selected = not self.selected

        if self.selected:
            self.style = discord.ButtonStyle.green
        else:
            self.style = self.base_style
        
        assert isinstance(self.view, Battlefield)
        self.view.selected_monster_button=self

        await interaction.response.edit_message(view=self.view)