import pygame
import pickle
import character
import functions
import objects
import abc
import random
from functions.values import screenborder
from operator import truth

class Buff(pygame.sprite.Sprite):
    __metaclass__ = abc.ABCMeta
    """
    use this to define buffs and debuffs
    """
    _erina_only = False
    _boss_only = False
    _special_only = None

    def __init__(self, buff_group, owner, time):
        '''
        __init__(buff_group, name, owner=None, time=-1): return None

            buff group 
        '''
        super().__init__(buff_group)
        self.owner = owner
        self.stack = {} # temp value in this
        if isinstance(self.owner, character.erina.Erina):
            self.type = 1
        elif isinstance(self,owner, objects.sprites.Boss):
            self.type = -1
        elif isinstance(self.owner, objects.sprites.Elf):
            self.type = 0
        
        # buff effect: timellarger than 0 and equal -1
        self.time = time
        self.timer = 0
        self.birth_time = 180
        self.death_time = 0 # max 30
        self.moveup = 0
        self.movedown = 0

        self.effective = True
        self.invalid = False

        self.image = pygame.surface.Surface((17,11)).convert()
        self.opacity = 1.00
        self.rect = self.image.get_rect()
        self.image.blit(self.image_temp, (0,0))
        self.rank = len(buff_group)
        self.temp_position = [0,0]

        if isinstance(owner, character.erina.Erina):
            self.temp_position[0] = screenborder.SCREEN_RIGHT
            self.temp_position[1] = screenborder.SCREEN_BOTTOM - 30 - 15*self.rank
            self.rect.left, self.rect.bottom = self.temp_position
        elif isinstance(owner, objects.sprites.Boss):
            self.temp_position[0] = screenborder.SCREEN_LEFT
            self.temp_position[1] = screenborder.SCREEN_TOP + 30 + 15*self.rank
        elif isinstance(owner, objects.sprites.Elf):
            self.rect.center = owner.center

    @classmethod
    def SetImage(cls, buff_name):
        buff_name = 'data/tmp/'+ buff_name +'.tmp'
        try:
            cls.image_temp = pygame.image.load(buff_name).convert_alpha()
        except FileNotFoundError:
            filename = 'data/obj/items/buffs.rbrb'
            with open(filename, 'rb') as f:
                images = pickle.load(f)
            for key,value in images.items():
                filename = 'data/tmp/imgs/'+key+'.tmp'
                with open(filename, 'wb') as f:
                    f.write(value)
            cls.(buff_name)

    def move_elf(self):
        self.rect.center = self.owner.center

    def move_in(self):
        if self.type == 1:
            if self.birth_time > 30:
                destination = screenborder.SCEREEN_RIGHT-50
            else:
                destination = screenborder.SCREEN_RIGHT-17
            speed = (self.rect.right - destination)/2 # problems unfit
            self.temp_position[0] += speed
            self.rect.right, self.rect.bottom = self.temp_position
        elif self.type == -1:
            if self.birth_time > 30:
                destination = screenborder.SCREEN_LEFT+50
            else:
                destination = screenborder.SCREEN_RIGHT+17
            speed = (self.rect.left - destination)/2 # problems unfit
            self.temp_position[0] += speed
            self.rect.left, self.rect.top = self.temp_position
        else:
            self.rect.center = self.owner.center
        self.birth_time -= 1

    def move_out(self):
        if self.type == 1:
            speed = (screenborder.SCREEN_RIGHT - self.rect.left)/2 # problems unfit
            self.temp_position[0] += speed
            self.rect.right, self.rect.bottom = self.temp_position
        elif self.type == -1:
            speed = (screenborder.SCREEN_LEFT - self.rect.right)/2 # problems unfit
            self.temp_position[0] += speed
            self.rect.left, self.rect.bottom = self.temp_position
        else:
            self.rect.center = self.owner.center
        self.death_time -= 1
        if self.death_time == 0:
            self.remove()

    def move_up(self):
        """
        only happened on boss side
        """
        destination = screenborder.SCREEN_TOP + 30 + 15*self.rank
        speed = (self.rect.top - destination)/2
        self.temp_position[1] -= speed
        self.rect.top, self.rect.left = self.temp_position
        self.moveup -= 1

    def move_down(self):
        """
        only happened on erina side
        """
        destination = screenborder.SCREEN_BOTTOM - 30 - 15*self.rank
        speed = (self.rect.bottom - destination)/2
        self.temp_position[1] += speed
        self.rect.right, self.rect.bottom = self.temp_position
        self.movedown -= 1

    def move(self):
        if self.time > 0:
            self.time -= 1
        if self.time == 0:
            self.death_time = 30
        if self.birth_time: self.move_in()
        elif self.death_time: self.move_out()
        if self.moveup: self.move_up()
        elif self.movedown: self.move_down()
        self.timer += 1

    def opacity_up(self):
        if self.opacity < 100:
            self.opacity += 6
            if self.opacity > 100:
                self.opacity = 100
            self.image.set_alpha(self.opacity)

    def opacity_down(self):
        if self.opacity > 20:
            self.opacity -= 6
            if self.opacity < 20:
                self.opacity = 20
            self.image.set_alpha(self.opacity)

    def opacity_check(self, erina):
        erina_rect = erina.rect
        count = len(self.groups())
        if erina_rect.right >= screenborder.SCREEN_RIGHT-60 and erina_rect.bottom > screenborder.SCREEN_BOTTOM-40-15*len(count) \
        or erina_rect.left <= screenborder.SCREEN_LEFT+60 and erian_rect.top > screenborder.SCREEN_TOP+40+15*len(count):
            self.opacity_down()
        else:
            self.opacity_up()

    def remove(self):
        for buff in self.groups()[0]:
            if buff.rank>self.rank:
                buff.rank -= 1
        self.kill()
    
    @abc.abstractmethod
    def check(self, *sprites):
        """
        Buff.buff_check(*sprites): Return None
        """    
        raise NotImplementedError

    def print_screen(self, screen):
        screen.blit(self.image, self.rect)

    def __setattr__(self, name, value):
        if name == 'rank':
            if isinstance(self.owner, character.erina.Erina):
                self.movedown = 30
            elif isinstance(self.owner, objects.sprites.Boss):
                self.moveup = 30
            else: pass
        return super().__setattr__(name, value)

    def __repr__(self):
        return '<' + self.__class__.__name__ + '>'

'''
class BuffImage(pygame.sprite.Sprite):
    """
    specify image of a buff(s)
    """
    def __init__(self, name):
        super().__init__()

    def SetImage(self, file_name):
        """
        set buff icon
        """
        f = open(file_name, 'rb')
        images = pickle.load(f)
        f.close()
        img_name = 'data/tmp/bf/' + self.name + '.tmp'
        img = open(img_name, 'wb')
        img.write(images[self.name])
        img.close()
        self.image = pygame.image.load(img_name).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.top = 0
        self.temp_left = 0
        self.temp_right = 0
        self.temp_top = 0
'''

class BuffGroup():
    """
    use this to restore buffs
    the group support following standard python operations:

        in      test if a buff is contained
        len     the number of buffs contained
        bool    test if any buffs are contained
        iter    iterate through all the buffs

    """
    _buffgroup = True

    def __init__(self, *buff):
        self.buffdict = {}
        for b in buff:
            self.add_internal(b)

    def buffs(self):
        return self.buffdict.keys()
        # return list(self.buffdict)

    def add_internal(self, buff):
        self.buffdict[buff] = buff.__class__.__name__

    def remove_internal(self, buff):
        for key, value in self.buffdict.items():
            if value == buff:
                del self.buffdict[key]
                break

    def has_internal(self, buff):
        for b in self.buffdict.values():
            if b == buff:
                return True
        return False

    def copy(self):
        """
        copy a group with all the same buffs

        BuffGroup.copy(): return BuffGroup

        Returns a copy of the group that is an instance of the same
        and has the same buffs in it.
        """
        return self.__class__(self.buffs())

    def __iter__(self):
        return iter(self.buffs())

    def __contains__(self, buff):
        return self.has_internal(buff)

    def add(self, *buffs):
        """
        add buff(s) to group
        
        BuffGroup.add(buff, list, group, ...): return none
        """
        for buff in buffs:
            if isinstance(buff, Buff):
                self.add_internal(buff)
            elif isinstance(buff, BuffGroup):
                self.add(buff)

    def remove(self, *buffs):
        """
        remove buff(s) from group

        BuffGroup.remove(buff, ...): return None
        """
        for buff in buffs:
            if self.has_internal(buff):
                self.remove_internal(buff)

    def has(self, *buffs):
        """
        ask if group has a buff

        BuffGroup.has(buff, ...): return bool
        """
        return_value = False

        for buff in buffs:
            if isinstance(buff, Buff):
                if self.has_internal(buff):
                    return_value = True
                else:
                    return False
            else:
                pass
        
        return return_value

    def empty(self):
        """
        remove all buffs
        
        BuffGroup.empty(): return None
        """
        self.buffdict = {}

    def print_screen(self, screen):
        for buff in self.buffs():
            buff.print_screen(screen)

    def __nonzero__(self):
        return truth(self.buffs())

    def __len__(self):
        """
        return number of buffs in group

        BuffGroup.len(group): return int
        """
        return len(self.buffs())

    def __repr__(self):
        return "<%s(%d buffs)>" % (self.__class__.__name__, len(self))


#
# all buffs here:
#

class SpeedDown(Buff):
    """
    Speed lowered by 20%
    """
    def __init__(self, buff_group, owner, time):
        super().__init__(buff_group, owner, time):
        self.stack[speed] = self.owner.speed

    def check(self, *enemy):
        if self.time==0:
            self.invalid = True
        if self.effective:
            self.owner.speed *= 0.8
            self.effective = False
        if self.invalid:
            self.owner.speed = self.stack['speed']
            self.invalid = False
            
SpeedDown.SetImage(speed_down)

class Numb(Buff):
    """
    All movement ceases intermittently
    """
    def __init__(self, buff_group, owner, time):
        super().__init__(buff_group, owner, time)
        self._erina_only = True
        self.stack['speed'] = self.owner.speed

        # balance unfit
        self.numb_timer = 20 + random.randint(-5,5)

    def check(self, *enemy):
        if self.time==0:
            self.invalid = True
        if self.effective:
            self.owner.speed = 0
            if self.numb_timer>0:
                self.numb_timer -= 1
            else:
                self.effective = False
        if self.invalid:
            self.owner.speed = self.stack['speed']

    def __setattr__(self, name, value):
        if name == 'timer':
            if value % 60 == 0:
                self.effective = True
                self.numb_timer = 20 + random.randint(-5,5)
        return super().__setattr__(name, value)

Numb.SetImage(numb)

class Ponised(Buff):
    """
    Lose HP over time
    """
    # balance unfit
    def check(self):
