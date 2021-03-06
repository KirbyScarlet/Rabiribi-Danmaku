import math
import random
import time

from objects.sprites import Boss
from objects.sprites import Danmaku
from functions.spell_card import SpellCard
from functions import snipe
from objects.danmaku import *
from math import pi

from functions.buff_debuff import SpeedDown

class Spell_1(SpellCard):
    """
    no-spell
    """
    def spell_normal(self, erina, birth_group, boss_group, illustration_group):
        temp_time = self.timer % 120
        if temp_time:
            if temp_time%10 == 1 and temp_time>60:
                #temp_snipe = snipe(self.boss, erina)
                offset = random.randint(-10,10)
                for i in range(-15,16):
                    gray_glow_dot(5, 50, birth_group, self.boss,
                        SpeedDown(time=600),
                        birth_time = 10, lazer = -1,
                        birth_speed = 5, 
                        direction = erina,
                        direction_offset = offset*pi/320 + i*pi/32,
                        speedtime = (60,120),
                        speedvalue = (0,1.5),
                        directiontime = (60,120),
                        directionvalue = ([pi/240*(-1)**((temp_time-1)//10),0],0)
                    )
                    #birth_group.add(temp)
                    '''
                    temp_danmaku.layer = 0
                    temp_danmaku.center = [self.boss.center[0], self.boss.center[1]]
                    temp_danmaku.direction.set(temp_snipe + i*math.pi/32 + math.pi*offset/320)
                    #temp_danmaku.speed = 2
                    birth_group.add(temp_danmaku)
                    '''
        else:
            pass
            self.boss.temp_position[0] = random.randint(50,380)
            self.boss.temp_position[1] = random.randint(50,160)

class Spell_2(SpellCard):
    """
    spell
    """
    def spell_normal(self, erina, birth_group, boss_group, illustration_group):
        temp_time = self.timer % 40
        if temp_time%15 == 1:
            angle = random.randint(0,628)/100
            for i in range(32):
                gray_glow_dot(5, 50, birth_group, self.boss,
                                  birth_time = 10,
                                  birth_speed = 10,
                                  direction = angle,
                                  direction_offset = 2*pi*i/32,
                                  danmaku_layer = 1,
                                  speedtime = (20,),
                                  speedvalue = (2,)
                                  )
            '''
                temp_danmaku = mid_orange_circle_cocoa_spell_1(self.boss.center)
                temp_danmaku.layer = 1
                temp_danmaku.center = list(self.boss.center)
                temp_danmaku.direction.set(angle + 2*math.pi/32*i)
                birth_group.add(temp_danmaku)
            '''
        if self.timer >= 300 and temp_time < 20:
            if temp_time == 0:
                self.temp_snipe = snipe(self.boss, erina)
            if temp_time % 2 == 1:
                for i in range(10):
                    for j in -1,1:
                        orange_glow_dot(5, 50, birth_group, self.boss,
                                          birth_speed = 3,
                                          direction = self.temp_snipe,
                                          direction_offset = 2*pi*i/10 + 2*pi*temp_time*j/314
                                          )
                        '''
                        temp_danmaku = small_blue_circle_cocoa_spell_2(self.boss.center)
                        temp_danmaku.layer = 0
                        temp_danmaku.center = list(self.boss.center)
                        temp_danmaku.time_rip = lambda: 1
                        temp_danmaku.speed = 4
                        temp_danmaku.direction.set(self.temp_snipe + 2*math.pi/10*i + 2*math.pi/128*temp_time*j)
                        birth_group.add(temp_danmaku)
                        '''
        else:
            self.boss.temp_position[0] = 225
            self.boss.temp_position[1] = 100


class Cocoa(Boss):
    """
    stage1a boss cocoa
    """
    def __init__(self):
        super().__init__('Cocoa')
        self.SetValue(1000, 18, 400)
        self.SetSpell(1800)
        self.SetSource('Cocoa.rbrb')
        # self.SetDanmakuUse('mid_orange_circle', 'small_blue_circle')
        self.spell_group.add(Spell_1(self,1,1800), Spell_2(self,2,3000,self.illustration))
    