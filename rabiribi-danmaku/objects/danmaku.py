from functions.sprites import Danmaku

class mid_orange_circle(Danmaku):
    def __init__(self, emitter, images):
        super().__init__()
        self.SetImage(images['mid_orange_circle'])
        self.SetValue(7,50,4,emitter)
        self.SetLiveCheck(-20,400,-10,500)
