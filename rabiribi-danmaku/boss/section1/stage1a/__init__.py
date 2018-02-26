import boss.section1.stage1a
import boss.section1.stage1a.cocoa
import boss.section1.stage1a.stage_mid
from boss.section1.stage1a.cocoa import Cocoa

# from boss.section1.stage1a.stage_mid import Stage1aMidBattle
# import functions.stage_run
# from boss.section1.stage1a.stage_mid import stage1amidbattle

# stage1a_mid = Stage1aMidBattle(4)
# stage1a_boss = functions.stage_run.BossBattle(2, Cocoa())

'''
def stage_end(me_erina, me_ribbon, difficulty, screen):
    stage1a_boss(me_erina, me_ribbon, difficulty, screen, True)

def stage_mid(stage):
    stage1amidbattle(stage)
    #stage1a_mid(me_erina, me_ribbon, difficulty, screen, True)

stage_mid = stage1amidbattle
'''

from boss.section1.stage1a.stage_mid import *

def stage_mid(stage):
    if stage.timer == 0:
        stage.bgm.load('data/bgm/rbs1s1am.ogg')
        stage.bgm.play(-1)
    if 60 <= stage.timer <= 300:
        if not stage.timer%30:
            elf_1(
                stage.elf_layer,
                birth_place = (15+random()*20, -30),
                birth_direction = pi/2,
                birth_speed = 1,
                directiontime = (120, 300),
                directionvalue = ([-pi/360, 0], 0)
            )
    elif stage.timer == 600:
        elf_2(
            stage.elf_layer,
            birth_place = (BATTLE_SCREEN_LEFT + 30, -20),
            birth_direction = pi/2,
            birth_speed = 2,
            speedtime = (80, 140, 180),
            speedvalue = (0, 0, 1)
        )
        elf_2(
            stage.elf_layer, 
            birth_place = (BATTLE_SCREEN_RIGHT - 30, -20),
            birth_direction = pi/2,
            birth_speed = 2,
            speedtime = (80, 140, 180),
            speedvalue = (0, 0, 1)
        )
    elif stage.timer == 940:
        stage.bgm.fadeout(1000)
    elif stage.timer == 1000:
        stage.timer = 0
        stage.part_run = False

def stage_end(stage):
    if not stage.timer:
        stage.boss_layer.add(Cocoa())
    # stage.spell_attack()
    if not stage.boss_layer:
        stage.part_run = False

def stage1a_main(window, stage):
    stage.part_run = True
    stage(window, stage_mid, 1)
    # talk
    stage.part_run = True
    stage(window, stage_end, 1)
    # stage 1a end