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
    # Attack damage output +1~2. Faster BP recovery if >10 badges equipped.
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

    def check(self, erina, *enemy):
        if erina.hp.base_hp != self.s['base_hp']:
            self.effective = True
            self.s['base_hp'] = erina.hp.base_hp
            erina.hp.max_hp -= self.s['add']
        if self.effective:
            self.s['add'] = (erina.base_hp * 0.075).__int__()
            erina.hp.max_hp += self.s['add']
            self.effective = False
        if self.invalid:
            erina.hp.max_hp -= self.s['add']
            self.invalid = False

    def miriam_check(self, miriam, erina):
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

    def check(self, erina, *enemy):
        if erina.hp.base_hp != self.s['base_hp']:
            self.effective = True
            self.s['base_hp'] = erina.hp.base_hp
            erina.hp.max_hp -= self.s['add']
        if self.effective:
            self.s['add'] = erina.base_hp * 0.125
            erina.max_hp += self.s['add']
            self.effective = False
        if self.invalid:
            erina.hp.max_hp -= self.s['add']
            self.invalid = False

    def miriam_check(self, miriam, erina):
        if self.effective:
            miriam.hp.max_hp += miriam.hp.base_hp * 0.125
            self.effective = False

HealthSurge.SetImage('health_surge')

class ManaPlus(Badge):
    """
    Max. MP += 12.5%
    """
    # mp under development
    def stack(self):
        self.s['base_mp'] = self.owner.mp.base_mp
        self.s['add'] = 0

    def check(self, erina, *enemy):
        if erina.ribbon.mp.base_mp != self.s['base_mp']:
            self.effective = True
            self.s['base_mp'] = erina.base_mp
            erina.ribbon.mp.max_mp -= self.s['add']
        if self.effective:
            self.s['add'] = erina.ribbion.base_mp * 0.125
            erina.ribbion.mp.max_mp += self.s['add']
            self.effective = False
        if self.invalid:
            erina.ribbion.mp.max_mp -= self.s['add']
            self.invalid = False

    def miriam_check(self, miriam, erina):
        if self.effective:
            miriam.mp.max_mp += miriam.mp.base_mp * 0.125
            self.effective = False

ManaPlus.SetImage('mana_plus')

class ManaSurge(Badge):
    """
    Max. MP +20%
    """
    def stack(self):
        self.s['base_mp'] = self.owner.mp.base_mp
        self.s['add'] = self.owner.mp.base_mp

    def check(self, erina, *enemy):
        if erina.mp.base_mp != self.s['base_mp']:
            self.effective = True
            self.s['base_mp'] = erina.ribbon.mp.base_mp
            erina.ribbon.mp.max_mp -= self.s['add']
        if self.effective:
            self.s['add'] = erina.ribbon.base_mp * 0.2
            erina.ribbon.mp.max_mp += self.s['add']
            self.effective = False
        if self.invalid:
            erina.ribbon.mp.max_mp -= self.s['add']
            self.invalid = False

    def miriam_check(self, miriam, erina):
        if self.effective:
            miriam.mp.max_mp += miriam.mp.base_mp * 0.2
            self.effective = False

ManaSurge.SetImage('mana_surge')

class CrisisBoost(Badge):
    """
    Attack + 25% when HP <20%
    """
    def stack(self):
        self.s['base_atk'] = self.owner.attack.base_atk
        self.s['add'] = 0

    def check(self, erina, *enemy):
        if erina.hp.hp < erina.hp.max_hp//5:
            if erina.atk.base_atk != self.s['base_atk']:
                self.effective = True
                self.s['base_atk'] = erina.attack.base_atk
                erina.attack.atk -= self.s['add']
            if self.effective:
                self.s['add'] = (erina.attack.base_atk * 0.25).__int__()
                erina.attack.atk += self.s['add']
                self.effective = False
        else:
            if not self.invalid:
                self.invalid = True
        if self.invalid:
            erina.attack.atk -= self.s['add']
            self.invalid = False

    def miriam_check(self, miriam, erina):
        if miriam.hp.hp < miriam.hp.max_hp//5:
            if miriam.attack.base_atk != self.s['base_atk']:
                self.effective = True
                self.s['base_atk'] = miriam.attack.base_atk
            if self.effective:
                self.s['add'] = (miriam.attack.base_atk * 0.25).__int__()
                miriam.attack.atk += self.s['add']
                self.effective = False
        else:
            if not self.invalid:
                self.invaled = True
        if self.invalid:
            miriam.attack.atk -= self.s['add']
            self.invalid = False

CrisisBoost.SetImage('crisis_boost')

class ATKGrow(Badge):
    """
    All damage output +1~2, Faster BP recovery if >10 badges equipped
    """
    def check(self, erina, *enemy):
        if len(erina.badges) >= 10:
            for e in *enemy:
                if e.damage.danmaku:
                    e.damage.danmaku += random.randint(1,2)
                    erina.ribbon.mp += 1
                elif e.damage.magic:
                    e.damage.magic += random.randint(1,2)
                    erina.ribbon.mp += 1
    
    def miriam_check(self, miriam, erina):
        if len(miriam.badges) >= 10:
            for e in enemy:
                if e.damage.danmaku:
                    e.damage.danmaku += random.randint(1,2)
                    miriam.mp += 100

ATKGrow.SetImage('atk_trade')

class DEFGrow(Badge):
    """
    All damage taken -1~2, Drop a recovery carrot if >10 badges equipped
    """
    def check(self, erina, *enemy):
        if len(erina.badges) >= 10:
            if erina.damage.danmaku:
                erina.damage.danmaku -= random.randint(1,2)
        
        # carrot under development

    def miriam_check(self, miriam, erina):
        if len(miriam.badges) >= 10:
            if miriam.damage.danmaku:
                miriam.damage.danmaku -= random.randint(1,2)
            elif miriam.damage.magic:
                miriam.damage.magic -= random.randint(1,2)

DEFGrow.SetImage('def_grow')

class ATKTrade(Badge):
    """
    Attack +25%, Damage taken +50%
    """
    def stack(self):
        self.s['base_atk'] = self.owner.attack.base_atk
        self.s['add'] = 0

    def check(self, erina, *enemy):
        if erina.attack.base_atk != self.s['base_atk']:
            self.s['base_atk'] = erina.attack.base_atk
            erina.attack.atk -= self.s['add']
            self.effective = True
        if self.effective:
            self.s['add'] = erina.attack.base_atk//4
            erina.attack.atk += self.s['add']
            self.effective = False
        if self.invalid:
            erina.attack.atk -= self.s['add']
            self.s['add'] = 0
            self.invalid = False
        if erina.damage.danmaku:
            erina.damage.danmaku *= 1.5

    def miriam_check(self, miriam, erina):
        if miriam.attack.base_atk != self.s['base_atk']:
            self.s['base_atk'] = miriam.attack.base_atk
            miriam.attack.atk -= self.s['add']
            self.effective = True
        if self.effective:
            self.s['add'] = miriam.attack.base_atk//4
            miriam.attack.atk += self.s['add']
            self.effective = False
        if self.invalid:
            miriam.attack.atk -= self.s['add']
            self.s['add'] = 0
            self.invalid = False
        if miriam.damage.physical_damage:
            miriam.damage.physical_damage *= 1.5

ATKTrade.SetImage('atk_trade')

class DEFTrade(Badge):
    """
    Damage taken -20%, Attack -15%
    """
    def stack(self):
        self.['base_atk'] = self.owner.attack.base_atk
        self.['sub'] = 0

    def check(self, erina, *enemy):
        if erina.attack.base_atk != self.['base_atk']:
            self.s['base_atk'] = erina.attack.base_atk
            erina.attack.base_atk += self,['sub']
            self.effective = True
        if self.effective:
            self.['sub'] = (erina.attack.base_atk*0.15).__int__()
            erina.attack.atk -= self.['sub']
            self.effective = False
        if self.invalid:
            erina.attack.atk += self.['sub']
            self.['sub'] = 0
            self.invalid = False
        if erina.damage.danmaku:
            erina.damage.danmaku *= 0.8

    def miriam_check(self, miriam, erina):
        miriam.attack.atk -= miriam.attack.base_atk * 0.15
        if miriam.damage.physical_damage:
            miriam.damage.physical_damage *= 0.8

DEFTrade.SetImage('def_trade')

class ArmStrength(Badge):
    """
    Piko Hammer attack +15%
    """
    # maybe useless

ArmStrength.SetImage('arm_strength')

class CarrotBoost(Badge):
    """
    Carrot Bomb attack +10% and more SP recover from Carrot Bombs
    """
    # maybe useless

CarrotBoost.SetImage('carrot_boost')

class Weaken(Badge):
    """
    Reduce enemies' invincibility time after getting hit
    """
    def check(self, erina, *enemy):
        pass

    def miriam_check(self, miriam, erina):
        if erina.invincible > 90:
            erina.invincible -= 1

Weaken.SetImage('weaken')

class SelfDefense(Badge):
    """
    Increase Erina's invincibility time after getting hit
    """
    def check(self, erina, *enemy):
        if erina.invincible:
            erina.invincible += 0.5

    def miriam_check(self, miriam, erina):
        pass

SelfDefense.SetImage('self_defense')

class Armored(Badge):
    """
    Reduce knockback from attacks and reduce collision damage
    """
    def check(self, erina, *enemy):
        if erina.damage.crash:
            erina.damage.crash *= 0.8
        
    def miriam_check(self, miriam, erina):
        if miriam.damage.crash:
            miriam.damage.crash *= 0.8

Armored.SetImage('armored')

