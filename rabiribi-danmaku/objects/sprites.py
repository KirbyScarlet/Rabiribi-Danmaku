import pygame
import math
import pickle
import os
import abc
import functions
from objects.action import DanmakuAction
from objects.action import direction
from functions.values import screenborder
from functions import snipe
from math import pi
import time

class position(list):
    def __init__(self):
        self.x = 0
        self.y = 0

    def set(self, value):
        if len(value)!=2:
            raise TypeError
        if isinstance(value, (tuple, list)):
            self.x, self.y = value
        elif isinstance(value, pygame.sprite.Sprite):
            self.x, self.y = tuple(value.center)
        else:
            raise TypeError

    def __getitem__(self, y):
        if y==0:
            return self.x
        elif y==1:
            return self.y
        else:
            raise IndexError

class Damage(object):
    """
    store damage per frame

    see ../functions/values.py
    """
    def __init__(self, sprite):
        self.sprite = sprite
        #=====================
        self.danmaku = 0
        self.crash = 0
        self.amulet = 0
        self.cocoabomb = 0
        self.boost = 0
        self.poison = 0
        self.burn = 0
        self.curse = 0
        self.reflect = 0
        self.endurance = 0
        self.instant = 0
        #=====================
        self.all_damage = 0

    def physical(self, value):
        pass

    def accident(self, value):
        pass

    def weapen(self, value, type):
        pass

    def buff(self, value, type):
        pass

    def __setattr__(self, name, value):
        super().__setattr__('all_damage', value)
        if name == 'danmaku':
            self.physical(value)
        elif name == 'crash':
            self.accident(value)
        elif name in ('amulet', 'cocoabomb', 'boost'):
            self.weapen(value, name)
        elif name in ('poison', 'burn', 'curse', 'reflect', 'endurance', 'instane'):
            self.buff(value, name)
        return super().__setattr__(name, value)

    def __call__(self, screen):
        """
        calculate all damage and print count on screen
        """
        pass

class Boss(pygame.sprite.Sprite):
    """
    use almost all the boss.
    """
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        """
        specify the name of the sprite
        """
        self.buff = functions.buff_debuff.BuffGroup()
        """
        the buffs boss have.
        """
        self.bgm = pygame.mixer.music
        """
        boss bgm specify
        """
        self.invincible = 0
        """
        if boss in invincible,
        resist all damage
        """
        self.frame_count = 0
        """
        use for animation
        """
        self.timer = 0
    
    def SetLevel(self, erina, difficulty):
        """
        specify attack damage, crash danmage, local difficulty
        """
        # under development
        self.level = 0

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
        self.illustration_count = len(self.images['illustration'])
        self.pixel_count = len(self.images['pixel'])
        self.illustration = self.images['illustration']
        self.pixel = self.images['pixel']
        self.pixel_frame = 0
        """
        define image information and default position
        """
        self.image = self.pixel[self.pixel_frame]   # image will use in a list
        self.rect = self.image.get_rect()
        self.center = [-35.0, 35.0]
        self.direction = direction()
        self.temp_position = [255.0, 100.0]
        self.rect.top = self.center[0] - 35
        self.rect.left = self.center[1] - 35
    
    # new framework useless
    def SetDanmakuUse(self, *danmaku_name):
        """
        specify danmaku that boss used
        """
        temp_image = {'birth':[], 'live':[]}
        self.danmaku_images = {}
        for each in danmaku_name:
            file_name = "data/obj/danmaku/" + each + ".rbrb"
            f = open(file_name, 'rb')
            sources = pickle.load(f)
            f.close()
            self.danmaku_images[each] = temp_image
            for i in range(len(sources['birth'])):
                img_name = 'data/tmp/imgs/' + each + '_rank_' + str(i) + '.tmp'
                try:
                    f = open(img_name, 'wb')
                except:
                    os.makedirs('data/tmp/imgs/')
                    f = open(img_name, 'wb')
                f.write(sources['birth'][i])
                f.close()
                self.danmaku_images[each]['birth'].append(pygame.image.load(img_name).convert_alpha())
            for i in range(len(sources['live'])):
                img_name = 'data/tmp/imgs/' + each + '_rank_' + str(i) + '.tmp'
                try:
                    f = open(img_name, 'wb')
                except:
                    os.makedirs('data/tmp/imgs/')
                    f = open(img_name, 'wb')
                f.write(sources['live'][i])
                f.close()
                self.danmaku_images[each]['live'].append(pygame.image.load(img_name).convert_alpha())

    def SetValue(self, max_hp, crash_damage, bonus_energy):
        """
        define the local property for every boss.

        all of the value will be changed var local difficulty
        """
        self.max_hp = max_hp
        self.hp = int(self.max_hp)
        self.crash_damage = crash_damage
        self.bonus_energy = bonus_energy
        self.damage_per_frame = 0
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
        self.spell_group = functions.spell_card.SpellGroup()
        self.spell_count = len(spell_list)
        """
        specify the time for each spell
        use a list to store spell time (second*frames)
        """
        self.spell_time = list(spell_list)
        self.spell_now = 1
    
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
    
    def move(self, *erina):
        """
        move functions
        
            sprite's temp_position sets a destination for itself
            and use temp_position and center (last frame)
            to calculate the direction and speed
        """
        distance = math.sqrt(
                        (self.center[0] - self.temp_position[0]) ** 2 + \
                        (self.center[1] - self.temp_position[1]) ** 2 )
        if distance:
            self.direction.set(functions.snipe(self.center, self.temp_position))
            self.speed = math.log(distance + 1.0)
        else:
            self.speed = 0
        if self.in_screen:
            self.InScreenCheck()
        self.center[0] += self.direction.x * self.speed
        self.center[1] += self.direction.y * self.speed
        self.rect.left = self.center[0] - 35
        self.rect.top = self.center[1] - 35 + 5*math.sin(6.28*self.frame_count/100)
        self.change_image()
        self.Frame_Count()

    def print_screen(self, screen):
        screen.blit(self.image, self.rect)

    def collide_check(self, shouting_group):
        if self.collide:
            temp = pygame.sprite.spritecollide(self, shouting_group, True, pygame.sprite.collide_circle)
            
            self.damage_check(temp)

    def damage_check(self, shouting_group):
        """
        check the ribbon magic danmaku damage.
        when hp<0, spell count minus 1 and 3 seconds in invincible
        """
        '''
        if 'defense_large_boost' in self.buff:
            self.defense = 0.1
        elif 'defense_boost' in self.buff:
            self.defense = 0.5
        elif 'defense_up' in self.buff:
            self.defense = 0.75
        else:
            self.defense = 1
            '''
        for each in shouting_group:
            self.hp -= each.damage * self.defense

    def spell_attack(self, difficulty, erina, birth_group, boss_group, illustration_group, danmaku_group):
        """
        prepared for every instance.
        """
        if self.hp > 0 and self.spell_group.__getattribute__('spell_' + str(self.spell_now)).timer < self.spell_group.__getattribute__('spell_' + str(self.spell_now)).spell_time:
            self.spell_group.__getattribute__('spell_' + str(self.spell_now))(difficulty, erina, birth_group, boss_group, illustration_group)
        elif self.hp <= 0 or self.spell_group.__getattribute__('spell_' + str(self.spell_now)).timer == self.spell_group.__getattribute__('spell_' + str(self.spell_now)).spell_time:
            for sprite in danmaku_group:
                sprite.kill()
            for sprite in birth_group:
                sprite.kill()
            self.hp = self.max_hp
            self.spell_now += 1
        if self.spell_now > self.spell_group.count:
            self.death()

    def change_image(self):
        if not self.frame_count % 12:
            self.pixel_frame += 1
            if self.pixel_frame >= self.pixel_count:
                self.pixel_frame = 0
        self.image = self.pixel[self.pixel_frame]
    
    def Frame_Count(self):
        """
        some animations spell a time
        """
        self.frame_count += 1
        if self.frame_count == 300:
            self.frame_count = 0

    def death(self):
        self.kill()

    def load_source(self, file_name):
        f = open('data/obj/boss/' + file_name, 'rb')
        sources = pickle.load(f)
        f.close()
        self.images = {'illustration':[], 'pixel':[], 'special':[]}
        for i in range(len(sources['illustration'])):
            img_name = 'data/tmp/imgs/' + self.name + '_illustration_' + str(i) + '.tmp'
            try:
                img_file = open(img_name, 'wb')
            except:
                os.makedirs('data/tmp/imgs/')
                img_file = open(img_name, 'wb')
            img_file.write(sources['illustration'][i])
            img_file.close()
            self.images['illustration'].append(pygame.image.load(img_name).convert_alpha())
        for i in range(len(sources['pixel'])):
            img_name = 'data/tmp/imgs/' + self.name + '_pixel_' + str(i) + '.tmp'
            try:
                img_file = open(img_name, 'wb')
            except:
                os.makedirs('data/tmp/imgs/')
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
        except:
            del self.bgm

    def clear_cache(self):
        os.system("del data/tmp/imgs/" + self.name + "*.tmp")
        os.system("del data/tmp/misc/" + self.name + "*.tmp")

class Danmaku(pygame.sprite.Sprite, DanmakuAction):
    __metaclass__ = abc.ABCMeta
    """
    specify most of danmaku type.
    only danmaku be defined there.
    lazer next
    """
    def __init__(self, 
                birth_group, birth_place, *args, 
                birth_time=10, lazer=-1,
                birth_place_offset = ((0),0), 
                danmaku_layer = 0, 
                birth_speed = 1.0, 
                direction = pi/2, 
                direction_offset = 0, 
                time_rip = False, 
                **kwargs):
        pygame.sprite.Sprite.__init__(self, birth_group)
        DanmakuAction.__init__(self, birth_place, *args, 
                                birth_place_offset=birth_place_offset, 
                                danmaku_layer=danmaku_layer, 
                                birth_speed=birth_speed, 
                                direction=direction, 
                                direction_offset=direction_offset, 
                                time_rip=time_rip, 
                                **kwargs)
        self.buff_catch = functions.buff_debuff.BuffGroup()
        """
        specify when miss opponite will have some buff or debuff
        """
        self.birth_time = birth_time
        """
        any danmaku have their birth time.
        before birth time have no damage.
        """
        self.live_time = lazer
        """
        some lazer will use this
        """
        self.timer = 0
        self.SetImage()
        #print('danmaku instance:', self.speed, self.center, self.direction)

        # music not specify
    
    def SetImage(self):
        """
        specify the pictures that danmaku sprite used.
        danmaku size will locked on a square shape

        some long danmaku also use circle collide check
        different color use different sprite.

        birth image will not at a size
        """
        #self.images = {'birth':[], 'live':[]}
        #if not self.read_source(danmaku_name, birth_frame, live_frame):
        #    self.load_source(danmaku_name)
        #    self.read_source(danmaku_name, birth_frame, live_frame)
        #self.load_source(danmaku_name)
        self.pixel = self.images['live']
        self.pixel_count = len(self.images['live'])
        self.birth = self.images['birth']
        self.birth_count = len(self.images['birth'])

        self.image = self.birth[0] # sometimes have more than 1 frame
        self.rect = self.image.get_rect()

        self.rect.left = self.center[0] - self.rect.width/2
        self.rect.top = self.center[1] - self.rect.height/2

    def SetValue(self, damage, energy, radius, image_change_fps=0, image_change_rotation=0):
        """
        define local damage, removing energy, and birth position
        """
        self.damage = damage
        self.energy = energy
        self.radius = radius

        """
        special value
        """
        self.image_change_fps = image_change_fps
        self.image_change_rotation = image_change_rotation
        self.live_time = -1
        self.collide = True
        self.collide_delete = True
        self.delete = False
        self.inscreen = True
        
    def SetLiveCheck(self, 
                     left = screenborder.SCREEN_LEFT, 
                     right = screenborder.SCREEN_RIGHT, 
                     top = screenborder.SCREEN_TOP, 
                     bottom = screenborder.SCREEN_BOTTOM,
                     live_time = -1):
        """
        when danmaku move out of this area,
        change delete count
        free this sprite for save ram space
        """
        self.left_border = left - self.rect.width/2
        self.right_border = right + self.rect.width/2
        self.top_border = top - self.rect.height/2
        self.bottom_border = bottom + self.rect.height/2
        self.live_time = live_time

    @classmethod
    def load_source(self, danmaku_name):
        """
        load sources functions
        class method

            load_source(danmaku_name): return None
        """
        self.images = {'birth':[], 'live':[]}
        f = open('data/obj/danmaku/' + danmaku_name + '.rbrb', 'rb')
        sources = pickle.load(f)
        f.close()
        for i in range(len(sources['birth'])):
            img_name = 'data/tmp/imgs/' + danmaku_name + '_birth_rank_' + str(i) + '.tmp'
            try:
                f = open(img_name, 'wb')
            except:
                os.makedirs('data/tmp/imgs/')
                f = open(img_name, 'wb')
            f.write(sources['birth'][i])
            f.close()
            self.images['birth'].append(pygame.image.load(img_name).convert_alpha())
        for i in range(len(sources['live'])):
            img_name = 'data/tmp/imgs/' + danmaku_name + '_live_rank_' + str(i) + '.tmp'
            try:
                f = open(img_name, 'wb')
            except:
                os.makedirs('data/tmp/imgs/')
                f = open(img_name, 'wb')
            f.write(sources['live'][i])
            f.close()
            self.images['live'].append(pygame.image.load(img_name).convert_alpha())

    '''
    def read_source(self):
        """
        read sources method:
            
            read_source(danmaku_name): return Bool

        if false, load sources first
        """
        for i in range(birth_frame):
            img_name = 'data/tmp/imgs/' + danmaku_name + '_birth_rank_' + str(i) + '.tmp'
            try: 
                self.images['birth'].append(pygame.image.load(img_name).convert_alpha())
            except:
                if i == 0:
                    return False
                break
        for i in range(live_frame):
            img_name = 'data/tmp/imgs/' + danmaku_name + '_live_rank_' + str(i) + '.tmp'
            try:
                self.images['live'].append(pygame.image.load(img_name).convert_alpha())
            except:
                if i == 0:
                    return False
        return True
    '''

    def image_change(self):
        """
        """
        if self.birth_time:
            if self.birth_time > 2:
                self.image = self.images['birth'][10-self.birth_time]
            else:
                self.image = self.images['birth'][8]
        else:
            if not self.image_change_fps:
                pass
            else:
                if self.timer % fps == 0:
                    self.image = self.images['live'][(self.timer/self.image_change_fps)%self.pixel_count]
                    self.image = pygame.transform.rotate(self.image, self.rotation)
        if not self.image_change_rotation:
            pass
        else:
            self.rotation += self.image_chagne_rotation
            self.image = pygame.transform.rotate(self.image, self.image_change_rotation)

    def live_check(self):
        """
        most danmaku have a constant moving area.
        """
        if self.live_time > 0:
            self.live_time -= 1
        if not self.live_time:
            self.delete = True
        elif self.rect.right < self.left_border or self.rect.left > self.right_border:
            self.delete = True
        elif self.rect.bottom < self.top_border or self.rect.top > self.bottom_border:
            self.delete = True
        else:
            self.delete = False

    def birth_check(self):
        if self.birth_time > 0:
            self.birth_time -= 1

    def death(self):
        """
        death animation
        """
        pass

    def move(self, *erina):
        """
        move function:

            it's different from boss sprite.
            it only can controled by speed and direction!
        """
        self.time_rip(*erina)
        self.image_change()
        self.center[0] += self.speed * self.direction.x
        self.center[1] += self.speed * self.direction.y
        self.rect.left = self.center[0] - self.rect.width/2
        self.rect.top = self.center[1] - self.rect.height/2
        self.birth_check()
        self.live_check()
        self.timer += 1

    def print_screen(self, screen):
        screen.blit(self.image, self.rect)

###

class Elf(pygame.sprite.Sprite):
    __metaclass__ = abc.ABCMeta
    """
    use for almost all mid boss
    """
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.buff = functions.buff_debuff.BuffGroup()
        self.invincible = 0
        self.frame_count = 0
        self.timer = 0
        #self.SetSource(file_name)

    def SetSource(self):
        """
        SetSource(file_name): return None
        """
        #self.load_source(file_name)
        self.pixel_count = len(self.images['pixel'])
        self.pixel = self.images['pixel']
        self.pixel_frame = 0
        self.image = self.pixel[self.pixel_count]
        self.rect = self.image.get_rect()
        self.direction = direction()
        self.temp_position = [-10.0,-10.0]
        self.center = [-10.0, 10.0]
        self.rect.top = self.center[0] - 10
        self.rect.left = self.center[1] - 10

    def SetValue(self, max_hp, crash_damage, bonus_energy):
        """
        SetValue(max_hp, crash_damage, bonus_energy): return None

        specify parament for elf
        """
        self.max_hp = max_hp
        self.hp = int(self.max_hp)
        self.crash_damage = crash_damage
        self.bonus_energy = bonus_energy
        self.collide = True
        self.in_screen = False
        self.live_time = -1
        self.speed = 0
        self.radius = 8
        self.defense = 1.0

    def move(self, *erina):
        distance = sqrt( \
                        (self.center[0] - self.temp_position[0]) ** 2 + \
                        (self.center[1] - self.temp_position[1]) ** 2 )
        if distance:
            self.direction.set(functions.snipe(self.temp_position, self.center))
            self.speed = math.log(distance + 1.0)/3
        else:
            self.speed = 0
        self.center[0] += self.direction.x * self.speed
        self.center[1] += self.direction.y * self.speed
        self.rect.left = self.center[0] - 35
        self.rect.top = self.center[1] - 35 + 5*math.sin(6.28*self.frame_count/100)
        self.Frame_Count()

    @classmethod
    def load_source(self, file_name):
        f = open('data/obj/elf/' + file_name + '.rbrb' ,'rb')
        sources = pickle.load(f)
        f.close()
        self.images = {"pixel":[]}
        for i in range(len(sources['pixel'])):
            img_name = 'data/tmp/imgs/' + file_name + '_pixle' + str(i) + '.tmp'
            try:
                img_file = open(img_name, 'wb')
            except:
                os.makedirs('data/tmp/imgs/')
                img_file = open(img_name, 'wb')
            img_file.write(sources['pixel'][i])
            img_file.close()
            self.images['pixel'].append(pygame.image.load(img_name).convert_alpha())

    def change_image(self):
        if not self.frame_count %12:
            self.pixel_frame += 1
            if self.pixel_frame >= self.pixel_count:
                self.pixel_frame = 0
        self.image = self.pixel[self.pixel_frame]
        
    def attack(self, difficulty, erina, birth_group, elf_group, danmaku_group):
        """
        specify attack methods
        """
        self.__getattribute__("attack_"+difficulty)(difficulty, erina, birth_group, elf_group, danmaku_group)

    def attack_easy(self, difficulty, erina, brith_group, elf_group, danmaku_group):
        pass

    def attack_normal(self, difficulty, erina, brith_group, elf_group, danmaku_group):
        pass

    def attack_hard(self, difficulty, erina, brith_group, elf_group, danmaku_group):
        pass

    def attack_hell(self, difficulty, erina, brith_group, elf_group, danmaku_group):
        pass

    def attack_bunny(self, difficulty, erina, brith_group, elf_group, danmaku_group):
        pass

    def print_screen(self, screen):
        screen.blit(self.image, self.rect)
