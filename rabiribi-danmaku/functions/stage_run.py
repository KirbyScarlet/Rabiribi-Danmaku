import pygame
import functions
import sys
import ui

class BossBattle():
    """
    stage end boss here
    """
    def __init__(self, erina, ribbon, difficulty, *boss):
        self.erina = erina
        self.ribbon = ribbon
        self.difficulty = difficulty
        self.clock = pygame.time.Clock()
        self.face = ui.face.Face()
        if len(boss) == 1:
            self.boss = boss
        else:
            self.boss = len(boss)
            for b in self.boss:
                self.__setattr__('boss'+str(b), boss[b])
                

    def GroupInit(self, number=0):
        """
        specify group counts.

            GroupInit(number=0): return none

        static layer:
            birth_layer: 6 frame have no damage.
            shouting_layer: ribbon attack.
            boost_layer: ribbon boost attack and amulet attack
            illustration_layer: illustration attack before spell attack
            item_layer: items
            energy_layer: boss bonus
            boss_layer: boss group

        dynamic layer:
            danmaku_layer: all danmaku in this group but not use
                              for damage check
            danmaku_layer_[number]: 
                              specify number to add group(s)
                              mostly, small danmaku will on top.
                              small rank on top.
        """
        self.danmaku_layer_count = number
        self.danmaku_layer = pygame.sprite.Group()
        self.birth_layer = pygame.sprite.Group()
        self.illustration_layer = pygame.sprite.Group()
        self.boss_layer = pygame.sprite.Group()
        self.energy_layer = pygame.sprite.Group()
        self.shouting_layer = pygame.sprite.Group()
        self.boost_layer = pygame.sprite.Group()
        self.item_layer = pygame.sprite.Group()
        # small number will on top. small danmaku is on top
        for n in range(self.danmaku_layer):
            self.__setattr__('danmaku_layer_'+str(n), pygame.sprite.Group())

    def BackgroundMusic(self):
        """
        specify background music

            BackgroundMusic(): return none

        bgm will automatic specify on boss_group
        """
        if isinstance(self.boss, functions.sprites.Boss) and hasattr(self.boss, bgm):
            self.bgm = self.boss.bgm

    def BuffCheck(self, erina, boss_group):
        """
        buff check

            BuffCheck(): return none
        """
        for b in boss_group:
            for f in b.buff:
                f.buff_check(b)
        for f in erina.buff:
            f.buff_check(erina)

    def UIAnimation(self):
        """
        under development
        """
        self.ui = self.face.face
        self.background = self.face.background
        
    def spell_card(self):
        """
        active spell attack
        """
        for b in boss_layer:
            if hasattr(b, 'spell_attack'):
                b.spell_attack(self.defficulty, erina, boss, boss_group, birth_group, effects_group)

    def KeyPress(self):
        """
        get key pressed
        """
        self.key_pressed = pygame.key.get_pressed()

    def SpriteMove(self):
        def sprite_move(*layer):
            for l in layer:
                for each in l:
                    each.move()
        sprite_move(
                    self.illustration_layer,
                    self.boss_layer,
                    self.shouting_layer,
                    self.energy_layer,
                    self.item_layer,
                    self.boost_layer,
                    self.danmaku_layer)

    def SpriteDel(self):

        def delete(layer):
            for sprite in layer:
                if hasattr(sprite, 'live_time'):
                    if sprite.live_time == 0:
                        sprite.remove(layer, self.danmaku_layer)
                elif hasattr(sprite, 'delete'):
                    if sprite.delete:
                        sprite.remove(layer, self.danmaku_layer)
                else:
                    pass

        def sprite_delete(*screen_layer):
            for layer in screen_layer:
                delete(layer)

        sprite_delete(
                      self.illustration_layer,
                      self.shouting_layer,
                      self.energy_layer,
                      self.item_layer,
                      self.boost_layer)
        for num in range(self.danmaku_layer):
            for each in self.__getattribute__('danmaku_layer_' + str(num)):
                each.delete(each)

    def CollideCheck(self, erina, boss_group):
        self.erina.collide_check(self.danmaku_group, boss_group)
        for b in self.boss_layer:
            b.collide_check(shouting_layer)

    def print_screen(self, screen):
        screen.blit(self.background, (0,0))

    def run(self):
        pass

class Pause():
    pass