import math
import random

from functions.sprites import Boss
from functions.sprites import Danmaku
from functions.spell_card import SpellCard
from functions import snipe

class cocoa_danmaku_1(Danmaku):
    """
    cocoa danmaku 1 
    use orange circle
    """
    def __init__(self, emitter):
        super().__init__('orange_circle')
        self.SetImage('data/danmaku/mid_orange_circle.rbrb')
        self.SetValue(7,50,4,emitter)
        self.SetLiveCheck(-20,400,-10,500)

class Spell_1(SpellCard):
    """
    no-spell
    """
    def spell(self, erina, boss, boss_group, birth_group, effects_group):
        temp_time = self.timer % 120
        if temp_time:
            if temp_time%10 == 1 and temp_time<62:
                temp_snipe = snipe(boss, erina)
                offset = random.randint(-10,10)
                for i in range(-8,9):
                    temp_danmaku = cocoa_danmaku_1(boss.center)
                    temp_danmaku.center = [boss.center[0], boss.center[1]]
                    temp_danmaku.direction = [math.cos(temp_snipe + i*math.pi/32 + math.pi*offset/320), math.sin(temp_snipe + i*math.pi/32 + math.pi*offset/320)]
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
        self.spell_group.add(Spell_1(1,1800,self.illustration))
    