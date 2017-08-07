from ui.option import Option
from ui.option import OptionGroup

###

""" main menu """
# 220 640 start option
mainmenuoptions = (
    'start', 
    'extra_start',
    'practice_start',  # maybe minigames
    'spell_practice',  # maybe useless
    'play_data',
    'replay',
    'music_room',
    'options',
    'manual',
    'quit'
    )
opts = map(
    lambda x: Option(
        x, 
        mainmenuoptions.index(x)+1, 
        (640,220+mainmenuoptions.index(x)*20), 
        (400,220*mainmenuoptions.index(x)*20), 
        (640,220+mainmenuoptions.index(x)*20), 
        2),
    mainmenuoptions
    )
mainmenu = OptionGroup(*opts)

""" ========= """