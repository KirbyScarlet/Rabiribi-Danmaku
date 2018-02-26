#######################
#  Under development  #
#######################


import pygame
import functions
import abc
import character
import ui.face
from functions.values import *


def _test(*args, **kwargs): pass


class Stage():
    """
    specify display output
    """
    __metaclass__ = abc.ABCMeta
    clock = pygame.time.Clock()
    screen = pygame.surface.Surface((400, 450))
    bgm = pygame.mixer.music
    face = ui.face.Face()

    def __init__(self, difficulty):
        """
        static or dynamic paraments
        """
        self.pause = 0
        self.esc = 0
        self.part_run = True
        self.groups()
        self.difficulty = difficulty
        self.ribbon = character.ribbon.Ribbon()
        self.erina = character.erina.Erina(self.ribbon)

    def groups(self):
        self.danmaku_layer_count = 8
        self.danmaku_layer = pygame.sprite.Group()
        self.birth_layer = pygame.sprite.Group()
        for n in range(8):
            self.__setattr__('danmaku_layer_'+str(n), pygame.sprite.Group())

        self.boss_layer = pygame.sprite.Group()
        self.elf_layer = pygame.sprite.Group()
        self.illustration_layer = pygame.sprite.Group()
            
        self.energy_layer = pygame.sprite.Group()
        self.shouting_layer = pygame.sprite.Group()
        self.boost_layer = pygame.sprite.Group()
        self.item_layer = pygame.sprite.Group()
        self.damage_value_layer = pygame.sprite.Group()
        # self.buff_layer = functions.buff_debuff.BuffGroup()
        # self.effects_layer = pygame.sprite.Group()

    def ui_animation(self):
        # under development
        self.ui = self.face.face
        self.background = self.face.background

    def buff_check(self):
        for b in self.boss_layer:
            for f in b.buff:
                f.buff_check(self.erina, self.elf_layer)

    def key_press(self):
        self.key_pressed = pygame.key.get_pressed()
        # joysticks under development

    def attack(self):
        for e in self.elf_layer:
            e.attack(self.difficulty, self.erina, self.birth_layer, self.elf_layer, self.danmaku_layer)
        for b in self.boss_layer:
            b.attack(self.difficulty, self.erina, self.birth_layer, self.boss_layer, self.illustration_layer, self.danmaku_layer)

    def _sprite_move(self, *layers):
        # mpool = multiprocessing.Pool()
        for layer in layers:
            for each in layer:
                # mpool.apply_async(each.move, self.erina)
                each.move(self.erina)
        # mpool.close()
        # mpool.join()
        
    def sprite_move(self):
        self._sprite_move(
                    self.illustration_layer,
                    self.boss_layer,
                    self.shouting_layer,
                    self.birth_layer,
                    self.energy_layer,
                    self.item_layer,
                    self.boost_layer,
                    self.elf_layer,
                    self.danmaku_layer,
                    self.erina.buff
                    )
        for boss in self.boss_layer:
            self._sprite_move(boss.buff)

    '''
    def spell_attack(self):
        for b in self.boss_layer:
            # if hasattr(b, 'spell_attack')
            b.spell_attack(self.difficulty,
                           self.erina,
                           self.birth_layer,
                           self.boss_layer,
                           self.illustration_layer,
                           self.danmaku_layer)
    '''

    def switch_layer(self):
        for sprite in self.birth_layer:
            if sprite.birth_time == 0:
                self.birth_layer.remove(sprite)
                self.danmaku_layer.add(sprite)
                self.__getattribute__('danmaku_layer_'+str(sprite.layer)).add(sprite)

    def _sprite_del(self, *layers):
        for layer in layers:
            for sprite in layer:
                if sprite.delete:
                    sprite.kill()

    def sprite_del(self):
        self._sprite_del(
                      self.illustration_layer,
                      self.shouting_layer,
                      self.energy_layer,
                      self.item_layer,
                      self.boost_layer,
                      self.danmaku_layer)

    def collide_check(self):
        self.erina.collide_check(self.danmaku_layer, self.boss_layer)
        for b in self.boss_layer:
            b.collide_check(self.shouting_layer)
        for b in self.elf_layer:
            b.collide_check(self.shouting_layer)

    def damage_check(self):
        #print(self.erina.damage.danmaku)
        #print(self.erina.hp)
        self.erina.damage(self.damage_value_layer)
        for b in self.boss_layer:
            b.damage(self.damage_value_layer)
        for b in self.elf_layer:
            b.damage(self.damage_value_layer)

    def debug(self, window):
        debug_words_pos_left = 430
        debug_words_pos_top = 300
        
        erina_position = "erina position: %2f , %2f" % (self.erina.center[0], self.erina.center[1])
        ribbon_position = "ribbon position: %2f , %2f" % (self.ribbon.center[0], self.ribbon.center[1])
        erina_health = "erina hp: %d/%d" % (self.erina.hp, self.erina.max_hp)
        danmaku_count = "danmaku count: %d" % (len(self.danmaku_layer) + len(self.birth_layer))
        shouting_count = "shouting count: %d" % len(self.shouting_layer)

        window.blit(functions.debug_font.render(erina_position, True, (255,0,0)), (debug_words_pos_left, debug_words_pos_top))
        window.blit(functions.debug_font.render(ribbon_position, True, (255,0,0)), (debug_words_pos_left, debug_words_pos_top + 20))
        window.blit(functions.debug_font.render(erina_health, True, (255,0,0)), (debug_words_pos_left, debug_words_pos_top + 40))
        for num,b in enumerate(self.boss_layer):
            b.name = "boss_"+b.name
            window.blit(functions.debug_font.render(b.__class__.__name__ + ": " + str(b.hp) + "/" + str(b.max_hp), True, (255,0,0)), (debug_words_pos_left, debug_words_pos_top + 60 + num*20))
        window.blit(functions.debug_font.render(danmaku_count, True, (255,0,0)), (debug_words_pos_left, debug_words_pos_top + 60 + len(self.boss_layer)*20))
        window.blit(functions.debug_font.render(shouting_count, True, (255,0,0)), (debug_words_pos_left, debug_words_pos_top + 80 + len(self.boss_layer)*20))

    def display(self, window):
        self.screen.fill((255, 255, 255))
        for sprite in self.illustration_layer:
            sprite.print_screen(self.screen)

        for sprite in self.energy_layer:
            sprite.print_screen(self.screen)

        for sprite in self.shouting_layer:
            sprite.print_screen(self.screen)
        self.screen.blit(self.erina.image, self.erina.rect)
        self.screen.blit(self.ribbon.image, self.ribbon.rect)

        for sprite in self.elf_layer:
            sprite.print_screen(self.screen)
        for sprite in self.boss_layer:
            sprite.print_screen(self.screen)
        for sprite in self.item_layer:
            sprite.print_screen(self.screen)

        for sprite in self.birth_layer:
            sprite.print_screen(self.screen)
        for num in range(8):
            for sprite in self.__getattribute__('danmaku_layer_%d' % num):
                sprite.print_screen(self.screen)

        for sprite in self.erina.buff:
            sprite.print_screen(self.screen)
        for sprite in self.boss_layer:
            for b in sprite.buff:
                b.print_screen(self.screen)

        for sprite in self.boost_layer:
            sprite.print_screen(self.screen)

        window.fill((255,255,255))
        window.blit(self.face.face, (0,0))
        window.blit(self.screen, (35, 15))

    def pause_check(self):
        if self.esc == pausetypes.NEUTRAL:
            if self.key_pressed[pygame.K_ESCAPE]:
                if self.pause == 0:
                    self.pause += 1
                    self.esc = pausetypes.PAUSING
                elif self.pause == 60:
                    self.pause -= 1
                    self.esc = pausetypes.UNPAUSING
        elif self.esc == pausetypes.PAUSING:
            if self.pause == 60:
                self.esc = pausetypes.NEUTRAL
            else:
                self.pause += 1
        elif self.esc == pausetypes.UNPAUSING:
            if self.pause == 0:
                self.esc = pausetypes.NEUTRAL
            else:
                self.pause -= 1

    def run(self, window, debug):
        # self.Attack()
        self.buff_check()
        self.attack()
        self.erina.move(self.key_pressed)
        self.ribbon.move(self.erina)
        self.ribbon.attack(self.shouting_layer, self.key_pressed)
        self.sprite_move()
        self.collide_check()
        self.damage_check()
        self.switch_layer()
        self.sprite_del()
        self.ui_animation()
        self.display(window)
        if debug: self.debug(window)
        window.blit(functions.debug_font.render(str(round(self.clock.get_fps(), 2)), True, (255,0,0)), (600,460))
        #pygame.display.flip()

    def __call__(self, window, func=_test, debug=False):
        self.timer = 0
        while self.part_run:
            func(self)
            functions.ExitCheck()
            self.key_press()
            self.pause_check()
            if self.pause == 0:
                self.run(window, debug)
            else:
                self.pause()
            self.timer += 1
            pygame.display.update()  # multi-process under development
            if not self.key_pressed[K_LCTRL]: self.clock.tick_busy_loop(60)
        return 0

    def pause(self):
        pass

    def menu(self):
        pass

    def game_over(self):
        pass

    def ending(self):
        pass