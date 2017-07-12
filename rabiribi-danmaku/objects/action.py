"""
define most danmaku actions
"""
from functions import snipe
from pygame.sprite import Sprite
from character.erina import Erina
from math import cos
from math import sin
from math import pi
import time

class direction():
    def __init__(self, center):
        self.x = 0.0
        self.y = 0.0
        self.vector = [0,0]
        self.center = center

    def set(self, *value):
        if len(value)==1:
            if isinstance(value[0], (float, int)):
                self._rad(value[0])
            elif isinstance(value[0], list):
                self._vector(value[0])
            elif isinstance(value[0], pygame.sprite.Sprite):
                self._rad(snipe(self.center, value[0]))
            else:
                raise TypeError
        elif len(value)==2:
            if isinstance(value, (tuple, list)):
                self._vector(*value)
            else:
                raise TypeError
        else:
            raise TypeError

    def offset(self, value):
        if isinstance(value, (float, int)):
            v = snipe((0,0), (self.x,self.y))
            self._rad(value+v)
        else:
            raise TypeError

    def _rad(self, value):
        self.x = cos(value)
        self.y = sin(value)

    def _vector(self, *value):
        #if abs(math.sqrt(value[0]**2 + value[1]**2))-1 > 0.1:
        #    raise ValueError
        self.x, self.y = value

    def __setattr__(self, name, value):
        if name=='x' or name=='y':
            pass
        return super().__setattr__(name, value)  

    def __getitem__(self, y):
        if y==0:
            return self.x
        elif y==1:
            return self.y
        else:
            raise IndexError

    def __str__(self):
        return '(%.4f,%.4f)' % (self.x, self.y)
    
    def __repr__(self):
        return 'direction vector = (%.4f,%.4f)' % (self.x, self.y)


class DanmakuAction():
    def __init__(self, birth_place, *args, 
                 birth_place_offset = ((0),0), 
                 danmaku_layer = 0, 
                 birth_speed = 0, 
                 direction = pi/2, 
                 direction_offset = 0, 
                 time_rip = False, 
                 **kwargs):
        """
        using:

            danmaku(self, birth_place, *args, 
                 birth_place_offset = (0,0), 
                 danmaku_layer = 0, 
                 birth_speed = 0, 
                 direction = pi/2, 
                 direction_offset = 0, 
                 time_rip = 'pass', 
                 **kwargs):

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
        self.timerip = 'pass\n'
        if time_rip:
            self.SetTimerip(**kwargs)
        #print('action instance:', self.speed, self.center, self.direction)

    def SetPosition(self, birth_place, birth_place_offset):
        if isinstance(birth_place, list):
            center = list(birth_place)
        elif isinstance(birth_place, Sprite):
            center = list(birth_place.center)
        else:
            raise TypeError
        if isinstance(birth_place_offset, tuple):
            if isinstance(birth_place_offset[0], Sprite):
                try:
                    self.SetPosition(birth_place, (snipe(center, birth_place_offset[0])+birth_place_offset[1], birth_place_offset[2]))
                except IndexError:
                    print("parament input error")
                    raise IndexError
            try:
                offset = [birth_place_offset[1]*cos(birth_place_offset[0]), birth_place_offset[0]*sin(birth_place_offset[0])]
            except IndexError:
                print("parament input error")
                raise IndexError
        else:
            raise TypeError
        self.center = [center[0]+offset[0], center[1]+offset[1]]
        self.setposition = True
    
    def SetDirection(self, danmaku_direction, direction_offset):
        if isinstance(danmaku_direction, (float, int)):
            self.direction = direction(self.center)
            self.direction.set(danmaku_direction + direction_offset)
        elif isinstance(danmaku_direction, Sprite):
            self.direction = direction(self.center)
            self.direction.set(snipe(self.center, danmaku_direction) + direction_offset)
        else:
            raise TypeError
        self.setdirection = True

    def SetSpeed(self, speed=False, **kwargs):
        self.setspeed = False
        if speed:
            self.speed = speed
            self.setspeed = True

    def __speed(self, time1=False, speed1=False, time2=False, speed2=False, iftype='elif'):
        if not isinstance(time1, (int, bool)):
            raise ValueError('time1 input error!', time1)
        elif not isinstance(time2, (int, bool)):
            raise ValueError('time2 input error!', time2)
        elif not isinstance(speed1, (int, float, bool)):
            raise ValueError('speed1 input error!', speed1)
        elif not isinstance(speed2, (int, float, bool)):
            raise ValueError('speed2 input error!', speed2)
        elif iftype not in ('elif', 'if'):
            raise ValueError("iftype only use 'if' or 'elif'", iftype)
        elif time1 == time2 and time2 != 0:
            raise ValueError('time specify error!')

        if isinstance(time2, bool):
            text = """
%s %d == self.timer:
    self.speed = %.16f """ % (iftype, time1, speed1)

        elif isinstance(time1, bool):
            if self.setspeed:
                if time2==0:
                    raise ValueError('time specify error')
                else:
                    return self.__speed(time1=0,speed1=float(self.speed),time2=time2,speed2=speed2,iftype=iftype)
            else:
                text = """
%s self.timer == 0:
    self.speed = %.16f """ % (iftype, speed2)
        else:
            accleration = (speed2-speed1)/float(time2-time1)
            if accleration == 0:
                text = """
%s %d == self.timer:
    self.speed = %.16f """ % (iftype, time1, time2, speed1)
            else:
                text = """
%s %d <= self.timer < %d:
    self.speed = %.16f * (self.timer - %d) + %.16f """ % (iftype, time1, time2, accleration, time1, speed1)
        return text

    # problems unfit
    def __direction(self, time1=False, direction1=False, time2=False, direction2=False, iftype='elif'):
        if not isinstance(time1, (int, bool)) or \
        not isinstance(time2, (int, bool)) or \
        not isinstance(direction1, (int, float, bool, Erina, tuple)) or \
        not isinstance(direction2, (int, float, bool, Erina, tuple)) or \
        iftype not in ('elif', 'if') or \
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
            if isinstance(direction1, Erina):
                text = """
                %s %d == self.timer:
                    self.direction.set(*erina)
                    
                """
            text = """
            %s %d < self.timer:
                self.direction.set(%.16f)
            """ % (iftype, time1, direction1+direction1offset)
        elif not time1:
            if isinstance(direction2, Erina):
                text ="""
                %s self.timer == %d:
                    self.direction.set(*erina)
                """ % (iftype, time2)
            text = """
            %s self.timer < %d:
                self.direction.set(%.16f)
            """ % (iftype, time2, direction2+direction2offset2)
        else:
            if isinstance(direction1, Erina):
                if isinstance(direction2, Erina):
                    text ="""
                    %s %d < self.timer < %d:
                        self.direction.set(*erina)
                    """ % (iftype, time1, time2)
                else:
                    text = """
                    %s %d == self.timer:
                        self.direction.set(*erina)
                    """ % (iftype, time1)
                return text
                
            accleration = (direction2+direction2offset-direction1-direction1offset1)/float(time2-time1)
            if accleration == 0:
                text = """
                %s %d == self.timer:
                    self.direction.set(%.16f)
                """ % (iftype, time1, time2, direction1)
            else:
                text = """
                %s %d <= self.timer < %d:
                    self.direction.set(%.16f * (self.timer - %d) + %.16f)
                """ % (iftype, time1, time2, accleration, time1, direction1+offset1)
        return text
    
    def SetTimerip(self, **kwargs):
        if not kwargs:
            self.timerip = 'pass\n'
        else:
            try:
                speedlist = [x for x in kwargs.keys() if 'speed' in x]
                speedlist.sort(key=lambda x: int(x.split('_')[1]))
                directionlist = [x for x in kwargs.keys() if 'direction' in x]
                directionlist.sort(key=lambda x: int(x.split('_')[1]))
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
                raise ValueError
            if speedlist:
                recent_time = speedlist[0]
                self.timerip = self.__speed(time2=int(recent_time.split('_')[1]), speed2=kwargs[recent_time], iftype='if')
                speedlist_length = len(speedlist)
                for sl in range(speedlist_length):
                    if sl+1 < speedlist_length:
                        recent_time2 = speedlist[sl+1]
                        recent_time1 = speedlist[sl]
                        self.timerip += self.__speed(time1=int(recent_time1.split('_')[1]), speed1=kwargs[recent_time1], time2=int(recent_time2.split('_')[1]), speed2=kwargs[recent_time2])
                    elif sl+1 == speedlist_length:
                        recent_time1 = speedlist[sl]
                        self.timerip += self.__speed(time1=int(recent_time1.split('_')[1]), speed1=kwargs[recent_time1])
            if directionlist:
                pass

    def time_rip(self, *erina):
        #print(self.timerip)
        exec(self.timerip)
        '''
        if self.timer<20:
            self.speed = -0.1*self.timer + 4
        elif self.timer==20:
            self.speed = 2
            '''