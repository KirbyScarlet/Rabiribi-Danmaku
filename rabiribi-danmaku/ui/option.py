import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group
from objects.action import OptionAction
import pickle

from functions.values import defaultkey
from pygame.locals import *

class Key(object):
    def __init__(self):
        self.key_hold = None
        self.delay_hold = 50  # frame
        self.delay_switch = 12  # frame, max 12

    def delay(self, key):
        if self.key_hold == key:
            if self.delay_hold > 0:
                self.delay_hold -= 1
            else:
                if self.delay_switch == 12:
                    self.delay_switch -= 1
                    return self.key_hold
                elif self.delay_switch == 0:
                    self.delay_switch = 12
                else:
                    self.delay_switch -= 1
        else:
            self.key_hold = key
            self.delay_hold = 50
            self.delay_switch = 12
            return key

    def __call__(self, keypress):
        for key, value in keypress:
            return self.delay(key)

class Option(Sprite, OptionAction):
    def __init__(self, rank, 
                    birth_place = (0,0), 
                    selected_position = (0,0), 
                    unselected_position = (0,0), 
                    rate = 2):
        """
        """
        Sprite.__init__(self)
        OptionAction(self, birth_place,
                       selected_position,
                       unselected_position,
                       rate)
        self.rank = rank    # small rank on top
        self.selected = False

    @classmethod
    def load_source(cls, name):
        """
        ?
        """
        with open('data/objs/opt/'+name+'.rbrb', 'rb') as f_i:
            t = pickle.load(f_i)
        for key, value in t.items():
            with open('data/tmp/'+key+'.tmp', 'wb') as f_o:
                f_o.write(value)

    def __new__(cls, name, *args, **kwargs):
        try:
            cls.image = pygame.image.load('data/tmp/'+name+'.tmp').convert()
        except pygame.error:
            cls.load_source(cls.__class__.__name__)
            cls.image = pygame.image.load('data/tmp/'+name+'.tmp').convert()
        return super().__new__(*args, **kwargs)

class OptionGroup(Group):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.menu_rank = 1
        self.key = Key()
        self.movein = 30  # max 30
        self,moveout = 0  # max 30

    def move_in(self):
        for opt in self:
            opt.move_in()
        self.movein -= 1
        return self.__class__.__name__

    def move_out(self):
        for opt in self:
            opt.move_out()
        self.moveout -= 1
        if self.moveout:
            return self.__class__.__name__
        else:
            self.movein = 30
            for opt in self:
                if opt.rank == self.menu_rank: return opt.__class__.__name__

    def move(self, keys):
        k = self.key(keys)
        if key == defaultkey.MOVE_UP:
            self.menu_rank -= 1
        elif key == defaultkey.MOVE_LEFT:
            self.menu_rane -= 1
        elif key == defaultkey.MOVE_DOWN:
            self.menu_rank += 1
        elif key == defaultkey.MOVE_DOWN:
            self.menu_rank += 1
        for opt in self:
            if opt.rank == self.menu_rank:
                opt.selected()
            else:
                opt.unselected()

    def __setattr__(self, name, value):
        if name == 'menu_rank':
            if value < 0:
                super().__setattr__('menu_rank', 8)
            elif value > 8:
                super().__setattr__('menu_rank', 1)
        return super().__setattr__(name, value)

    def __call__(self):
        keys = defaultkey.filter(pygame.key.get_pressed())
        if self.movein: return self.move_in()
        elif self.moveout: return self.move_out()
        else: return self.move(keys)
