import pygame
import pickle
import character
import functions
import objects
from functions.values import screenborder

class Buff(pygame.sprite.Sprite):
    """
    use this to define buffs and debuffs
    """
    def __init__(self, buff_group, name, owner=None, time=-1):
        super().__init__(buff_group)
        self.name = name
        self.owner = owner
        self.stack = {} # temp value in this
        if isinstance(self.owner, character.erina.Erina):
            self.type = 1
        elif isinstance(self,owner, objects.sprites.Boss):
            self.type = -1
        elif isinstance(self.owner, objects.sprites.Elf):
            self.type = 0
        

        # if timer > 10 or timer == -1, it's buff time
        self.time = time
        self.timer = 0
        self.birth_time = 180
        self.death_time = 30

        self.image = pygame.surface.Surface((17,11)).convert()
        self.rect = self.image.get_rect()
        self.image.blit(self.image_temp, (0,0))
        self.rank = len(buff_group)
        self.temp_position = [0,0]

        if isinstance(owner, character.erina.Erina):
            self.temp_position[0] = screenborder.SCREEN_RIGHT
            self.temp_position[1] = screenborder.SCREEN_BOTTOM - 30 - 20*self.rank
            self.rect.left, self.rect.bottom = self.temp_position
        elif isinstance(owner, objects.sprites.Boss):
            self.temp_position[0] = screenborder.SCREEN_LEFT
            self.temp_position[1] = screenborder.SCREEN_TOP + 30 + 20*self.rank
        elif isinstance(owner, objects.sprites.Elf):
            self.rect.center = owner.center

    @classmethod
    def SetImage(cls, buff_name):
        buff_name = 'data/tmp/'+ buff_name +'.tmp'
        try:
            cls.image_temp = pygame.image.load(buff_name).convert_alpha()
        except FileNotFoundError:
            filename = 'data/obj/items/buffs.rbrb'
            with open(filename,'rb') as f:
                images = pickle.load(f)
            for key,value in images.items():
                filename = 'data/tmp/imgs/'+key+'.tmp'
                with open(filename,'wb') as f:
                    f.write(value)
            cls.(buff_name)

    def move_elf(self):
        self.rect.center = self.owner.center

    def move_in(self):
        if self.type == 1:
            destination = [screenborder.SCEREEN_RIGHT-50, screenborder.SCREEN_BOTTOM-30-20*self.rank]
            speed = (self.rect.right - destination[0])/2 # problems unfit
            self.direction = functions.snipe((self.rect.right, self.rect.bottom), destination, type='vector')
            self.temp_position[0] += self.direction[0]*speed
            self.temp_position[1] += self.direction[1]*speed # problems unfit
            self.rect.right, self.rect.bottom = self.temp_position
        elif self.type == -1:
            destination = [screenborder.SCREEN_LEFT+50, screenborder.SCREEN_TOP+30+20*self.rank]
            speed = (self.rect.left - destination[0])/2
            self.direction = functions.snipe((self.rect.left, self.rect.top), destination, type='vector')
            self.temp_position[0] += self.direction[0]*speed
            self.temp_position[1] += self.direction[1]*speed
            self.rect.left, self.rect.top = self.temp_position
        else:
            self.rect.center = self.owner.center

    def move_out(self):
        if self.type == 1:
            speed = (screenborder.SCREEN_RIGHT-self.rect.left)/2 # problems unfit
            self.temp_position[0] += speed
            self.rect.right, self.rect.bottom = self.temp_position
        elif self.type == -1:
            speed = (screenborder.SCREEN_LEFT-self.rect.right)/2 # problems unfit
            self.temp_position[0] += speed
            self.rect.left, self.rect.bottom = self.temp_position
        else:
            pass

    def move_up(self):
        """
        only happened on boss side
        """
        destination = screenborder.SCREEN_TOP + 30 + 20*self.rank
        speed = (self.rect.top - destination)/2
        self.temp_position[1] -= speed
        self.rect.top, self.rect.left = self.temp_position

    def move_down(self):
        """
        only happened on erina side
        """
        destination = screenborder.SCREEN_BOTTOM - 30 - 20*self.rank
        speed = (self.rect.bottom - destination)/2
        self.temp_position[1] += speed
        self.rect.right, self.rect.bottom = self.temp_position

    def move(self):
        if isinstance(self.owner, character.erina.Erina):
            self.move_erina()
        elif isinstance(self,owner, objects.sprites.Boss):
            self.move_boss()
        elif isinstance(self.owner, objects.sprites.Elf):
            self.move_elf()


    def opacity_up(self):
        pass

    def opacity_off(self):
        pass

    def opacity_check(self, erina):
        if erina.rect.right >= Screen

    def remove(self):
        for buff in self.groups()[0]:
            if buff.rank>self.rank:
                buff.rank -= 1
        self.kill()
    
    def check(self, *sprites):
        """
        Buff.buff_check(*sprites): Return None

        origin is buff who owned
        *enemy store opponity(s)
        """    
        pass

class BuffGroup(pygame.sprite.Group): pass

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

    def __init__(self):
        self.buffdict = {}

    def buffs(self):
        return list(self.buffdict)

    def add_internal(self, buff):
        self.buffdict[buff] = len(self)+1

    def remove_internal(self, buff):
        for b in self.buffdict:
            if b.name == buff:
                count = self.buffdict[b]
                del self.buffdict[b]
                break
        for b in self.buffdict:
            if self.buffdict[b] > count:
                self.buffdict[b] -= 1

    def has_internal(self, buff):
        for b in self.buffdict:
            if b.name == buff:
                return True

    def copy(self):
        """
        copy a group with all the same sprites

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
                if not self.has_internal(buff):
                    self.add_internal(buff)
            else:
                try:
                    self.add(*buffs)
                except (TypeError, AttributeError):
                    if hasattr(buff, '_spritegroup'):
                        for b in buff.buffs():
                            if not self.has_internal(b):
                                self.add_internal(b)
                    elif not self.has_internal(buff):
                        self.add_internal(buff)

    def remove(self, *buffs):
        """
        remove buff(s) from group

        BuffGroup.remove(buff, ...): return None
        """
        for buff in buffs:
            if isinstance(buff, Buff):
                if self.has_internal(buff):
                    self.remove_internal(buff)
            else:
                try:
                    self.remove(*buffs)
                except (TypeError, AttributeError):
                    if hasattr(buff, '_buffgroup'):
                        for b in buff.buffs():
                            if self.has_internal(b):
                                self.remove_internal(b)
                    elif self.has_internal(buff):
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
        for b in self.buffs():
            self.remove_internal(b)

    def print(self, owner):
        pass

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

'''
#
# all buffs here:
#

class SpeedDown(Buff):
    """
    Speed lowered by 20%
    """
    def __init__(self, owner='boss'):
        Buff.__init__(self, 'speed down')
        self.owner = owner
        self.image = images[0]
        self.rect = self.image.get_rect()
        
    def move_in(self, owner):
        pass

    def move_out(self, owner):
        pass

    def check(self, origin, *enemy):
        if self.timer > 0 and self.timer < 10:
            pass
        elif self.timer == 10:
            self.active = False
            origin.speed *= 1.25
        elif self.timer > 10 or self.timer == -1:
            if self.active:
                pass
            else:
                origin.speed *= 0.8
                self.active = True
        self.timer -= 1

class Numb(Buff):
    """
    All movement ceases intermittently
    """
    def __init__(self):
        Buff.__init__(self, 'numb')