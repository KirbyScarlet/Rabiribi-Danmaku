"""
define most danmaku actions
"""
import pygame.transform as transform
from functions import snipe
from functions import vector
from functions import angle
from pygame.sprite import Sprite
# from character.erina import Erina
from math import cos
from math import sin
from math import pi
from random import random
import time

class direction():
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.r = 0
        self.vector = [0,0]

    def set(self, *value):
        '''
        direction.set(*value): return none
        '''
        if len(value)==1:
            if isinstance(value[0], (float, int)):
                self._rad(value[0])
                return
            elif isinstance(value[0], (tuple, list)):
                self._vector(value[0])
                return
            else:
                raise TypeError
        elif len(value)==2:
            self._vector(*value)
            return
        else:
            raise TypeError

    def offset(self, value):
        if isinstance(value, (float, int)):
            self.r += value
            self._rad(self.r)
        else:
            raise TypeError

    def _rad(self, value):
        self.r = value
        self.x = cos(value)
        self.y = sin(value)

    def _vector(self, *value):
        #if abs(math.sqrt(value[0]**2 + value[1]**2))-1 > 0.1:
        #    raise ValueError
        self._rad(snipe((0,0), value))

    def __setattr__(self, name, value):
        if name in ('x','y','r','vector'):
            return super().__setattr__(name, value)  
        else:
            raise AttributeError("attribute deny")

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

class AbstractAction():
    """
    Action(birth_place, 
           birth_place_offset,
           birth_direction,
           birth_direction_offset,
           *args,
           speedtime = (),
           speedvalue = (),
           directiontime = (),
           directionvalue = (),
           **kwargs
           ): return action instance
        
            birth_place: specify the coordinate of sprite
            birth_place_offset: specify the polar coordinate offset of sprite
                                birth_place_offset = (<radian>,<distance>)
            speedtime = (): specify time (frame) when speed change
                            speedtime = (30,)
            speedvalue = (): specify speed (float) at speedtime
                             speedvalue = (2.5,)
            directiontime = (): specify time (frame) when direction change
            directionvalue = (): specify direction at directiontime (type tuple)
                                directionvalue = (
                                    pi/2,  # static offset value
                                    (erina, pi/64),  # static value
                                    [pi/96, pi/256],  # dynamic offset value
                                    {x:0, y:}  # dynamic offset with different axis
                                    )

    """
    def __init__(self, birth_place,
                 birth_place_offset,
                 birth_speed,
                 birth_direction, 
                 birth_direction_offset, *args,
                 speedtime = (),
                 speedvalue = (),
                 directiontime = (),
                 directionvalue = (),
                 **kwargs
                 ):
        self.SetPosition(birth_place, birth_place_offset)
        self.SetDirection(birth_direction, birth_direction_offset)
        self.SetSpeed(birth_speed)
        self.timerip = False
        if speedtime or directiontime:
            self.SetTimerip(speedtime, speedvalue, directiontime, directionvalue)


    def SetPosition(self, birth_place, birth_place_offset):
        if isinstance(birth_place, Sprite):
            center = tuple(birth_place.center)
        elif isinstance(birth_place, (list, tuple)):
            center = tuple(birth_place)
        else:
            raise TypeError
        if birth_place_offset:
            if isinstance(birth_place_offset, tuple):
                if isinstance(birth_place_offset[0], Sprite):
                    self.SetPosition(birth_place, (snipe(center, birth_place_offset[0]), birth_place_offset[1]))
                offset = (birth_place_offset[1]*cos(birth_place_offset[0]), birth_place_offset[1]*sin(birth_place_offset[0]))
            else:
                raise TypeError
        self.center = [center[0]+offset[0], center[1]+offset[1]]
        self.setposition = True
    
    def SetDirection(self, danmaku_direction, direction_offset):
        if isinstance(danmaku_direction, float):
            self.direction = direction()
            self.direction.set(danmaku_direction + direction_offset)
        elif isinstance(danmaku_direction, Sprite):
            self.direction = direction()
            self.direction.set(snipe(self.center, danmaku_direction) + direction_offset)
        else:
            raise TypeError
        self.setdirection = True

    def SetSpeed(self, speed=False, **kwargs):
        self.setspeed = False
        self.speedtime_left, self.speedtime_right = 0,0
        self.accleration = 0
        self.setaccleration = False
        self.freeze = False
        if speed:
            self.speed = speed
            self.birth_speed = speed
            self.setspeed = True

    # low efficiency
    def __speed_old(self, time1=False, speed1=False, time2=False, speed2=False, iftype='elif'):
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

    # problems unfit and low efficiency
    def __direction_old(self, time1=False, direction1=False, time2=False, direction2=False, iftype='elif'):
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
    #
    def __speed_count1(self):
        if self.setspeed:
            if not self.setaccleration:
                self.accleration = (self.speedvalue[0]-self.birth_speed)/self.speedtime[0]
                self.setaccleration = True
            if self.accleration:
                self.speed = self.birth_speed + self.accleration*self.timer
            else:
                self.speed = self.speedvalue[0]
                self.speedtime_count = 0
        else:
            self.speed = self.speedvalue[0]
            self.speedtime_count = 0

    def __speed_ease(self, time_range):
        if time_range:
            if self.freeze:
                return
            if not self.setaccleration:
                self.accleration = (self.speedvalue_right - self.speedvalue_left)/(self.speedtime_right - self.speedtime_left)
                self.setaccleration = True
                self.freeze = False
                """
            except ZeroDivisionError:
                if time2 == 0:
                    raise ZeroDivisionError("time specify error at %d" % time1)
                if time1 == 0:
                    raise ValueError("time specify conflict at 0")
                    """
            if self.accleration:
                self.speed = self.speedvalue_left + self.accleration*(self.timer - self.speedtime_left)
            else:
                self.freeze = True
                self.speed = self.speedvalue_left
        else:
            if self.freeze:
                return
            if not self.setaccleration:
                self.accleration = (self.speedvalue_right - self.speedvalue_left)/(self.speedtime_right - self.speedtime_left)
                self.setaccleration = True
                """
            except ZeroDivisionError:
                if time2 == 0:
                    raise ZeroDivisionError("time specify error at %d" % time1)
                if time1 == 0:
                    raise ValueError("time specify conflict at 0")
                    """
            if self.accleration:
                self.speed = self.speedvalue[self.speedtime_range] + self.accleration*(self.timer - self.speedtime[self.speedtime_range])
            else:
                self.freeze = True
                self.speed = self.speedvalue[self.speedtime_range]

    def __speed(self, *erina):
        if self.speedtime_count==1:
            if self.timer <= self.speedtime[0]:
                self.__speed_count1()
                return
        if self.speedtime_count>1:
            if self.timer <= self.speedtime_last:
                self.__speed_ease(self.speedtime_range)
                if self.timer == self.speedtime_right:
                    if self.timer == self.speedtime_last:
                        self.speed = self.speedvalue_last
                        self.speedtime_count = 0
                        return
                    self.speedtime_range += 1
                    self.speedtime_left, self.speedtime_right = self.speedtime[self.speedtime_range-1], self.speedtime[self.speedtime_range]
                    self.speedvalue_left, self.speedvalue_right = self.speedvalue[self.speedtime_range-1], self.speedvalue[self.speedtime_range]
                    self.setaccleration = False
                    self.freeze = False
        else: 
            return
            
    def __direction_freeze_ease(self, *erina):
        # if direction value is a tuple
        # print('tuple')
        if hasattr(self.directionvalue_range[0], '_type'):
            self.direction.set(snipe(self.center, *erina))
        else:
            self.direction.set(self.directionvalue_range[0])
        self.direction.offset(self.directionvalue_range[1])

    def __direction_easy_ease(self):
        # if direction value is a list
        # offset number per frame
        self.direction.offset(self.directionvalue_range[0]+self.directionvalue_range[1]*(self.timer-self.directiontime_left))

    def __direction_offset_ease(self):
        # if direction value is a single float
        self.direction.offset(self.directionvalue_range)

    # bugs unfit
    def __direction_axis_offset(self):
        # if direction value is a single dictionary with keywords 'x' and 'y'
        print(self.direction)
        if 'x' in self.directionvalue_range.keys():
            if self.direction.y == 0: return
            else:
                self.direction.set(1/self.direciton.y*self.direction.x+self.directionvalue_range['x'], 1)
        if 'y' in self.directionvalue_range.keys():
            if self.direction.x == 0: return
            else:
                self.direction.set(1, 1/self.direction.x*self.direction.y+self.directionvalue_range['y'])

    def __direction(self, *erina):
        if self.timer < self.directiontime_first:
            pass
        elif self.timer > self.directiontime_last:
            if isinstance(self.directionvalue_range, (float, int, tuple)): return
            elif isinstance(self.directionvalue_range, list): self.__direction_easy_ease()
            #elif isinstance(self.directionvalue_range, dict): self.__direction_axis_offset()
            else: raise TypeError
            return
        elif self.timer == self.directiontime_last:
            self.directionvalue_range = self.directionvalue_last
            if isinstance(self.directionvalue_range, (float,int)): self.__direction_offset_ease()
            elif isinstance(self.directionvalue_range, tuple): self.__direction_freeze_ease(*erina)
            elif isinstance(self.directionvalue_range, list): self.__direction_easy_ease()
            #elif isinstance(self.directionvalue_range, dict): self.__direction_axis_offset()
            else: raise TypeError
            return
        elif self.directiontime_left <= self.timer <= self.directiontime_right:
            if self.timer == self.directiontime_left:
                if isinstance(self.directionvalue_range, (float,int)): self.__direction_offset_ease()
                elif isinstance(self.directionvalue_range, tuple): self.__direction_freeze_ease(*erina)
                elif isinstance(self.directionvalue_range, list): self.__direction_easy_ease()
                #elif isinstance(self.directionvalue_range, dict): self.__direction_axis_offset()
                else: raise TypeError
                return
            elif self.timer == self.directiontime_right:
                self.directiontime_range += 1
                self.directionvalue_range = self.directionvalue[self.directiontime_range]
                self.directiontime_left, self.directiontime_right = self.directiontime[self.directiontime_range], self.directiontime[self.directiontime_range+1]
                if isinstance(self.directionvalue_range, (float,int)): self.__direction_offset_ease()
                elif isinstance(self.directionvalue_range, tuple): self.__direction_freeze_ease(*erina)
                elif isinstance(self.directionvalue_range, list): self.__direction_easy_ease()
                #elif isinstance(self.directionvalue_range, dict): self.__direction_axis_offset()
                else: raise TypeError
                return
            else:
                if isinstance(self.directionvalue_range, (float, int, tuple)): pass
                elif isinstance(self.directionvalue_range, list): self.__direction_easy_ease()
                #elif isinstance(self.directionvalue_range, dict): self.__direction_axis_offset()
                else: raise TypeError

    def SetTimerip(self, speedtime, speedvalue, directiontime, directionvalue):
        self.speedtime = speedtime
        self.speedvalue = speedvalue
        self.directiontime = directiontime
        self.directionvalue = directionvalue

        self.speedtime_count = len(self.speedtime)
        self.direction_count = len(self.directiontime)
        
        if self.speedtime_count:
            self.speed_rip = True
            self.speedtime_last = self.speedtime[-1]
            self.speedvalue_last = self.speedvalue[-1]
            self.speedtime_range = 0
            self.speedtime_left, self.speedtime_right = 0, self.speedtime[0]
            self.speedvalue_left, self.speedvalue_right = self.birth_speed, self.speedvalue[0]
        else:
            self.speed_rip = False
        if self.direction_count:
            self.direction_rip = True
            self.directiontime_first = self.directiontime[0]
            # self.directionvalue_first = self.directionvalue[0]
            self.directiontime_last = self.directiontime[-1]
            self.directionvalue_last = self.directionvalue[-1]
            self.directiontime_range = 0
            self.directionvalue_range = self.directionvalue[self.directiontime_range]
            self.direciton_dictionary = False
            if self.direction_count > 1:
                self.directiontime_left = self.directiontime[0]
                self.directiontime_right = self.directiontime[1]
            else:
                self.directiontime_left = 0
                self.directiontime_right = self.directiontime[0]
        else:
            self.direction_rip = False
        
        self.timerip = True

        # low efficiency on danmaku birthtime
        """
        try:
            self.speedtime = [x for x in kwargs.keys() if 'speed' in x]
            self.speedtime.sort(key=lambda x: int(x.split('_')[1]))
            self.directiontime = [x for x in kwargs.keys() if 'direction' in x]
            self.directiontime.sort(key=lambda x: int(x.split('_')[1]))

            self.speedvalue = tuple(map(lambda x:kwargs[x], self.speedtime))
            self.directionvalue = tuple(map(lambda x:kwargs[x], self.directiontime))
            self.speedtime = tuple(map(lambda x:int(x.split('_')[1]), self.speedtime))
            self.directiontime = tuple(map(lambda x:tuple(x.split['_'][1], x.split['_'][-1]), self.directiontime))

            self.speedtime_count = len(self.speedtime)
            self.directiontime_count = len(self.directiontime)

            self.speedtime_last = self.speedtime[-1]
            self.speedvalue_last = self.speedvalue[-1]
            self.speedtime_range = 0
            self.speedtime_left, self.speedtime_right = 0, self.speedtime[0]
            self.speedvalue_left, self.speedvalue_right = self.birth_speed, self.speedvalue[0]

            self.timerip = True
        except ValueError:
            raise ValueError('''
            use keywords:
                speed_20 = 4.0
                    ^ ^ ^    ^
                    |  |  |    |_____set value
                    |  |  |_________set sprite timer, 60 frames per second default
                    |  |____________stynax use
                    |_______________speed or direction
            ''')
        """
        
        # old framework instance
        '''
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
            '''

    def time_rip(self, *erina):
        if not self.timerip:
            pass
        else:
            if self.speed_rip:
                self.__speed(*erina)
            if self.direction_rip:
                self.__direction(*erina)

        # low efficiency
        #exec(self.timerip)


class DanmakuAction(AbstractAction):
    def __init__(self, birth_place,
                 birth_place_offset = (), 
                 danmaku_layer = 0, 
                 birth_speed = False, 
                 direction = pi/2, 
                 direction_offset = 0, 
                 speedtime = (),
                 speedvalue = (),
                 directiontime = (),
                 directionvalue = (),
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
                **kwargs: specify speed and direction in time:
                    format:
                        speed_<speed timer> = <speed value>
                        direction_<direction_timer1>[_<direction_timer2>] = (<direction_value>, <direction_offset>)
                    for example:
                    speed_20 = 4.0
                       ^ ^ ^    ^
                       |  |  |    |_____set value
                       |  |  |_________set sprite timer, 60 frames per second default
                       |  |____________stynax use
                       |_______________speed or direction
                                        when use direction mode, value can use a tuple for direction and offset

                    direction_10 = pi/2         offset value
                    direction_20 = (erina, pi/128)      static value
                    direction_30 = [pi/64, pi/720]      dynamic offset value, rad/frame
                    direction_40 = {'x':0, 'y':-1}     dynamic offset with different axis
        """
        super().__init__(birth_place,
                 birth_place_offset,
                 birth_speed,
                 direction, 
                 direction_offset,
                 speedtime = speedtime,
                 speedvalue = speedvalue,
                 directiontime = directiontime,
                 directionvalue = directionvalue,
                 **kwargs
                 )
        self.layer = danmaku_layer
        #print('action instance:', self.speed, self.center, self.direction)


class ElfAction(AbstractAction):
    '''
    def __init__(self, birth_place = (30, -30),
                 birth_direction = pi/2, 
                 birth_speed = 2,
                 birth_place_offset = (0,0),
                 birth_direction_offset = 0,
                 speedtime = (),
                 speedvalue = (),
                 directiontime = (),
                 directionvalue = (),
                 **kwargs
                 ):
        super().__init__(
                        birth_place,
                        birth_place_offset,
                        birth_speed,
                        birth_direction, 
                        birth_direction_offset,
                        speedtime = speedtime,
                        speedvalue = speedvalue,
                        directiontime = directiontime,
                        directionvalue = directionvalue
                        #**kwargs
                        )
        pass
    '''

class OptionAction():
    def __init__(self, rank,
                 birth_place = (0,0), 
                 selected_position = (0,0),
                 unselected_position = (0,0),
                 select_rate = 2.0,
                 moveio_rate = 4.0,
                 **kwargs):
        """
        using:

            MenuAction(birth_place,
                         selected_position = (0,0),
                         unselected_position = (0,0),
                         rate = 2.0,
                         **kwargs)

            ?
            rate: easy-ease speed, high rate with low speed, at least 2.0
        """
        self.rank = rank
        self.center = list(birth_place)
        self.rate_s = select_rate
        self.rate_io = moveio_rate
        self.birth_place = birth_place
        self.selected_position = selected_position
        self.unselected_position = unselected_position
        self.move_in_time = 30 + rank

    def selected(self):
        speed = (self.selected_position[0] - self.center[0])/self.rate_s, (self.selected_position[1] - self.center[1])/self.rate_s
        self.center = [self.center[0]+speed[0], self.center[1]+speed[1]]

    def unselected(self):
        speed = (self.unselected_position[0] - self.center[0])/self.rate_s, (self.unselected_position[1] - self.center[1])/self.rate_s
        self.center = [self.center[0]+speed[0], self.center[1]+speed[1]]

    def move_in(self):
        if 0 < self.move_in_time < 30:
            speed = (self.unselected_position[0] - self.center[0])/self.rate_io, (self.unselected_position[1] - self.center[1])/self.rate_io
            self.center = [self.center[0]+speed[0], self.center[1]+speed[1]]
        self.move_in_time -= 1
        '''
        speed = (2*self.unselected_position[0] - self.birth_place[0] - self.center[0])/self.rate_io, 
                (2*self.unselected_position[1] - self.birth_place[1] - self.center[1])/self.rate_io
        print(self.center)
        self.center = [self.center[0]+speed[0], self.center[1]+speed[1]]
        '''

    def move_out(self):
        L = self.birth_place[0]-self.unselected_position[0], self.birth_place[1]-self.unselected_position[1]
        speed = (L[0] - (self.birth_place[0]-self.center[0]))/self.rate_io, (L[1] - (self.birth_place[1]-self.center[1]))/self.rate_io
        self.center = [self.center[0]+speed[0], self.center[1]+speed[1]]

    def __setattr__(self, name, value):
        if name == 'rate':
            if value < 2:
                raise AttributeError("rate value must larger than 2\n")
        return super().__setattr__(name, value)

class ItemAction(object):
    """
    specify items movement
    """
    def __init__(self, birth_place
                 birth_place_offset,
                 *args,
                 **kwargs
                 ):
        self.timer = 0
        self.SetPosition(birth_place, birth_place_offset)
        self.itemline = False

    def SetPosition(self, birth_place, offset):
        if isinstance(birth_place, Sprite):
            center = birth_place.center
        elif isinstance(birth_place, (list, tuple)):
            center = birth_place
        if offset:
            x,y = offset[1]*cos(offset[0]), offset[1]*sin(offset[0])
        self.center = [center[0]+x, center[1]+y]

    def birth_move(self):
        self.speed = self.timer*3/40
        self.center[1] += self.speed

    def regular_move(self):
        self.speed = 1.5
        self.center[1] += 1.5

    def snipe_move(self, erina):
        self.speed = 2
        self.direction = snipe(self,center, erina)
        self.center = [self.speed*self.direction[0], self.speed*self.direction[1]]

    