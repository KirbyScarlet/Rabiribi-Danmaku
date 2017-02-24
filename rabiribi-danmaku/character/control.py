import pygame

import character.erina
import character.ribbon

from pygame.locals import *

def move(bg_size):
    me = character.erina.Erina(bg_size)
    me_ribbon = character.ribbon.Ribbon(bg_size)

    key_pressed = pygame.key.get_pressed()

    me.moveSpeed(key_pressed[K_LSHIFT])

    #自机方向控制
    if key_pressed[K_w] or key_pressed[K_UP] or key_pressed[K_s] or key_pressed[K_DOWN]:  
        if (key_pressed[K_w] or key_pressed[K_UP]) and (key_pressed[K_s] or key_pressed[K_DOWN]):
            if UD_control:
                if me.UpDown_control == 8:
                    me.UpDownControl(2)
                elif me.UpDown_control == 2:
                    me.UpDownControl(8)
                UD_control = False
        else:
            if key_pressed[K_w] or key_pressed[K_UP]:
                me.UpDownControl(8)
                UD_control = True
            if key_pressed[K_s] or key_pressed[K_DOWN]:
                me.UpDownControl(2)
                UD_control = True
    else:
        me.UpDownControl(0)
    if key_pressed[K_a] or key_pressed[K_LEFT] or key_pressed[K_d] or key_pressed[K_RIGHT]: 
        if (key_pressed[K_a] or key_pressed[K_LEFT]) and (key_pressed[K_d] or key_pressed[K_RIGHT]):
            if LR_control:
                if me.LeftRight_control == 6:
                    me.LeftRightControl(4)
                elif me.LeftRight_control == 4:
                    me.LeftRightControl(6)                  
                LR_control = False
        else:
            if key_pressed[K_d] or key_pressed[K_RIGHT]:
                me.LeftRightControl(6)
                LR_control = True
            if key_pressed[K_a] or key_pressed[K_LEFT]:
                me.LeftRightControl(4)
                LR_control = True
    else:       
        me.LeftRightControl(0)
    me.moveUpDown()
    me.moveLeftRight()
    me_ribbon.move(me.center)
    #自机+子机控制
    screen.blit(me.image, me.rect)
    screen.blit(me_ribbon.image, me_ribbon.rect)
