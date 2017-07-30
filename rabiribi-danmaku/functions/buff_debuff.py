import pygame
import pickle
import objects
import abc
import random
from functions.values import screenborder
from operator import truth
from objects.counter import BuffTimer

class AllBuffs:
    """
    define all buffs
    """
    speed_down = 0
    # Speed lowered by 20%
    numb = 0
    # All movement ceases intermittently
    ponised = 0
    # Lose HP over time
    attack_down = 0
    # Attack lowered by 25%
    defense_down = 0
    # Defense lowered by 25%
    cursed = 0
    # Take 50% of damage given.
    # Enemies with "Cursed" take 2% damage of their Max. HP
    # with a maximum damage of 666 points
    stunned = 0
    # All movement ceases.
    ban_skill = 0
    # Can't perform physical, non-magic attacks.
    mona_down = 0
    # Lose MP over time
    freeze = 0
    # When attacking, lose 3% HP every second.
    burn = 0
    # Lose 15% HP every 2 seconds.
    # Enemies with "Burn" lose 2-3 HP every 0.05 Seconds
    attack_up = 0
    # Attack raised by 25%
    defense_up = 0
    # Defense raised by 25%
    hp_recover = 0
    # Recover 1-3 HP every 0.25 seconds
    sp_recover = 0
    # Improve SP recovery rate.
    shrink = 0
    # Speed increased by 30%, attack lowered by 15%.
    # and damage taken increased by 30%
    # something else happens too
    giant = 0
    # Speed decreased by 50%, attack raised by 50%
    # and damage taken reduced by 50%
    # Something esle happens too.
    arrest = 0
    # A chance to slow down opponents by 20% when attacking
    speed_up = 0
    # Speed increased by 25%.
    badge_copy = 0
    # Opponent's badge perks are replicated.
    null_melee = 0
    # No damage taken from physical attacks.
    # Damage taken from carrot bomb increased by 62.5%
    defense_boost = 0
    # Damage taken reduced by 10-50%
    # 5%-25% in Boss Rush mode
    defense_drop = 0
    # Damage taken increased by 100%-300%
    stamina_down = 0
    # SP consumption increased by 325%
    null_slow = 0
    # Cannot be slowed down.
    super_armour = 0
    # No stun effect after being damaged
    quad_damage = 0
    # Attack raised by 400%
    double_damage = 0
    # Attack raised by 200%
    speedy = 0
    # Movement speed increased by 20%
    maxhp_up = 0
    # Max. HP increased proportional to characters unlocked.
    # Enemies with this status have a 10% Max. HP increase.
    maxmp_up = 0
    # Max. MP increased proportional to characters unlocked.
    # Enemieswith this status have greater attack frequency.
    amulet_cut = 0
    # Amulet consumption lowered by 25%.
    hp_regen = 0
    # Recover 2 HP every 1.5 seconds.
    # Enemies with this status recover 2% of Max. HP.
    mp_regen = 0
    # Recover 2MP every second.
    give_atk_down = 0
    # A chance to give opponents "Attack Down" when attacking.
    give_def_down = 0
    # A chance to give opponents "Defense Down" when attacking.
    unstable = 0
    # Speed changes randomly
    boost_fail = 0
    # Lose BP over time.
    hex_cancel = 0
    # No damage taken from every 6th attack.
    lucky_seven = 0
    # Every 7th successful attack inflicts 77% more damage.
    quick_reflex = 0
    # Lowers stun time by 75%.
    defense_large_boost = 0
    # Damage taken reduced by 50-100%.
    # 25%-50% in Boss Rash
    endurance = 0
    # Immune to all attacks, but lose HP over time.
    fatigue = 0
    # Speed and jump height lowered by 20%.
    reflect_99 = 0
    # 100% of damage taken reflected back to opponent.
    # Only applicable for attacks above 99 points.
    # Opponent's health will not fall below 1 HP
    survival_instinct = 0
    # HP cannot fall below 1.
    amulet_drain = 0
    # Lose amulet charge over time.
    mortality = 0
    # Lose all invulnerability when performing any moves.
    no_badges = 0
    # Lose effects from equipped badges.
    instant_death = 0
    # All attacks cause 4444 points of damage.
    health_absorb = 0
    # Absorb HP equal to 2 times the damage given.
    power_absorb = 0
    # Inflict a 100% SP, 33% MP, and 25% BP reduction in the opponent.
    revenge_300 = 0
    # "Instant death" status dealt to opponent.
    # Triggered when damage taken from one attack >300 points.
    bunny_lover = 0
    # Damage taken reduced by 50% when the opponent is a bunny
    healing = 0
    # Recover HP over time.
    t_minus_two = 0
    # Gain "T Minus One" status after a successful attack.
    t_minus_one = 0
    # Gain "Attack Boost" status after a successful consecutive attack.
    attack_boost = 0
    # Bullet hell density increased.
    zero_offense = 0
    # Attack reduced by 100%
    halo_buff = 0
    # Damage taken reduced by 10% after three "Game Over"
    # Status removed after "Halo Boost" expires.
    # Does not apply above Normal difficulty
    halo_boost_lv1 = 0
    # Damage taken -15%. Amulet recharges 33% faster.
    # Recover 1 HP for every three successful attacks.
    # Gained after 3-4 "Game Over", No buff above "Normal"
    halo_boost_lv2 = 0
    # Damage taken -27.5%. Amulet recharges 67% faster.
    # Recover 1 HP for every two successful attacks.
    # Gained after 5-6 "Game Over", No buff above "Noraml"
    halo_boost_lv3 = 0
    # Damage taken -40%. Amulet recharges 100% faster.
    # Recover 1 HP for every successful attack.
    # Gained after 7+ "Game Over", No buff above "Normal"

class Buff(pygame.sprite.Sprite):
    __metaclass__ = abc.ABCMeta
    """
    use this to define buffs and debuffs
    """
    _erina_only = False
    _boss_only = False
    _special_only = None

    '''
    def __new__(cls, *buff_group, owner=None, time=-1):
        if owner and timer > 0:
            return super().__new__(*buff_group, owner, time)
        else:
            cls._instance = cls
            cls._instance.time = time
            return cls._instance
    '''

    def __init__(self, owner=None, time=-1):
        """
        __init__(owner=None, time=-1): return None

            buff group 
        """
        super().__init__()
        if owner: self.init(owner)
        
        # buff effect: timellarger than 0 and equal -1
        self.time = time

    def init(self, owner):
        #self.owner = owner
        super().__setattr__('owner', owner)
        self.stack = {} # temp value in this
        self.timer = 0
        self.birth_time = 120
        self.death_time = 20 # max 30
        self.moveup = 0
        self.movedown = 0

        self.effective = True
        self.invalid = False

        self.image = pygame.surface.Surface((17,11)).convert()
        self.opacity = 255
        self.rect = self.image.get_rect()
        #self.image.blit(self.image_temp, (0,0))
        self.rank = len(self.owner.buff)
        self.temp_position = [0,0]

        self.delete = False

        if self.owner._type == 'erina':
            self.temp_position[0] = screenborder.SCREEN_RIGHT
            self.temp_position[1] = screenborder.SCREEN_BOTTOM - 30 - 15*self.rank
            self.rect.left, self.rect.bottom = self.temp_position
        elif self.owner._type == 'boss':
            self.temp_position[0] = screenborder.SCREEN_LEFT
            self.temp_position[1] = screenborder.SCREEN_TOP + 30 + 15*self.rank
        elif self.owner._type == 'elf':  # under development
            self.rect.center = owner.center

    @classmethod
    def SetImage(cls, buff_name):
        buff_name = 'data/tmp/imgs/'+ buff_name +'.tmp'
        try:
            cls.image_temp = pygame.image.load(buff_name).convert_alpha()
        except pygame.error:
            filename = 'data/obj/items/buffs.rbrb'
            with open(filename, 'rb') as f:
                images = pickle.load(f)
            for key,value in images.items():
                filename = 'data/tmp/imgs/'+key+'.tmp'
                with open(filename, 'wb') as f:
                    f.write(value)
            cls.image_temp = pygame.image.load(buff_name).convert_alpha()

    def move_elf(self):
        self.rect.center = self.owner.center

    def move_in(self):
        if self.owner._type == 'erina':
            if self.birth_time > 30:
                destination = screenborder.SCREEN_RIGHT-50
            else:
                destination = screenborder.SCREEN_RIGHT
            speed = (self.rect.right - destination)/4 # problems unfit
            self.temp_position[0] -= speed
            self.rect.right, self.rect.bottom = self.temp_position
        elif self.owner._type == 'boss':
            if self.birth_time > 30:
                destination = screenborder.SCREEN_LEFT+50
            else:
                destination = screenborder.SCREEN_RIGHT+17
            speed = (self.rect.left - destination)/4 # problems unfit
            self.temp_position[0] += speed
            self.rect.left, self.rect.top = self.temp_position
        else:
            self.rect.center = self.owner.center
        self.birth_time -= 1

    def move_out(self):
        if self.owner._type == 'erina':
            speed = (screenborder.SCREEN_RIGHT+5 - self.rect.left)/2 # problems unfit
            self.temp_position[0] += speed
            self.rect.right, self.rect.bottom = self.temp_position
        elif self.owner._type == 'boss':
            speed = (screenborder.SCREEN_LEFT - self.rect.right)/2 # problems unfit
            self.temp_position[0] -= speed
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
        self.temp_position[1] -= speed
        self.rect.right, self.rect.bottom = self.temp_position
        self.movedown -= 1

    def move(self, erina):
        self.opacity_check(erina)
        if self.time > 0:
            self.time -= 1
        else:
            self.move_out()
        if self.birth_time: self.move_in()
        if self.moveup: self.move_up()
        if self.movedown: self.move_down()
        self.timer += 1
        #print(len(self.groups()))

    def opacity_up(self):
        if self.opacity < 255:
            self.opacity += 10
            if self.opacity > 255:
                self.opacity = 255

    def opacity_down(self):
        if self.opacity > 50:
            self.opacity -= 10
            if self.opacity < 50:
                self.opacity = 50

    def opacity_check(self, erina):
        erina_rect = erina.rect
        count = len(self.owner.buff)
        if self.owner._type == 'erina':
            if erina_rect.right >= screenborder.SCREEN_RIGHT-60 and erina_rect.bottom > screenborder.SCREEN_BOTTOM-40-15*count:
                self.opacity_down()
            else:
                self.opacity_up()
        elif self.owner._type == 'boss':
            if erina_rect.left <= screenborder.SCREEN_LEFT+60 and erian_rect.top > screenborder.SCREEN_TOP+40+15*count:
                self.opacity_down()
            else:
                self.opacity_up()

    def remove(self):
        for buff in self.owner.buff:
            if buff.rank > self.rank:
                buff.rank -= 1
        self.owner.buff.remove(self)
    
    @abc.abstractmethod
    def check(self, *sprites):
        """
        Buff.buff_check(*sprites): Return None
        """    
        raise NotImplementedError

    def print_screen(self, screen):
        self.image.blit(screen, (self.rect.left-640, self.rect.top-480))
        self.image.blit(self.image_temp, (0,0))
        self.image.set_alpha(self.opacity)
        screen.blit(self.image, self.rect)

    def __setattr__(self, name, value):
        if name == 'rank':
            if self.owner._type == 'erina':
                self.movedown = 30
            elif self.owner._type == 'boss':
                self.moveup = 30
            else: pass
        elif name == 'owner':
            self.init(value)
            return
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

class BuffGroup(pygame.sprite.Group):
    def add_internal(self, sprite):
        name = sprite.__class__.__name__
        for key, value in self.spritedict.items():
            if value == name:
                key.time = sprite.time
                key.birth_time = 120
                key.death_time = 20
                key.effective = True
                key.invalid = False
                return
        self.spritedict[sprite] = sprite.__class__.__name__

    def has_internal(self, sprite):
        return (sprite in self.spritedict) or (sprite in self.spritedict.values())

    def remove_internal(self, sprite):
        if isinstance(sprite, pygame.sprite.Sprite):
            del self.spritedict[sprite]
        elif isinstance(sprite, str):
            for key, value in self.spritedict.items():
                if sprite == 'value':
                    r = key
                    break
            del self.spritedict[r]
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
    _spritegroup = True

    def __init__(self, *buff):
        self.buffdict = {}
        for b in buff:
            self.add_internal(b)

    def buffs(self):
        return list(self.buffdict)
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
            buff.add_internal(self)

    def remove(self, *buffs):
        """
        remove buff(s) from group

        BuffGroup.remove(buff, ...): return None
        """
        for buff in buffs:
            if isinstance(buff, Buff):
                self.remove_internal(buff.__class__.__name__)
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

    def move(self):
        for each in self.buffs():
            each.move()

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
    def __init__(self, *buff_group, owner=None, time=-1):
        super().__init__(*buff_group, owner, time)
        

    def init(self, owner):
        super().init(owner)
        self.stack['fast'] = self.owner.fast
        self.stack['slow'] = self.owner.slow

    def check(self, *enemy):
        if self.time==0:
            self.invalid = True
        if self.effective:
            self.owner.fast = 2
            self.owner.slow = 1
            self.effective = False
        if self.invalid:
            self.owner.fast = self.stack['fast']
            self.owner.slow = self.stack['slow']
            self.invalid = False
            
SpeedDown.SetImage('speed_down')

class Numb(Buff):
    """
    All movement ceases intermittently
    """
    def __init__(self, *buff_group, owner=None, time=-1):
        super().__init__(*buff_group, owner, time)
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

Numb.SetImage('numb')

class Ponised(Buff):
    """
    Lose HP over time
    """
    # balance unfit
    def check(self):
        pass