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
        self.danmaku_layer = number
        self.birth_layer = pygame.sprite.Group()
        self.illustration_layer = pygame.sprite.Group()
        self.boss_layer = pygame.sprite.Group()
        self.energy_layer = pygame.sprite.Group()
        self.shouting_layer = pygame.sprite.Group()
        self.boost_layer = pygame.sprite.Group()
        # small number will on top. small danmaku is on top
        for n in range(self.danmaku_layer):
            self.__setattr__('danmaku_layer_'+str(n), pygame.sprite.Group())

    def BackgroundMusic(self):
        if isinstance(self.boss, functions.sprites.Boss) and hasattr(self.boss, bgm):
            self.bgm = self.boss.bgm

    def BuffCheck(self, erina, boss_group):
        for b in boss_group:
            for f in b.buff:
                f.check(b)

    def Face(self, face):
        pass

    def KeyPress(self):
        pass

    def SpriteMove(self):
        pass

    def SpriteDel(self):
        pass

    def CollideCheck(self, erina, boss_group):
        pass

    def print_screen(self):
        pass

    def run(self):
        pass

class Pause():
    pass