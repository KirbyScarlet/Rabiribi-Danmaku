from functions.sprites import Danmaku

class mid_orange_circle(Danmaku):
    def __init__(self, emitter):
        super().__init__('mid_orange_circle')
        self.SetValue(7,50,4,emitter)
        self.SetLiveCheck(-20,400,-10,500)
mid_orange_circle.load_source('mid_orange_circle')

class small_blue_circle(Danmaku):
    def __init__(self, emitter):
        super().__init__('small_blue_circle')
        self.SetValue(7,50,4,emitter)
        self.SetLiveCheck()
small_blue_circle.load_source('small_blue_circle')