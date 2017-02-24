import pygame
import math
import functions
import pickle
import os
from functions import *

class Boss(pygame.sprite.Sprite):
    """
    use almost all the boss.
    """
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        """
        specify the name of the sprite
        """
        self.name = name
        """
        the buffs boss have.
        """
        self.buff = functions.buff_debuff.BuffGroup()
        """
        boss bgm specify
        """
        self.bgm = pygame.mixer.music
        """
        if boss in invincible,
        resist all damage
        """
        self.invincible = 0
        """
        use for animation
        """
        self.frame_count = 0
        self.timer = 0
    
    def SetSource(self, file_name):
        """
        specify the pictures that the boss sprite used
        boss size will be locked on 70*70 pixs
        
        boss stayed picture have 5 frames
        boss turn left or right have 2 frames
        
        boss illustration have 3 frames
        
        all the illustration will be turned into surface type and write in a file.
        each boss have their own file.
        """
        self.load_source(file_name)
        self.__illustration_count = len(self.images['illustration'])
        self.__pixel_count = len(self.images['pixel'])
        self.__illustration = self.images['illustration']
        self.__pixel = self.images['pixel']
        self.__pixel_frame = 0
        """
        define image information and default position
        """
        self.image = self.__pixel[self.__pixel_frame]   # image will use in a list
        self.rect = self.image.get_rect()
        self.direction = [0,-1]
        self.center = [-35.0, 35.0]
        self.temp_position = [255.0, 100.0]
        self.rect.top = self.center[0] - 35
        self.rect.left = self.center[1] - 35
    
    def SetValue(self, max_hp, crash_damage, bonus_energy):
        """
        define the local property for every boss.

        all of the value will be changed var local difficulty
        """
        self.max_hp = max_hp
        self.hp = int(self.max_hp)
        self.crash_damage = crash_damage
        self.bonus_energy = bonus_energy
        """
        special value
        """
        self.collide = True
        self.in_screen = True
        self.speed = 0
        self.radius = 25
        self.defense = 1.00
    
    def SetSpell(self, *spell_list):
        """
        spell card count.
        the number will be different by local difficulty
        all spell and not-spell will all mark as spell card
        """
        self.spell_count = len(spell_list)
        """
        specify the time for each spell
        use a list to store spell time (second*frames)
        """
        self.spell_time = list(spell_list)
    
    def InScreenCheck(self):
        """
        boss position usually stay in rect (50-420) (50-200)
        """
        if self.temp_position[0] < 50:
            self.temp_position[0] = 50
        elif self.temp_position[0] > 420:
            self.temp_position[0] = 420
        if self.temp_position[1] < 50:
            self.temp_position[1] = 50
        elif self.temp_position[1] > 200:
            self.temp_position[1] = 200
    
    def move(self):
        """
        move functions
        
            sprite's temp_position sets a destination for itself
            and use temp_position and center (last frame)
            to calculate the direction and speed
        """
        distance = sqrt( \
                        (self.center[0] - self.temp_position[0]) ** 2 + \
                        (self.center[1] - self.temp_position[1]) ** 2 )
        if distance:
            self.direction = [
                            (self.temp_position[0] - self.center[0]) / distance, 
                            (self.temp_position[1] - self.center[1]) / distance ]
            self.speed = math.log(distance + 1.0)/3
        else:
            self.speed = 0
        if self.in_screen:
            self.InScreenCheck()
        self.center[0] += self.direction[0] * self.speed
        self.center[1] += self.direction[1] * self.speed
        self.rect.left = self.center[0] - 35
        self.rect.top = self.center[1] - 35 + 5*math.sin(6.28*self.frame_count/100)
        self.Frame_Count()

    def collide_check(self, shouting_group):
        if self.collide:
            temp = pygame.sprite.spritecollide(each, self, True, pygame.sprite.collide_circle)
            each.damage(temp)

    def damage(self, shouting_group):
        """
        check the ribbon magic danmaku damage.
        when hp<0, spell count minus 1 and 3 seconds in invincible
        """
        
        if self.buff.defense_large_boost:
            self.defense = 0.1
        elif self.buff.defense_boost:
            self.defense = 0.5
        elif self.buff.defense_up:
            self.defense = 0.75
        else:
            self.defense = 1

    def spell_attack(self, difficulty, me_erina, boss_group, birth_group, effects_group):
        """
        prepared for every instance.
        """
        pass

    def change_image(self):
        if not self.frame_count % 12:
            self.__pixel_frame += 1
            if self.__pixel_frame >= self.__pixel_count:
                self.__pixel_frame = 0
        self.image = self.__pixel[self.__pixel_frame]
 
    def Frame_Count(self):
        """
        some animations spell a time
        """
        self.frame_count += 1
        if self.frame_count == 300:
            self.frame_count = 0

    def load_source(self, file_name):
        sources = pickle.load(open(file_name, 'rb'))
        self.images = {'illustration':[], 'pixel':[], 'special':[]}
        for i in range(len(sources['illustration'])):
            img_name = 'data/tmp/imgs/' + self.name + '_illustration_' + str(i) + '.tmp'
            try:
                img_file = open(img_name, 'wb')
            except:
                os.mkdir('data/tmp/imgs/')
                img_file = open(img_name, 'wb')
            img_file.write(sources['illustration'][i])
            img_file.close()
            self.images['illustration'].append(pygame.image.load(img_name).convert_alpha())
        for i in range(len(sources['pixel'])):
            img_name = 'data/tmp/imgs/' + self.name + '_pixel_' + str(i) + '.tmp'
            try:
                img_file = open(img_name, 'wb')
            except:
                os.makedirs('data/tmp/imgs')
                img_file = open(img_name, 'wb')
            img_file.write(sources['pixel'][i])
            img_file.close()
            self.images['pixel'].append(pygame.image.load(img_name).convert_alpha())
        for i in range(len(sources['special'])):
            img_name = 'data/tmp/imgs/' + self.name + '_special_' + str(i) + '.tmp'
            try:
                img_file = open(img_name, 'wb')
            except:
                os.makedirs('data/tmp/imgs/')
                img_file = open(img_name, 'wb')
            img_file.write(sources['special'][i])
            img_file.close()
            self.images['special'].append(pygame.image.load(img_name).convert_alpha())
        try:
            misc_name = 'data/tmp/misc/' + self.name + '.tmp'
            try:
                misc_file = open(misc_name, 'wb')
            except:
                os.makedirs('data/tmp/misc/')
                misc_file = open(misc_name, 'wb')
            misc_file.write(sources['music'])
            misc_file.close()
            self.bgm.load(misc_name)
    
    def clear_cache(self):
        os.system("del data/tmp/imgs/*.tmp")
        os.system("del data/tmp/misc/*.tmp")
    

class Danmaku(pygame.sprite.Sprite):
    """
    specify most any danmaku type.
    only danmaku be defined there.
    lazer danmaku next
    """
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        """
        to distinguish with other type of danmaku
        """
        self.buff_catch = functions.buff_debuff.Buff()
        """
        specify when miss opponite will have some buff or debuff
        """
        self.birth_time = 10
        """
        any danmaku have their birth time.
        before birth time have no damage.
        """
        self.live_time = -1
        """
        some lazer will use this
        """
        # music not specify

    def SetImage(self, pixel, birth_pixel):
        """
        specify the pictures that danmaku sprite used.
        danmaku size will locked on a square shape

        some long danmaku also use circle collide check
        different color use different sprite.

        birth image will not at a size
        """
        self.__pixel = pixel
        self.__pixel_count = len(pixel)
        self.__birth_pixel = birth_pixel

        self.image = self.__birth_pixel[0] # sometimes have more than 1 frame
        self.rect = self.image.get_rect()

        self.speed = 0
        self.direction = [0.0, -1.0]

    def SetValue(self, damage, energy, radius, birth_position):
        """
        define local damage, removing energy, and birth position
        """
        self.damage = damage
        self.energy = energy
        self.birth_position = birth_position
        self.radius = radius

        self.center = list(self.birth_position)
        self.rect.left = self.center[0] - self.rect.width/2
        self.rect.top = self.center[1] - self.rect.height/2
        """
        special value
        """
        self.collide = True
        self.collide_delete = True
        self.delete = False
        self.inscreen = True

    def SetLiveCheck(self, left, right, top, bottom):
        """
        when danmaku move out of this area,
        change delete count
        free this sprite to save ram space
        """
        self.left_border = left
        self.right_border = right
        self.top_border = top
        self.bottom_border = bottom 

    def live_check(self):
        """
        most danmaku have a constant moving area.
        """
        if not self.live_time:
            self.delete = True
        elif self.center[0] < self.left_border or self.center[0] > self.right_border:
            self.delete = True
        elif self.center[1] < self.top_border or self.center[1] > self.bottom_border:
            self.delete = True
        else:
            self.delete = False

    def move(self):
        """
        move function:

            it's different from boss sprite.
            it only can controled by speed and direction!
        """
        self.center[0] += self.speed * self.direction[0]
        self.center[1] += self.speed * self.direction[1]
        self.rect.left = self.center[0] - self.rect.width/2
        self.rect.top = self.center[1] - self.rect.height/2
        if self.live_time > 0:
            self.live_time -= 1

###

class Elf(pygame.sprite.Sprite):
    """
    use for almost all mid boss
    """
    def __init__(self, file_name):
        pygame.sprite.Sprite.__init__()
        self.buff = functions.buff_debuff.BuffGroup()
        self.invincible = 0
        self.frame_count = 0
        self.timer = 0

    def SetSource(self, file_name):
        self.load_source(file_name)
        self.__pixel_count = len(self.images['pixel'])
        self.__pixel = len(self.images['pixel'])
        self.__pixel_frame = 0
        self.image = self.__pixel[self.__pixel_count]
        self.rect = self.image.get_rect()
        self.temp_position = [-10.0,-10.0]
        self.center = [-10.0, 10.0]
        self.rect.top = self.center[0] - 10
        self.rect.left = self.center[1] - 10

    def SetValue(self, max_hp, crash_damage, bonus_energy):
        self.max_hp = max_hp
        self.hp = int(self.max_hp)
        self.crash_damage = crash_damage
        self.bonus_energy = bonus_energy
        self.collide = True
        self.in_screen = False
        self.speed = 0
        self.radius = 8
        self.defense = 1.0

    def move(self):
        distance = sqrt( \
                        (self.center[0] - self.temp_position[0]) ** 2 + \
                        (self.center[1] - self.temp_position[1]) ** 2 )
        if distance:
            self.direction = [
                            (self.temp_position[0] - self.center[0]) / distance, 
                            (self.temp_position[1] - self.center[1]) / distance ]
            self.speed = math.log(distance + 1.0)/3
        else:
            self.speed = 0
        self.center[0] += self.direction[0] * self.speed
        self.center[1] += self.direction[1] * self.speed
        self.rect.left = self.center[0] - 35
        self.rect.top = self.center[1] - 35 + 5*math.sin(6.28*self.frame_count/100)
        self.Frame_Count()
