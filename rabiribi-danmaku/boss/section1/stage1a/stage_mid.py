import pygame
import math

import objects.sprites
import functions
import functions.stage_run
import functions.values
import functions.buff_debuff

from math import pi
from objects.elf import *

class elf_1(elf_blue_small):
    def attack_normal(self, difficulty, erina, brith_group, elf_group, danmaku_group):
        if 60 < self.timer < 64:
            mid_orange_circle(
                birth_group, self.center,
                birth_time = 2,
                danmaku_layer = 1,
                direction = erina,
            )


class Stage1aMidBattle(functions.stage_run.MidBattle):
    """
    stage1a battle
    stage boss: cocoa
    mid boss: none
    bgm: adventrue start here
    """
    def __init__(self, erina, ribbon, difficulty, danmaku_layer_count, *mid_boss, **kwargs):
        self.setBGM("data/bgm/rbs1s1a.ogg")
        super().__init__(erina, ribbon, difficulty, danmaku_layer_count, *mid_boss, **kwargs)
        #self.stage_time = 5400

    def MidAttack(self, *args, **kwargs):
        if time == 420:
            elf_1(self.elf_layer,
                birth_place = (40, -30),
                birth_direction = pi/2,
                birth_speed = 2,
                directiontime = (1, 60),
                directionvalue = ([-pi/120,0], 0)
                )
        elif time == 422:
            elf_1(self.elf_layer,
                  birth_place = (240, -30),
                  birth_direction = pi/2,
                  birth_speed = 2,
                  directiontime = (1,60),
                  directionvalue = ([pi/120, 0], 0)
                  )

