import math
import random

from functions.sprites import Boss
from functions.sprites import Danmaku
from functions.spell_card import SpellCard
from functions import snipe

class mid_orange_circle(Danmaku):
    """
    cocoa danmaku 1 
    use orange circle
    """
    def __init__(self, emitter, images):
        super().__init__()
        self.SetImage(images[self.__class__.__name__])
        self.SetValue(7,50,4,emitter)
        self.SetLiveCheck(-20,400,-10,500)

class Spell_1_Normal(SpellCard):
    """
    no-spell
    """
    def spell_normal(self, erina, boss, boss_group, birth_group, effects_group):
        temp_time = self.timer % 120
        if temp_time:
            if temp_time%10 == 1 and temp_time<62:
                temp_snipe = snipe(boss, erina)
                offset = random.randint(-10,10)
                for i in range(-8,9):
                    temp_danmaku = mid_orange_circle(boss.center, boss.danmaku_images)
                    temp_danmaku.layer = 0
                    temp_danmaku.center = [boss.center[0], boss.center[1]]
                    temp_danmaku.direction = [math.cos(temp_snipe + i*math.pi/32 + math.pi*offset/320), math.sin(temp_snipe + i*math.pi/32 + math.pi*offset/320)]
                    temp_danmaku.speed = 2
                    birth_group.add(temp_danmaku)
        else:
            pass
            boss.temp_position[0] = random.randint(50,380)
            boss.temp_position[1] = random.randint(50,160)
        self.timer += 1

class Cocoa(Boss):
    """
    stage1a boss cocoa
    """
    def __init__(self):
        super().__init__('Cocoa')
        self.SetValue(1000, 18, 400)
        self.SetSpell(1800)
        self.SetSource('data/boss/sec1/Cocoa.rbrb')
        self.SetDanmakuUse('mid_orange_circle')
        self.spell_group.add(Spell_1_Normal(1,1800,self.illustration))
    