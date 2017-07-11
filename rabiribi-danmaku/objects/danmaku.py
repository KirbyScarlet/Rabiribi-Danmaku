from objects.sprites import Danmaku

class mid_orange_circle(Danmaku):
    def __init__(self, birth_group, birth_place, *args, **kwargs):
        super().__init__(birth_place, *args, **kwargs)
        self.SetValue(7,50,4)
        self.SetLiveCheck(-20,400,-10,500)
mid_orange_circle.load_source('mid_orange_circle')

class small_blue_circle(Danmaku):
    def __init__(self, birth_group, birth_place, *args, **kwargs):
        super().__init__(birth_group, birth_place, *args, **kwargs)
        self.SetValue(7,50,4)
        self.SetLiveCheck()
small_blue_circle.load_source('small_blue_circle')