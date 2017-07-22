__doc__ = ''' '''

import pygame
from pygame.sprite import Sprite

class ItemGroup():
    '''
    for sprites store items
    '''
    def __init__(self):
        self.count = 0
        self.items = {HP:0, ATK:0, COCOABOMB:0}

    def add(self, *items):
        for item in items:
            self.items[item] += 1

class Item(Sprite):
    pass

class HP(Item):
    pass

class ATK(Item):
    pass

class COCOABOMB(Item):
    pass

