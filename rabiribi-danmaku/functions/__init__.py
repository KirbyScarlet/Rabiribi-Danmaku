"""
function tools
"""
import functions.run
import functions.spell_card
import functions.values
import functions.stage_run
import functions.buff_debuff

__doc__ = ["debug_font", "me_erina", "me_ribbon", "ExitCheck",
           "snipe", "angle", "clear_cache"]

import pygame

debug_font = pygame.font.Font(None, 20)

import character.erina
import character.ribbon

me_erina = character.erina.Erina()
me_ribbon = character.ribbon.Ribbon()

import platform
from pygame.sprite import Sprite
from math import sqrt
from math import asin
from math import pi
from math import cos
from math import sin
from random import random
from os import system
from os import remove
from sys import exit

def ExitCheck():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            functions.clear_cache()
            exit()

class SnipeError(TypeError):
    pass

def snipe(origin, destination, type='rad'):
    """
    snipe function here:

        snipe(origin, destination, type='rad'): return int

        both parament can be a sprite or a direction
        type: 'rad' or 'vector'

        return a rad value
    """
    if isinstance(origin, (list, tuple)):
        origin_x = origin[0]
        origin_y = origin[1]
    elif isinstance(origin, Sprite):
        origin_x = origin.center[0]
        origin_y = origin.center[1]
    else:
        print("snipe parament error")
        raise TypeError
    if isinstance(destination, (list, tuple)):
        destination_x = destination[0]
        destination_y = destination[1]
    elif isinstance(destination, Sprite):
        destination_x = destination.center[0]
        destination_y = destination.center[1]
    else:
        print("snipe parament error")
        raise TypeError
    delta_x = destination_x - origin_x
    delta_y = destination_y - origin_y
    if delta_x==0 and delta_y==0:
        return random() * 2 * pi
        raise SnipeError
    distance = sqrt(delta_x ** 2 + delta_y ** 2)
    temp_snipe = asin(delta_y/distance)
    if delta_x < 0:
        if delta_y > 0:
            snipe = pi - temp_snipe
        elif delta_y < 0:
            snipe = -pi - temp_snipe
        elif delta_y == 0:
            snipe = pi
    elif delta_x == 0:
        if delta_y > 0:
            snipe = pi/2
        elif delta_y < 0:
            snipe = -pi/2
    else:
        snipe = temp_snipe
    if type == 'rad':
        return snipe
    elif type == 'vector':
        return [cos(snipe), sin(snipe)]
    else:
        print("parament error")
        raise TypeError

def angle(direction):
    """
    return rad of a direction:

        angle(direction): return int

        return a rad value
    """
    temp_rad = asin(direction[1])
    if direction[0] < 0:
        if direction[1] > 0:
            rad = pi - temp_rad
        elif direction[1] < 0:
            rad = -pi - temp_rad
    else:
        rad = temp_rad
    return rad

def clear_cache(*dir):
    if platform.system() == "Windows":
        if dir:
            for each in dir:
                ch = "del data\\tmp\\" + each + "\\*.tmp"
                system(ch)
        else:
            system("del data\\tmp\\bf\\*.tmp")
            system("del data\\tmp\\bg\\*.tmp")
            system("del data\\tmp\\imgs\\*.tmp")
            system("del data\\tmp\\mid\\*.tmp")
            system("del data\\tmp\\misc\\*.tmp")
    elif platform.system() == "Linux":
        if dir:
            for each in dir:
                ch = "rm data/tmp/" + each + "/*.tmp"
                system(ch)
        else:
            system("rm data/tmp/bf/*.tmp")
            system("rm data/tmp/bg/*.tmp")
            system("rm data/tmp/imgs/*.tmp")
            system("rm data/tmp/mid/*.tmp")
            system("rm data/tmp/misc/*.tmp")
            