from objects.sprites import Danmaku

class mid_orange_circle(Danmaku): pass
mid_orange_circle.load_source('mid_orange_circle')
mid_orange_circle.SetValue(7,50,4)
mid_orange_circle.SetLiveCheck(-20,400,-10,500)

class small_blue_circle(Danmaku): pass
small_blue_circle.load_source('small_blue_circle')
small_blue_circle.SetValue(7,50,4)
small_blue_circle.SetLiveCheck()