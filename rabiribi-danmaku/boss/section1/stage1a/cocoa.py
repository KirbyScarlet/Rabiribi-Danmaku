import pygame
import math
import random
from functions.sprites import Boss

class Cocoa(Boss):
    """
    stage1a boss cocoa
    """
    def __init__(self):
        super().__init__('Cocoa')
        self.SetValue(1000, 18, 400)
        self.SetSpell(1800)
        self.SetSource('data/chara/sec1/Cocoa.rbrb')

    def spell_1(self, difficulty, me_erina, boss_group, birth_group, effects_group):
        if self.spell_time < 1800:
            temp_time = self.spell_time % 120
            if temp_time:
                if temp_time%10 == 1 and temp_time<62:
                    temp_snipe = functions.snipe(self, me_erina)
                    offset = randint(-10,10)
                    for i in range(-8,9):
                        temp_danmaku = cocoa_danmaku_1(self.center)
                        temp_danmaku.center = [self.center[0], self.center[1]]
                        temp_danmaku.direction = [cos(temp_snipe + i*pi/32 + pi*offset/320), sin(temp_snipe + i*pi/32 + pi*offset/320)]
                        birth_group.add(temp_danmaku)
            else:
                pass
                self.temp_position[0] = randint(50,380)
                self.temp_position[1] = randint(50,160)
        self.spell_time += 1