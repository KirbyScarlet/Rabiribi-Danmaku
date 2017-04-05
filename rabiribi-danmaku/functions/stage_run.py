import pygame
import functions
import sys
import ui

class BossBattle():
    """
    stage end boss here
    """
    def __init__(self, erina, ribbon, difficulty, danmaku_layer_count, *boss):
        self.erina = erina
        self.ribbon = ribbon
        self.difficulty = difficulty
        self.clock = pygame.time.Clock()
        self.face = ui.face.Face()
        self.boss = len(boss)
        self.pause = False
        self.set_bgm = True
        self.play_bgm = False
        functions.debug_font = pygame.font.Font(None, 20)
        for b in range(self.boss):
            self.__setattr__('boss_'+str(b), boss[b])
        self.GroupInit(danmaku_layer_count)

    def GroupInit(self, number):
        """
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
        self.danmaku_layer = pygame.sprite.Group()
        self.birth_layer = pygame.sprite.Group()
        self.illustration_layer = pygame.sprite.Group()
        self.boss_layer = pygame.sprite.Group()
        for n in range(self.boss):
            self.boss_layer.add(self.__getattribute__('boss_'+str(n)))
        self.energy_layer = pygame.sprite.Group()
        self.shouting_layer = pygame.sprite.Group()
        self.boost_layer = pygame.sprite.Group()
        self.item_layer = pygame.sprite.Group()
        # small number will on top. 
        for n in range(self.danmaku_layer_count):
            self.__setattr__('danmaku_layer_'+str(n), pygame.sprite.Group())

    def BackgroundMusic(self):
        """
        specify background music

            BackgroundMusic(): return none

        bgm will automatic specify on boss_group
        """
        if self.set_bgm:
            for b in self.boss_layer:
                if hasattr(b, 'bgm'):
                    self.bgm = b.bgm
                    self.set_bgm = False
                    break
        if self.play_bgm:
            pass
        else:
            self.play_bgm = True
            self.bgm.play(-1)

    def BuffCheck(self):
        """
        buff check

            BuffCheck(): return none
        """
        for b in self.boss_layer:
            for f in b.buff:
                f.buff_check(b)
        for f in self.erina.buff:
            f.buff_check(erina)

    def UIAnimation(self):
        """
        under development
        """
        self.ui = self.face.face
        self.background = self.face.background
        
    def SpellCard(self):
        """
        active spell attack
        """
        for b in self.boss_layer:
            if hasattr(b, 'spell_attack'):
                b.spell_attack(self.difficulty, self.erina, self.birth_layer, self.boss_layer, self.illustration_layer)

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
                    self.birth_layer,
                    self.energy_layer,
                    self.item_layer,
                    self.boost_layer,
                    self.danmaku_layer)

    def SwitchLayer(self):
        for sprite in self.birth_layer:
            if sprite.birth_time == 0:
                self.birth_layer.remove(sprite)
                self.danmaku_layer.add(sprite)
                self.__getattribute__('danmaku_layer_' + str(sprite.layer)).add(sprite)

    def SpriteDel(self):
        def delete(layer):
            for sprite in layer:
                if hasattr(sprite, 'delete'):
                    if sprite.delete:
                        sprite.kill()
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
                      self.boost_layer,
                      self.danmaku_layer)

    def CollideCheck(self):
        self.erina.collide_check(self.danmaku_layer, self.boss_layer)
        for b in self.boss_layer:
            b.collide_check(self.shouting_layer)

    def Debug(self, screen):
        debug_words_pos_left = 430
        debug_words_pos_top = 300
        
        erina_position = "erina position: " + str(round(self.erina.center[0], 2)) + " , " + str(round(self.erina.center[1], 2))
        ribbon_position = "ribbon position: " + str(round(self.ribbon.center[0], 2)) + " , " + str(round(self.ribbon.center[1], 2))
        erina_health = "erina hp: " + str(self.erina.hp) + "/" + str(self.erina.max_hp)
        danmaku_count = "danmaku count:" + str(len(self.danmaku_layer) + len(self.birth_layer))

        screen.blit(functions.debug_font.render(erina_position, True, (255,0,0)), (debug_words_pos_left, debug_words_pos_top))
        screen.blit(functions.debug_font.render(ribbon_position, True, (255,0,0)), (debug_words_pos_left, debug_words_pos_top + 20))
        screen.blit(functions.debug_font.render(erina_health, True, (255,0,0)), (debug_words_pos_left, debug_words_pos_top + 40))
        for num in range(self.boss):
            b = self.__getattribute__("boss_"+str(num))
            screen.blit(functions.debug_font.render(b.__class__.__name__ + ": " + str(b.hp) + "/" + str(b.max_hp), True, (255,0,0)), (debug_words_pos_left, debug_words_pos_top + 60 + num*20))
        screen.blit(functions.debug_font.render(danmaku_count, True, (255,0,0)), (debug_words_pos_left, debug_words_pos_top + 80 + num*20))


    def PrintScreen(self, screen):
        screen.blit(self.background, (0,0))
        for sprite in self.energy_layer:
            sprite.print_screen(screen)
        for sprite in self.shouting_layer:
            sprite.print_screen(screen)
        for sprite in self.illustration_layer:
            sprite.print_screen(screen)
        screen.blit(self.erina.image, self.erina.rect)
        screen.blit(self.ribbon.image, self.ribbon.rect)
        for sprite in self.boss_layer:
            sprite.print_screen(screen)
        for sprite in self.item_layer:
            sprite.print_screen(screen)
        for sprite in self.birth_layer:
            sprite.print_screen(screen)
        for num in range(self.danmaku_layer_count-1,-1,-1):
            for sprite in self.__getattribute__('danmaku_layer_' + str(num)):
                sprite.print_screen(screen)
            sprite.print_screen(screen)
        for sprite in self.boost_layer:
            sprite.print_screen(screen)
        screen.blit(self.face.face, (0,0))

    def __repr__(self):
        return 'stage boss attack'

    def __call__(self, screen, debug = False):
        while not self.pause:
            functions.ExitCheck()
            self.BackgroundMusic()
            self.KeyPress()
            self.BuffCheck()
            self.SpellCard()
            self.erina.move(self.key_pressed)
            self.ribbon.move(self.erina)
            self.ribbon.attack(self.shouting_layer, self.key_pressed)
            self.SpriteMove()
            self.CollideCheck()
            self.SwitchLayer()
            self.SpriteDel()
            self.UIAnimation()
            self.PrintScreen(screen)
            if debug: self.Debug(screen)
            screen.blit(functions.debug_font.render(str(round(self.clock.get_fps(), 2)), True, (255,0,0)), (600,460))
            pygame.display.update()
            self.clock.tick(60)

class Pause():
    pass