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
        for b in self.boss:
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
        for n in self.boss:
            self.boss_layer.add(self.__getattribute__('boss_'+str(n)))
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
        for b in boss_layer:
            if hasattr(self.boss, bgm):
                self.bgm = self.boss.bgm
                break

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
        
    def SpellCard(self):
        """
        active spell attack
        """
        for b in boss_layer:
            if hasattr(b, 'spell_attack'):
                b.spell_attack(self.difficulty, self.erina, self.boss_layer, self.birth_layer, self.energy_layer)

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

    def CollideCheck(self):
        self.erina.collide_check(self.danmaku_layer, boss_layer)
        for b in self.boss_layer:
            b.collide_check(shouting_layer)

    def PrintScreen(self, screen):
        screen.blit(self.background, (0,0))
        for sprite in energy_layer:
            sprite.print_screen(screen)
        for sprite in shouting_layer:
            sprite.print_screen(screen)
        for sprite in illustration_layer:
            sprite.print_screen(screen)
        screen.blit(self.erina.image, self.erina.rect)
        screen.blit(self.ribbon.image, self.ribbon.rect)
        for sprite in boss_layer:
            sprite.print_screen(screen)
        for sprite in item_layer:
            sprite.print_screen(screen)
        for sprite in birth_layer:
            sprite.print_screen(screen)
        for sprite in danmaku_layer:
            sprite.print_screen(screen)
        for sprite in boost_layer:
            sprite.print_screen(screen)

    def Debug(self):
        debug_words_pos_left = 430
        debug_words_pos_top = 300
        
        erina_position = "erina position: " + str(round(me_erina.center[0], 2)) + " , " + str(round(me_erina.center[1], 2))
        ribbon_position = "ribbon position: " + str(round(me_ribbon.center[0], 2)) + " , " + str(round(me_ribbon.center[1], 2))
        erina_health = "erina hp: " + str(me_erina.hp) + "/" + str(me_erina.max_hp)
        boss_health = "boss hp: " + str(stage_boss.hp) + "/" + str(stage_boss.max_hp)
        danmaku_count = "danmaku count:" + str(len(danmaku_group) + len(birth_group))

        screen.blit(font.render(erina_position, True, (255,0,0)), (debug_words_pos_left, debug_words_pos_top))
        screen.blit(font.render(ribbon_position, True, (255,0,0)), (debug_words_pos_left, debug_words_pos_top + 20))
        screen.blit(font.render(erina_health, True, (255,0,0)), (debug_words_pos_left, debug_words_pos_top + 40))
        screen.blit(font.render(boss_health, True, (255,0,0)), (debug_words_pos_left, debug_words_pos_top + 60))
        screen.blit(font.render(danmaku_count, True, (255,0,0)), (debug_words_pos_left, debug_words_pos_top + 100))

    def __repr__(self):
        return 'stage boss attack'

    def __call__(self, screen, debug = False):
        while not self.pause:
            functions.ExitCheck()

class Pause():
    pass