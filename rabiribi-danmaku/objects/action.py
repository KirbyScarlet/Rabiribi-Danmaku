"""
define most danmaku actions
"""
from functions import snipe

class DanmakuAction():
    def __init__(self, birth_group, birth_place, *args, danmaku_layer=0, birth_speed=0, direction=[0,1], offset=0, **kwargs):
        """
        using:

            danmaku(birth_group, birth_place, ..., danmaku_layer=0, speed = 0, direction = False, offset = 0, ...): return None

                birth_group: specify birth group
                birth_place: specify danmaku birth place
                danmaku_layer = 0: defaulty on the top
                birth_speed = 0: specify danmaku speed when birth
                direction = False: default direction is [0,1]
        """
        self.center = list(birth_place)
        self.layer = danmaku_layer
    
    def SetDirection(self, sprite, target, offset):
        self.direction = snipe(sprite, target) + offset

    def SetSpeed(self, speed=False, **kwargs):
        if speed:
            self.speed = speed
        self.speed_change = len(kwargs)

    def time_rip(self, *erina):
        pass
