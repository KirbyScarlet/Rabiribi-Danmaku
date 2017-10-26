import pygame
import pickle

class Number(pygame.sprite.Sprite):
    """
    #
    """
    def __init__(self, size):
        super().__init__() # buff layer
        self.size = size # force square per character
        self.resize()
        self.number = 0
        '''
        self.number_size = 0
        self.surface = None
        '''
        self.type = 0 # 1 for increase and -1 for decrease
        self.change = True

    @classmethod    
    def SetImage(cls, number_type):
        file_name = 'data/tmp/imgs/' + number_type + '.tmp'
        try:
            cls.image = pygame.image.load(file_name).convert_alpha()
        except pygame.error:
            with open('data/font/number.rbrb','rb') as f_i:
                with open(file_name, 'wb') as f_o:
                    f_o.write(pickle.load(f_i)[number_type])
            cls.image = pygame.image.load(file_name).convert_alpha()
            cls.rect = cls.image.get_rect() # force square per character
    
    def resize(self):
        self.image = pygame.transform.scale(self.image, (self.rect.width*self.size/self.rect.height, self.size))

    def _chop(self, count):  # ?
        return pygame.rect.Rect((self.size*value, 0, self.size, self.size))

    def _position(self, count):
        return self.size*value, 0

    def __len__(self):
        return len(str(self.number))

    def __setattr__(self, name, value):
        if name == 'number':
            if value == self.number:
                super().__setattr__('change', False)
            else:
                super().__setattr__('change', True)
                L = len(str(value))
                if L != self.number_size:
                    super().__setattr__('number_size', L)
                    super().__setattr__('surface', pygame.surface.Surface((value*self.size, self.size)).convert())
        return super().__setattr__(name, value)

    def __call__(self, number):
        self.number = number
        if self.change:
            for i in range(self.number_size, -1, -1):
                x = self.number % (10**i)
                self.surface.blit(self.image, self._position(x), self._chop(x))
        return self.surface

class BuffTimer(Number):
    def __call__(self, number):
        return super().__call__(number//60)
BuffTimer.SetImage('number1')