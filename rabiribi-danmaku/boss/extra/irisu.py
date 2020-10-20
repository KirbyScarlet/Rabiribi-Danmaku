import pygame
import math
import random
import platform
import functions.buff_debuff
from random import *
from math import *

class Irisu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        if platform.system()=='Windows':
            oimage = pygame.image.load("images\\boss\\Irisu\\Irisu.png")
        if platform.system()=='Linux' or platform.system()=='Darwin':
            oimage = pygame.image.load("images/boss/Irisu/Irisu.png")
        self.image = pygame.transform.scale(oimage, (60,75))
        self.rect = self.image.get_rect()
        self.speed = 1
        self.center = [225, 100]
        self.rect.left = self.center[0] - 30
        self.rect.top = self.center[1] - 37
        self.buff = functions.buff_debuff.BuffGroup()
        self.bgm = pygame.mixer.music
        #self.bgm.load("bgm/Rabi-Ribi Original Soundtrack - 46 RFN - III.ogg")

    def move(self, frame_count):
        #self.center[1] += sin(6.28*frame_count/100)
        self.rect.left = self.center[0] - 30
        self.rect.top = self.center[1] - 37 + 5*sin(6.28*frame_count/100)

class Irisu_danmaku_type_1(pygame.sprite.Sprite):
    def __init__(self, boss_position):
        pygame.sprite.Sprite.__init__(self)
        
        if platform.system()=='Windows':
            self.image = pygame.image.load("images\\boss\\Irisu\\Irisu_danmaku_1.png").convert_alpha()
        if platform.system()=='Linux' or platform.system()=='Darwin':
            self.image = pygame.image.load("images/boss/Irisu/Irisu_danmaku_1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.center = [float(boss_position[0]), float(boss_position[1])]
        self.rect.left = self.center[0] - 10
        self.rect.top = self.center[1] - 10
        self.special = [0,0,0]
        self.counter = 0
        self.direction = [float(0), float(0)]
        self.distance_judge = 1
        self.speed = float(0)
        self.radius = 5
    """
    def birth(self, boss_position):
        self.center = boss_position
        self.temp_biu = []
        randseed = randint(0,628)
        self.danmaku_count = 8
        for i in range(self.danmaku_count):
            #self.center = Irisu.center
            self.direction = 1
            self.direction = [cos(randseed + 628/self.danmaku_count * i), \
                              sin(randseed + 628/self.danmaku_count * i)]
            self.special = i % 2
            self.temp_biu.append(self)
    """
    def type1_move(self, center_position):
        self.distance = sqrt( \
                            (self.center[0] - float(center_position[0])) ** 2 + \
                            (self.center[1] - float(center_position[1])) ** 2)
        if self.distance < 148:
            self.speed = 7/250000 * self.distance**2 - 7/250 * self.distance  + 7.01
        #elif self.distance > 148 and self.distance < 150:
        #    self.speed = 0.01
        elif self.distance > 150:
            self.speed = 0.7 * atan(self.distance-105 / 100) 
            if self.distance_judge:
                self.speed = 1 * atan(self.distance-105 / 100) 
                if self.special[0]%2:
                    self.direction = [cos((self.special[2]*2 + 628/(float(self.special[1])) * self.special[0]) / 100 + pi/4), \
                                      sin((self.special[2]*2 + 628/(float(self.special[1])) * self.special[0]) / 100 + pi/4)]
                else:
                    self.direction = [cos((self.special[2]*2 + 628/(float(self.special[1])) * self.special[0]) / 100 - pi/4), \
                                      sin((self.special[2]*2 + 628/(float(self.special[1])) * self.special[0]) / 100 - pi/4)]
            self.distance_judge = 0
            
        self.center[0] += self.speed * self.direction[0]
        self.center[1] += self.speed * self.direction[1]
        self.rect.left = self.center[0] - 10
        self.rect.top = self.center[1] - 10
        
    def final_spell_move(self):
        self.center[0] += self.speed * self.direction[0]
        self.center[1] += self.speed * self.direction[1]
        self.rect.left = self.center[0] - 10
        self.rect.top = self.center[1] - 10
        
def Irisu_danmaku_type_1_birth(boss_position, danmaku_group, frame_count):
    global danmaku_birth_count
    global danmaku_birth_dealy
    global danmaku_birth_tag
    danmaku_birth_count = 80
    danmaku_birth_delay = 50
    if not frame_count % danmaku_birth_delay:
        for i in range(danmaku_birth_count):
            temp = Irisu_danmaku_type_1(boss_position)
            temp.special = [i, danmaku_birth_count, frame_count]
            temp.direction = [cos((frame_count*2 + 628/(float(danmaku_birth_count)) * i) / 100), \
                              sin((frame_count*2 + 628/(float(danmaku_birth_count)) * i) / 100)]
            danmaku_group.add(temp)

def Irisu_Final_Spell(erina_position, danmaku_group, run_control, time):
    global danmaku_birth_delay
    global danmaku_birth_tag
    screen_center = [225, 240]
    if time in [60, 240, 420, 600, 780, 900, 1020, 1140, 1260, 1380, 1500, 1620, 1740]:
    #if not time % 120 and False:
        randseed = randint(0,628)
        for i in range(48):
            temp = Irisu_danmaku_type_1([225, 240])
            temp.speed = 1
            temp.direction = [cos((randseed + 628/(48.0) * i) / 100), \
                              sin((randseed + 628/(48.0) * i) / 100)]
            temp.center = [225 + -temp.direction[0] * 300, 240 + -temp.direction[1] * 300]
            danmaku_group.add(temp)
            
    if time in [2200, 2320, 2440, 2560, 2680, 2800, 2920, 3040, 3160, 3280, 3400, 3520, 3640, 3760, 3880]:
    #if not time % 180 and False:
        randseed = randint(-16,16)
        for i in range(16):
            temp1 = Irisu_danmaku_type_1(screen_center)
            temp1.speed = 1
            temp1.direction = [-1,0]
            temp1.center = [450, 32*i + randseed]
            danmaku_group.add(temp1)
            
        randseed = randint(-16,16) 
        for i in range(16):
            temp2 = Irisu_danmaku_type_1(screen_center)
            temp2.speed = 1
            temp2.direction = [1,0]
            temp2.center = [-120, 32*i + randseed]
            danmaku_group.add(temp2)
        
        randseed = randint(-16,16)  
        for i in range(16):
            temp3 = Irisu_danmaku_type_1(screen_center)
            temp3.speed = 1
            temp3.direction = [0,-1]
            temp3.center = [32*i + randseed, 540]
            danmaku_group.add(temp3)
            
        randseed = randint(-16,16)
        for i in range(16):
            temp4 = Irisu_danmaku_type_1(screen_center)
            temp4.speed = 1
            temp4.direction = [0,1]
            temp4.center = [32*i + randseed, -180]
            danmaku_group.add(temp4)
            
    if time>4200 and time<6000:
    #if not time%10:
        if not time % 10:
            Speed = 1
            num = 8
            for i in range(num):
                temp = Irisu_danmaku_type_1(screen_center)
                temp.speed = Speed
                temp.direction = [cos((time + 628/num * i) / 100), \
                                  sin((time + 628/num * i) / 100)]
                temp.center = [225 + -temp.direction[0] * 300, 240 + -temp.direction[1] * 300]
                danmaku_group.add(temp)
