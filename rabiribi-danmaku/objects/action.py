"""
define most danmaku actions
"""
from functions import snipe
from pygame.sprite import Sprite
from character.erina import Erina
from math import cos
from math import sin
from math import pi

class DanmakuAction():
    def __init__(self, birth_group, birth_place, *args, 
                 birth_place_offset = (0,0), 
                 danmaku_layer = 0, 
                 birth_speed = 0, 
                 direction = pi/2, 
                 direction_offset = 0, 
                 time_rip = 'pass', 
                 **kwargs):
        """
        using:

            danmaku(self, birth_group, birth_place, *args, 
                 birth_place_offset = (0,0), 
                 danmaku_layer = 0, 
                 birth_speed = 0, 
                 direction = pi/2, 
                 direction_offset = 0, 
                 time_rip = 'pass', 
                 **kwargs): return None

                birth_group: specify birth group
                birth_place: specify danmaku birth place
                danmaku_layer = 0: defaulty on the top
                birth_speed = 0: specify danmaku speed when birth
                direction = False: default direction is [0,1]
        """
        self.SetPosition(birth_place, birth_place_offset)
        self.layer = danmaku_layer
        self.SetDirection(direction, direction_offset)
        birth_group.append(self)

    def SetPosition(self, birth_place, birth_place_offset):
        if isinstance(birth_place, list):
            center = birth_place
        elif isinstance(birth_place, Sprite):
            center = list(birth_place.center)
        else:
            raise TypeError
        if isinstance(birth_place_offset, tuple):
            offset = [birth_place_offset[1]*cos(birth_place_offset[0]), birth_place_offset[0]*sin(birth_place_offset[0])]
        else:
            raise TypeError
        self.center = center[0]+offset[0]
    
    def SetDirection(self, direction, direction_offset):
        if isinstance(direction, float or int):
            self.direction.x = cos(direction)
            self.direction.y = sin(direction)
        if isinstance(direction, Erina):
            self.direction.set(snipe(self.center, direction))
        self.direction = snipe(sprite, target) + offset

    def SetSpeed(self, speed=False, **kwargs):
        if speed:
            self.speed = speed
        self.speed_change = len(kwargs)

    def SetTimerip(self, **kwargs):
        if not kwargs:
            self.timerip = 'pass'
        else:
            pass
        
    def time_rip(self, timerip, *erina):
        exec(timerip)
