import pygame
import math

import objects.sprites
import functions
import functions.stage_run
import functions.values
import functions.buff_debuff

from objects.elf import *

class elf_1(elf_blue_small):
    def __init__(self):
        super().__init__()


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
        self.stage_time = 5400

    def MidAttack(self, *args, **kwargs):
        pass

