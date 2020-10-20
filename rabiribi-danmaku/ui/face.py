import pygame
import platform
from random import *

class Face(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.face_list = []
        if platform.system()=='Windows':
            self.background = pygame.image.load("images\\faces\\bottom.png")
            self.face_list.extend([\
            pygame.image.load("images\\faces\\face_00000.png").convert_alpha(), \
            pygame.image.load("images\\faces\\face_00001.png").convert_alpha(), \
            pygame.image.load("images\\faces\\face_00002.png").convert_alpha(), \
            pygame.image.load("images\\faces\\face_00003.png").convert_alpha(), \
            pygame.image.load("images\\faces\\face_00004.png").convert_alpha(), \
            pygame.image.load("images\\faces\\face_00005.png").convert_alpha(), \
            pygame.image.load("images\\faces\\face_00006.png").convert_alpha(), \
            pygame.image.load("images\\faces\\face_00007.png").convert_alpha(), \
            pygame.image.load("images\\faces\\face_00008.png").convert_alpha(), \
            pygame.image.load("images\\faces\\face_00009.png").convert_alpha(), \
            pygame.image.load("images\\faces\\face_00010.png").convert_alpha(), \
            pygame.image.load("images\\faces\\face_00011.png").convert_alpha(), \
            pygame.image.load("images\\faces\\face_00012.png").convert_alpha(), \
            pygame.image.load("images\\faces\\face_00013.png").convert_alpha(), \
            pygame.image.load("images\\faces\\face_00014.png").convert_alpha(), \
            pygame.image.load("images\\faces\\face_00015.png").convert_alpha(), \
            pygame.image.load("images\\faces\\face_00016.png").convert_alpha(), \
            pygame.image.load("images\\faces\\face_00017.png").convert_alpha(), \
            pygame.image.load("images\\faces\\face_00018.png").convert_alpha(), \
            pygame.image.load("images\\faces\\face_00019.png").convert_alpha(), \
            ])
        if platform.system()=='Linux' or platform.system()=='Darwin':
            self.background = pygame.image.load("images/faces/bottom.png")
            self.face_list.extend([\
            pygame.image.load("images/faces/face_00000.png").convert_alpha(), \
            pygame.image.load("images/faces/face_00001.png").convert_alpha(), \
            pygame.image.load("images/faces/face_00002.png").convert_alpha(), \
            pygame.image.load("images/faces/face_00003.png").convert_alpha(), \
            pygame.image.load("images/faces/face_00004.png").convert_alpha(), \
            pygame.image.load("images/faces/face_00005.png").convert_alpha(), \
            pygame.image.load("images/faces/face_00006.png").convert_alpha(), \
            pygame.image.load("images/faces/face_00007.png").convert_alpha(), \
            pygame.image.load("images/faces/face_00008.png").convert_alpha(), \
            pygame.image.load("images/faces/face_00009.png").convert_alpha(), \
            pygame.image.load("images/faces/face_00010.png").convert_alpha(), \
            pygame.image.load("images/faces/face_00011.png").convert_alpha(), \
            pygame.image.load("images/faces/face_00012.png").convert_alpha(), \
            pygame.image.load("images/faces/face_00013.png").convert_alpha(), \
            pygame.image.load("images/faces/face_00014.png").convert_alpha(), \
            pygame.image.load("images/faces/face_00015.png").convert_alpha(), \
            pygame.image.load("images/faces/face_00016.png").convert_alpha(), \
            pygame.image.load("images/faces/face_00017.png").convert_alpha(), \
            pygame.image.load("images/faces/face_00018.png").convert_alpha(), \
            pygame.image.load("images/faces/face_00019.png").convert_alpha(), \
            ])

        self.list_number = randint(0,19)
        self.face = self.face_list[self.list_number]

    def ChangeFace(self, control):
        if not control:
            self.list_number = randint(0,19)
        else:
            self.list_number = control - 1
        
        
