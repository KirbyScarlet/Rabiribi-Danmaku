#!/usr/bin/python3 

# This fucking game
# project starts on Oct 25 2016
# rabiribi danmaku

import pygame

pygame.init()
pygame.mixer.init()

bg_size = width, height = 640, 480
screen = pygame.display.set_mode(bg_size, pygame.DOUBLEBUF)
pygame.display.set_caption("RabiRibi-Danmaku demo")
icon = pygame.image.load("images/ribbon cover.png")
pygame.display.set_icon(icon)

import sys
import traceback
import ui
import functions
import boss
import character

me_erina = character.erina.Erina()
me_ribbon = character.ribbon.Ribbon()

global difficulty

def main():
    print("Hello Rabiribi Danmaku")
    #ui.welcome.opening(screen)
    #ui.menu.menu_switch(screen)
    difficulty = 'normal'
    import boss.section1.stage1a
    boss.section1.stage1a.stage(me_erina, me_ribbon, difficulty, screen)
    stage1boss = functions.stage_run.BossBattle(me_erina, me_ribbon, difficulty, 2, boss.section1.stage1a.cocoa.Cocoa())
    stage1boss(screen, debug=True)

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
        functions.clear_cache()