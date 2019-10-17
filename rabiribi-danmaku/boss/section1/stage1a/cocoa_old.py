import pygame
import math
import random
import platform
import functions

from pygame.locals import *
from random import *
from math import *

class cocoa_danmaku_1(pygame.sprite.Sprite):
    def __init__(self, boss_position):
        pygame.sprite.Sprite.__init__(self)
        if platform.system() == 'Windows':
            self.cocoa_danmaku_type1 = pygame.image.load("images\\boss\\Cocoa\\cocoa_danmaku_type1_00.png").convert_alpha()
        if platform.system() == 'Linux' or platform.system()=='Darwin':
            self.cocoa_danmaku_type1 = pygame.image.load("images/boss/Cocoa/cocoa_danmaku_type1_00.png").convert_alpha()
        self.image = self.cocoa_danmaku_type1
        self.rect = self.image.get_rect()
        self.center = [boss_position[0], boss_position[1]]
        self.rect.left = self.center[0] - 10
        self.rect.top = self.center[1] - 10
        self.direction = [0.0,-1.0]
        
        self.damage = 13
        self.speed = 2.5
        self.birth_life = 6
        self.special_count = 0
        self.radius = 0
        self.effects_time = 60
        
    def move(self):
        self.center[0] += self.speed * self.direction[0]
        self.center[1] += self.speed * self.direction[1]
        self.rect.left = self.center[0] - 10
        self.rect.top = self.center[1] - 10
        if self.effects_time:
            self.effects_time -= 1
        else:
            self.effects_time = 60

class cocoa_danmaku_1_effects(pygame.sprite.Sprite):
    def __init__(self, danmaku):
        pygame.sprite.Sprite.__init__(self)
        self.cocoa_danmaku_type1_effects = []
        for i in range(0,10):
            ch = "images/boss/Cocoa/cocoa_danmaku_type2_0" + str(i) + ".png"
            self.cocoa_danmaku_type1_effects.append(pygame.image.load(ch).convert_alpha())
        self.image = self.cocoa_danmaku_type1_effects[0]
        self.direction = danmaku.direction
        self.center = danmaku.center
        self.rect = self.cocoa_danmaku_type1_effects[0].get_rect()
        self.rect.left = self.center[0] - 10
        self.rect.top = self.center[1] - 10
        self.speed = danmaku.speed
        self.lifetime = 30
    
    def move(self):
        self.center[0] += self.speed * self.direction[0]
        self.center[1] += self.speed * self.direction[1]
        self.rect.left = self.center[0] - self.lifetime/5 * self.direction[0]
        self.rect.top = self.center[1] - self.lifetime/5 * self.direction[1]
        self.image = self.cocoa_danmaku_type1_effects[9 - self.lifetime//3]

class cocoa_bomb(pygame.sprite.Sprite):
    def __init__(self):
        pass

class Cocoa(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        if platform.system() == 'Windows':
            oimage1 = pygame.image.load("images\\boss\\Cocoa\\Cocoa_00.png").convert_alpha()
            oimage2 = pygame.image.load("images\\boss\\Cocoa\\Cocoa_01.png").convert_alpha()
            oimage3 = pygame.image.load("images\\boss\\Cocoa\\Cocoa_02.png").convert_alpha()
            #self.illustraction = pygame.image.load("image\\boss\\Cocoa\\Cocoa_tachie.png").convert_alpha()
        if platform.system() == 'Linux' or platform.system()=='Darwin':
            oimage1 = pygame.image.load("images/boss/Cocoa/Cocoa_00.png").convert_alpha()
            oimage2 = pygame.image.load("images/boss/Cocoa/Cocoa_01.png").convert_alpha()
            oimage3 = pygame.image.load("images/boss/Cocoa/Cocoa_02.png").convert_alpha()
            #self.illustraction = pygame.image.load("images/boss/Cocoa/Cocoa_tachie.png").convert_alpha()
        
        self.image = pygame.transform.scale(oimage2, (60,75))
        #self.image = oimage2
        self.name = "cocoa"
        self.rect = self.image.get_rect()
        self.center = [255.0, 100.0]
        self.temp_position = [255, 100]
        self.direction = [0, -1]
        self.rect.left = self.center[0] - 30
        self.rect.top = self.center[1] - 37
        
        self.speed = 2
        self.radius = 20
        
        self.collide = 1
        self.hp = 1000
        self.max_hp = 1000
        self.spell = 3
        self.crash = 9
        self.energy = 90
        self.spell_time = 0
        
        self.bgm = pygame.mixer.music
        self.bgm.load("bgm/Rabi-Ribi Original Soundtrack - 36 Get On With It.ogg")
        
    def move(self):
        if self.temp_position[0] < 50:
            self.temp_position[0] = 50
        elif self.temp_position[0] > 420:
            self.temp_position[0] = 420
        if self.temp_position[1] < 50:
            self.temp_position[1] = 50
        elif self.temp_position[1] > 200:
            self.temp_position[1] = 200
        
        distance = sqrt( \
                        (self.center[0] - self.temp_position[0]) ** 2 + \
                        (self.center[1] - self.temp_position[1]) ** 2 )
        if distance:
            self.direction = [
                            (self.temp_position[0] - self.center[0]) / distance, 
                            (self.temp_position[1] - self.center[1]) / distance ]
            self.speed = log(distance + 1)/3
        else:
            self.speed = 0
        self.center[0] += self.direction[0] * self.speed
        self.center[1] += self.direction[1] * self.speed
        self.rect.left = self.center[0] - 30
        self.rect.top = self.center[1] - 37
    
    def damage(self, shouting_group):
        for each in shouting_group:
            self.hp -= each.damage
        if self.hp < 0:
            self.hp = 0
            self.spell -= 1
    
    def cocoa_spell_1(self, difficulty, me_erina, boss_group, birth_group, effects_group):
        if self.spell_time < 1800:
            temp_time = self.spell_time % 120
            if temp_time:
                if temp_time%10 == 1 and temp_time<62:
                    temp_snipe = functions.snipe(self, me_erina)
                    offset = randint(-10,10)
                    for i in range(-8,9):
                        temp_danmaku = cocoa_danmaku_1(self.center)
                        temp_danmaku.center = [self.center[0], self.center[1]]
                        temp_danmaku.direction = [cos(temp_snipe + i*pi/32 + pi*offset/320), sin(temp_snipe + i*pi/32 + pi*offset/320)]
                        birth_group.add(temp_danmaku)
            else:
                pass
                self.temp_position[0] = randint(50,380)
                self.temp_position[1] = randint(50,160)
        self.spell_time += 1
