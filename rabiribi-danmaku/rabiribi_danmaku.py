#!/usr/bin/python3 

# This fucking game
# project starts on Oct 25 2016
# rabiribi danmaku

import sys
import os
'''
p = sys.argv[-1].split('/')
l = len(p)
if l > 1:
    if l == 2 and p[0]=='.': pass
    else:
        syspath = os.path.abspath('.')
        for i in range(l-1):
            syspath += '/'
            syspath += p[i]
syspath += '/'
'''
syspath = os.path.split(__file__)[0]
os.chdir(syspath)

import pygame

pygame.init()
pygame.mixer.init()

bg_size = width, height = 640, 480
window = pygame.display.set_mode(bg_size, pygame.DOUBLEBUF)
pygame.display.set_caption("RabiRibi-Danmaku demo")
icon = pygame.image.load("images/ribbon cover.png")
pygame.display.set_icon(icon)

'''
class MainLoop():
    """
    one process use for print screen
    """
    bg_size = width, height = 640, 480
    window = pygame.display.set_mode(bg_size, pygame.DOUBLEBUF)
    pygame.display.set_caption("RabiRibi-Danmaku demo")
    icon = pygame.image.load("images/ribbon cover.png")
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()

    def blit(self, screens, position):
        return self.window.blit(screens, position)

    def update(self, fps=60):
        pygame.display.update()
        self.clock.tick_busy_loop(fps)
''' # multi-process without testing

import traceback
import functions
import character
import ui

# me_ribbon = character.ribbon.Ribbon()
# me_erina = character.erina.Erina(me_ribbon)

global difficulty

def main():
    print("Hello Rabiribi Danmaku")
    #ui.welcome.opening(screen)
    #ui.menu.menu_switch(screen)
    difficulty = 'normal'
    #import ui.menu
    #ui.menu.menu(screen)
    '''
    import boss.section1.stage1a
    boss.section1.stage1a.stage_mid(me_erina, me_ribbon, difficulty, window)
    boss.section1.stage1a.stage_end(me_erina, me_ribbon, difficulty, window)
    '''
    stage = functions.stage.Stage(difficulty)
    import boss.section1
    boss.section1.section1_main(window, stage)

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        functions.clear_cache()
        input()
