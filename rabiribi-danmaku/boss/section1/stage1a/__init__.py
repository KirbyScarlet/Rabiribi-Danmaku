import boss.section1.stage1a.cocoa
import boss.section1.stage1a.stage_mid
import functions.stage_run
from boss.section1.stage1a.cocoa import Cocoa

#stage1a_mid = functions.stage_run.MidBattle(4)
stage1a_boss = functions.stage_run.BossBattle(2, Cocoa())

def stage(me_erina, me_ribbon, difficulty, screen):
    stage1a_boss(me_erina, me_ribbon, difficulty, screen, True)