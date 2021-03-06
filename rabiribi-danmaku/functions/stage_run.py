#######################
#  Under development  #
#######################

import pygame
import functions
import sys
import abc
import multiprocessing
import ui.face
from functions.values import pausetypes

#mpool = multiprocessing.Pool()

class Battle():
    __metaclass__ = abc.ABCMeta
    """
    stage run
    """
    def __init__(self, danmaku_layer_count, *args, **kwargs):
        """
        specify erina instance, ribbon instance, local difficulty and faces
        """
        #self.erina = erina
        #self.ribbon = ribbon
        #self.difficulty = difficulty
        self.clock = pygame.time.Clock()
        self.face = ui.face.Face()
        self.boss = len(args)
        self.pause = 0
        self.esc = 0
        self.set_bgm = True
        self.play_bgm = False
        self.part_run = True
        self.timer = 0
        

    def GroupInit(self, number):
        """

        # 

        specify group counts.

            GroupInit(number): return none

        static layer:
            birth_layer: birth frame have no damage.
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
        self.danmaku_layer = pygame.sprite.Group()  # all danmau
        self.birth_layer = pygame.sprite.Group()  # danmaku with no damage
        self.illustration_layer = pygame.sprite.Group()  # spell illustration
        self.boss_layer = pygame.sprite.Group()  # all boss
        self.elf_layer = pygame.sprite.Group()  #  all elf
        for n in range(self.boss):
            self.boss_layer.add(self.__getattribute__('boss_'+str(n)))
        self.energy_layer = pygame.sprite.Group()  # bonus energy
        self.shouting_layer = pygame.sprite.Group()  # ribbon shouting
        self.boost_layer = pygame.sprite.Group()  # ribbon boost
        self.item_layer = pygame.sprite.Group()  # items
        self.damage_layer = pygame.sprite.Group()  # print damage numbers
        # self.buff_layer = pygame.sprite.Groups()
        for n in range(self.danmaku_layer_count):  # small rank will on top. 
            self.__setattr__('danmaku_layer_'+str(n), pygame.sprite.Group())
        self.BackgroundMusic()

    def BackgroundMusic(self, *music):
        """
        specify background music

            BackgroundMusic(): return none

        bgm will automatic specify on boss_group
        """
        if self.set_bgm:
            if music:
                self.bgm = music(0)
                self.set_bgm = False
            else:
                for b in self.boss_layer:
                    if hasattr(b, 'bgm'):
                        self.bgm = b.bgm
                        self.set_bgm = False
                        break

    def PlayBgm(self):
        if self.play_bgm:
            pass
        else:
            self.play_bgm = True
            self.bgm.play(-1)

    # maybe useless ?
    def PauseBgm(self):
        if self.play_bgm:
            self.bgm.pause()
            self.play_bgm = False

    def BuffCheck(self):
        """
        buff check

            BuffCheck(): return none
        """
        for b in self.boss_layer:
            for f in b.buff:
                f.buff_check(self.erina, iter(self.elf_layer))
        self.erina.buff_check(iter(self.boss_layer), iter(self.elf_layer))

    def UIAnimation(self):
        """
        under development
        """
        self.ui = self.face.face
        self.background = self.face.background
    
    @abc.abstractmethod
    def Attack(self, *args, **kwargs):
        """
        active spell attack
        """
        print("define attack method first")
        raise NotImplementedError

    def KeyPress(self):
        """
        get key pressed
        """
        self.key_pressed = pygame.key.get_pressed()

    def sprite_move(self, *layers):
        #mpool = multiprocessing.Pool()
        for layer in layers:
            for each in layer:
                #mpool.apply_async(each.move, self.erina)
                each.move(self.erina)
        #mpool.close()
        #mpool.join()
        
    def SpriteMove(self):
        self.sprite_move(
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
            self.sprite_move(boss.buff)

    def SwitchLayer(self):
        for sprite in self.birth_layer:
            if sprite.birth_time == 0:
                self.birth_layer.remove(sprite)
                self.danmaku_layer.add(sprite)
                self.__getattribute__('danmaku_layer_' + str(sprite.layer)).add(sprite)

    def sprite_del(self, *layers):
        for layer in layers:
            for sprite in layer:
                if sprite.delete:
                    sprite.kill()

    def SpriteDel(self):
        self.sprite_del(
                      self.illustration_layer,
                      self.shouting_layer,
                      self.energy_layer,
                      self.item_layer,
                      self.boost_layer,
                      self.danmaku_layer)

    def CollideCheck(self):
        self.erina.collide_check(self.danmaku_layer, self.boss_layer)
        for b in self.boss_layer:
            b.collide_check(self.shouting_layer)
        for e in self.elf_layer:
            e.collide_check(self.shouting_layer)

    def DamageCheck(self):
        self.erina.damage(self.damage_layer)
        for b in self.boss_layer:
            b.damage(self.damage_layer)
        for e in self.elf_layer:
            e.damage(self.damage_layer)

    def Debug(self, screen):
        debug_words_pos_left = 430
        debug_words_pos_top = 300
        
        erina_position = "erina position: " + str(round(self.erina.center[0], 2)) + " , " + str(round(self.erina.center[1], 2))
        ribbon_position = "ribbon position: " + str(round(self.ribbon.center[0], 2)) + " , " + str(round(self.ribbon.center[1], 2))
        erina_health = "erina hp: " + str(self.erina.hp) + "/" + str(self.erina.max_hp)
        danmaku_count = "danmaku count:" + str(len(self.danmaku_layer) + len(self.birth_layer))
        shouting_count = "shouting count:" + str(len(self.shouting_layer))

        screen.blit(functions.debug_font.render(erina_position, True, (255,0,0)), (debug_words_pos_left, debug_words_pos_top))
        screen.blit(functions.debug_font.render(ribbon_position, True, (255,0,0)), (debug_words_pos_left, debug_words_pos_top + 20))
        screen.blit(functions.debug_font.render(erina_health, True, (255,0,0)), (debug_words_pos_left, debug_words_pos_top + 40))
        for num in range(self.boss):
            b = self.__getattribute__("boss_"+str(num))
            screen.blit(functions.debug_font.render(b.__class__.__name__ + ": " + str(b.hp) + "/" + str(b.max_hp), True, (255,0,0)), (debug_words_pos_left, debug_words_pos_top + 60 + num*20))
        screen.blit(functions.debug_font.render(danmaku_count, True, (255,0,0)), (debug_words_pos_left, debug_words_pos_top + 60 + self.boss*20))
        screen.blit(functions.debug_font.render(shouting_count, True, (255,0,0)), (debug_words_pos_left, debug_words_pos_top + 80 + self.boss*20))

    def PrintScreen(self, screen):
        screen.blit(self.background, (0,0))
        for sprite in self.illustration_layer:
            sprite.print_screen(screen)

        for sprite in self.energy_layer:
            sprite.print_screen(screen)

        for sprite in self.shouting_layer:
            sprite.print_screen(screen)
        screen.blit(self.erina.image, self.erina.rect)
        screen.blit(self.ribbon.image, self.ribbon.rect)

        for sprite in self.elf_layer:
            sprite.print_screen(screen)
        for sprite in self.boss_layer:
            sprite.print_screen(screen)
        for sprite in self.item_layer:
            sprite.print_screen(screen)

        for sprite in self.birth_layer:
            sprite.print_screen(screen)
        for num in range(self.danmaku_layer_count-1,-1,-1):
            for sprite in self.__getattribute__('danmaku_layer_' + str(num)):
                sprite.print_screen(screen)

        for sprite in self.erina.buff:
            sprite.print_screen(screen)
        for sprite in self.boss_layer:
            for b in sprite.buff:
                b.print_screen(screen)

        for sprite in self.boost_layer:
            sprite.print_screen(screen)

        screen.blit(self.face.face, (0,0))

    def PauseCheck(self):
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

    def run(self, screen, debug):
        #self.BackgroundMusic()
        self.BuffCheck()
        self.Attack()
        self.erina.move(self.key_pressed)
        self.ribbon.move(self.erina)
        self.ribbon.attack(self.shouting_layer, self.key_pressed)
        self.SpriteMove()
        self.CollideCheck()
        self.DamageCheck()
        self.SwitchLayer()
        self.SpriteDel()
        self.UIAnimation()
        self.PrintScreen(screen)
        if debug: self.Debug(screen)
        screen.blit(functions.debug_font.render(str(round(self.clock.get_fps(), 2)), True, (255,0,0)), (600,460))
        pygame.display.flip()

    def __call__(self, erina, ribbon, difficulty, screen, debug = False):
        self.erina = erina 
        self.ribbon = ribbon
        self.difficulty = difficulty
        for b in self.boss_layer:
            if hasattr(b, 'music_name'):
                self.bgm.load(b.music_name)
        self.bgm.play(-1)
        while self.part_run:
            functions.ExitCheck()
            self.KeyPress()
            self.PauseCheck()
            if self.pause == 0:
                self.run(screen, debug)
                #print(self.erina.buff)
                # print("=============================================")
                #for each in self.danmaku_layer:
                #    print(each.center, each.speed, each.direction)
            else:
                pass
            #self.clock.tick(60)
            self.timer += 1
            self.clock.tick_busy_loop(60)

class BossBattle(Battle):
    """
    stage end boss here
    """
    def __init__(self, danmaku_layer_count, *boss):
        super().__init__(danmaku_layer_count, *boss)
        for b in range(self.boss):
            self.__setattr__('boss_'+str(b), boss[b])
        self.GroupInit(danmaku_layer_count)
        
    def SpellCard(self):
        """
        active spell attack
        """
        for b in self.boss_layer:
            if hasattr(b, 'spell_attack'):
                b.spell_attack(self.difficulty, 
                               self.erina, 
                               self.birth_layer, 
                               self.boss_layer, 
                               self.illustration_layer, 
                               self.danmaku_layer)

    def Attack(self):
        self.PlayBgm()
        self.SpellCard()

class MidBattle(Battle):
    """
    stage mid battle, sometimes boss here
    """
    def __init__(self, danmaku_layer_count, *mid_boss, **kwargs):
        super().__init__(danmaku_layer_count, *mid_boss, **kwargs)
        self.GroupInit(danmaku_layer_count)
        #self.BackgroundMusic()

    @abc.abstractmethod
    def MidAttack(self, *args, **kwargs):
        """
        active midbattle
        """
        print("define mid method first")
        raise NotImplementedError
    
    @abc.abstractmethod
    def MidBossAttack(self, *args, **kwargs):
        """
        MidBossAttack(*args, **kwargs): return None
        if no middle boss, use pass
        """
        print("define middle boss first or use pass")
        raise NotImplementedError
    
    def SetBGM(self, file_name):
        self.bgm = pygame.mixer.music
        self.bgm.load(file_name)
        self.set_bgm = False

    def Attack(self):
        self.PlayBgm()
        self.MidAttack()

from functions.values import mainmenu
from functions.values import startmenu
from functions.values import extrastart
from functions.values import practicestart
from functions.values import playdata
from functions.values import musicroom
from functions.values import options
from functions.values import manual
from functions.values import quit  # just for fun

class Menu():
    def __init__(self, *opts):
        self.clock = pygame.time.Clock()
        self.part_run = True
        self.option = ['main_menu']
        self.all_options = {}
        for each in opts:
            self.all_options[each.name] = each

        self.bgm = pygame.mixer.music
        self.set_bgm = 2
        self.new_bgm = 'menu'

    def KeyPress(self):
        """
        get key pressed
        """
        self.key_pressed = pygame.key.get_pressed()

    def BackgroundMusic(self, *music):
        if music:
            self.bgm.fadeout(500)
            self.set_bgm = 30
            self.new_bgm = music[0]
        if self.set_bgm:
            self.set_bgm -= 1
            if self.set_bgm == 1:
                self.bgm.load('data/bgm/'+self.new_bgm+'.ogg')
                self.bgm.play(-1)

    def Animation(self, screen):
        screen.fill((255,255,255))
        pass

    def PrintScreen(self, screen):
        pygame.display.update()

    def __call__(self, screen):
        while self.part_run:
            functions.ExitCheck()
            self.BackgroundMusic()
            self.Animation(screen)
            self.KeyPress()
            self.all_options[self.option[-1]](self.key_pressed, screen)
            self.PrintScreen(screen)
            self.clock.tick_busy_loop(60)

class Pause():
    pass