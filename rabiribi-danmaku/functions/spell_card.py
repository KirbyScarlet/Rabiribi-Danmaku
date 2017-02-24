import pygame
import random
import math
from _operator import truth

class IllustrationAttack(pygame.sprite.Sprite):
    """
    some spell attack will use a image
        
        IllustrationAttack([illustration_list]): return none.
    """
    def __init__(self, illustration_list):
        self._illustration = random.choice(illustration_list)
        self.image = self._illustration
        self.rect = self.image.get_rect()
        self.rect.left = 200
        self.rect.top = 200
        self.timer = 0
        self.delete = False

    def move(self):
        self.rect.top += 2
        self.image.set_alpha(1020 - abs(17/4*(self.timer - 30)) - abs(17/4*(self.timer - 150)))
        self.timer += 1
        if self.timer == 300:
            self.delete = True

class SpellCard():
    """
    specify any spell attack.

        __init__(spell_type, spell_range):
        spell_attack(difficulty, me_erina, boss_group, birth_group, effects_group): return none

    """
    def __init__(self, spell_time, *illustration):
        """
        __init__(spell_type, spell_range[, illustration]):

            spell_type:     spell or non-spell, type bool
            *illustration:  if spell have illustration attack,this will be
                            a spell card, otherwise not.
            spell_range:    range of spell, type int
        """
        self.type = False
        self.range = 0
        self.time = spell_time
        self.timer = 0
        if illustration:
            self.type = True
            self.illustration = illustration

    def illustration_attack(self, effects_group):
        """
        show illustration before attack

            illustration:       boss illustration list.
            effects_group:    any effects sprites group
        """
        if self.timer == 0:
            effects_group.add(IllustrationAttack(self.illustration))

    def spell_card(self, erina, boss_group, danmaku_group, effects_group):
        """
        check type.
        """
        if self.type:
            self.illustration_attack(effects_group)
        self.spell

    def spell(self, erina, boss_group, danmaku_group, effects_group):
        """
        define this in objects
        """
        pass

class SpellGroup():
    """
    some spell card won't used in some local difficulty
    use group to control
    """
    _spellgroup = True
    
    def __init__(self):
        self.spelldict = {}
        self.lostspell = []

    def spells(self):
        return list(self.spelldict)

    def add_internal(self, spell):
        self.spelldict[spell] = 0

    def remove_internal(self, spell):
        s = self.spelldict[spell]
        if s:
            self.lostspell.append(s)
        del self.spelldict[spell]

    def has_internal(self, spell):
        return spell in self.spelldict

    def copy(self):
        """
        maybe useless

        copy a group with all same spell cards

        SpellGroup.copy(): retrun SpellGroup
        """
        return self.__class__(self.spells())

    def __iter__(self):
        return iter(self,spells())

    def __contains__(self, spell):
        return self.has_internal(spell)

    def add(self, *spells):
        """
        add spell(s) to group

        SpellGroup.add(spells, list): return none
        """
        for spell in spells:
            if isinstance(spell, SpellCard):
                if not self.has_internal(spell):
                    self.add_internal(spell)
            else:
                try:
                    self.add(*spells)
                except (TypeError, AttributeError):
                    if hasattr(spell, '_spellgroup'):
                        for s in spell.spells():
                            if not self.has_internal(s):
                                self.add_internal(s)
                    elif not self.has_internal(spell):
                        self.add_internal(spell)

    def remove(self, *spells):
        """
        remove spell cards from group

        SpellGroup.remove(spell, ...): return None
        """
        for spell in spells:
            if isinstance(spell, SpellCard):
                if self.has_internal(spell):
                    self.remove_internal(spell)
            else:
                try: 
                    self.remove(*spells)
                except (TypeError, AttributeError):
                    if hasattr(BufferError, '_spellgroup'):
                        for s in spell.spells():
                            if self.has_internal(s):
                                self.remove_internal(s)
                    elif self.has_internal(spell):
                        self.remove_internal(spell)

    def has(self, *spells):
        """
        ask if group has a buff

        SpellGroup.has(buff, ...): Return bool
        """
        return_value = False

        for spell in spells:
            if isinstance(spell, SpellCard):
                if self.has_internal(spell):
                    return_value = True
                else:
                    return False
            else:
                try:
                    if self.has(*spells):
                        return_value = True
                    else:
                        return False
                except (TypeError, AttributeError):
                    if hasattr(spell, '_spellgroup'):
                        for s in spell.spells():
                            if self.has_internal(s):
                                retrun_value = True
                            else:
                                return False
                    else:
                        if self.has_internal(spell):
                            return_value = True
                        else:
                            return False
        return return_value

    def empty(self):
        """
        maybe useless

        remove all spells

        SpellGroup.empty(): return None
        """
        for spell in self.spells():
            self.remove_internal(spell)

    def __nonzero__(self):
        return truth(self.spells())

    def __len__(self):
        """
        return number of spells in group:

        SpellGroup.len(group): return int
        """
        return len(self.spells())

    def __repr__(self):
        return "<%s(%d spell cards)>" % (self.__class__.__name__, len(self))

