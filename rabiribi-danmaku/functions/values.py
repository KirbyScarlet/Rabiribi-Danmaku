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

    @classmethod
    def direction(cls):
        return (cls.MOVE_LEFT, cls.MOVE_RIGHT, cls.MOVE_UP, cls.MOVE_DOWN)

    @classmethod
    def settingkey(cls):
        pass

    @classmethod
    def __contains__(cls, name):
        return name in tuple(cls.__dict__.values())

    @classmethod
    def filter(cls, keys):
        return {
                cls.MOVE_LEFT: keys[cls.MOVE_LEFT],
                cls.MOVE_RIGHT: keys[cls.MOVE_RIGHT],
                cls.MOVE_UP: keys[cls.MOVE_UP],
                cls.MOVE_DOWN: keys[cls.MOVE_DOWN],
                cls.MOVE_SLOW: keys[cls.MOVE_SLOW],
                cls.SHOUTING: keys[cls.SHOUTING],
                cls.AMULET: keys[cls.AMULET],
                cls.BOOST: keys[cls.BOOST],
                cls.SWITCH_MAGIC_LEFT: keys[cls.SWITCH_MAGIC_LEFT],
                cls.SWITCH_MAGIC_RIGHT: keys[cls.SWITCH_MAGIC_RIGHT]
                }

# Local difficulty
class difficulty:
    EASY = 4
    NORMAL = 8
    HARD = 16
    HELL = 32
    BUNNY = 64
    EXTRA = 48

# damage type
class damagetype:
    # physical damage
    DANMAKU = 1
    # accident damage
    CRASH = 2
    # weapen damage
    AMULET = 3
    COCOABOMB = 4
    BOOST = 5
    # buff damage
    POISON = 6
    FREEZE = 7
    BURN = 8
    CURSE = 9
    REFLECT = 99
    # special buff damage
    ENDURANCE = -1
    INSTANT = 4444

class pausetypes: 
    NEUTRAL = 0
    PAUSING = 1
    UNPAUSING = -1