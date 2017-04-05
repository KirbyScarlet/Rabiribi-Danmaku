import pygame
import functions.buff_debuff
import functions.run
import functions.spell_card
import functions.sprites
import functions.values
import functions.stage_run
from math import sqrt
from math import asin
from math import pi
from os import system
from os import remove
from sys import exit

debug_font = pygame.font.Font(None, 20)

def ExitCheck():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
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
    