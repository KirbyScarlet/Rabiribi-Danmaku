import sys
import pygame
import traceback
import random
import platform

from pygame.locals import *
from random import *

class Menu_Main():
    def __init__(self):
        if platform.system() == 'Linux' or platform.system()=='Darwin':
            self.image_start = pygame.image.load("images/title/main_menu/start.png").convert_alpha()
            self.image_extra_start = pygame.image.load("images/title/main_menu/extra_start.png").convert_alpha()
            self.image_practice_start = pygame.image.load("images/title/main_menu/practice_start.png").convert_alpha()
            self.image_spell_practice = pygame.image.load("images/title/main_menu/spell_practice.png").convert_alpha()
            self.image_play_data = pygame.image.load("images/title/main_menu/replay.png").convert_alpha()
            self.image_replay = pygame.image.load("images/title/main_menu/play_data.png").convert_alpha()
            self.image_music_room = pygame.image.load("images/title/main_menu/music_room.png").convert_alpha()
            self.image_options = pygame.image.load("images/title/main_menu/options.png").convert_alpha()
            self.image_manual = pygame.image.load("images/title/main_menu/manual.png").convert_alpha()
            self.image_quit = pygame.image.load("images/title/main_menu/quit.png").convert_alpha()
        if platform.system() == 'Windows':
            self.image_start = pygame.image.load("images\\title\\main_menu\\start.png").convert_alpha()
            self.image_extra_start = pygame.image.load("images\\title\\main_menu\\extra_start.png").convert_alpha()
            self.image_practice_start = pygame.image.load("images\\title\\main_menu\\practice_start.png").convert_alpha()
            self.image_spell_practice = pygame.image.load("images\\title\\main_menu\\spell_practice.png").convert_alpha()
            self.image_play_data = pygame.image.load("images\\title\\main_menu\\replay.png").convert_alpha()
            self.image_replay = pygame.image.load("images\\title\\main_menu\\play_data.png").convert_alpha()
            self.image_music_room = pygame.image.load("images\\title\\main_menu\\music_room.png").convert_alpha()
            self.image_options = pygame.image.load("images\\title\\main_menu\\options.png").convert_alpha()
            self.image_manual = pygame.image.load("images\\title\\main_menu\\manual.png").convert_alpha()
            self.image_quit = pygame.image.load("images\\title\\main_menu\\quit.png").convert_alpha()
        
        self.image_start_rect = self.image_start.get_rect()
        self.image_extra_start_rect = self.image_extra_start.get_rect()
        self.image_practice_start_rect = self.image_practice_start.get_rect()
        self.image_spell_practice_rect = self.image_spell_practice.get_rect()
        self.image_play_data_rect = self.image_play_data.get_rect()
        self.image_replay_rect = self.image_replay.get_rect()
        self.image_music_room_rect = self.image_music_room.get_rect()
        self.image_options_rect = self.image_options.get_rect()
        self.image_manual_rect = self.image_manual.get_rect()
        self.image_quit_rect = self.image_quit.get_rect()
        
        left_position = 640
        term = 10
        self.left_temp_pos = [ \
                left_position + term * 1, \
                left_position + term * 2, \
                left_position + term * 3, \
                left_position + term * 4, \
                left_position + term * 5, \
                left_position + term * 6, \
                left_position + term * 7, \
                left_position + term * 8, \
                left_position + term * 9, \
                left_position + term * 10 \
                ]
        
        self.image_start_rect.left = self.left_temp_pos[0]
        self.image_extra_start_rect.left = self.left_temp_pos[1]
        self.image_practice_start_rect.left = self.left_temp_pos[2]
        self.image_spell_practice_rect.left = self.left_temp_pos[3]
        self.image_play_data_rect.left = self.left_temp_pos[4]
        self.image_replay_rect.left = self.left_temp_pos[5]
        self.image_music_room_rect.left = self.left_temp_pos[6]
        self.image_options_rect.left = self.left_temp_pos[7]
        self.image_manual_rect.left = self.left_temp_pos[8]
        self.image_quit_rect.left = self.left_temp_pos[9]
        
        top_position = 220
        self.image_start_rect.top = top_position + 20*1
        self.image_extra_start_rect.top = top_position + 20*2
        self.image_practice_start_rect.top = top_position + 20*3
        self.image_spell_practice_rect.top = top_position + 20*4
        self.image_play_data_rect.top = top_position + 20*5
        self.image_replay_rect.top = top_position + 20*6
        self.image_music_room_rect.top = top_position + 20*7
        self.image_options_rect.top = top_position + 20*8
        self.image_manual_rect.top = top_position + 20*9
        self.image_quit_rect.top = top_position + 20*10
        
        self.image_select = [1,0,0,0,0,0,0,0,0,0]
        
    def main_menu_image_move_in(self):
        left_position = 400
        rato = 100
        speed = [ \
                     (self.left_temp_pos[0] - left_position) ** 1.5 / rato, \
                     (self.left_temp_pos[1] - left_position) ** 1.5 / rato, \
                     (self.left_temp_pos[2] - left_position) ** 1.5 / rato, \
                     (self.left_temp_pos[3] - left_position) ** 1.5 / rato, \
                     (self.left_temp_pos[4] - left_position) ** 1.5 / rato, \
                     (self.left_temp_pos[5] - left_position) ** 1.5 / rato, \
                     (self.left_temp_pos[6] - left_position) ** 1.5 / rato, \
                     (self.left_temp_pos[7] - left_position) ** 1.5 / rato, \
                     (self.left_temp_pos[8] - left_position) ** 1.5 / rato, \
                     (self.left_temp_pos[9] - left_position) ** 1.5 / rato \
                    ]
        
        self.left_temp_pos[0] -= speed[0]
        self.left_temp_pos[1] -= speed[1]
        self.left_temp_pos[2] -= speed[2]
        self.left_temp_pos[3] -= speed[3]
        self.left_temp_pos[4] -= speed[4]
        self.left_temp_pos[5] -= speed[5]
        self.left_temp_pos[6] -= speed[6]
        self.left_temp_pos[7] -= speed[7]
        self.left_temp_pos[8] -= speed[8]
        self.left_temp_pos[9] -= speed[9]
        
        self.image_start_rect.left = self.left_temp_pos[0]
        self.image_extra_start_rect.left = self.left_temp_pos[1]
        self.image_practice_start_rect.left = self.left_temp_pos[2]
        self.image_spell_practice_rect.left = self.left_temp_pos[3]
        self.image_play_data_rect.left = self.left_temp_pos[4]
        self.image_replay_rect.left = self.left_temp_pos[5]
        self.image_music_room_rect.left = self.left_temp_pos[6]
        self.image_options_rect.left = self.left_temp_pos[7]
        self.image_manual_rect.left = self.left_temp_pos[8]
        self.image_quit_rect.left = self.left_temp_pos[9]
    
    def main_menu_image_move_out(self):
        left_position_temp = 650
        rato = 100
        rang = 2
        
        for i in range(10):
            if self.image_select[i]:
                temp = i
                
        left_position = [ \
                         left_position_temp + 50 - 5 * abs(temp-0), \
                         left_position_temp + 50 - 5 * abs(temp-1), \
                         left_position_temp + 50 - 5 * abs(temp-2), \
                         left_position_temp + 50 - 5 * abs(temp-3), \
                         left_position_temp + 50 - 5 * abs(temp-4), \
                         left_position_temp + 50 - 5 * abs(temp-5), \
                         left_position_temp + 50 - 5 * abs(temp-6), \
                         left_position_temp + 50 - 5 * abs(temp-7), \
                         left_position_temp + 50 - 5 * abs(temp-8), \
                         left_position_temp + 50 - 5 * abs(temp-9) \
                        ]
        
        speed = [ \
                     (left_position[0] + rang * (10 - abs(temp-0)) - self.left_temp_pos[0]) ** 1.5 / rato, \
                     (left_position[1] + rang * (10 - abs(temp-1)) - self.left_temp_pos[1]) ** 1.5 / rato, \
                     (left_position[2] + rang * (10 - abs(temp-2)) - self.left_temp_pos[2]) ** 1.5 / rato, \
                     (left_position[3] + rang * (10 - abs(temp-3)) - self.left_temp_pos[3]) ** 1.5 / rato, \
                     (left_position[4] + rang * (10 - abs(temp-4)) - self.left_temp_pos[4]) ** 1.5 / rato, \
                     (left_position[5] + rang * (10 - abs(temp-5)) - self.left_temp_pos[5]) ** 1.5 / rato, \
                     (left_position[6] + rang * (10 - abs(temp-6)) - self.left_temp_pos[6]) ** 1.5 / rato, \
                     (left_position[7] + rang * (10 - abs(temp-7)) - self.left_temp_pos[7]) ** 1.5 / rato, \
                     (left_position[8] + rang * (10 - abs(temp-8)) - self.left_temp_pos[8]) ** 1.5 / rato, \
                     (left_position[9] + rang * (10 - abs(temp-9)) - self.left_temp_pos[9]) ** 1.5 / rato \
                    ]
        
        self.left_temp_pos[0] += speed[0]
        self.left_temp_pos[1] += speed[1]
        self.left_temp_pos[2] += speed[2]
        self.left_temp_pos[3] += speed[3]
        self.left_temp_pos[4] += speed[4]
        self.left_temp_pos[5] += speed[5]
        self.left_temp_pos[6] += speed[6]
        self.left_temp_pos[7] += speed[7]
        self.left_temp_pos[8] += speed[8]
        self.left_temp_pos[9] += speed[9]
        
        self.image_start_rect.left = self.left_temp_pos[0]
        self.image_extra_start_rect.left = self.left_temp_pos[1]
        self.image_practice_start_rect.left = self.left_temp_pos[2]
        self.image_spell_practice_rect.left = self.left_temp_pos[3]
        self.image_play_data_rect.left = self.left_temp_pos[4]
        self.image_replay_rect.left = self.left_temp_pos[5]
        self.image_music_room_rect.left = self.left_temp_pos[6]
        self.image_options_rect.left = self.left_temp_pos[7]
        self.image_manual_rect.left = self.left_temp_pos[8]
        self.image_quit_rect.left = self.left_temp_pos[9]
        
    def main_menu_move(self):
        
        for i in range(10):
            if self.image_select[i] == 0:
                temp = self.left_temp_pos[i]
                self.left_temp_pos[i] += (temp - 420)**2/50
            if self.image_select[i] == 1:
                temp = self.left_temp_pos[i]
                self.left_temp_pos[i] -= (temp - 400)**2/50

        self.image_start_rect.left = self.left_temp_pos[0]
        self.image_extra_start_rect.left = self.left_temp_pos[1]
        self.image_practice_start_rect.left = self.left_temp_pos[2]
        self.image_spell_practice_rect.left = self.left_temp_pos[3]
        self.image_play_data_rect.left = self.left_temp_pos[4]
        self.image_replay_rect.left = self.left_temp_pos[5]
        self.image_music_room_rect.left = self.left_temp_pos[6]
        self.image_options_rect.left = self.left_temp_pos[7]
        self.image_manual_rect.left = self.left_temp_pos[8]
        self.image_quit_rect.left = self.left_temp_pos[9]

    def main_menu_switch(self):
        global switch_control
        global running_control
        if not switch_control:
            key_pressed = pygame.key.get_pressed()
            for i in range(10):
                if self.image_select[i]:
                    temp = i
            if key_pressed[K_DOWN]:
                self.image_select[temp] = 0
                if temp+1 == 10 :
                    self.image_select[0] = 1
                else:
                    self.image_select[temp+1] = 1
                switch_control = 10
            elif key_pressed[K_UP]:
                self.image_select[temp] = 0
                if temp-1 == -1:
                    self.image_select[9] = 1
                else:
                    self.image_select[temp-1] = 1
                switch_control = 10
            elif key_pressed[K_x]:
                self.image_select[temp] = 0
                self.image_select[9] = 1
                switch_control = 10
            elif key_pressed[K_z]:
                if self.image_select[9]:
                    pygame.quit()
                    sys.exit()
                    pass
                else:
                    running_control['main']['intime'] = 0
                    running_control['main']['move_out'] = 40
            else:
                pass
        else:
            switch_control -= 1
                
    def main_menu_print(self, screen):
        screen.blit(self.image_start, self.image_start_rect)
        screen.blit(self.image_extra_start, self.image_extra_start_rect)
        screen.blit(self.image_practice_start, self.image_practice_start_rect)
        screen.blit(self.image_spell_practice, self.image_spell_practice_rect)
        screen.blit(self.image_play_data, self.image_play_data_rect)
        screen.blit(self.image_replay, self.image_replay_rect)
        screen.blit(self.image_music_room, self.image_music_room_rect)
        screen.blit(self.image_options, self.image_options_rect)
        screen.blit(self.image_manual, self.image_manual_rect)
        screen.blit(self.image_quit, self.image_quit_rect)
                
class Menu_Start():
    def __init__(self):
        if platform.system() == 'Linux' or platform.system()=='Darwin':
            self.image_casual = pygame.image.load("images/title/start/casual.png").convert_alpha()
            self.image_novice = pygame.image.load("images/title/start/novice.png").convert_alpha()
            self.image_normal = pygame.image.load("images/title/start/normal.png").convert_alpha()
            self.image_hard = pygame.image.load("images/title/start/hard.png").convert_alpha()
            self.image_hell = pygame.image.load("images/title/start/hell.png").convert_alpha()
            self.image_bunny_exclusion = pygame.image.load("images/title/start/bunny_exclusion.png").convert_alpha()
            self.image_impossible = pygame.image.load("images/title/start/impossible.png").convert_alpha()
        if platform.system() == 'Windows':
            self.image_casual = pygame.image.load("images\\title\\start\\casual.png").convert_alpha()
            self.image_novice = pygame.image.load("images\\title\\start\\novice.png").convert_alpha()
            self.image_normal = pygame.image.load("images\\title\\start\\normal.png").convert_alpha()
            self.image_hard = pygame.image.load("images\\title\\start\\hard.png").convert_alpha()
            self.image_hell = pygame.image.load("images\\title\\start\\hell.png").convert_alpha()
            self.image_bunny_exclusion = pygame.image.load("images\\title\\start\\bunny_exclusion.png").convert_alpha()
            self.image_impossible = pygame.image.load("images\\title\\start\\impossible.png").convert_alpha()
        
        self.image_casual_rect = self.image_casual.get_rect()
        self.image_novice_rect = self.image_novice.get_rect()
        self.image_normal_rect = self.image_normal.get_rect()
        self.image_hard_rect = self.image_hard.get_rect()
        self.image_hell_rect = self.image_hell.get_rect()
        self.image_bunny_exclusion_rect = self.image_bunny_exclusion.get_rect()
        self.image_impossible_rect = self.image_impossible.get_rect()
        
        self.image_casual_rect.left = 220
        self.image_novice_rect.left = 220
        self.image_normal_rect.left = 220
        self.image_hard_rect.left = 220
        self.image_hell_rect.left = 220
        self.image_bunny_exclusion_rect.left = 220
        self.image_impossible_rect.left = 220
        
        self.top_temp_pos = -100
        self.top_pos = 480
        self.rate = 100
               
        self.image_casual_rect.top = self.top_pos + self.rate
        self.image_novice_rect.top = self.image_casual_rect.top + self.rate
        self.image_normal_rect.top = self.image_novice_rect.top + self.rate
        self.image_hard_rect.top = self.image_normal_rect.top + self.rate
        self.image_hell_rect.top = self.image_hard_rect.top + self.rate
        self.image_bunny_exclusion_rect.top = self.image_hell_rect.top + self.rate
        self.image_impossible_rect.top = self.image_bunny_exclusion_rect.top + self.rate
        
        self.image_select = [0,0,1,0,0,0,0]
        self.select_top_pos = [ \
                                self.image_casual_rect, \
                                self.image_novice_rect, \
                                self.image_normal_rect, \
                                self.image_hard_rect, \
                                self.image_hell_rect, \
                                self.image_bunny_exclusion_rect, \
                                self.image_impossible_rect \
                                ]
        self.select_top_temp_pos = [ \
                                self.image_casual_rect.top, \
                                self.image_novice_rect.top, \
                                self.image_normal_rect.top, \
                                self.image_hard_rect.top, \
                                self.image_hell_rect.top, \
                                self.image_bunny_exclusion_rect.top, \
                                self.image_impossible_rect.top \
                                ]        
    def menu_start_move_in(self):
        rate = 100
        speed = (self.top_pos - self.top_temp_pos) ** 1.5 / rate

        self.top_pos -= speed

        self.image_casual_rect.top = self.top_pos + self.rate
        self.image_novice_rect.top = self.image_casual_rect.top + self.rate
        self.image_normal_rect.top = self.image_novice_rect.top + self.rate
        self.image_hard_rect.top = self.image_normal_rect.top + self.rate
        self.image_hell_rect.top = self.image_hard_rect.top + self.rate
        self.image_bunny_exclusion_rect.top = self.image_hell_rect.top + self.rate
        self.image_impossible_rect.top = self.image_bunny_exclusion_rect.top + self.rate
        
    def menu_start_move_out(self):
        rate = 400
        speed = (600 - self.top_pos) ** 1.5 / rate
        
        self.top_pos += speed
        
        self.image_casual_rect.top = self.top_pos + self.rate
        self.image_novice_rect.top = self.image_casual_rect.top + self.rate
        self.image_normal_rect.top = self.image_novice_rect.top + self.rate
        self.image_hard_rect.top = self.image_normal_rect.top + self.rate
        self.image_hell_rect.top = self.image_hard_rect.top + self.rate
        self.image_bunny_exclusion_rect.top = self.image_hell_rect.top + self.rate
        self.image_impossible_rect.top = self.image_bunny_exclusion_rect.top + self.rate
            
    def menu_start_move(self):
        rate = 10
        for i in range(7):
            if self.image_select[i]:
                temp = i
        self.top_temp_pos = 100 - temp * self.rate
        speed = (self.top_pos - self.top_temp_pos) / rate
        
        self.top_pos -= speed
        self.image_casual_rect.top = self.top_pos + self.rate
        self.image_novice_rect.top = self.image_casual_rect.top + self.rate
        self.image_normal_rect.top = self.image_novice_rect.top + self.rate
        self.image_hard_rect.top = self.image_normal_rect.top + self.rate
        self.image_hell_rect.top = self.image_hard_rect.top + self.rate
        self.image_bunny_exclusion_rect.top = self.image_hell_rect.top + self.rate
        self.image_impossible_rect.top = self.image_bunny_exclusion_rect.top + self.rate

        self.select_top_temp_pos = [ \
                                self.image_casual_rect.top, \
                                self.image_novice_rect.top, \
                                self.image_normal_rect.top, \
                                self.image_hard_rect.top, \
                                self.image_hell_rect.top, \
                                self.image_bunny_exclusion_rect.top, \
                                self.image_impossible_rect.top \
                                ]
    
    def menu_start_difficulty_move_out(self):
        rate = 10
        for i in range(7):
            if self.image_select[i]:
                temp = i
        for i in range(0,7):
            if i < temp:
                self.select_top_pos[i].top -= (self.select_top_pos[i].top + 80) / rate
            if i == temp:
                self.select_top_pos[i].top += (400 - self.select_top_pos[i].top) / rate
                self.select_top_pos[i].left -= (self.select_top_pos[i].left - 20) / rate
            if i > temp:
                self.select_top_pos[i].top += (560 - self.select_top_pos[i].top) / rate
        
        self.image_casual_rect = self.select_top_pos[0]
        self.image_novice_rect = self.select_top_pos[1]
        self.image_normal_rect = self.select_top_pos[2]
        self.image_hard_top_rect = self.select_top_pos[3]
        self.image_hell_rect_rect = self.select_top_pos[4]
        self.image_bunny_exclusion_rect = self.select_top_pos[5]
        self.image_impossible_rect = self.select_top_pos[6]
        
    def menu_start_difficulty_move_back(self):
        rate = 10
        
        for i in range(7):
            if self.image_select[i]:
                temp = i
        
        for i in range(7):
            if i < temp:
                self.select_top_pos[i].top += (9.0 + self.select_top_temp_pos[i] - self.select_top_pos[i].top) / rate
            if i == temp:
                self.select_top_pos[i].top += (self.select_top_temp_pos[i] - self.select_top_pos[i].top) / rate
                self.select_top_pos[i].left += (230 - self.select_top_pos[i].left) / rate
            if i > temp:
                self.select_top_pos[i].top += (self.select_top_temp_pos[i] - self.select_top_pos[i].top) / rate
        
        self.image_casual_rect = self.select_top_pos[0]
        self.image_novice_rect = self.select_top_pos[1]
        self.image_normal_rect = self.select_top_pos[2]
        self.image_hard_top_rect = self.select_top_pos[3]
        self.image_hell_rect_rect = self.select_top_pos[4]
        self.image_bunny_exclusion_rect = self.select_top_pos[5]
        self.image_impossible_rect = self.select_top_pos[6]
        
    def menu_start_switch(self):
        global switch_control
        global running_control
        if not switch_control:
            key_pressed = pygame.key.get_pressed()
            for i in range(7):
                if self.image_select[i]:
                    temp = i
            if key_pressed[K_DOWN]:
                self.image_select[temp] = 0
                if temp == 6:
                    self.image_select[0] = 1
                else:
                    self.image_select[temp+1] = 1
                switch_control = 10
            elif key_pressed[K_UP]:
                self.image_select[temp] = 0
                if temp == 0:
                    self.image_select[6] = 1
                else:
                    self.image_select[temp-1] = 1
                switch_control = 10
            elif key_pressed[K_x]:
                if running_control['start']['intime']['switch_difficulty']:
                    running_control['start']['intime']['switch_difficulty'] = 0
                    running_control['start']['move_out'] = 40
                elif running_control['start']['intime']['switch_ribbon']:
                    running_control['start']['intime']['switch_ribbon'] = 0
                    running_control['start']['intime']['ribbon_to_difficulty'] = 40
            elif key_pressed[K_z]:
                if running_control['start']['intime']['switch_difficulty']:
                    running_control['start']['intime']['switch_difficulty'] = 0
                    running_control['start']['intime']['difficulty_to_ribbon'] = 40
        else:
            switch_control -= 1
    
    def menu_start_print(self, screen):
        screen.blit(self.image_casual, self.image_casual_rect)
        screen.blit(self.image_novice, self.image_novice_rect)
        screen.blit(self.image_normal, self.image_normal_rect)
        screen.blit(self.image_hard, self.image_hard_rect)
        screen.blit(self.image_hell, self.image_hell_rect)
        screen.blit(self.image_bunny_exclusion, self.image_bunny_exclusion_rect)
        screen.blit(self.image_impossible, self.image_impossible_rect)

class Menu_Extra_Start():
    def __init__(self):
        
        if platform.system() == 'Linux' or platform.system()=='Darwin':
            self.image_extra = pygame.image.load("images/title/extra/extra.png").convert_alpha()
        if platform.system() == 'Windows':
            self.image_extra = pygame.image.load("images\\title\\extra\\extra.png").convert_alpha()
        
        self.image_extra_rect = self.image_extra.get_rect()
       
        self.top_pos = 480
        self.left_pos = 120
        
        self.image_extra_rect.top = self.top_pos
        self.image_extra_rect.left = 120

    def menu_extra_move_in(self):
        rate = 100
        speed = (self.top_pos - 150) ** 1.5 / rate
        
        self.top_pos -= speed
        self.image_extra_rect.top = self.top_pos
        
    def menu_extra_move_out(self):
        rate = 100
        speed = (600 - self.top_pos) ** 1.5 / rate
        
        self.top_pos += speed
        self.image_extra_rect.top = self.top_pos

    def menu_extra_difficulty_move_out(self):
        rate = 10
        speed = [ \
                (self.top_pos - 380) / rate, \
                (self.left_pos + 100) / rate \
                ]
        self.top_pos -= speed[0]
        self.left_pos -= speed[1]
        self.image_extra_rect.top = self.top_pos
        self.image_extra_rect.left = self.left_pos
        
    def menu_extra_difficulty_move_back(self):
        rate = 10
        speed = [ \
                (self.top_pos - 150) / rate, \
                (self.left_pos - 120) / rate \
                ]
        self.top_pos -= speed[0]
        self.left_pos -= speed[1]
        self.image_extra_rect.top = self.top_pos
        self.image_extra_rect.left = self.left_pos

    def menu_extra_switch(self):
        global switch_control
        global running_control
        key_pressed = pygame.key.get_pressed()
        if not switch_control:
            if key_pressed[K_UP] and key_pressed[K_DOWN]:
                switch_control = 10
            elif key_pressed[K_x]:
                if running_control['extra_start']['intime']['switch_difficulty']:
                    running_control['extra_start']['intime']['switch_difficulty'] = 0
                    running_control['extra_start']['move_out'] = 40
                elif running_control['extra_start']['intime']['switch_ribbon']:
                    running_control['extra_start']['intime']['switch_ribbon'] = 0
                    running_control['extra_start']['intime']['ribbon_to_difficulty'] = 40
                
            elif key_pressed[K_z]:
                if running_control['extra_start']['intime']['switch_difficulty']:
                    running_control['extra_start']['intime']['switch_difficulty'] = 0
                    running_control['extra_start']['intime']['difficulty_to_ribbon'] = 40

        else:
            switch_control -= 1
    
    def menu_extra_print(self, screen):
        screen.blit(self.image_extra, self.image_extra_rect)

class Menu_Practice_start():
    def __init__(self):
        
        if platform.system() == 'Linux' or platform.system()=='Darwin':
            self.image_section1_stage1a = pygame.image.load("images/title/spell_practice/section1_stage1a.png").convert_alpha()
            self.image_section1_stage1b = pygame.image.load("images/title/spell_practice/section1_stage1b.png").convert_alpha()
            self.image_section1_stage2a = pygame.image.load("images/title/spell_practice/section1_stage2a.png").convert_alpha()
            self.image_section1_stage2b = pygame.image.load("images/title/spell_practice/section1_stage2b.png").convert_alpha()
            self.image_section1_stage3a = pygame.image.load("images/title/spell_practice/section1_stage3a.png").convert_alpha()
            self.image_section1_stage3b = pygame.image.load("images/title/spell_practice/section1_stage3b.png").convert_alpha()
            self.image_section1_stage4a = pygame.image.load("images/title/spell_practice/section1_stage4a.png").convert_alpha()
            self.image_section1_stage4b = pygame.image.load("images/title/spell_practice/section1_stage4b.png").convert_alpha()
            self.image_section1_stage5 = pygame.image.load("images/title/spell_practice/section1_stage5.png").convert_alpha()
            self.image_section1_stage6 = pygame.image.load("images/title/spell_practice/section1_stage6.png").convert_alpha()
            self.image_section2_stage1a = pygame.image.load("images/title/spell_practice/section2_stage1a.png").convert_alpha()
            self.image_section2_stage1b = pygame.image.load("images/title/spell_practice/section2_stage1b.png").convert_alpha()
            self.image_section2_stage2a = pygame.image.load("images/title/spell_practice/section2_stage2a.png").convert_alpha()
            self.image_section2_stage2b = pygame.image.load("images/title/spell_practice/section2_stage2b.png").convert_alpha()
            self.image_section2_stage3a = pygame.image.load("images/title/spell_practice/section2_stage3a.png").convert_alpha()
            self.image_section2_stage3b = pygame.image.load("images/title/spell_practice/section2_stage3b.png").convert_alpha()
            self.image_section2_stage4 = pygame.image.load("images/title/spell_practice/section2_stage4.png").convert_alpha()
            self.image_section2_stage5 = pygame.image.load("images/title/spell_practice/section2_stage5.png").convert_alpha()
            self.image_section2_stage6 = pygame.image.load("images/title/spell_practice/section2_stage6.png").convert_alpha()

        if platform.system() == 'Windows':
            self.image_section1_stage1a = pygame.image.load("images\\title\\spell_practice\\section1_stage1a.png").convert_alpha()
            self.image_section1_stage1b = pygame.image.load("images\\title\\spell_practice\\section1_stage1b.png").convert_alpha()
            self.image_section1_stage2a = pygame.image.load("images\\title\\spell_practice\\section1_stage2a.png").convert_alpha()
            self.image_section1_stage2b = pygame.image.load("images\\title\\spell_practice\\section1_stage2b.png").convert_alpha()
            self.image_section1_stage3a = pygame.image.load("images\\title\\spell_practice\\section1_stage3a.png").convert_alpha()
            self.image_section1_stage3b = pygame.image.load("images\\title\\spell_practice\\section1_stage3b.png").convert_alpha()
            self.image_section1_stage4a = pygame.image.load("images\\title\\spell_practice\\section1_stage4a.png").convert_alpha()
            self.image_section1_stage4b = pygame.image.load("images\\title\\spell_practice\\section1_stage4b.png").convert_alpha()
            self.image_section1_stage5 = pygame.image.load("images\\title\\spell_practice\\section1_stage5.png").convert_alpha()
            self.image_section1_stage6 = pygame.image.load("images\\title\\spell_practice\\section1_stage6.png").convert_alpha()
            self.image_section2_stage1a = pygame.image.load("images\\title\\spell_practice\\section2_stage1a.png").convert_alpha()
            self.image_section2_stage1b = pygame.image.load("images\\title\\spell_practice\\section2_stage1b.png").convert_alpha()
            self.image_section2_stage2a = pygame.image.load("images\\title\\spell_practice\\section2_stage2a.png").convert_alpha()
            self.image_section2_stage2b = pygame.image.load("images\\title\\spell_practice\\section2_stage2b.png").convert_alpha()
            self.image_section2_stage3a = pygame.image.load("images\\title\\spell_practice\\section2_stage3a.png").convert_alpha()
            self.image_section2_stage3b = pygame.image.load("images\\title\\spell_practice\\section2_stage3b.png").convert_alpha()
            self.image_section2_stage4 = pygame.image.load("images\\title\\spell_practice\\section2_stage4.png").convert_alpha()
            self.image_section2_stage5 = pygame.image.load("images\\title\\spell_practice\\section2_stage5.png").convert_alpha()
            self.image_section2_stage6 = pygame.image.load("images\\title\\spell_practice\\section2_stage6.png").convert_alpha()
        
        self.image_section1_stage1a_rect = self.image_section1_stage1a.get_rect()
        self.image_section1_stage1b_rect = self.image_section1_stage1b.get_rect()
        self.image_section1_stage2a_rect = self.image_section1_stage2a.get_rect()
        self.image_section1_stage2b_rect = self.image_section1_stage2b.get_rect()
        self.image_section1_stage3a_rect = self.image_section1_stage3a.get_rect()
        self.image_section1_stage3b_rect = self.image_section1_stage3b.get_rect()
        self.image_section1_stage4a_rect = self.image_section1_stage4a.get_rect()
        self.image_section1_stage4b_rect = self.image_section1_stage4b.get_rect()
        self.image_section1_stage5_rect = self.image_section1_stage5.get_rect()
        self.image_section1_stage6_rect = self.image_section1_stage6.get_rect()
        self.image_section2_stage1a_rect = self.image_section2_stage1a.get_rect()
        self.image_section2_stage1b_rect = self.image_section2_stage1b.get_rect()
        self.image_section2_stage2a_rect = self.image_section2_stage2a.get_rect()
        self.image_section2_stage2b_rect = self.image_section2_stage2b.get_rect()
        self.image_section2_stage3a_rect = self.image_section2_stage3a.get_rect()
        self.image_section2_stage3b_rect = self.image_section2_stage3b.get_rect()
        self.image_section2_stage4_rect = self.image_section2_stage4.get_rect()
        self.image_section2_stage5_rect = self.image_section2_stage5.get_rect()
        self.image_section2_stage6_rect = self.image_section2_stage6.get_rect()
        
        self.left_master = 80
        self.left_slave = 100

        self.image_section1_stage1a_rect.left = self.left_slave
        self.image_section1_stage1b_rect.left = self.left_slave
        self.image_section1_stage2a_rect.left = self.left_slave
        self.image_section1_stage2b_rect.left = self.left_slave
        self.image_section1_stage3a_rect.left = self.left_slave
        self.image_section1_stage3b_rect.left = self.left_slave
        self.image_section1_stage4a_rect.left = self.left_slave
        self.image_section1_stage4b_rect.left = self.left_slave
        self.image_section1_stage5_rect.left = self.left_slave
        self.image_section1_stage6_rect.left = self.left_slave
        
        self.image_section1_stage1a_rect.top = self.image_section1_rect.top
        self.image_section1_stage1b_rect.top = self.image_section1_rect.top
        self.image_section1_stage2a_rect.top = self.image_section1_rect.top
        self.image_section1_stage2b_rect.top = self.image_section1_rect.top
        self.image_section1_stage3a_rect.top = self.image_section1_rect.top
        self.image_section1_stage3b_rect.top = self.image_section1_rect.top
        self.image_section1_stage4a_rect.top = self.image_section1_rect.top
        self.image_section1_stage4b_rect.top = self.image_section1_rect.top
        self.image_section1_stage5_rect.top = self.image_section1_rect.top
        self.image_section1_stage6_rect.top = self.image_section1_rect.top
        
        self.image_section2_stage1a_rect.left = self.left_slave
        self.image_section2_stage1b_rect.left = self.left_slave
        self.image_section2_stage2a_rect.left = self.left_slave
        self.image_section2_stage2b_rect.left = self.left_slave
        self.image_section2_stage3a_rect.left = self.left_slave
        self.image_section2_stage3b_rect.left = self.left_slave
        self.image_section2_stage4_rect.left = self.left_slave
        self.image_section2_stage5_rect.left = self.left_slave
        self.image_section2_stage6_rect.left = self.left_slave
        
        self.image_section2_stage1a_rect.top = self.image_section2_rect.top
        self.image_section2_stage1b_rect.top = self.image_section2_rect.top
        self.image_section2_stage2a_rect.top = self.image_section2_rect.top
        self.image_section2_stage2b_rect.top = self.image_section2_rect.top
        self.image_section2_stage3a_rect.top = self.image_section2_rect.top
        self.image_section2_stage3b_rect.top = self.image_section2_rect.top
        self.image_section2_stage4_rect.top = self.image_section2_rect.top
        self.image_section2_stage5_rect.top = self.image_section2_rect.top
        self.image_section2_stage6_rect.top = self.image_section2_rect.top
        
    def menu_practice_section1_move_in():
        pass
    def menu_practice_section1_move_out():
        pass

class Menu_Spell_Practice():
    def __init__(self):
        if platform.system() == 'Linux' or platform.system()=='Darwin':
            self.image_section1 = pygame.image.load("images/title/spell_practice/section1.png").convert_alpha()
            self.image_section2 = pygame.image.load("images/title/spell_practice/section2.png").convert_alpha()
            self.image_extra = pygame.image.load("images/title/spell_practice/extra.png").convert_alpha()
            self.image_overdrive = pygame.image.load("images/title/spell_practice/overdrive.png").convert_alpha()
        if platform.system() == 'Windows':
            self.image_section1 = pygame.image.load("images\\title\\spell_practice\\section1.png").convert_alpha()
            self.image_section2 = pygame.image.load("images\\title\\spell_practice\\section2.png").convert_alpha()
            self.image_extra = pygame.image.load("images\\title\\spell_practice/extra.png").convert_alpha()
            self.image_overdrive = pygame.image.load("images\\title\\spell_practice\\overdrive.png").convert_alpha()
        
        self.image_section1_rect = self.image_section1.get_rect()
        self.image_section2_rect = self.image_section2.get_rect()
        self.image_extra_rect = self.image_extra.get_rect()
        self.image_overdrive_rect = self.image_overdrive.get_rect()
        
        self.left_master = 80
        self.left_slave = 100
        self.left_master_temp_pos = [-80] * 4
        self.left_section1_temp_pos = [-80] * 10
        self.left_section2_temp_pos = [-80] * 9
        
        self.image_section1_rect.left = -80
        self.image_section2_rect.left = -80
        self.image_extra_rect.left = -80
        self.image_overdrive_rect.left = -80
        
        self.image_section1_rect.top = 100
        self.image_section2_rect.top = 120
        self.image_extra_rect.top = 140
        self.image_overdrive_rect.top = 160
            
        self.section_select = [4,1,0,0,0]
        
        self.image_select = self.section_select

    def menu_spell_main_move_in(self):
        rate = 100
        speed = [ \
                (self.left_master - self.left_master_temp_pos[0]) ** 1.5 / rate, \
                (self.left_master - self.left_master_temp_pos[1]) ** 1.5 / rate, \
                (self.left_master - self.left_master_temp_pos[2]) ** 1.5 / rate, \
                (self.left_master - self.left_master_temp_pos[3]) ** 1.5 / rate \
                ]

        self.left_master_temp_pos[0] += speed[0]
        self.left_master_temp_pos[1] += speed[1]
        self.left_master_temp_pos[2] += speed[2]
        self.left_master_temp_pos[3] += speed[3]
        
        self.image_section1_rect.left = self.left_master_temp_pos[0]
        self.image_section2_rect.left = self.left_master_temp_pos[1]
        self.image_extra_rect.left = self.left_master_temp_pos[2]
        self.image_overdrive_rect.left = self.left_master_temp_pos[3]
    
    def menu_spell_main_move_out(self):
        rate = 100
        speed = [ \
                (self.left_master_temp_pos[0] + 100) ** 1.5 / rate, \
                (self.left_master_temp_pos[1] + 100) ** 1.5 / rate, \
                (self.left_master_temp_pos[2] + 100) ** 1.5 / rate, \
                (self.left_master_temp_pos[3] + 100) ** 1.5 / rate \
                ]
        
        self.left_master_temp_pos[0] -= speed[0]
        self.left_master_temp_pos[1] -= speed[1]
        self.left_master_temp_pos[2] -= speed[2]
        self.left_master_temp_pos[3] -= speed[3]
        
        self.image_section1_rect.left = self.left_master_temp_pos[0]
        self.image_section2_rect.left = self.left_master_temp_pos[1]
        self.image_extra_rect.left = self.left_master_temp_pos[2]
        self.image_overdrive_rect.left = self.left_master_temp_pos[3]
        
    def menu_spell_main_move(self):
        for i in range(self.section_select[0]):
            if i: temp = i
        for i in range(self.section_select[0]):
            if self.section_select[i+1]:
                speed = (70 - self.left_master_temp_pos[i]) / 3.0
                self.left_master_temp_pos[i] += speed
            else:
                speed = (self.left_master_temp_pos[i] - 60) / 3.0
                self.left_master_temp_pos[i] -= speed
        
        self.image_section1_rect.left = self.left_master_temp_pos[0]
        self.image_section2_rect.left = self.left_master_temp_pos[1]
        self.image_extra_rect.left = self.left_master_temp_pos[2]
        self.image_overdrive_rect.left = self.left_master_temp_pos[3]
    
    def menu_spell_section1_move_in():
        pass
    def menu_spell_section1_move_out():
        pass
    def menu_spell_section1_move():
        pass
    def menu_spell_section2_move_in():
        pass
    def menu_spell_section2_move_out():
        pass
    def menu_spell_section2_move():
        pass
    def menu_spell_extra_move_in():
        pass
    def menu_spell_extra_move_out():
        pass
    def menu_spell_extra_move():
        pass
    def menu_spell_overdrive_move_in():
        pass
    def menu_spell_overdrive_move_out():
        pass
    def menu_spell_overdrive_move():
        pass
    
    def menu_spell_switch(self):
        global switch_control
        global running_control
        key_pressed = pygame.key.get_pressed()
        if not switch_control:
            if key_pressed[K_DOWN]:
                for i in range(1,self.image_select[0]+1):
                    if self.image_select[i]:
                        temp = i
                self.image_select[temp] = 0
                if temp == self.image_select[0]:
                    self.image_select[1] = 1
                else:
                    self.image_select[temp+1] = 1
                switch_control = 10
            elif key_pressed[K_UP]:
                for i in range(1,self.image_select[0]+1):
                    if self.image_select[i]:
                        temp = i
                self.image_select[temp] = 0
                if temp == 1:
                    self.image_select[self.image_select[0]] = 1
                else:
                    self.image_select[temp-1] = 1
                switch_control = 10
            elif key_pressed[K_LEFT]:
                pass
            elif key_pressed[K_RIGHT]:
                pass
            elif key_pressed[K_x]:
                if running_control['spell_practice']['intime']['switch_section']:
                    running_control['spell_practice']['intime']['switch_section'] = 0
                    running_control['spell_practice']['move_out'] = 40
                elif running_control['spell_practice']['intime']['section1']:
                    running_control['spell_practice']['intime']['section1'] = 0
                    running_control['spell_practice']['intime']['switch_section'] = 1
                elif running_control['spell_practice']['intime']['section2']:
                    running_control['spell_practice']['intime']['section2'] = 0
                    running_control['spell_practice']['intime']['switch_section'] = 1
                elif running_control['spell_practice']['intime']['extra']:
                    running_control['spell_practice']['intime']['extra'] = 0
                    running_control['spell_practice']['intime']['switch_section'] = 1
                elif running_control['spell_practice']['intime']['overdrive']:
                    running_control['spell_practice']['intime']['overdrive'] = 0
                    running_control['spell_practice']['intime']['switch_section'] = 1
            elif key_pressed[K_z]:
                if menu_spell.image_select[0] == 4:
                    if menu_spell.image_select[1]:
                        running_control['spell_practice']['intime']['switch_section'] = 0
                        running_control['spell_practice']['intime']['section1'] = 1
                    elif menu_spell.image_select[2]:
                        running_control['spell_practice']['intime']['switch_section'] = 0
                        running_control['spell_practice']['intime']['section2'] = 1
                    elif menu_spell.image_select[3]:
                        running_control['spell_practice']['intime']['switch_section'] = 0
                        running_control['spell_practice']['intime']['extra'] = 1
                    elif menu_spell.image_select[4]:
                        running_control['spell_practice']['intime']['switch_section'] = 0
                        running_control['spell_practice']['intime']['overdrive'] = 1   
        else:
            switch_control -= 1
        
    def menu_spell_print(self, screen):
        global running_control
        
        screen.blit(self.image_section1, self.image_section1_rect)
        screen.blit(self.image_section2, self.image_section2_rect)
        screen.blit(self.image_extra, self.image_extra_rect)
        screen.blit(self.image_overdrive, self.image_overdrive_rect)
        
        if running_control['spell_practice']['intime']['section1']:
            screen.blit(self.image_section1_stage1a, self.image_section1_stage1a_rect)
            screen.blit(self.image_section1_stage1b, self.image_section1_stage1b_rect)
            screen.blit(self.image_section1_stage2a, self.image_section1_stage2a_rect)
            screen.blit(self.image_section1_stage2b, self.image_section1_stage2b_rect)
            screen.blit(self.image_section1_stage3a, self.image_section1_stage3a_rect)
            screen.blit(self.image_section1_stage3b, self.image_section1_stage3b_rect)
            screen.blit(self.image_section1_stage4a, self.image_section1_stage4a_rect)
            screen.blit(self.image_section1_stage4b, self.image_section1_stage4b_rect)
            screen.blit(self.image_section1_stage5, self.image_section1_stage5_rect)
            screen.blit(self.image_section1_stage6, self.image_section1_stage6_rect)
            
        if running_control['spell_practice']['intime']['section2']:
            screen.blit(self.image_section2_stage1a, self.image_section2_stage1a_rect)
            screen.blit(self.image_section2_stage1b, self.image_section2_stage1b_rect)
            screen.blit(self.image_section2_stage2a, self.image_section2_stage2a_rect)
            screen.blit(self.image_section2_stage2b, self.image_section2_stage2b_rect)
            screen.blit(self.image_section2_stage3a, self.image_section2_stage3a_rect)
            screen.blit(self.image_section2_stage3b, self.image_section2_stage3b_rect)
            screen.blit(self.image_section2_stage4, self.image_section2_stage4_rect)
            screen.blit(self.image_section2_stage5, self.image_section2_stage5_rect)
            screen.blit(self.image_section2_stage6, self.image_section2_stage6_rect)
        
def menu_switch(screen):
    global switch_control
    global running_control

    menu_main = Menu_Main()
    menu_start = Menu_Start()
    menu_extra = Menu_Extra_Start()
    menu_practice = Menu_Spell_Practice()
    menu_spell = Menu_Spell_Practice()
    
    switch_control = 10

    bottom = []
    bottom.append(pygame.image.load("images/faces/bottom.png").convert())
    bottom.append(bottom[0].get_rect())
    
    running_control = {'main': \
                            {'move_in':40, 'move_out':0, 'intime':0}, \
                        'start': \
                            {'move_in':0, 'move_out':0, 'intime': \
                                                        {'switch_section':0, \
                                                         'section_to_difficulty':0, \
                                                         'switch_difficulty':0, \
                                                         'difficulty_to_ribbon':0, \
                                                         'switch_ribbon':0, \
                                                         'ribbon_to_difficulty':0 \
                                                         } \
                            }, \
                        'extra_start': \
                            {'move_in':0, 'move_out':0, 'intime': \
                                                        {'switch_difficulty':0, \
                                                         'difficulty_to_ribbon':0, \
                                                         'switch_ribbon':0, \
                                                         'ribbon_to_difficulty':0 \
                                                         } \
                            }, \
                        'practice_start': \
                            {'move_in':0, 'move_out':0, 'intime': \
                                                        {'switch_difficulty':0, \
                                                         'difficulty_to_section':0, \
                                                         'switch_section':0 \
                                                         } \
                            }, \
                        'spell_practice': \
                            {'move_in':0, 'move_out':0, 'intime': \
                                                        {'switch_section':0, \
                                                         'section1':0, \
                                                         'section2':0, \
                                                         'extra':0, \
                                                         'overdrive':0 \
                                                         } \
                            }, \
                        'play_data': \
                            {'move_in':0, 'move_out':0, 'intime':0}, \
                        'replay': \
                            {'move_in':0, 'move_out':0, 'intime':0}, \
                        'music_room': \
                            {'move_in':0, 'move_out':0, 'intime':0}, \
                        'options': \
                            {'move_in':0, 'move_out':0, 'intime':0}, \
                        'manual': \
                            {'move_in':0, 'move_out':0, 'intime':0}, \
                        'quit':0 \
                        }
    
    running = True
    clock = pygame.time.Clock()
    
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        if running_control['main']['move_in']:
            menu_main.main_menu_image_move_in()
            running_control['main']['move_in'] -= 1
            if running_control['main']['move_in'] == 20:
                running_control['main']['intime'] = 1
        elif running_control['main']['intime']:
            menu_main.main_menu_switch()
            menu_main.main_menu_move()
        elif running_control['main']['move_out']:
            menu_main.main_menu_image_move_out()
            running_control['main']['move_out'] -= 1
            if running_control['main']['move_out'] == 0:
                if menu_main.image_select[0]:
                    running_control['start']['move_in'] = 40
                elif menu_main.image_select[1]:
                    running_control['extra_start']['move_in'] = 40
                elif menu_main.image_select[2]:
                    running_control['practice_start']['move_in'] = 40
                elif menu_main.image_select[3]:
                    running_control['spell_practice']['move_in'] = 40
                    """
                elif menu_main.image_select[4]:
                    running_control['play_data']['move_in'] = 60
                elif menu_main.image_select[5]:
                    running_control['replay']['move_in'] = 60
                elif menu_main.image_select[6]:
                    running_control['music_room']['move_in'] = 60
                elif menu_main.image_select[7]:
                    running_control['options']['move_in'] = 60
                elif menu_main.image_select[8]:
                    running_control['manual']['move_in'] = 60 
                else:
                    pygame.quit()
                    sys.exit()
                    """
                else:
                    running_control['main']['move_in'] = 40
        
        elif running_control['start']['move_in']:
            menu_start.menu_start_move_in()
            running_control['start']['move_in'] -= 1
            if running_control['start']['move_in'] == 0:
                running_control['start']['intime']['switch_difficulty'] = 1
        elif running_control['start']['intime']['switch_difficulty']:
            menu_start.menu_start_switch()
            menu_start.menu_start_move()
        elif running_control['start']['intime']['difficulty_to_ribbon']:
            menu_start.menu_start_difficulty_move_out()
            running_control['start']['intime']['difficulty_to_ribbon'] -= 1
            if running_control['start']['intime']['difficulty_to_ribbon'] == 0:
                running_control['start']['intime']['switch_ribbon'] = 1
        elif running_control['start']['intime']['switch_ribbon']:
            menu_start.menu_start_switch()
        elif running_control['start']['intime']['ribbon_to_difficulty']:
            menu_start.menu_start_difficulty_move_back()
            running_control['start']['intime']['ribbon_to_difficulty'] -= 1
            if running_control['start']['intime']['ribbon_to_difficulty'] == 0:
                running_control['start']['intime']['switch_difficulty'] = 1
        elif running_control['start']['move_out']:
            menu_start.menu_start_move_out()
            running_control['start']['move_out'] -= 1
            if running_control['start']['move_out'] == 0:
                running_control['main']['move_in'] = 40
                
        elif running_control['extra_start']['move_in']:
            menu_extra.menu_extra_move_in()
            running_control['extra_start']['move_in'] -= 1
            if running_control['extra_start']['move_in'] == 0:
                running_control['extra_start']['intime']['switch_difficulty'] = 1
        elif running_control['extra_start']['intime']['switch_difficulty']:
            menu_extra.menu_extra_switch()
        elif running_control['extra_start']['intime']['difficulty_to_ribbon']:
            menu_extra.menu_extra_difficulty_move_out()
            running_control['extra_start']['intime']['difficulty_to_ribbon'] -= 1
            if running_control['extra_start']['intime']['difficulty_to_ribbon'] == 0:
                running_control['extra_start']['intime']['switch_ribbon'] = 1
        elif running_control['extra_start']['intime']['switch_ribbon']:
            menu_extra.menu_extra_switch()
        elif running_control['extra_start']['intime']['ribbon_to_difficulty']:
            menu_extra.menu_extra_difficulty_move_back()
            running_control['extra_start']['intime']['ribbon_to_difficulty'] -= 1
            if running_control['extra_start']['intime']['ribbon_to_difficulty'] == 0:
                running_control['extra_start']['intime']['switch_difficulty'] = 1
        elif running_control['extra_start']['move_out']:
            menu_extra.menu_extra_move_out()
            running_control['extra_start']['move_out'] -= 1
            if running_control['extra_start']['move_out'] == 0:
                running_control['main']['move_in'] = 40
                
        elif running_control['spell_practice']['move_in']:
            menu_spell.menu_spell_main_move_in()
            running_control['spell_practice']['move_in'] -= 1
            if running_control['spell_practice']['move_in'] == 0:
                running_control['spell_practice']['intime']['switch_section'] = 1
        elif running_control['spell_practice']['intime']['switch_section']:
            menu_spell.menu_spell_switch()
            menu_spell.menu_spell_main_move()
        elif running_control['spell_practice']['move_out']:
            menu_spell.menu_spell_main_move_out()
            running_control['spell_practice']['move_out'] -= 1
            if running_control['spell_practice']['move_out'] == 0:
                running_control['main']['move_in'] = 40
        
        elif running_control['practice_start']['move_in']:
            pass
        
        screen.blit(bottom[0], bottom[1])
        menu_main.main_menu_print(screen)
        menu_start.menu_start_print(screen)
        menu_extra.menu_extra_print(screen)
        menu_spell.menu_spell_print(screen)
            
        pygame.display.flip()
        clock.tick(60)
