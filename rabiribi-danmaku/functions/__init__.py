import pygame
import functions.buff_debuff
import functions.run
import functions.spell_card
import functions.sprites
import functions.values
from math import sqrt
from math import asin
from math import pi
from os import system
from os import remove
from sys import exit

def ExitCheck():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            functions.clear_cache()
            exit()

def snipe(origin_sprite, enemy_sprite):
    """
    snipe function here:

        snipe(Sprite, Sprite): return int

        return a rad value
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
    