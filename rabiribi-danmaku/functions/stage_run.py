import pygame
import functions
import sys
import ui

class BossBattle():
    """
    boss battle here
    """
    def __init__(self, erina, ribbon, *boss):
        self.erina = erina
        self.ribbon = ribbon
        if len(boss) == 1:
            self.boss = boss
        else:
            self.boss = len(boss)
            for b in self.boss:
                self.__setattr__('boss'+str(b), boss[b])
                

    def GroupInit(self, number=0):
        """
        specify group counts.
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
        if isinstance(self.boss, functions.sprites.Boss) and hasattr(self.boss, bgm):
            self.bgm = self.boss.bgm

    def BuffCheck(self, erina, boss_group):
        for b in boss_group:
            for f in b.buff:
                f.buff_check(b)
        for f in erina.buff:
            f.buff_check(erina)

    def Face(self, face):
        pass

    def spell_card(self):
        pass

    def KeyPress(self):
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

    def print_screen(self):
        pass

    def run(self):
        pass

class Pause():
    pass