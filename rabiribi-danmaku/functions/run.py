import pygame
import boss
import math
import character
import ui
import sys
import functions

from pygame.locals import *
from math import *

timer = 0

font = pygame.font.Font(None, 20)

def danmaku_del(danmaku_group):
    for each in danmaku_group:
        if each.live_check():
            danmaku_group.remove(each)

def shouting_del(shouting_group):
    for each in shouting_group:
        if each.center[0] < -175 or each.center[0] > 625 \
           or each.center[1] < -610 or each.center[1] > 640:
            shouting_group.remove(each)
            
def boss_del(boss_group):
    for each in boss_group:
        try:
            each.livetime == 0
            boss_group.remove(each)
        except:
            pass

def effects_del(effects_group):
    for each in effects_group:
        if each.center[0] < -175 or each.center[0] > 625 \
           or each.center[1] < -610 or each.center[1] > 640:
            effects_group.remove(each)

def sprites_del(*sprites_group):
    for group in sprites_group:
        for sprite in group:
            if hasattr(sprite, 'live_time'):
                if sprite.live_time == 0:
                    group.remove(sprite)
            if hasattr(sprite, 'delete'):
                if sprite.delete:
                    group.remove(sprite)
            

def sprites_move(*sprites_group):
    for group in sprites_group:
        for each in group:
            each.move()           

def print_screen(screen,
                    background,
                    boss_group,
                    stage_boss,
                    birth_group,
                    danmaku_group,
                    shouting_group,
                    effects_group,
                    energy_group,
                    me_erina,
                    me_ribbon,
                    face,
                    debug):
    screen.blit(background, (0,0))
    for temp in boss_group:
        screen.blit(temp.image, temp.rect)
    screen.blit(stage_boss.image, stage_boss.rect)
    screen.blit(me_erina.image, me_erina.rect)
    screen.blit(me_ribbon.image, me_ribbon.rect)
    for temp in shouting_group:
        screen.blit(temp.image, temp.rect)
    for temp in effects_group:
        screen.blit(temp.image, temp.rect)
    for remp in energy_group:
        screen.blit(temp.image, temp.rect)
    for temp in birth_group:
        screen.blit(temp.image, temp.rect)
    for temp in danmaku_group:
        screen.blit(temp.image, temp.rect)
    screen.blit(face.face, (0,0))
    
    if debug:
        debug_words_pos_left = 430
        debug_words_pos_top = 360
        
        erina_position = "erina position: " + str(round(me_erina.center[0], 2)) + " , " + str(round(me_erina.center[1], 2))
        ribbon_position = "ribbon position: " + str(round(me_ribbon.center[0], 2)) + " , " + str(round(me_ribbon.center[1], 2))
        erina_health = "erina hp: " + str(me_erina.hp) + "/" + str(me_erina.max_hp)
        boss_health = "boss hp: " + str(stage_boss.hp) + "/" + str(stage_boss.max_hp)
        
        screen.blit(font.render(erina_position, True, (255,0,0)), (debug_words_pos_left, debug_words_pos_top))
        screen.blit(font.render(ribbon_position, True, (255,0,0)), (debug_words_pos_left, debug_words_pos_top + 20))
        screen.blit(font.render(erina_health, True, (255,0,0)), (debug_words_pos_left, debug_words_pos_top + 40))
        screen.blit(font.render(boss_health, True, (255,0,0)), (debug_words_pos_left, debug_words_pos_top + 60))

def stage_mid(screen, me_erina, me_ribbon, difficulty):
    pass

def stage_boss(screen, me_erina, me_ribbon, difficulty, stage_boss):
    global miss
    global pause
    face = ui.face.Face()
    miss = 0
    boost = 0
    pause = 0
    
    clock = pygame.time.Clock()

    birth_group = pygame.sprite.Group()
    danmaku_group = pygame.sprite.Group()
    shouting_group = pygame.sprite.Group()
    boss_group = pygame.sprite.Group()
    effects_group = pygame.sprite.Group()
    energy_group = pygame.sprite.Group()
    
    boss_group.add(stage_boss)
    
    stage_boss.bgm.play(-1)
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                functions.clear_cache()
                sys.exit()
        
        #key pressed here:
        me_erina.key_pressed = pygame.key.get_pressed()

        #buff check here:
        for b in boss_group:
            for f in b.buff:
                f.check(b)
        for f in me_erina.buff:
            f.check(me_erina)
        
        #boss spell attack on here:
        stage_boss.spell_attack(1, me_erina, boss_group, birth_group, effects_group)
        
        if not miss:
            me_erina.move()
            me_ribbon.move(me_erina)
            me_ribbon.attack(shouting_group, me_erina.key_pressed)
        else:
            for each in danmaku_group:
                danmaku_group.remove(each)
            me_erina.reset(miss)
            miss -= 1

        # sprite move here:
        sprites_move(
                     birth_group, 
                     danmaku_group, 
                     shouting_group, 
                     effects_group, 
                     energy_group, 
                     boss_group
                     )
        
        for each in birth_group:
            if each.birth_life == 0:
                birth_group.remove(each)
                danmaku_group.add(each)
            else:
                each.birth_life -= 1
        
        # sprite del here:
        danmaku_del(danmaku_group)
        shouting_del(shouting_group)
        effects_del(effects_group)
        boss_del(boss_group)

        #damage check here:
        me_erina.collide_check(danmaku_group, boss_group)
        stage_boss.collide_check(shouting_group)
        

        # printing screen here:
        print_screen(screen,
                    face.background,
                    boss_group,
                    stage_boss, 
                    birth_group,
                    danmaku_group,
                    shouting_group,
                    effects_group,
                    energy_group,
                    me_erina,
                    me_ribbon,
                    face,
                    1)
        
        screen.blit(font.render(str(round(clock.get_fps(), 2)), True, (255,0,0)), (600,460))
        
        pygame.display.flip()
        #pygame.display.update()
        
        clock.tick(60)
