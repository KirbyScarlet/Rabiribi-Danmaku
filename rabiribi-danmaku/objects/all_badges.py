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

class LuckySeven_badge(Badge):
    """
    Deal 107% or 177% damage on every 7th hit
    """
    def check(self, erina, *enemy):
        if self.effective:
            erina.buff.add(functions.buff_debuff.LuckySeven(time=-1))
            self.effective = False
        if self.invalid:
            erina.buff.LuckySeven.time = 1
            self.invalid = False

    def miriam_check(self, miriam, erina):
        if self.effective:
            miriam.buff.add(functions.buff_debuff.LuckySeven(time=-1))
            self.effective = False
        if self.invalid:
            miriam.buff.LuckySeven.time = 1
            self.invalid = False

LuckySeven_badge.SetImage('lucky_seven_badge')

class HexCancel_badge(Badge):
    """
    No damage for every 6th hit taken but amulet drained for 3 seconds
    """
    def check(self, erina, *enemy):
        if self.effective:
            erina.buff.add(functions.buff_debuff.HexCancel(time=-1))
            self.effective = False
        if self.invalid:
            erina.buff.HexCancel.time = 1
            self.invalid = False
    
    def miriam_check(self, miriam, erina):
        if self.effective:
            miriam.buff.add(functions.buff_debuff.HexCancel(time=-1))
            self.effective = False
        if self.invalid:
            miriam.buff.HexCancel.time = 1
            self.invalid = False

HexCancel_badge.SetImage('hex_cancel_badge')

class PureLove(Badge):
    """
    In Boss Battles, take almost no collision damage from female enemies
    """
    def check(self, erina, *enemy):
        for e in *enemy:
            if e._type == 'boss':
                e.crash = 0

    def stack(self):
        self.s['fire_ore'] = 0

    def miriam_check(self, miriam, erina):
        # under development
        if self.effective:
            erina.item.fire_ore = 0
            self.effective = False
        elif self.invalid:
            erina.item.fire_ore = self.s['fire_ore']
            self.invalid = False

PureLove.SetImage('pure_love')

class ToxicStrike(Badge):
    """
    add a poison effect to all attacks
    """
    # under development
    # balance unfit
    def check(self, erina, *enemy):
        for e in *enemy:
            if e.damage.physical_damage:
                e.buff.add(functions.buff_debuff.Poisond(time=301))

    def miriam_check(self, miriam, erina):
        if erina.damage.danmaku:
            erina.buff.add(functions.buff_debuff.Poisond(time=1501))

ToxicStrike.SetImage('toxic_strike')

class FrameCancel(Badge):
    """
    Cancel the fifth Piko Hammer Combo by pressing [donw]
    """
    # useless

FrameCancel.SetImage('frame_cancel')

class HealthWager(Badge):
    """
    Max. MP +37.5%, Max. Health -25%
    """
    def init(self):
        super().__init__()
        self.eff_hp = True
        self.eff_mp = True

    def stack(self):
        self.s['base_hp'] = 0
        self.s['hp_add'] = 0
        self.s['base_mp'] = 0
        self.s['mp_add'] = 0

    def check(self, erina, *enemy):
        if self.s['base_hp'] != erina.hp.base_hp:
            self.s['base_hp'] = erina.hp.base_hp
            erina.hp.base_hp -= self.['hp_add']
            self.eff_hp = True
        if self.s['base_mp'] != erina.ribbon.mp.base_mp:
            self.s['base_mp'] = erina.ribbon.mp.base_mp
            erina.ribbon.mp.base_mp -= self.['mp_add']
            self.eff_mp = True
        if self.eff_hp:
            self.s['hp_add'] = erina.hp.base_hp//4
            erina.hp.sub(self.s['hp_add'])
            self.eff_hp = False
        if self.eff_mp:
            self.s['mp_add'] = (erina.ribbon.mp.base_mp*0.375).__int__()
            erina.ribbon.mp.add(self.s['mp_add'])
            self.eff_mp = False
        if self.invalid:
            erina.hp.add(self.s['hp_add'])
            erina.ribbon.mp.sub(self.s['hp_sub'])
            self.s['hp_add'] = 0
            self.s['hp_sub'] = 0
            self.invalid = False

    def miriam_check(self, miriam, erina):
        if self.effective:
            miriam.hp.sub(miriam.hp.base_hp*0.25)
            miriam.mp.add(miriam.mp.max_mp*0.375)
            self.effective = False

HealthWager.SetImage('health_wager')

class ManaWager(Badge):
    """
    Max. Health +17.5. Max. MP -32.5%
    """
    def init(self):
        super().__init__()
        self.eff_hp = True
        self.eff_mp = True

    def stack(self):
        self.s['base_hp'] = 0
        self.s['hp_add'] = 0
        self.s['base_mp'] = 0
        self.s['mp_add'] = 0

    def check(self, erina, *enemy):
        if self.s['base_hp'] != erina.hp.base_hp:
            self.s['base_hp'] = erina.hp.base_hp
            erina.hp.base_hp -= self.['hp_add']
            self.eff_hp = True
        if self.s['base_mp'] != erina.ribbon.mp.base_mp:
            self.s['base_mp'] = erina.ribbon.mp.base_mp
            erina.ribbon.mp.base_mp -= self.['mp_add']
            self.eff_mp = True
        if self.eff_hp:
            self.s['hp_add'] = erina.hp.base_hp*0.175
            erina.hp.add(self.s['hp_add'])
            self.eff_hp = False
        if self.eff_mp:
            self.s['mp_add'] = (erina.ribbon.mp.base_mp*0.325).__int__()
            erina.ribbon.mp.sub(self.s['mp_add'])
            self.eff_mp = False
        if self.invalid:
            erina.hp.sub(self.s['hp_add'])
            erina.ribbon.mp.add(self.s['hp_sub'])
            self.s['hp_add'] = 0
            self.s['hp_sub'] = 0
            self.invalid = False

    def miriam_check(self, miriam, erina):
        if self.effective:
            miriam.hp.add(miriam.hp.base_hp*0.175)
            miriam.mp.sub(miriam.mp.max_mp*0.325)
            self.effective = False

ManaWager.SetImage('mana_wager')

class StaminaPlus(Badge):
    """
    Reduce all SP usage by 25%
    """
    # useless

StaminaPlus.SetImage('stamina_plus')

class Blessed(Badge):
    """
    Increase Bunny Amulet recharge speed
    """
    def check(self, erina, *enemy):
        if self.effective:
            erina.amulet += 1

    def miriam_check(self, miriam, erina):
        '?'
        # under development

Blessed.SetImage('blessed')

class HitboxDown(Badge):
    """
    Reduce Erina's hitbox size
    """
    # under development
    def check(self, erina, *enemy):
        if self.effective:
            erina.radius = 1
        
    def miriam_check(self, miriam, *enemy):
        miriam.radius = 10

HitboxDown.SetImage('hitbox_down')

class CashBack(Badge):
    """
    Increase EN gained from enemies
    """
    # under development
    def check(self, erina, *enemy):
        pass

    def miriam_check(self, miriam, erina):
        pass

CashBack.SetImage('cashback')

class Survival(Badge):
    """
    Endure a tatal hit if HP>1 point
    """
    def check(self, erina, *enemy):
        if self.effective:
            if erina.damage.all_damage:
                if erina.damage.all_damage >= erina.hp.hp > 1:
                    erina.damage.all_damage = erina.hp.hp-1

    def miriam_check(self, miriam, erina):
        if self.effective:
            miriam.buff.add(functions.buff_debuff.SurvivalInstinct())
            self.effective = False
        if self.invalid:
            miriam.buff.SurvivalInstinct.time = 1
            self.invalid = False

Survival.SetImage('survival')

class TopForm(Badge):
    """
    Resist 'Speed Down', 'Attack Down', 'Defense Down', and 'Numb' effects
    """
    def stack(self):
        self.ss = ('SpeedDown', 'AttackDown', 'DefenseDown', 'Numb')
    
    def check(self, erina, *enemy):
        if erina.damage.get_buff:
            for b in self.ss:
                if b in erina.damage.get_buff:
                    erina.damage.get_buff.remove(b)

    def miriam_check(self, miriam, erina):
        if miriam.damage.get_buff:
            for b in self.ss:
                if b in miriam.damage.get_buff:
                    miriam.damage.get_buff.remove(b)

TopForm.SetImage('top_form')

class ToughSkin(Badge):
    """
    Resist 'Toxic', 'Curse', and 'Burn' effects
    """
    def stack(self):
        self.ss = ('Ponised', 'Curse', 'Burn')

    def check(self, erina, *enemy):
        if erina.damage.get_buff:
            for b in self.ss:
                if b in erina.damage.get_buff:
                    erina.damage.get_buff.remove(b)

    def check(self, miriam, erina):
        if miriam.damage.get_buff:
            for b in self.ss:
                if b in miriam.damage.get_buff:
                    miriam.damage.get_buff.remove(b)

ToughSkin.SetImage('tough_skin')

class ErinaBadge(Badge):
    """
    Damage taken -10%. Item Effect +20%. 
    """
    # under development

ErinaBadge.SetImage('erina_badge')

class RibbonBadge(Badge):
    """
    MP usage -15%
    """
    # under developmetn

RibbonBadge.SetImage('ribbon_badge')

class AutoTrigger(Badge):
    """
    Auto use Bunny Amulet if charge is 2 or above
    Drains all MP and SP
    """
    # maybe useless
    # under development
    def check(self, erina, *enemy):
        if erina.damage.physical_damage:
            erina.amulet(2)  # under developmet

    def miriam_check(self, miriam, erina):
        pass

AutoTrigger.SetImage('auto_trigger')
    