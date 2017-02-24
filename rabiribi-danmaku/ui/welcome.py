import pygame
import math
import platform
import random
import sys

from math import *
from random import *
from pygame.locals import *

class now_loading_images():
    def __init__(self):

        self.image = []
        self.rect = []

        if platform.system() == 'Linux':
            for i in range(10):
                ch = "images/welcome/now_loading/now_loading_00" + str(i) + ".png"
                self.image.append(pygame.image.load(ch).convert_alpha())
            for i in range(10,100):
                ch = "images/welcome/now_loading/now_loading_0" + str(i) + ".png"
                self.image.append(pygame.image.load(ch).convert_alpha())
            for i in range(100,360):
                ch = "images/welcome/now_loading/now_loading_" + str(i) + ".png"
                self.image.append(pygame.image.load(ch).convert_alpha())
        if platform.system() == 'Windows':
            for i in range(10):
                ch = "images\\welcome\\now_loading\\now_loading_00" + str(i) + ".png"
                self.image.append(pygame.image.load(ch).convert_alpha())
            for i in range(10,100):
                ch = "images\\welcome\\now_loading\\now_loading_0" + str(i) + ".png"
                self.image.append(pygame.image.load(ch).convert_alpha())
            for i in range(100,360):
                ch = "images\\welcome\\now_loading\\now_loading_" + str(i) + ".png"
                self.image.append(pygame.image.load(ch).convert_alpha())

        for i in range(360):
            temp = self.image[i].get_rect()
            temp.top = 400
            temp.left = 350
            self.rect.append(temp)

class Wall_paper():
    def __init__(self):
        if platform.system() == 'Linux':
            self.wall_paper = { \
                "Aruraune":pygame.image.load("images/welcome/wallpaper/Aruraune.jpg"), \
                "Ashuri":pygame.image.load("images/welcome/wallpaper/Ashuri.jpg"), \
                "Chocolate":pygame.image.load("images/welcome/wallpaper/Chocolate.jpg"), \
                "Cicini":pygame.image.load("images/welcome/wallpaper/Cicini.jpg"), \
                "Cocoa":pygame.image.load("images/welcome/wallpaper/Cocoa.jpg"), \
                "Erina":pygame.image.load("images/welcome/wallpaper/Erina.jpg"), \
                "Irisu":pygame.image.load("images/welcome/wallpaper/Irisu.jpg"), \
                "Kotri":pygame.image.load("images/welcome/wallpaper/Kotri.jpg"), \
                "Lilith":pygame.image.load("images/welcome/wallpaper/Lilith.jpg"), \
                "Miriam":pygame.image.load("images/welcome/wallpaper/Miriam.jpg"), \
                "Miru":pygame.image.load("images/welcome/wallpaper/Miru.jpg"), \
                "Nieve":pygame.image.load("images/welcome/wallpaper/Nieve.jpg"), \
                "Nixie":pygame.image.load("images/welcome/wallpaper/Nixie.jpg"), \
                "Noah":pygame.image.load("images/welcome/wallpaper/Noah.jpg"), \
                "Pandora":pygame.image.load("images/welcome/wallpaper/Pandora.jpg"), \
                "Ribbon":pygame.image.load("images/welcome/wallpaper/Ribbon.jpg"), \
                "Rita":pygame.image.load("images/welcome/wallpaper/Rita.jpg"), \
                "Rumi":pygame.image.load("images/welcome/wallpaper/Rumi.jpg"), \
                "Saya":pygame.image.load("images/welcome/wallpaper/Saya.jpg"), \
                "Seana":pygame.image.load("images/welcome/wallpaper/Seana.jpg"), \
                "Syaro":pygame.image.load("images/welcome/wallpaper/Syaro.jpg"), \
                "Vanilla":pygame.image.load("images/welcome/wallpaper/Vanilla.jpg") \
            }
        if platform.system() == 'Windows':
            self.wall_paper = { \
                "Aruraune":pygame.image.load("images\\welcome\\wallpaper\\Aruraune.jpg"), \
                "Ashuri":pygame.image.load("images\\welcome\\wallpaper\\Ashuri.jpg"), \
                "Chocolate":pygame.image.load("images\\welcome\\wallpaper\\Chocolate.jpg"), \
                "Cicini":pygame.image.load("images\\welcome\\wallpaper\\Cicini.jpg"), \
                "Cocoa":pygame.image.load("images\\welcome\\wallpaper\\Cocoa.jpg"), \
                "Erina":pygame.image.load("images\\welcome\\wallpaper\\Erina.jpg"), \
                "Irisu":pygame.image.load("images\\welcome\\wallpaper\\Irisu.jpg"), \
                "Kotri":pygame.image.load("images\\welcome\\wallpaper\\Kotri.jpg"), \
                "Lilith":pygame.image.load("images\\welcome\\wallpaper\\Lilith.jpg"), \
                "Miriam":pygame.image.load("images\\welcome\\wallpaper\\Miriam.jpg"), \
                "Miru":pygame.image.load("images\\welcome\\wallpaper\\Miru.jpg"), \
                "Nieve":pygame.image.load("images\\welcome\\wallpaper\\Nieve.jpg"), \
                "Nixie":pygame.image.load("images\\welcome\\wallpaper\\Nixie.jpg"), \
                "Noah":pygame.image.load("images\\welcome\\wallpaper\\Noah.jpg"), \
                "Pandora":pygame.image.load("images\\welcome\\wallpaper\\Pandora.jpg"), \
                "Ribbon":pygame.image.load("images\\welcome\\wallpaper\\Ribbon.jpg"), \
                "Rita":pygame.image.load("images\\welcome\\wallpaper\\Rita.jpg"), \
                "Rumi":pygame.image.load("images\\welcome\\wallpaper\\Rumi.jpg"), \
                "Saya":pygame.image.load("images\\welcome\\wallpaper\\Saya.jpg"), \
                "Seana":pygame.image.load("images\\welcome\\wallpaper\\Seana.jpg"), \
                "Syaro":pygame.image.load("images\\welcome\\wallpaper\\Syaro.jpg"), \
                "Vanilla":pygame.image.load("images\\welcome\\wallpaper\\Vanilla.jpg") \
            }
        self.number = {1:"Aruraune", \
                       2:"Ashuri", \
                       3:"Chocolate", \
                       4:"Cicini", \
                       5:"Cocoa", \
                       6:"Erina", \
                       7:"Irisu", \
                       8:"Kotri", \
                       9:"Lilith", \
                       10:"Miriam", \
                       11:"Miru", \
                       12:"Nieve", \
                       13:"Nixie", \
                       14:"Noah", \
                       15:"Pandora", \
                       16:"Ribbon", \
                       17:"Rita", \
                       18:"Rumi", \
                       19:"Saya", \
                       20:"Seana", \
                       21:"Syaro", \
                       22:"Vanilla" \
                       }

        for i in range(1,23):
            self.wall_paper[self.number[i]] = pygame.transform.scale(self.wall_paper[self.number[i]], (853,480))
        self.rect = []
        for i in range(1,23):
            temp = self.wall_paper[self.number[i]].get_rect()
            temp.left = -213
            temp.top = 0
            self.rect.append(temp)

def opening(screen):
    time_count = 0
    running = True

    Wallpaper = Wall_paper()
    loading_image = now_loading_images()
    randseed = randint(1,22)
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(Wallpaper.wall_paper[Wallpaper.number[randseed-1]], Wallpaper.rect[randseed])
        screen.blit(loading_image.image[time_count], loading_image.rect[time_count])
        time_count += 1
        if time_count == 360:
            running = False
        pygame.display.flip()
        clock.tick(45)
