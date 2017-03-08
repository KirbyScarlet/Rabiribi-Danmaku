#!/usr/bin/python3 

# This fucking game
# project starts on Oct 25 2016
# rabiribi danmaku

import pygame

pygame.init()
pygame.mixer.init()

bg_size = width, height = 640, 480
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("RabiRibi-Danmaku demo")
icon = pygame.image.load("images/ribbon cover.png")
pygame.display.set_icon(icon)

import sys
import traceback
import ui
import boss
import character
import functions

me_erina = character.erina.Erina()
me_ribbon = character.ribbon.Ribbon()
serface = ui.face.Face()

global difficulty

def main():
    #ui.welcome.opening(screen)
    #ui.menu.menu_switch(screen)
    input()
    difficulty = 1
    functions.run.stage_boss(screen, me_erina, me_ribbon, difficulty, boss.section1.stage1a.cocoa.Cocoa())
    
if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
    else:
        functions.clear_cache()