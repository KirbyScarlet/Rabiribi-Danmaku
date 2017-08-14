import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group
from functions.action import OptionAction
import pickle

from functions.values import defaultkey
from pygame.locals import *
from math import cos

class Key(object):
    def __init__(self):
        self.key_hold = None
        self.delay_hold = 50  # frame
        self.delay_switch = 12  # frame, max 12

    def delay(self, key):
        if self.key_hold == key:
            if self.delay_hold > 0:
                self.delay_hold -= 1
                return None
            else:
                if self.delay_switch == 12:
                    self.delay_switch -= 1
                    return self.key_hold
                elif self.delay_switch == 0:
                    self.delay_switch = 12
                    return None
                else:
                    self.delay_switch -= 1
                    return None
        else:
            self.key_hold = key
            self.delay_hold = 50
            self.delay_switch = 12
            return key

    def __call__(self, keypress):
        for key, value in keypress.items():
            if value:
                return self.delay(key)
        self.key_hold = None
        return None

class Option(Sprite, OptionAction):
    def __init__(self, name, rank, 
                    birth_place = (0,0), 
                    selected_position = (0,0), 
                    unselected_position = (0,0), 
                    rate_s = 2, 
                    rate_io = 4):
        """
        """
        Sprite.__init__(self)
        OptionAction.__init__(self, rank, birth_place,
                       selected_position,
                       unselected_position,
                       rate_s,
                       rate_io)
        #self.rank = rank    # small rank on top
        self.select = False
        self.timer = 0
        self.alpha = 155.0
        self.name = name
        try:
            self.image = pygame.image.load('data/tmp/imgs/'+name+'.tmp').convert_alpha()
        except pygame.error:
            # reload source ?
            with open('data/objs/opt/options.rbrb', 'rb') as f_i:
                t = pickle.load(f_i)
            for key, value in t.items():
                with open('data/tmp/'+key+'.tmp', 'wb') as f_o:
                    f_o.write(value)
                pass
        self.rect = self.image.get_rect()
        self.surface = pygame.surface.Surface((self.rect.width, self.rect.height)).convert()

    def move(self):
        if self.select:
            self.selected()
            self.alpha = 225.0 + 30*cos(self.timer/8)
        else:
            self.unselected()
            self.alpha = 155.0
        self.timer += 1
        self.rect.left, self.rect.top = self.center

    def __setattr__(self, name, value):
        if name == 'timer':
            if value > 1256:
                return super().__setattr__('timer', 0)
        return super().__setattr__(name, value)

    def print_screen(self, screen, *args, **kwargs):
        self.rect.left, self.rect.top = self.center
        print(self.center)
        self.surface.blit(screen, (self.rect.left-640, self.rect.top-480))
        self.surface.blit(self.image,(0,0))
        self.surface.set_alpha(self.alpha)
        screen.blit(self.surface, self.rect)

class OptionGroup(Group):
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.load_source(self.name)
        self.menu_rank = 1
        self.key = Key()
        self.movein = 30  # max 30
        self.moveout = 0  # max 30
        self.ret = None

    @classmethod
    def load_source(cls, name):
        """
        ?
        """
        with open('data/objs/opt/'+name+'.rbrb', 'rb') as f_i:
            t = pickle.load(f_i)
        for key, value in t.items():
            with open('data/tmp/imgs/'+key+'.tmp', 'wb') as f_o:
                f_o.write(value)

    def move_in(self, screen):
        for opt in self:
            opt.move_in()
            opt.print_screen(screen)
        self.movein -= 1
        return self.name

    def move_out(self, screen):
        for opt in self:
            opt.move_out()
            opt.print_screen(screen)
        self.moveout -= 1
        if self.moveout:
            return self.name
        else:
            self.movein = 30
            for opt in self:
                if opt.rank == self.menu_rank: return opt.name

    def move(self, keys, screen):
        k = self.key(keys)
        if k == defaultkey.MOVE_UP:
            self.menu_rank -= 1
        elif k == defaultkey.MOVE_LEFT:
            self.menu_rank -= 1
        elif k == defaultkey.MOVE_DOWN:
            self.menu_rank += 1
        elif k == defaultkey.MOVE_RIGHT:
            self.menu_rank += 1
        elif k == defaultkey.SHOUTING:
            for opt in self:
                if opt.rank == self.menu_rank:
                    self.ret = opt.name
        elif k == defaultkey.AMULET:
            self.move_out = 30
        for opt in self:
            if opt.rank == self.menu_rank:
                opt.select = True
            else:
                opt.select = False
            #print(opt.name, opt.select, opt.rank, opt.center)
            opt.move()
            opt.print_screen(screen)

    def __setattr__(self, name, value):
        if name == 'menu_rank':
            self.timer = 0
            if value < 1:
                return super().__setattr__('menu_rank', len(self))
            elif value > len(self):
                return super().__setattr__('menu_rank', 1)
        return super().__setattr__(name, value)

    def __call__(self, key, screen):
        keys = defaultkey.filter(key)
        if self.movein: return self.move_in(screen)
        elif self.moveout: return self.move_out(screen)
        else: return self.move(keys, screen)
