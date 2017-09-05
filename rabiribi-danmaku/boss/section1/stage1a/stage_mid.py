import pygame
import math

import objects.sprites
import functions
import functions.stage_run
import functions.values
import functions.buff_debuff
import random

from functions.buff_debuff import *
from functions.values import screenborder
from random import random
from math import pi
from objects.elf import *
from objects.danmaku import *

class elf_1(elf_blue_small):
    def attack_normal(self, erina, birth_layer, elf_layer, danmaku_layer):
        if 60 <= self.timer <= 100:
            if not self.timer%10:
                orange_glow_dot(3, 50,
                    birth_layer, self, Ponised(time=800),
                    birth_time = 2,
                    danmaku_layer = 1,
                    direction = erina,
                    birth_speed = 6.5,
                    speedtime = (30,),
                    speedvalue = (2.0,)
                )

class elf_2(elf_red_small):
    def attack_normal(self, erina, birth_layer, elf_layer, danmaku_layer):
        if self.timer == 89:
            self.snipe = functions.snipe(self, erina)
        elif 90 <= self.timer < 150:
            if self.timer < 103:
                for i in range(-1,2):
                    green_glow_dot(5, 50,
                        birth_layer, self, 
                        birth_place_offset = ((self.snipe + pi/2), i*(self.timer-90)*2),
                        birth_time = 2,
                        danmaku_layer = 0,
                        direction = self.snipe,
                        birth_speed = 5,
                        speedtime = (30,),
                        speedvalue = (2,)
                    )
            elif 105 <= self.timer <= 120:
                green_glow_dot(5, 50,
                    birth_layer, self,
                    birth_time = 2,
                    danmaky_layer = 0,
                    direction = self.snipe,
                    birth_speed = 5,
                    speedtime = (30,),
                    speedvalue = (2,)
                )
        elif self.timer == 149:
            self.snipe = functions.snipe(self, erina)
        elif 150 <= self.timer < 210:
            if self.timer < 163:
                for i in range(-1,2):
                    green_glow_dot(5, 50,
                        birth_layer, self,
                        birth_place_offset = ((self.snipe + pi/2), i*(self.timer-150)*2),
                        birth_time = 2,
                        danmaku_layer = 0,
                        direction = self.snipe,
                        birth_speed = 5,
                        speedtime = (30,),
                        speedvalue = (2,)
                    )
            elif 165 <= self.timer <= 180:
                green_glow_dot(5, 50,
                    birth_layer, self,
                    birth_time = 2,
                    danmaku_layer = 0,
                    direction = self.snipe,
                    birth_speed = 5,
                    speedtime = (30,),
                    speedvalue = (2,)
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
        elif self.timer == 600:
            elf_2(
                self.elf_layer,
                birth_place = (screenborder.SCREEN_LEFT + 30, -20),
                birth_direction = pi/2,
                birth_speed = 2,
                speedtime = (80, 140, 180),
                speedvalue = (0, 0, 1)
            )
            elf_2(
                self.elf_layer, 
                birth_place = (screenborder.SCREEN_RIGHT - 30, -20),
                birth_direction = pi/2,
                birth_speed = 2,
                speedtime = (80, 140, 180),
                speedvalue = (0, 0, 1)
            )
        elif self.timer == 940:
            self.bgm.fadeout(1000)
        elif self.timer == 1000:
            self.part_run = False