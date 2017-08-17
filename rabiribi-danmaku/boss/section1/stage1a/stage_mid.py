import pygame
import math

import objects.sprites
import functions
import functions.stage_run
import functions.values
import functions.buff_debuff
import random

from functions.buff_debuff import *
from random import random
from math import pi
from objects.elf import *
from objects.danmaku import mid_orange_circle

class elf_1(elf_blue_small):
    def attack_normal(self, erina, birth_layer, elf_layer, danmaku_layer):
        if 60 <= self.timer <= 100:
            if not self.timer%10:
                mid_orange_circle(
                    birth_layer, self, Ponised(time=800),
                    birth_time = 2,
                    danmaku_layer = 1,
                    direction = erina,
                    birth_speed = 5.0,
                    speedtime = (30,),
                    speedvalue = (2.0,)
                )


class Stage1aMidBattle(functions.stage_run.MidBattle):
    """
    stage1a battle
    stage boss: cocoa
    mid boss: none
    bgm: adventrue start here
    """
    def __init__(self, danmaku_layer_count, *mid_boss, **kwargs):
        self.SetBGM("data/bgm/rbs1s1am.ogg")
        super().__init__(danmaku_layer_count, *mid_boss, **kwargs)
        #self.stage_time = 5400

    def MidAttack(self, *args, **kwargs):
        for e in self.elf_layer:
            e.attack(self.difficulty, self.erina, self.birth_layer, self.elf_layer, self.danmaku_layer)
        if 60 <= self.timer <= 300:
            if not self.timer%30:
                elf_1(self.elf_layer,
                    birth_place = (40+random()*20, -30),
                    birth_direction = pi/2,
                    birth_speed = 1,
                    directiontime = (120, 300),
                    directionvalue = ([-pi/360,0], 0)
                )
        elif self.timer == 940:
            self.bgm.fadeout(1000)
        elif self.timer == 1000:
            self.part_run = False