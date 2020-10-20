import pygame
import math
import platform
import random
from math import *
from pygame.locals import *
# from functions.values import screenborder
from functions.values import *
# from functions.values import damagetype

class MP(object):
    """
    specify ribbon mana value
    """
    _base_mp = 10000
    def __init__(self, ribbon):
        self.ribbon = ribbon
        self.mp = 10000
        self.max_mp = 10000
        self.base_mp = 10000

    def __setattr__(self, name, value):
        value = value.__int__()
        if name in 'max_mp':
            if self.mp > self.max_mp:
                self.mp = self.max_mp
        return super().__setattr__(name, value)

    def add(self, value):
        self.mp += value

    def sub(self, value):
        self.mp -= value

    def full(self):
        self.mp = self.max_mp

    def empty(self):
        self.mp = 0

    def boost(self, max_boost=False):
        h = self.max_mp//2
        if self.mp > h:
            self.mp -= h
        elif self.mp == self.max_mp:
            if self.max_boost:
                self.empty()
            else:
                self.mp -= h

    def __repr__(self):
        return "< ribbon MP: %d/%d >" % (self.mp, self.max_mp)

    def __str__(self):
        return "MP: %d\nMaxMP: %d\nBaseMP: %d" % (self.mp, self.max_mp, self.base_mp)

class green_danmaku(pygame.sprite.Sprite):
    def __init__(self, me_ribbon):
        pygame.sprite.Sprite.__init__(self)
        if platform.system() == 'Linux' or platform.system()=='Darwin':
            oimage = pygame.image.load("images/character/Ribbon/ribbon_green.png").convert_alpha()
        if platform.system() == 'Windows':
            oimage = pygame.image.load("images\\character\\Ribbon\\ribbon_green.png").convert_alpha()
        self.image = oimage
        self.rect = self.image.get_rect()
        
        self.radius = 10
        self.damage = 10+random.randint(0,1)
        
        self.center = [me_ribbon.center[0], me_ribbon.center[1]]
        self.direction = [0,-1]
        self.rect.left = self.center[0] - 10
        self.rect.top = self.center[1] - 10
        self.delete = False
        
        self.speed = 8 + random.random()*2

        self._type = damagetype.MAGIC
    
    def move(self, *erina):
        self.center[0] += self.speed * self.direction[0]
        self.center[1] += self.speed * self.direction[1]
        self.rect.top = self.center[0] - 10
        self.rect.left = self.center[1] - 10
        if self.rect.top < BATTLE_SCREEN_TOP or \
           self.rect.left < BATTLE_SCREEN_LEFT or \
           self.rect.right > BATTLE_SCREEN_RIGHT or \
           self.rect.bottom > BATTLE_SCREEN_BOTTOM:
            self.delete = True

    def print_screen(self, screen):
        screen.blit(self.image, self.rect)

class purple_danmaku(pygame.sprite.Sprite):
    def __init__(self, me_ribbon):
        pygame.sprite.Sprite.__init__(self)
        if platform.system() == 'Linux' or platform.system()=='Darwin':
            oimage = pygame.image.load("images/character/Ribbon/ribbon_purple.png").convert_alpha()
        if platform.system() == 'Windows':
            oimage = pygame.image.load("images\\character\\Ribbon\\ribbon_purple.png").convert_alpha()
        self.image = oimage
        self.rect = self.image.get_rect()
        
        self.radius = 5
        self.damage = 10
        
        self.center = [me_ribbon.center[0], me_ribbon.center[1]]
        self.direction = [0,-1]
        self.rect.left = self.center[0] - 5
        self.rect.top = self.center[1] - 5
        self.delete = False
        
        self.speed = 10

        self._type = damagetype.MAGIC
        
    def move(self, *erina):
        self.center[0] += self.speed * self.direction[0]
        self.center[1] += self.speed * self.direction[1]
        self.rect.top = self.center[0] - 5
        self.rect.left = self.center[1] - 5
        if self.rect.top < BATTLE_SCREEN_TOP or \
           self.rect.left < BATTLE_SCREEN_LEFT or \
           self.rect.right > BATTLE_SCREEN_RIGHT or \
           self.rect.bottom > BATTLE_SCREEN_BOTTOM:
            self.delete = True

    def print_screen(self, screen):
        screen.blit(self.image, self.rect)

class Ribbon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        if platform.system()=='Windows':
            oimage = pygame.image.load("images\\character\\Ribbon\\Ribbon.png").convert_alpha()
        if platform.system()=='Linux' or platform.system()=='Darwin':
            oimage = pygame.image.load("images/character/Ribbon/Ribbon.png").convert_alpha()
        self.image = pygame.transform.scale(oimage, (16,20))
        self.rect = self.image.get_rect()
        self.center = [225, 370]
        self.rect.left = self.center[0] - 8
        self.rect.top = self.center[1] - 10
        
        self.energy = 500
        self.max_energy = 1000
        self.radius = 1
        self.shouting_delay = 0
        
        self.danmaku_mode = ["red", "yellow", "blue", "green", "purple", "carrot", "egg"]
        self.danmaku_type = "green"
        
    def move(self, master):
        destination = [master.center[1] - 30, master.center[0]]
        distance = math.sqrt( \
                            (destination[0] - self.center[0]) ** 2 + \
                            (destination[1] - self.center[1]) ** 2 )
        direction = [ \
                    (destination[0] - self.center[0]) / distance, \
                    (destination[1] - self.center[1]) / distance]

        speed = distance ** 2 / 500.0
        """
        if distance > 50:
            speed = int(exp(distance))
        else:
            speed = int(sqrt(sqrt(distance)))
"""
        self.center[0] += speed * direction[0]
        self.center[1] += speed * direction[1]

        self.rect.top = int(self.center[0] - 8)
        self.rect.left = int(self.center[1] - 10)
        
    def purple_attack(self, shouting_group, key_pressed):
        if not self.shouting_delay:
            key = key_pressed
        try:
            if key[K_z]:
                if not self.shouting_delay:
                    for i in range(-10,11):
                        temp = purple_danmaku(self)
                        temp.direction = [\
                                          cos((314 + 10*i) / 100), \
                                          sin((314 + 10*i) / 100)]
                        shouting_group.add(temp)
                self.shouting_delay += 1
        except:
            self.shouting_delay += 1
        if self.shouting_delay > 15:
            self.shouting_delay = 0

    def red_attack(self, shouting_group):
        pass
    
    def blue_attack(self, shouting_group):
        pass
    
    def green_attack(self, shouting_group, key_pressed):
        if not self.shouting_delay:
            key = key_pressed
        try:
            if key[K_z]:
                if not self.shouting_delay:
                    for i in range(-3,4):
                        temp = green_danmaku(self)
                        temp.direction = [\
                                          cos((314 + 5*i + random.random()*5) / 100), \
                                          sin((314 + 5*i + random.random()*5) / 100)]
                        shouting_group.add(temp)
                self.shouting_delay += 1
        except:
            self.shouting_delay += 1
        if self.shouting_delay > 10:
            self.shouting_delay = 0

    def yellow_attack(self, shouting_group):
        pass
    
    def carrot_attack(self, shouting_group):
        pass

    def attack(self, shouting_group, key_pressed):
        self.__getattribute__(self.danmaku_type + '_attack')(shouting_group, key_pressed)
        """
        if self.danmaku_type == "purple":
            self.purple_attack(shouting_group, key_pressed)
        elif self.danmaku_type == "red":
            self.red_attack(shouting_group)
        elif self.danmaku_type == "blue":
            self.blue_attack(shouting_group)
        elif self.danmaku_type == "green":
            self.green_attack(shouting_group)
        elif self.danmaku_type == "yellow":
            self.yellow_attack(shouting_group)
        elif self.danmaku_type == "carrot":
            self.carrot_attack(shouting_group)
        """

class energy(pygame.sprite.Sprite):
    def __init__(self, boss):
        pass
        
    def boost_attract(energy_group, me_ribbon):
        pass
