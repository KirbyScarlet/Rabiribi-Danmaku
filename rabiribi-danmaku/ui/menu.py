from ui.option import Option
from ui.option import OptionGroup
from functions.stage_run import Menu

###
"""
##main_menu
  │
  ├── start
  │   ├── section1
  │   │   ├── casual
  │   │   ├── novice
  │   │   ├── normal
  │   │   ├── hard
  │   │   ├── hell
  │   │   ├── bunny exclusion   [clear hell]
  │   │   └── impossible        [clear bunny exclusion]
  │   └── section2 
  │       ├── casual            [clear at least section1 casual]
  │       ├── novice            [clear at least section1 novice]
  │       ├── normal            [clear at least section1 normal]
  │       ├── hard              [clear at least section1 hard]
  │       ├── hell              [clear section1 hell]
  │       ├── bunny exclusion   [clear section1 bunny exclusion hell]
  │       └── impossible        [clear all]
  ├── extra start
  │   └── extra    [clear at least normal section1]
  ├── practice start  [under development]
  │   ├── casual
  │   ├── novice
  │   ├── normal
  │   ├── hard
  │   ├── hell
  │   ├── bunny exclusion
  │   │   ├── section1
  │   │   │   ├── stage1a (cocoa)
  │   │   │   ├── stage1b (ashiri)
  │   │   │   ├── stage2a (kotri green)
  │   │   │   ├── stage2b (pandora)
  │   │   │   ├── stage3a (rita)
  │   │   │   ├── stage3b (cocoa 2)
  │   │   │   ├── stage4a (nieve, nixie)
  │   │   │   ├── stage4b (vanilla, chocolate)
  │   │   │   ├── stage5 (miru)
  │   │   │   └── stage6 (noah)
  │   │   └── section2
  │   │       ├── stage cicini
  │   │       ├── stage syaro
  │   │       ├── stage seana 1
  │   │       ├── stage seana 2
  │   │       ├── stage ashiri 2
  │   │       ├── stage rita illustration
  │   │       ├── stage pandora illustration
  │   │       ├── stage aruraune
  │   │       ├── stage lilith
  │   │       ├── stage saya  [all member(except irisu) clear before exist]
  │   │       ├── stage kotri red (stage4)
  │   │       ├── stage miriam (stage5)
  │   │       └── stage rumi (stage6)
  │   └── impossible
  ├── mini game
  │   ├── ribbon attack
  │   ├── vanilla and chocolate's helloween
  │   ├── uprprc members attack 1
  │   ├── ...
  │   ├── uprprc members attack 7
  │   ├── lilith' costum
  │   ├── lili attack
  │   ├── bixie attack
  │   ├── cicini's inventions
  │   ├── uprprc girl
  │   └── ... under development
  ├── play data
  │   ├── high score
  │   ├── spell card collected
  │   ├── items collected
  │   ├── ... under development
  │   └── buff and debuff collected
  ├── replay
  ├── music room
  │   ├── music 01
  │   ├── ...
  │   └── music 48
  ├── options
  │   ├── defalut hp   [slider 50 ~ 200]
  │   ├── graphic
  │   │   ├── 16bit
  │   │   └── 32bit
  │   ├── bgm
  │   │   ├── off
  │   │   ├── wav
  │   │   ├── midi
  │   │   └── volume
  │   ├── sound
  │   │   └── volume
  │   ├── mode
  │   │   ├── fullscreen
  │   │   └── window
  │   │       ├── 640*480
  │   │       ├── 960*720
  │   │       └── 1280*960
  │   ├── slow mode [off or on]
  │   ├── reset
  │   └── keyconfig
  │       ├── shouting             [default 'z']
  │       ├── amulet               [default 'x']
  │       ├── boost                [default 'c']
  │       ├── switch magic left    [default 'a']
  │       ├── switch magic right   [default 's']
  │       ├── move slow            [default 'left shift']
  │       ├── move up              [default 'KEY_UP']
  │       ├── move down            [default 'KEY_DOWN']
  │       ├── move left            [default 'KEY_LEFT']
  │       ├── move right           [default 'KEY_RIGHT']
  │       ├── reset
  │       └── key config quit
  ├── manual
  │   ├── story
  │   ├── character introduction
  │   ├── ... under development
  │   └── how to rabi
  └── quit
"""
###

""" main menu """
# 220 640 start option
main_menu = OptionGroup('main_menu')
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
        (400,220+mainmenuoptions.index(x)*20), 
        (420,220+mainmenuoptions.index(x)*20), 
        2,10),
    mainmenuoptions
    )
main_menu.add(*opts)
""" ========= """

menu = Menu(main_menu)