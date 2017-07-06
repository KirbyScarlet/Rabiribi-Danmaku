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
                 time_rip = False, 
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
                 **kwargs):

                birth_group: specify birth group
                birth_place: specify danmaku birth place
                *args: fit mistakes
                danmaku_layer = 0: defaulty on the top
                birth_speed = 0: specify danmaku speed when birth
                direction = pi/2: default direction is [0,2*pi]
                                   if direction parament is a vector, lose acuricy
                direction_offset = 0: a radium number
                time_rip = False: if timerip set to true, use keyword argument.
                **kwargs: for example:
                    speed_20 = 4.0
                       ^ ^ ^    ^
                       |  |  |    |_____set value
                       |  |  |_________set sprite timer, 60 frames per second default
                       |  |____________stynax use
                       |_______________speed or direction
                                        when use direction mode, value can use a tuple for direction and offset
                                        direction_20 = (sprite, pi/16)
                    direction_10_30 = pi/2,pi/3
                    ^   ^   ^   ^       ^
                    |   |   |   |       |________set values, as path as direction time
                    |   |   |   |________________set stop time
                    |   |   |____________________set start time
                    |   |________________________stynax usage
                    |____________________________only direction
        """
        self.SetPosition(birth_place, birth_place_offset)
        self.layer = danmaku_layer
        self.SetDirection(direction, direction_offset)
        self.SetSpeed(birth_speed)
        self.SetTimerip(**kwargs)
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
        self.setposition = True
    
    def SetDirection(self, direction, direction_offset):
        if isinstance(direction, (float, int)):
            self.direction.set(direction + direction-offset)
        if isinstance(direction, Erina):
            self.direction.set(snipe(self.center, direction))
        self.setdirection = True

    def SetSpeed(self, speed=False, **kwargs):
        if speed:
            self.speed = speed
            self.setspeed = True

    def __speed(self, time1=False, speed1=False, time2=False, speed2=False, iftype='elif'):
        if not isinstance(time1, (int, bool)) or 
        not isinstance(time2, (int, bool)) or 
        not isinstance(speed1, (int, float, bool)) or 
        not isinstance(speed2, (int, float, bool)) or
        iftype not in 'elif', 'if' or
        time1 == time2:
            raise ValueError
        if not time2:
            if self.setspeed and speed1!=0:
                return self.__speed(0,float(self.speed),time2,speed2,iftype)
            text = 
            """
            %s %d < self.timer:
                self.speed = %.16f
            """ % (iftype, time1, speed1)
        elif not time1:
            text = 
            """
            %s self.timer < %d:
                self.speed = %.16f
            """ % (iftype, time2, speed2)
        else:
            accleration = (speed2-speed1)/float(time2-time1)
            if accleration == 0:
                text = 
                """
                %s %d <= self.timer < %d:
                    self.speed = %.16f
                """ % (iftype, time1, time2, speed1)
            else:
                text = 
                """
                %s %d <= self.timer < %d:
                    self.speed = %.16f * (self.timer - %d) + %.16f
                """ % (iftype, time1, time2, accleration, time1, speed1)
        return text

    # problems unfit
    def __direction(self, time1=False, direction1=False, time2=False, direction2=False, iftype='elif'):
        if not isinstance(time1, (int, bool)) or 
        not isinstance(time2, (int, bool)) or 
        not isinstance(direction1, (int, float, bool, Erina, tuple)) or 
        not isinstance(direction2, (int, float, bool, Erina, tuple)) or
        iftype not in 'elif', 'if' or
        time1 == time2:
            raise ValueError
        if isinstance(direction1, tuple):
            direction1, direction1offset = direction1
        else:
            direction1offset = 0
        if isinstance(direction2, tuple):
            direction2, direction2offset = direction2
        else:
            direction1offset = 0
        if not time2:
            if self.setdirection and direction1!=0:
                return self.__direction(0, float(self.direction), time2, direction2, iftype)
            text = 
            """
            %s %d < self.timer:
                self.direction.set(%.16f)
            """ % (iftype, time1, direction1+direction1offset)
        elif not time1:
            text = 
            """
            %s self.timer < %d:
                self.direction.set(%.16f)
            """ % (iftype, time2, direction2+direction2offset2)
        else:
            if isinstance(direction1, Erina):
                
            accleration = (direction2+direction2offset-direction1-direction1offset1)/float(time2-time1)
            if accleration == 0:
                text = 
                """
                %s %d == self.timer:
                    self.direction.set(%.16f)
                """ % (iftype, time1, time2, direction1)
            else:
                text = 
                """
                %s %d <= self.timer < %d:
                    self.direction.set(%.16f * (self.timer - %d) + %.16f)
                """ % (iftype, time1, time2, accleration, time1, direction1+offset1)
        return text
    
    def SetTimerip(self, **kwargs):
        if not kwargs:
            self.timerip = 'pass\n'
        else:
            try:
                speedlist = sorted([x for x in kwargs.keys() if 'speed' in x], key=lambda x: int(x.split('-')[-1]), reverse=True)
                directionlist = sorted([x for x in kwargs.keys() if 'direction' in x], key=lambda x: int(x.split('-')[1]), reverse=True)
            except ValueError:
                print("""
                use keywords:
                    speed_20 = 4.0
                        ^ ^ ^    ^
                        |  |  |    |_____set value
                        |  |  |_________set sprite timer, 60 frames per second default
                        |  |____________stynax use
                        |_______________speed or direction
                """)
            if speedlist:
                recent_time = speedlist.pop()
                

    def time_rip(self, timerip, *erina):
        exec(timerip)
