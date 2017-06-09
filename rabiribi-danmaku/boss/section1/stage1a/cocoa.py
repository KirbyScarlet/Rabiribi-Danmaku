import math
import random

from functions.sprites import Boss
from functions.sprites import Danmaku
from functions.spell_card import SpellCard
from functions import snipe
from objects.danmaku import mid_orange_circle

class mid_orange_circle_cocoa_spell_1(mid_orange_circle):
    def __init__(self, emitter, images):
        super().__init__(emitter, images)

    def time_rip(self):
        if self.timer < 10:
            self.speed = 6
        elif 10 < self.timer < 20:
            self.speed = -0.4*self.timer+10
        else:
            self.speed = 2

class Spell_1(SpellCard):
    """
    no-spell
    """
    def spell_normal(self, erina, birth_group, boss_group, illustration_group):
        temp_time = self.timer % 120
        if temp_time:
            if temp_time%10 == 1 and temp_time<62:
                temp_snipe = snipe(self.boss, erina)
                offset = random.randint(-10,10)
                for i in range(-8,9):
                    temp_danmaku = mid_orange_circle_cocoa_spell_1(self.boss.center, self.boss.danmaku_images)
                    temp_danmaku.layer = 0
                    temp_danmaku.center = [self.boss.center[0], self.boss.center[1]]
                    temp_danmaku.direction = [math.cos(temp_snipe + i*math.pi/32 + math.pi*offset/320), math.sin(temp_snipe + i*math.pi/32 + math.pi*offset/320)]
                    #temp_danmaku.speed = 2
                    birth_group.add(temp_danmaku)
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
                temp_danmaku = mid_orange_circle_cocoa_spell_1(self.boss.center, self.boss.danmaku_images)
                temp_danmaku.layer = 1
                temp_danmaku.center = list(self.boss.center)
                temp_danmaku.direction = [math.cos(angle + 2*math.pi/32*i), math.sin(angle + 2*math.pi/32*i)]
                birth_group.add(temp_danmaku)
        if self.timer >= 300 and temp_time < 20:
            if temp_time == 0:
                self.temp_snipe = snipe(self.boss, erina)
            if temp_time % 2 == 1:
                for i in range(10):
                    for j in -1,1:
                        temp_danmaku = mid_orange_circle_cocoa_spell_1(self.boss.center, self.boss.danmaku_images)
                        temp_danmaku.layer = 0
                        temp_danmaku.center = list(self.boss.center)
                        temp_danmaku.time_rip = lambda: 1
                        temp_danmaku.speed = 4
                        temp_danmaku.direction = [math.cos(self.temp_snipe + 2*math.pi/10*i + 2*math.pi/128*temp_time*j), 
                                                  math.sin(self.temp_snipe + 2*math.pi/10*i + 2*math.pi/128*temp_time*j)]
                        birth_group.add(temp_danmaku)
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
        self.SetSource('data/obj/boss/Cocoa.rbrb')
        self.SetDanmakuUse('mid_orange_circle')
        self.spell_group.add(Spell_1(self,1,1800), Spell_2(self,2,3000,self.illustration))
    