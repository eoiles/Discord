'''
This is the class that construct the ui of the discord bot
divided in few sub classes, each handle a specific part of the ui
this class work as a data store all the ui infomation that need to be displayed
It can be both interpreted by the display.py or the discord bot
When passed to the display.py, it will be printed to the terminal.
When passed to the discord bot, it will be sent to the discord channel.


TitleBar
Location, Time(180 seconds)

Battlefield
1,1  1,2  1,3
2,1  2,2  2,3
3,1  3,2  3,3

Hands
Card1 Card2 Card3

CardDetail
Display the selected card, updated when detail button is clicked.

PlayerMenu
player1 hp mana detail ready
player2 hp mana detail ready
and so on
'''

