"""
This file define all badges
"""
import pygame
import pickle
import objects
import abc
import random
from functions.action import ItemAction
from functions.values import screenborder

class AllBadges:
    health_plus = 0         
    # Max. Health +7.5%
    health_surge = 0       
    # Max. Health +12.5%
    mana_plus = 0          
    # Max. MP +12.5%
    mana_surge = 0         
    # Max. MP +20%
    crisis_boost = 0         
    # Attack +25% when HP <20%
    atk_grow = 0           
    # Attack damage output +1~2. Faster BPO recovery if >10 badges equipped.
    def_grow = 0           
    # All damage taken -1~2. Drop a recovery carrot if >10 badges equipped.
    atk_trade = 0          
    # Attack +25%. Damage taken +50%
    def_trade = 0          
    # Damage taken -20%. Attack -15%
    arm_strength = 0       
    # Piko Hammer attack +15%
    carrot_boost = 0       
    # Carrot Bomb attack +10% and more SP recover from Carrot Bombs.
    weaken = 0             
    # Reduce enemies' invincibility time after getting hit.
    self_defense = 0        
    # Increase Erina's invincibility time after getting hit.
    armored = 0            
    # Reduce knockback from attacks and reduce collision damage.
    lucky_seven = 0         
    # Deal 107% or 177% damage on every 7th hit.
    hex_cancel = 0          
    # No damage for every 6th hit taken but amulet charge drained for 3 seconds.
    pure_love = 0           
    # In Boss Battles, take almost no collision damage from female enemies.
    toxic_strike = 0         
    # add a poison effect to all attacks.
    frame_cancel = 0       
    # Cancel the fifth Piko Hammer Combo by pressing [down]
    health_wager = 0       
    # Max. MP +37.5. Max. Health -25%.
    mana_wager = 0        
    # Max. Health +17.5. Max. MP -32.5%.
    stamina_plus = 0       
    # Reduce all SP usage by 25%
    blessed = 0             
    # Increase Bunny Amulet recharge speed.
    hitbox_down = 0        
    # Reduce Erina's hitbox size.
    cashback = 0        
    # Increase EN gained from enemies.
    survival = 0            
    # Endure a tatal hit if HP > 1 point.
    top_form = 0           
    # Resist 'Speed Down', 'Attack Down', 'Defense Down', and 'numb' effects.
    tough_skin = 0         
    # Resist 'Toxic', Curse', and 'Burn' effects.
    erina_badge = 0        
    # Dmg. taken -10%. Item Effect +20%. Hold C to extend hammer combo 5.
    ribbon_badge = 0       
    # MP Usage -15%. Hold X after releasing charged shot for repeated shots.
    auto_trigger = 0        
    # Auto use Bunny Amulet if charge is 2 or above, drains all MP and SP.

class Badge(pygame.sprite.Sprite):
    __metaclass__ = abc.ABCMeta
    """
    this is use for define badges
    """
    _item_mode = True
    _miriam_mode = False  # miriam's badge copy buff

    def __init__(self, *badge_group, miriam=None):
        """
        __init__(self, *badge_group):

            badges group will be items group
        """
        super().__init__(*badge_group)
        # under development
        self.fall = False
        self.image = pygame.surface.Surface((20,20)).convert()
        self.opacity = 255
        self.rect = self.image.get_rect()
        self.temp_position = [0,0]
        
        self.delete = False

        self.rect = self.image.get_rect()
        self.temp_position = [0,0]
        self.s = {}

    def stack(self):
        pass

    def init(self):
        self.effective = True
        self.invalid = False
        
    @classmethod
    def SetImage(cls, badge_name):
        _badge_name = 'data/tmp/imgs/' + badge_name + '.tmp'
        try:
            cls.image_temp = pygame.image.load(_badge_name).convert_alpha()
        except pygame.error:
            filename = 'data/objs/items/badges.rbrb'
            with open(filename, 'rb') as f:
                images = pickle.load(f)
            for key,value in images.items():
                filename = 'data/tmp/imgs/'+key+'.tmp'
                with open(filename, 'wb') as f:
                    f.write(value)
            cls.image_temp = pygame.image.load(_badge_name)

    def remove(self):
        if self.rect.top > screenborder.SCREEN_BOTTOM:
            self.kill()

    @abc.abstractmethod
    def check(self, erina, *enemy):
        raise NotImplementedError

    def print_item(self, screen):
        screen.blit(self.image_temp, self.rect)

    def print_esc(self, screen):
        pass

    def print_screen(self, screen):
        if self._item_mode:
            self.print_item(screen)
        else:
            self.print_esc(screen)

    def __setattr__(self, name, value):
        if name == 'owner':
            self.init()
        return super().__setattr__(name, value)
        
    def __repr__(self):
        return '< badge ' + self.__class__.__name__ + ' >'

class BadgeGroup(pygame.sprite.Group):
    def add_internal(self, sprite):
        name = sprite.__class__.__name__
        for key, value in self.spritedict.items():
            if value == name:
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
                self.__delattr__(r)

class HealthPlus(Badge):
    """
    Max. Health +7.5%
    """
    def stack(self):
        self.s['base_hp'] = self.owner.hp.base_hp
        self.s['add'] = 0

    def check(self, erina):
        if erina.hp.base_hp != self.s['base_hp']:
            self.effective = True
            self.s['base_hp'] = erina.hp.base_hp
        if self.effective:
            self.s['add'] = (erina.base_hp * 0.075).__int__()
            erina.hp.max_hp += self.s['add']
            self.effective = False
        if self.invalid:
            erina.hp.max_hp -= self.s['add']
            self.invalid = False

    def miriam_check(self, miriam):
        if self.effective:
            miriam.hp.max_hp += miriam.hp.base_hp * 0.075
            self.effective = False

HealthPlus.SetImage('health_plus')

class HealthSurge(Badge):
    """
    Max. Health +12.5%
    """
    def stack(self):
        self.s['base_hp'] = self.owner.hp.base_hp
        self.s['add'] = 0

    def check(self, erina):
        if erina.hp.base_hp != self.s['base_hp']:
            self.effective = True
            self.s['base_hp'] = erina.hp.base_hp
        if self.effective:
            self.s['add'] = erina.base_hp * 0.125
            erina.max_hp += self.s['add']
            self.effective = False
        if self.invalid:
            erina.hp.max_hp -= self.s['add']
            self.invalid = False

    def miriam_check(self, miriam):
        if self.effective:
            miriam.hp.max_hp += miriam.hp.base_hp * 0.125
            self.effective = False

HealthSurge.SetImage('health_surge')

class ManaPlus(Badge):
    """
    Max. MP += 12.5%
    """
