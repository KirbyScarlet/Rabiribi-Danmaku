"""
function tools
"""

__doc__ = ["debug_font", "me_erina", "me_ribbon", "ExitCheck",
           "snipe", "angle", "clear_cache"]

import pygame

debug_font = pygame.font.Font(None, 20)

'''
import character.erina
import character.ribbon

me_erina = character.erina.Erina()
me_ribbon = character.ribbon.Ribbon()
'''

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

class HP(object):
    """
    HP(max_hp): return HP

        HP.add(value)
        HP.sub(value)
        HP.full(value)
        HP.empty()
        HP.maxhp(value)
    """
    def __init__(self, maxhp):
        self.maxhp = maxhp
        self.hp = int(self.max_hp)

    def add(self, value):
        self.hp += value

    def sub(self, value):
        self.hp -= value

    def full(self, value):
        self.hp = int(self.maxhp)

    def empty(self, value):
        self.hp = 0

    def __setattr__(self, name, value):
        if name == 'hp':
            if value > self.maxhp:
                value = self.maxhp
        return super().__setattr__(name, value)

class MP(object):
    """
    MP(max_mp):

        MP.add(value)
        MP.sub(value)
        MP.full(value)
        MP.empty(value)
        MP.boost()
    """
    def __init__(self, max_mp):
        self.maxmp = max_mp
        self.mp = int(self.max_mp)

    def add(self, value):
        self.mp += value

    def sub(self, value):
        self.mp -= value

    def full(self, value):
        self.mp = int(self.maxmp)

    def empty(self, value):
        self.mp = 0

    def __setattr__(self, name, value):
        if name == 'mp':
            if value > self.maxhp:
                value = self.max_hp
        return super().__setattr__(name, value)

class ATK(object):
    """
    ?
    """
    # under development
    def __init__(self, sprite, atk):
        self.sprite = sprite
        self.atk = atk
        self.base_atk = atk

    def __setattr__(self, name, value):
        value = value.__int__()
        return super().__setattr__(name, value)

def vector(x, y):
    """
    vector(x, y): return float

        return a radian from a vector
    """
    d = sqrt(x**2 + y**2)
    v = asin(y/d)
    if x < 0:
        if y > 0:
            v = pi - v
        elif y < 0:
            v = -pi - v
        elif y == 0:
            v = pi
    elif x > 0:
        pass
    else:
        if y > 0:
           v = pi/2
        elif y < 0:
            v = -pi/2
    return v

def angle(vector1, vector2):
    """
    angle(vector1, vector2): return float

        return
    """
    if isinsance(vector1, float):
        v1 = vector1
    elif isinstance(vector1, (list, tuple)):
        v1 = vector(*vector1)
    if isinstance(vector2, float):
        v2 = vector2
    elif isinstance(vector2, (list, tuple)):
        v2 = vector(*vector2)
    v = v2 - v1
    while v < -pi:
        v += 2*pi
    while v >= pi:
        v -= 2*pi
    return v

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
    '''
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
    '''
    snipe = vector(delta_x, delta_y)
    if type == 'rad':
        return snipe
    elif type == 'vector':
        return [cos(snipe), sin(snipe)]
    else:
        print("parament error")
        raise TypeError

'''
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
'''

import time
def time_check(fun, *args, **kwargs):
    a = time.time()
    ret = fun(*args, **kwargs)
    print(fun.__name__, time.time()-a)
    return ret

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
            
import functions.action
import functions.values
import functions.spell_card
import functions.stage_run
import functions.buff_debuff
