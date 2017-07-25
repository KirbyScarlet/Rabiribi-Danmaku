"""
some local static value here.
"""
from pygame.locals import *

# Screen border
class screenborder:
    SCREEN_LEFT = 35
    SCREEN_RIGHT = 415
    SCREEN_TOP = 15
    SCREEN_BOTTOM = 465

    SCREEN_WIDTH = 380
    SCREEN_HEIGHT = 450

    SCREEN_CENTER_X = 225
    SCREEN_CENTER_Y = 240

    SCREEN_ITEM_LINE = 165

    SCREEN_CENTER = (225, 240)

    SCREEN_MID_TOP = (225, 15)
    SCREEN_MID_BOTTOM = (225, 465)
    SCREEN_MID_LEFT = (35, 240)
    SCREEN_MID_RIGHT = (415, 240)

    SCREEN_TOP_LEFT = (35, 15)
    SCREEN_TOP_RIGHT = (415, 15)
    SCREEN_BOTTOM_TOP = (35, 465)
    SCREEN_BOTTOM_RIGHT = (415, 465)

# Control keys default
class defaultkey:
    MOVE_LEFT = K_LEFT
    MOVE_RIGHT = K_RIGHT
    MOVE_UP = K_UP
    MOVE_DOWN = K_DOWN

    MOVE_SLOW = K_LSHIFT
    SHOUTING = K_z
    AMULET = K_x
    BOOST = K_c

    SWITCH_MAGIC_LEFT = K_a
    SWITCH_MAGIC_RIGHT = K_s

# Local difficulty
class difficulty:
    easy = 4
    normal = 8
    hard = 16
    hell = 32
    bunny = 64
    extra = 48

# damage type
class damagetype:
    # physical damage
    danmaku = 1
    # accident damage
    crash = 2
    # weapen damage
    amulet = 3
    cocoabomb = 4
    boost = 5
    # buff damage
    poison = 6
    freeze = 7
    burn = 8
    curse = 9
    reflect = 99
    endurance = -1
    instant = 4444