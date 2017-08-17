import boss.section1.stage1a
import boss.section1.stage1a.cocoa
import boss.section1.stage1a.stage_mid
from boss.section1.stage1a.cocoa import Cocoa
from boss.section1.stage1a.stage_mid import Stage1aMidBattle
import functions.stage_run


stage1a_mid = Stage1aMidBattle(4)
stage1a_boss = functions.stage_run.BossBattle(2, Cocoa())

def stage_end(me_erina, me_ribbon, difficulty, screen):
    stage1a_boss(me_erina, me_ribbon, difficulty, screen, True)

def stage_mid(me_erina, me_ribbon, difficulty, screen):
    stage1a_mid(me_erina, me_ribbon, difficulty, screen, True)