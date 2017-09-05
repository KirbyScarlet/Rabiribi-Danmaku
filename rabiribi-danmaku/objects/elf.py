from objects.sprites import Elf

class elf_blue_small(Elf):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.SetSource()
        self.SetValue(200,10,10)
elf_blue_small.load_source("elf_blue_small")

class elf_yellow_small(Elf):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.SetSource()
        self.SetValue(200,10,10)
elf_yellow_small.load_source("elf_yellow_small")

class elf_green_small(Elf):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.SetSource()
        self.SetValue(200,10,10)
elf_green_small.load_source("elf_green_small")

class elf_red_small(Elf):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.SetSource()
        self.SetValue(100,10,10)
elf_red_small.load_source("elf_red_small")