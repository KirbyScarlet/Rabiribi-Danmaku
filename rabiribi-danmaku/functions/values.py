"""
some local static number here.
"""
import pygame.locals
# Screen border
class screenborder:
    SCREEN_LEFT = 35
    SCREEN_RIGHT = 415
    SCREEN_TOP = 15
    SCREEN_BOTTOM = 465

    SCREEN_CENTER_X = 225
    SCREEN_CENTER_Y = 240

    SCREEN_ITEM_LINE = 165

    SCREEN_CENTER = [225, 240]

    SCREEN_MID_TOP = [225, 15]
    SCREEN_MID_BOTTOM = [225, 465]
    SCREEN_MID_LEFT = [35, 240]
    SCREEN_MID_RIGHT = [415, 240]

    SCREEN_TOP_LEFT = [35, 15]
    SCREEN_TOP_RIGHT = [415, 15]
    SCREEN_BOTTOM_TOP = [35, 465]
    SCREEN_BOTTOM_RIGHT = [415, 465]

# Control
class keycontrol:
    MOVE_LEFT = K_LEFT
    MOVE_RIGHT = K_RIGHT
    MOVE_UP = K_UP
    MOVE_DOWN = K_DOWN

    MOVE_SLOW = L_SHIFT
    SHOUTING = K_z
    AMULET = K_x
    BOOST = K_c

    SWITCH_MAGIC_LEFT = K_a
    SWITCH_MAGIC_RIGHT = K_s

# Local difficulty
class difficulty:
    easy = 'easy'
    normal = 'normal'
    hard = 'hard'
    hell = 'hell'
    bunny = 'bunny'
    extra = 'extra'