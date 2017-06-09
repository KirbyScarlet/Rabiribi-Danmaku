from functions.sprites import Elf

class elf_blue_small(Elf):
    def __init__(self):
        super().__init__("elf_blue_small")
        self.SetSource("data/obj/elf/elf_blue_small.rbrb")
        self.SetValue(200,10,10)

class elf_yellow_small(Elf):
    def __init__(self):
        super().__init__("elf_yellow_small")
        self.SetSource("data/obj/elf/elf_yellow_small.rbrb")
        self.SetValue(200,10,10)

class elf_green_small(Elf):
    def __init__(self):
        super().__init__("elf_yellow_small")
        self.SetSource("data/obj/elf/elf_green_small.rbrb")
        self.SetValue(200,10,10)

class elf_red_small(Elf):
    def __init__(self):
        super().__init__("elf_red_small")
        self.SetSource("data/obj/elf/elf_red_small.rbrb")
        self.SetValue(100,10,10)