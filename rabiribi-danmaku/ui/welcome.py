import pygame
import math
import platform
import random
import sys
import os.path

from math import *
from random import *
from pygame.locals import *

class now_loading_images():
    def __init__(self):
        self.image = []
        self.rect = []

        for i in range(360):
            # Platform independent path with right justified file index
            ch = os.path.join("..", "images", "welcome", "now_loading", "now_loading_" + str(i).rjust(3, '0') + ".png")
            self.image.append(pygame.image.load(ch).convert_alpha())
            temp = self.image[i].get_rect()
            temp.top = 400
            temp.left = 350
            self.rect.append(temp)

class Wall_paper():
    def __init__(self):
        self.characters = ["Aruraune",
                           "Ashuri",
                           "Chocolate",
                           "Cicini",
                           "Cocoa",
                           "Erina",
                           "Irisu",
                           "Kotri",
                           "Lilith",
                           "Miriam",
                           "Miru",
                           "Nieve",
                           "Nixie",
                           "Noah",
                           "Pandora",
                           "Ribbon",
                           "Rita",
                           "Rumi",
                           "Saya",
                           "Seana",
                           "Syaro",
                           "Vanilla"
                           ]

        # Initialize wallpapers with list comprehension
        self.wall_paper = [
            pygame.image.load(os.path.join("..", "images", "welcome", "wallpaper", "{}.jpg".format(character))) for
            character in self.characters]

        # Each rect corresponds to the wall_paper at the same index
        self.rect = []
        for i in range(len(self.characters)):
            self.wall_paper[i] = pygame.transform.scale(self.wall_paper[i], (853, 480))
            temp = self.wall_paper[i].get_rect()
            temp.left = -213
            temp.top = 0
            self.rect.append(temp)

def opening(screen):
    time_count = 0
    running = True

    Wallpaper = Wall_paper()
    loading_image = now_loading_images()

    # Seed is generated inclusively at the endpoints
    randseed = randint(0, len(Wallpaper.characters) - 1)
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Both wall_paper and rect are accessed through index
        screen.blit(Wallpaper.wall_paper[randseed], Wallpaper.rect[randseed])
        screen.blit(loading_image.image[time_count], loading_image.rect[time_count])
        time_count += 1
        if time_count == 360:
            running = False
        pygame.display.flip()
        clock.tick(45)
