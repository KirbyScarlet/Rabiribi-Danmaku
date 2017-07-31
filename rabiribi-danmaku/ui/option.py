from pygame.sprite import Sprite
from pygame.sprite import Group
from objects.action import OptionAction

class option(Sprite):
    def __init__(self, rank):
        """
        """
        self.rank = rank # small rank on top

    @classmethod
    def load_source(cls, name):
        

class option_group(Group):
    pass

class menu(option, OptionAction):
    pass

