import pygame
import math

import functions
import functions.sprites
import functions.stage_run
import functions.values
import functions.buff_debuff

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
        self.timer = 0
        

    def MidAttack(self, *args, **kwargs):
        pass

    
        