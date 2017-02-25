import pygame
import pickle

"""
image = []
file = open('cocoa.rbrb', 'wb')
for i in range(9):
    ch = 'cocoa0' + str(i+1) + '.png'
    temp = open(ch, 'rb')
    image.append(temp.read())
    temp.close()
temp = open('cocoa10.png', 'rb')
image.append(temp.read())
temp.close()

pickle.dump(image, file)
file.close()
"""
img_group = {'birth':[], 'live':[]}
for i in range(9,0,-1):
    ch = 'cocoa_danmaku_type2_0'+str(i)+'.png'
    f = open(ch, 'rb')
    img_group['birth'].append(f.read())
    f.close()
f = open('cocoa_danmaku_type1_00.png','rb')
img_group['live'].append(f.read())
img_file = open('mid_orange_circle.rbrb','wb')
pickle.dump(img_group, img_file)
img_file.close()
