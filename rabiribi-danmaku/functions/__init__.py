import math
import random
import os

from math import *
from random import *

def snipe(origin_sprite, enemy_sprite):
    """
    snipe function here:
    snipe(Sprite, Sprite)
    it return a rad number
    """
    delta_x = enemy_sprite.center[0] - origin_sprite.center[0]
    delta_y = enemy_sprite.center[1] - origin_sprite.center[1]
    distance = sqrt(delta_x ** 2 + delta_y ** 2)
    temp_snipe = asin(delta_y/distance)
    if delta_x < 0:
        if delta_y > 0:
            snipe = pi - temp_snipe
        elif delta_y < 0:
            snipe = -pi - temp_snipe
    else:
        snipe = temp_snipe
    return snipe

def clear_cache(*dir):
    for each in dir:
        pass
    
"""
some local static number here.
"""
# screen range:
SCREEN_LEFT = 35
SCREEN_RIGHT = 415
SCREEN_TOP = 15
SCREEN_BOTTOM = 465

# default key:
MOVE_LEFT = 'K_LEFT'
MOVE_RIGHT = 'K_RIGHT'
MOVE_UP = 'K_UP'
MOVE_DOWN = 'K_DOWN'

MOVE_SLOW = 'L_SHIFT'
SHOUTING = 'K_z'
AMULET = 'K_x'
BOOST = 'K_c'

SWITCH_MAGIC_LEFT = 'K_a'
SWITCH_MAGIC_RIGHT = 'K_s'