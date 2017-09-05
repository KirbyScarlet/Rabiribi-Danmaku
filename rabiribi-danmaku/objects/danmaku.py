from objects.sprites import Danmaku
from math import pi
from functions.values import screenborder

'''
class mid_orange_circle(Danmaku):
    def __init__(self, birth_group, birth_place, *args, **kwargs):
        super().__init__(birth_group, birth_place, *args, **kwargs)
        self.SetValue(7,50,4)
        self.SetLiveCheck()
mid_orange_circle.load_source('mid_orange_circle')

class small_blue_circle(Danmaku):
    def __init__(self, birth_group, birth_place, *args, **kwargs):
        super().__init__(birth_group, birth_place, *args, **kwargs)
        self.SetValue(7,50,4)
        self.SetLiveCheck()
small_blue_circle.load_source('small_blue_circle')
'''

class gray_glow_dot(Danmaku): pass
gray_glow_dot.load_source('gray_glow_dot', 2)

class orange_glow_dot(Danmaku): pass
orange_glow_dot.load_source('orange_glow_dot', 2)

class green_glow_dot(Danmaku): pass
green_glow_dot.load_source('green_glow_dot', 2)