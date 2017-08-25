import pygame
import pickle
import objects
import abc
import random
from functions.values import screenborder
from operator import truth
from objects.counter import BuffTimer
from functions.values import defaultkey

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

    _item_mode = False

    '''
    def __new__(cls, *buff_group, owner=None, time=-1):
        if owner and timer > 0:
            return super().__new__(*buff_group, owner, time)
        else:
            cls._instance = cls
            cls._instance.time = time
            return cls._instance
    '''

    def __init__(self, *buff_group, owner=None, time=-1):
        """
        __init__(owner=None, time=-1): return None

            buff group 
        """
        super().__init__(*buff_group)
        if owner: 
            super().__setattr__('owner', owner)
            self.init(owner)
        # buff effect: timellarger than 0 and equal -1
        self.time = time
        self.s = {}

    def stack(self, *args, **kwargs):
        pass

    def init(self, owner):
        #self.owner = owner
        super().__setattr__('owner', owner)
        #self.stack = {} # temp value in this
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
        _buff_name = 'data/tmp/imgs/'+ buff_name +'.tmp'
        try:
            cls.image_temp = pygame.image.load(_buff_name).convert_alpha()
        except pygame.error:
            filename = 'data/objs/items/buffs.rbrb'
            with open(filename, 'rb') as f:
                images = pickle.load(f)
            for key,value in images.items():
                filename = 'data/tmp/imgs/'+key+'.tmp'
                with open(filename, 'wb') as f:
                    f.write(value)
            cls.image_temp = pygame.image.load(_buff_name).convert_alpha()

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
        elif self.time == 0:
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
            self.stack()
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
        self.spritedict[sprite] = name
        self.__setattr__(name, sprite)

    def has_internal(self, sprite):
        return (sprite in self.spritedict) or (sprite in self.spritedict.values())

    def remove_internal(self, sprite):
        if isinstance(sprite, pygame.sprite.Sprite):
            del self.spritedict[sprite]
            self.__delattr__(sprite.__class__.__name__)
        elif isinstance(sprite, str):
            r = False
            for key, value in self.spritedict.items():
                if sprite == value:
                    r = key
                    break
            if r:
                del self.spritedict[r]
                self.__delattr__(sprite)
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
    def stack(self):
        self.s['fast'] = self.owner.fast
        self.s['slow'] = self.owner.slow

    def check(self, erina, *enemy):
        if self.time==0:
            self.invalid = True
        if self.effective:
            self.owner.fast = 2
            self.owner.slow = 1
            self.effective = False
        if self.invalid:
            self.owner.fast = self.s['fast']
            self.owner.slow = self.s['slow']
            self.invalid = False
            
SpeedDown.SetImage('speed_down')

class Numb(Buff):
    """
    All movement ceases intermittently
    """
    def stack(self):
        self.s['speed'] = self.owner.speed
        # balance unfit
        self.numb_timer = 20 + random.randint(-5,5)

    def check(self, erina, *enemy):
        if self.time==0:
            self.invalid = True
        if self.effective:
            self.owner.speed = 0
            if self.numb_timer>0:
                self.numb_timer -= 1
            else:
                self.effective = False
        if self.invalid:
            self.owner.speed = self.s['speed']

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
    p_timer = 0
    def check(self, erina, *enemy):
        if self.p_timer % 45 == 0:
            self.owner.damage.poisond += 1
        self.p_timer += 1

Ponised.SetImage('ponised')

class AttackDown(Buff):
    """
    Attack lowered by 25%
    """
    def stack(self):
        self.s['attack'] = self.owner.atk

    def check(self, erina, *enemy):
        if self.time == 0:
            self.invalid = True
        if self.effective:
            self.owner.atk -= (self.owner.atk/4).__int__()
            self.effective = False
        if self.invalid:
            self.owner.atk = self.s['attack']
        '''
        if self.owner._type == 'erina':
            for e in enemy:
                r = e.damage.danmaku * 0.25
                e.damage.danmaku -= r.__int__()
        else:
            # under development
            r = erina.damage.danmaku * 0.25
            erina.damage.danmaku -= r.__int__()
        '''

AttackDown.SetImage('attack_down')

class DefenseDown(Buff):
    """
    Defense lowered by 25%
    """
    def check(self, erina, *enemy):
        self.owner.damage.danmaku += (self.owner.damage.danmaku/4).__int__()
        self.owner.damage.magic += (self.owner.damage.magic/4).__int__()

DefenseDown.SetImage('defense_down')

class Cursed(Buff):
    """
    Take 50% of damage given
    Enemies with "Cursed" take 2% damage of their Max.Hp
    with a maximum damage of 666 points
    """
    def check(self, erina, *enemy):
        if self.owner._type == 'erina':
            for e in enemy:
                self.owner.damage.cursed += e.damage.danmaku//2
        else:
            if erina.damage.danmaku or erina.damage.get_buff:
                d = (self.owner.hp*0.02).__int__()
                if d > 666:
                    d = 666
                self.owner.damage.cursed += d

Cursed.SetImage('cursed')

class Stunned(Buff):
    """
    All movement ceases
    """
    _erina_only = True
    def stack(self):
        self.s['fast'] = self.owner.fast
        self.s['slow'] = self.owner.slow

    def check(self, erina, *enemy):
        if self.time == 0:
            self.invalid = True
        if self.effective:
            self.owner.fast = 0
            self.owner.slow = 0
            self.effective = False
        if self.invalid:
            self.owner.fast = self.s['fast']
            self.owner.slow = self.s['slow']
            self.invalie = False

Stunned.SetImage('cursed')

class BanSkill(Buff):
    """
    Can't perform physical, non-magic attacks.
    """
    _erina_only = True
    
BanSkill.SetImage('ban_skill')

class MonaDown(Buff):
    """
    Lose MP over time
    """
    _erina_only = True
    def check(self, erina, *enemy):
        self.owner.ribbon.mp -= 1
        # balance unfit

MonaDown.SetImage('mona_down')

class Freeze(Buff):
    """
    When attacking, lose 3% HP every second
    """
    _erina_only = True
    def init(self, owner):
        super().init(owner)
        self.delay_timer = 0

    def check(self, erina, *enemy):
        k = pygame.key.get_pressed()
        if k[defaultkey.SHOUTING]:
            self.delay_timer = 60
        if self.delay_timer:
            if self.delay_timer % 20 == 0:
                self.owner.damage.freeze += (self.owner.hp*0.01).__int__()
        
Freeze.SetImage('freeze')

class Burn(Buff):
    """
    Lose 15% HP every 2 seconds
    Enemies with "Burn" lose 2-3 HP every 0.05 Seconds
    """
    def init(self, owner):
        super().init(owner)

    def check(self, erina, *enemy):
        if self.owner._type == 'erina':
            if self.timer % 40 == 0:
                self.owner.damage.burn += (self.owner.hp*0.05).__int__()
        else:
            if self.timer % 3 == 0:
                self.owner.damage.burn += random.randint(2,3)

Burn.SetImage('burn')

class AttackUp(Buff):
    """
    Attack raised by 25%
    """
    def stack(self):
        self.s['attack'] = self.owner.atk
    
    def check(self, erina, *enemy):
        if self.time == 0:
            self.invalid = True
        if self.effective:
            self.owner.atk -= (self.owner.atk/4).__int__()
            self.effective = False
        if self.invalid:
            self.owner.atk = self.s['attack']

AttackUp.SetImage('attack_up')

class DefenseUp(Buff):
    """
    Defense raised by 25%
    """
    def check(self, erina, *enemy):
        self.owner.damage.danmaku -= (self.owner.damage.danmaku/4).__int__()
        self.owner.damage.magic -= (self.owner.damage.magic/4).__int__()
DefenseUp.SetImage('defense_up')

class HPRecover(Buff):
    """
    Recover 1-3 HP every 0.25 seconds
    """
    def check(self, erina, *enemy):
        if self.timer % 15 == 0:
            hp = random.randint(1,3)
            self.owner.hp += hp
            if self.owner.hp >= self.owner.max_hp:
                self.owner.hp = int(self.owner.max_hp)

HPRecover.SetImage('hp_recover')

class SPRecover(Buff):
    """
    Improve SP recovery rate
    """
    _erina_only = True
    def check(self, erina, *enemy):
        self.owner.ribbon.sp += 1

SPRecover.SetImage('sp_recover')

class Shrink(Buff):
    """
    Speed increased by 30%, attack lowered by 15%
    and damage taken increased by 30%
    something else happens too
    """
    # under development
    _erina_only = True
    def stack(self):
        self.s['fast'] = self.owner.fast
        self.s['slow'] = self.owner.slow
        self.s['attack'] = self.owner.atk
        self.s['rect'] = self.owner.rect

    def check(self, erina, *enemy):
        if hasattr(self.owner.buff, 'Giant'):
            self.owner.buff.Giant.time = 0
        self.owner.damage.danmaku += (self.owner.damage.danmaku*0.3).__int__()
        self.owner.damage.magic += (self.owner.damage.magec*0.3).__int__()
        if self.time == 0:
            self.invalid = True
        if self.effective:
            self.owner.fast += self.owner.fast*0.3
            self.owner.slow += self.owner.slow*0.3
            self.owner.atk -= (self.owner.atk*0.15).__int__()
            '''
            self.owner.rect = pygame.transform.scale(0.5)
            '''
            self.effective = False
        if self.invalid:
            self.owner.fast = self.s['fast']
            self.owner.slow = self.s['slow']
            self.owner.atk = self.s['attack']
            '''
            self.owner.rect = pygame.transform.scale(2)
            '''

Shrink.SetImage('shrink')

class Giant(Buff):
    """
    Speed decreased by 50%
    and damage taken reduced by 50%
    Something else happens too
    """
    _erina_only = True
    def stack(self):
        self.s['fast'] = self.owner.fast
        self.s['slow'] = self.owner.slow
        self.s['attack'] = self.owner.atk
        self.s['rect'] = self.owner.rect

    def check(self, erina, *enemy):
        if hasattr(self.owner.buff, 'Shrink'):
            self.owner.buff.Shrink.time = 0
        if self.time == 0:
            self.invalid = True
        if self.effective:
            self.owner.fast /= 2
            self.owner.slow /= 2
            self.owner.atk = (self.onwer.atk/2).__int__()
            '''
            self.owner.rect = pygame.transform.scale(2)
            '''
            self.effective = False
        if self.invalid:
            self.owner.fast = self.s['fast']
            self.owner.slow = self.s['slow']
            self.owner.atk = self.s['attack']
            '''
            self.owner.rect = pygame.transform.scale(0.5)
            '''

Shrink.SetImage('shrink')

class Arrest(Buff):
    """
    A chanse to slow down apponents by 20% when attacking
    """
    # under development
    # maybe useless
    _erina_only = True
    def check(self, erina, *enemy):
        if random.random() < 0.2:
            self.owner.ribbon.buff.add(SpeedDown)

Arrest.SetImage('arrest')

class SpeedUp(Buff):
    """
    Speed increased by 25%
    """
    def stack(self):
        if self.owner._type == 'erina':
            self.s['fast'] = self.owner.fast
            self.s['slow'] = self.owner.slow
        else:
            self.s['speed'] = self.owner.speed

    def check(self, erina, *enemy):
        if self.time == 0:
            self.invalid = True
        if self.effective:
            if self.owner._type == 'erina':
                self.owner.fast *= 1.25
                self.owner.slow *= 1.25
            else:
                self.owner.speed *= 1.25
            self.effective = False
        if self.invalid:
            for k,v in self.s.items():
                self.owner.__setattr__(k,v)

SpeedUp.SetImage('speed_up')

class BadgeCopy(Buff):
    """
    Opponent's badge perks are replicated
    """
    _boss_only = True
    _special_only = 'miriam'
    def check(self, erina, *enemy):
        if self.effective:
            self.owner.badge.add(erina,badge)
            self.effective = False

BadgeCopy.SetImage('badge_copy')

class NullMelee(Buff):
    """
    No damage taken from physical attacks
    Damage taken from carrot bomb increased by 62.5%
    """
    # under development
    # maybe useless
    _boss_only = True
    def check(self, erina, *enemy):
        self.owner.damage.danmaku = 0

NullMelee.SetImage('null_melee')

class DefenseBoost(Buff):
    """
    Damage taken reduced by 50%
    25% in Boss Rush mode
    """
    def check(self, erina, *enemy):
        self.owner.damage.danmaku -= self.owner.damage.danmaku//2
        self.owner.damage.magic -= self.owner.damage.magic//2

DefenseBoost.SetImage('defense_boost')

class DefenseDrop(Buff):
    """
    Damage taken increased by 100%-300%
    """
    def check(self, erina, *enemy):
        rate = 1+random.random()*2
        self.owner.damage.danmaku += (self.owner.damage.danmaku*rate).__int__()
        self.owner.damage.magic += (self.owner.damage.magic*rate).__int__()

DefenseDrop.SetImage('defense_drop')

class StaminaDown(Buff):
    """
    SP consumption increased by 325%
    """
    # useless
    def check(self, erina, *enemy):
        '''just for fun'''

StaminaDown.SetImage('stamina_down')

class NullSlow(Buff):
    """
    Cannot be slowed down
    """
    # under development
    def check(self, erina, *enemy):
        if isinstance(self.owner.timer, float):
            self.owner.timer = self.owner.timer.__int__()+1

NullSlow.SetImage('null_slow')

class SuperArmour(Buff):
    """
    No stun effect after being damaged
    """
    # useless
    def check(self, erina, *enemy):
        '''just for fun'''
        # maybe effects

SuperArmour.SetImage('super_armour')

class QuadDamage(Buff):
    """
    Attack raised by 400%
    """
    def stack(self):
        self.s['attack'] = self.owner.atk

    def check(self, erina, *enemy):
        if self.time == 0:
            self.invalid = True
        if self.effective:
            self.owner.atk *= 4
            self.effective = False
        if self.invalid:
            self.owner.atk = self.s['attack']
            
QuadDamage.SetImage('quad_damage')

class DoubleDamage(Buff):
    """
    Attack raised by 200%
    """
    def stack(self):
        self.s['attack'] = self.owner.atk

    def check(self, erina, *enemy):
        if self.time == 0:
            self.invalid = True
        if self.effective:
            self.owner.atk *= 2
            self.effective = False
        if self.invalid:
            self.owner.atk = self.s['attack']

DoubleDamage.SetImage('double_damage')

class Speedy(Buff):
    """
    Movement speed increased by 20%
    """
    def stack(self):
        if self.owner._type == 'erina':
            self.s['fast'] = self.owner.fast
            self.s['slow'] = self.owner.slow
        else:
            self.s['speed'] = self.owner.speed

    def check(self, erina, *enemy):
        if self.time == 0:
            self.invalid = Ture
        if self.effective:
            if self.owner._type == 'erina':
                self.owner.fast *= 1.2
                self.owner.slow *= 1.2
            else:
                self.owner.speed *= 1.2
            self.effective = False
        if self.invalid:
            for k,v in self.s.items():
                self.owner.__setattr__(k,v)

Speedy.SetImage('speedy')

class MaxHPUp(Buff):
    """
    Max.HP increased proportional to characters unlocked.
    Enemies with this status have a 10% MaxHP increase
    """
    # under development
    def stack(self):
        self.s['maxhp'] = self.owner.max_hp

    def check(self, erina, *enemy):
        if self.time == 0:
            self.invalid = True
        if self.effective:
            self.owner.max_hp += self.owner.max_hp//10
            self.effective = False
        if self.invalid:
            self.owner.max_hp == self.s['maxhp']
            if self.owner.hp > self.owner.max_hp:
                self.owner.hp = int(self.owner.max_hp)

MaxHPUp.SetImage('maxhp_up')

class MaxMPUp(Buff):
    """
    Max. MP increased proportional to characters unlocked
    Enemis with this status have greater attack frequency
    """
    # maybe useless
    _erina_only = True
    _special_only = 'miriam'
    def stack(self):
        self.s['maxmp'] = self.owner.max_mp

    def check(self, erina, *enemy):
        if self.time == 0:
            self.invalid = True
        if self.effective:
            self.owner.max_mp += self.owner.max_mp//10
            self.effective = False
        if self.invalid:
            self.owner.max_mp = self.s['maxmp']

MaxMPUp.SetImage('maxmp_up')

class AmuletCut(Buff):
    """
    Amulet consumption lowered by 25%
    """
    # under development
    _erina_only = True
    _special_only = 'miriam'
    def check(self, erina, *enemy):
        if self.time == 0:
            self.invalid = True
        if self.effective:
            self.owner.amulet_consume = 750
            self.effective = False
        if self.invalid:
            self.owner.amulet_consume = 1000

AmuletCut.SetImage('amulet_cut')

class HPRegen(Buff):
    """
    Recover 2 HP every 1.5 seconds.abcEnemies with this status recover 2% of Max. HP
    """
    def check(self, erina, *enemy):
        if self.owner._type == 'erina':
            if self.timer % 90 == 0:
                self.owner.hp += 2  # balance unfit
        else:
            if self.timer % 90 == 0:
                self.owner.hp += self.owner.max_hp//50

HPRegen.SetImage('hp_regen')

class MPRegen(Buff):
    """
    Recover 2 MP every second
    """
    # under deveopment
    # balance unfit
    # maybe useless
    _erina_only = True
    def check(self, erina, *enemy):
        self.owner.ribbon.mp += 2

MPRegen.SetImage('mp_regen')

class GiveAtkDown(Buff):
    """
    A chance to give opponents "Attack Down" when attacking
    """
    # under development
    # maybe useless
    _erina_only = True
    def check(self, erina, *enemy):
        if random.random() < 0.2:
            self.owner.ribbon.buff.add(AttackDown)

GiveAtkDown.SetImage('give_atk_down')

class GiveDefDown(Buff):
    """
    A chance to give opponents "Defense Down" when attacking
    """
    # under development
    # maybe useless
    _erina_only = True
    def check(self, erina, *enemy):
        if random.random() < 0.2:
            self.owner.ribbon.buff.add(DefenseDown)

GiveDefDown.SetImage('give_def_down')

class Unstable(Buff):
    """
    Speed changes randomly
    """
    _erina_only = True
    def stack(self):
        self.s['fast'] = self.owner.fast
        self.s['slow'] = self.owner.slow
    
    def check(self, erina, *enemy):
        if self.time == 0:
            self.invalid = True
        if self.effective:
            r = random.random()
            self.owner.fast += -1 + 3*r
            self.owner.slow += -1 + 2*r
            self.effective = False
        if self.invalid:
            self.owner.fast = self.s['fast']
            self.owner.slow = self.s['slow']
            self.invalid = False

    def __setattr__(self, name, value):
        if name == 'timer':
            if value % 300 == 0:
                self.effective = True
            elif (value + 150) % 300 == 0:
                self.invalid = True
        return super().__setattr__(name, value)

Unstable.SetImage('unstable')

class BoostFail(Buff):
    """
    lose BP over time
    """
    # under development
    # balance unfit
    _erina_only = True
    def check(self, erina, *enemy):
        self.owner.ribbon.mp -= 2

BoostFail.SetImage('boost_fail')

class HexCancel(Buff):
    """
    No damage taken from every 6th attack
    """
    def init(self, owner):
        super().init(owner)
        self.damage_count = 0

    def check(self, erina, *enemy):
        if self.owner.damage.danmaku or self.owner.damage.magic:
            self.damage_count += 1
            if self.damage_count == 6:
                self.owner.damage.danmaku = 0
                self.owner.damage.magic = 0
                self.damage_count = 0

HexCancel.SetImage('hex_cancel')

class LuckySeven(Buff):
    """
    Every 7th successful attack inflicts 7% or 77% more damage
    """
    def init(self, owner):
        super().init(owner)
        self.successful_attack = 0

    def check(self, erina, *enemy):
        if self.owner._type == 'erina':
            for e in enemy:
                if e.damage.danmaku or e.damage.magic:
                    self.successful_attack += 1
                    if self.successful_attack == 7:
                        e.damage.danmaku += (e.damage.danmaku*0.77).__int__()
                        e.damage.magic += (e.damage.magic*0.77).__int__()
        else:
            if erina.damage.danamku:
                self.successful_attack += 1
                if self.successful_attack == 7:
                    erina.damage.danmaku = (erina.damage.danmaku*0.77).__int__()

LuckySeven.SetImage('lucky_seven')

class QuickReflex(Buff):
    """
    Lowers stun time by 75%
    """
    # useless
    # maybe add effects

QuickReflex.SetImage('quick_reflex')

class DefenseLargeBoost(Buff):
    """
    Damage taken reduced by 50-100%
    25-50% in Boss Rash
    """
    # balance unfit
    _boss_only = True
    def check(self, erina, *enemy):
        self.owner.damage.danmaku -= (self.owner.damage.danmaku*0.8).__int__()
        self.owner.damage.magic -= (self.owner.damage.magic*0.8).__int__()
        self.owner.damage.amulet -= (self.owner.damage.amulet*0.8).__int__()
        self.owner.damage.cocoabomb -= (self.owner.damage.cocoabomb*0.8).__int__()
        self.owner.damage.boost -= (self.owner.damage.boost*0.8).__int__()

DefenseLargeBoost.SetImage('defense_large_boost')

class Endurance(Buff):
    """
    Immune to all attacks, but lose HP over time
    """
    _boss_only = True
    def check(self, erina, *enemy):
        self.owner.damage.danmaku = 0
        self.owner.damage.magic = 0
        self.owner.damage.amulet = 0
        self.owner.damage.cocoabomb = 0
        self.owner.damage.boost = 0
        self.owner.damage.endurance = 2

class Fatigue(Buff):
    """
    Speed and jump[?] height lowered by 20%
    """
    # useless 
    # maybe under water

Fatigue.SetImage('fatigue')

class Reflect99(Buff):
    """
    100% of damage taken reflected back to opponent
    Only applicable for attacks above 99 points
    Opponent's health will not fal below 1 HP
    """
    # under development
    def check(self, erina, *enemy):
        if self.owner._type == 'erina':
            if self.owner.damage.danmaku > 99:
                for e in enemy:
                    e.damage.reflect = self.owner.damage.danmaku
        else:
            d = self.owner.damage.danmaku + self.owner.damage.magic
            if d > 99:
                erina.damage.reflect = d

Reflect99.SetImage('reflect_99')

class SurvivalInstinct(Buff):
    """
    HP cannot fall below 1
    """
    def check(self, erina, *enemy):
        if self.owner._type == 'erina':
            if self.owner.hp > 1:
                self.time = 0
        else:
            self.owner.damage.all_damage = 0
            
SurvivalInstinct.SetImage('survival_instinct')

class AmuletDrain(Buff):
    """
    Lose amulet charge over time
    """
    _erina_only = True
    def check(self, erina, *enemy):
        self.owner.amulet = 0

AmuletDrain.SetImage('amulet_drain')

class Mortality(Buff):
    """
    Lose all invulnerablity when performing any movement
    """
    def check(self, erina, *enemy):
        if self.owner.invincible:
            self.owner.invincible = 1

Mortality.SetImage('mortality')

class NoBadges(Buff):
    """
    Lose effects from equipped badges
    """
    # under development
    _erina_only = True
    def stack(self):
        self.s['badges'] = self.owner.badges.copy()

    def check(self, erina, *enemy):
        if self.time == 0:
            self.invalid = True
        if self.effective:
            self.owner.badges.empty()
            self.effective = False
        if self.invalid:
            self.owner.badges.add(self.s['badges'])

NoBadges.SetImage('no_badges')

class InstantDeath(Buff):
    """
    All attacks cause 4444 points of damage
    """
    def check(self, erina, *enemy):
        if self.owner._type == 'erina':
            if self.owner.damage.danmaku:
                self.owner.damage.danmaku = 0
                self.owner.damage.instant = 4444
        else:
            if self.owner.damage.danmaku or self.owenr.damage.magic:
                self.owner.damage.danmaku, self.owenr.damage.magic = 0, 0
                self.owner.damage.instant = 4444

InstantDeath.SetImage('instant_death')

class HealthAbsorb(Buff):
    """
    Absorb HP equal to 2 times the damage given
    """
    _boss_only = True
    def check(self, erina, *enemy):
        if erina.damage.danmaku:
            self.owner.hp += erina.damage.danmaku*2
            if self.owner.hp > self.owner.max_hp:
                self.owner.hp = int(self.owner.max_hp)

HealthAbsorb.SetImage('health_absorb')

class PowerAbsorb(Buff):
    """
    Inflict a 100%SP, 33% MP, and 25 BP reduction in the opponent
    """
    # under development
    _boss_only = True
    def check(self, erina, *enemy):
        if erina.damage.danmaku:
            erina.ribbon.mp -= erina.ribbon.mp // 3

PowerAbsorb.SetImage('power_absorb')

class Revenge300(Buff):
    """
    "Instant death" status dealt to opponent.
    triggered when damage taken from one attack >300 points
    """
    _boss_only = True
    _special_only = 'irisu'
    def init(self, owner):
        super().init(owner)
        self.effective = False

    def check(self, erina, *enemy):
        if self.owner.damage.danmaku > 300:
            self.effective = True
        elif self.owner.damage.magic > 300:
            self.effective = True
        elif self.owner.damage.boost > 300:
            self.effective = True
        elif self.owner.damage.cocoabomb > 300:
            self.effective = True
        # under development
        elif self.owner.damage.amulet > 300:
            self.effective = True
        if self.effective:
            erina.buff.add(InstantDeath())

Revenge300.SetImage('revenge_300')

class BunnyLover(Buff):
    """
    Damage taken reduced by 50% when the opponent is a bunny
    """
    def init(self, owner):
        super().init(owner)
        self.bunny = 'erina', 'irisu'

    def check(self, erina, *enemy):
        if self.owner._type == 'erina':
            for e in enemy:
                if e.name in self.bunny:
                    e.damage.all_damage = e.damage.all_damage//2
        else:
            erina.damage.all_damage = erina.damage.all_damage//2

BunnyLover.SetImage('bunny_lover')

class Healing(Buff):
    """
    Recover HP over time
    """
    def check(self, erina, *enemy):
        if self.owner._type == 'erina':
           if self.timer % 30 == 0:
               self.owner.hp += 2
               if self.owenr.hp > self.owner.max_hp:
                   self.owenr.hp = int(self.owenr.max_hp)
        else:
            self.owner.hp += 2
            if self.owenr.hp > self.owner.max_hp:
                self.owner.hp = int(self.owner.max_hp)

Healing.SetImage('healing')

class AttackBoost(Buff):
    """
    Bullet hell density increased
    """
    _boss_only = True
    _special_only = '?'
    # under development
    # maybe useless
    def check(self, erina, *enemy):
        '''
        it's hard to describe
        '''
        
AttackBoost.SetImage('attack_boost')

class TMinusOne(Buff):
    """
    Gain "Attack Boost" status after a successful attack
    """
    _boss_only = True
    _special_only = '?'
    # under development
    # maybe useless
    def check(self, erina, *enemy):
        if self.damage.danamku:
            self.owner.buff.add(AttackBoost())
            self.time = 0

TMinusOne.SetImage('t_minus_one')

class TMinusTwo(Buff):
    """
    Gain "T Minus One" status after a successful attack
    """
    _boss_only = True
    _special_only = '?' 
    # under development
    # maybe useless
    def check(self, erina, *enemy):
        if erina.damage.danmaku:
            self.owner.buff.add(TMinusOne())
            self.time = 0

TMinusTwo.SetImage('t_minus_two')

class ZeroOffence(Buff):
    """
    Attack reduced by 100%
    """
    _boss_only = True
    def check(self, erina, *enemy):
        self.owner.damage.danmaku = 0
        self.owner.damage.magic = 0
        self.owner.damage.amulet = 0
        self.owner.damage.cocoabomb = 0
        self.owner.damage.boost = 0

class HaloBuff(Buff):
    """
    Damage taken reduced by 10% after three "Game Over"
    Status removed after "Halo Boost" expires.
    [?] Does not apply above Normal difficulty [?]
    """
    # under development
    _erina_only = True
    def check(self, erina, *enemy):
        self.owner.damage.all_damage -= self.owner.damage.all_damage//10

HaloBuff.SetImage('halo_buff')

class HaloBoostLv1(Buff):
    """
    Damage taken -15%. Amulet recharges 33% faster.
    Recover 1 HP for every three[?] successful attacks.
    Gained after 3-4 "Game Over", No buff above "Normal"
    """
    # under development
    _erina_only = True
    def init(self, owner):
        super().init(owner)
        self.successful_attack = 0

    def check(self, erina, *enemy):
        for e in enemy:
            if enemy.damage.danmaku:
                self.successful_attack += 1
            if enemy.damage.magic:
                self.successful_attack += 1
            if self.successful_attack >= 3:
                self.owner.hp += 1
                self.successfun_attack -= 3
        self.owner.damage.all_damage -= (self.owner.damage.all_damage*0.15).__int__()
        self.owner.amulet += 1

HaloBoostLv1.SetImage('halo_boost_lv1')

class HaloBoostLv2(Buff):
    """
    Damage taken -27.5%. Amulet recharges 67% faster.
    Recover 1 HP for every two successful attacks.
    Gained after 5-6 "Game Over", No buff above "Noraml"
    """
    # under development
    _erina_only = True
    def init(self, owner):
        super().init(owner)
        self.successful_attack = 0

    def check(self, erina, *enemy):
        for e in enemy:
            if enemy.damage.danmaku:
                self.successful_attack += 1
            if enemy.damage.magic:
                self.successful_attack += 1
            if self.successful_attack >= 2:
                self.owner.hp += 1
                self.successfun_attack -= 2
        self.owner.damage.all_damage -= (self.owner.damage.all_damage*0.275).__int__()
        self.owner.amulet += 2

HaloBoostLv1.SetImage('halo_boost_lv2')

class HaloBoostLv3(Buff):
    """
    Damage taken -40%. Amulet recharges 100% faster.
    Recover 1 HP for every successful attack.
    Gained after 7+ "Game Over", No buff above "Normal"
    """
    # under development
    _erina_only = True
    def init(self, owner):
        super().init(owner)
        self.successful_attack = 0

    def check(self, erina, *enemy):
        for e in enemy:
            if enemy.damage.danmaku:
                self.successful_attack += 1
            if enemy.damage.magic:
                self.successful_attack += 1
            self.owner.hp += self.successful_attack
        self.owner.damage.all_damage -= (self.owner.damage.all_damage*0.275).__int__()
        self.owner.amulet += 2

HaloBoostLv1.SetImage('halo_boost_lv3')