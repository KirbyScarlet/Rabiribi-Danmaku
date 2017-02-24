import pygame
import pickle
"""
pygame.init()
screen = pygame.display.set_mode((600,400))
img = pygame.image.load('Cocoa_00.rbrb').convert_alpha()
screen.blit(img,(0,0))
pygame.display.flip()
"""
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
"""
file = open("cocoa01.png", 'rb')
img = open('a.png', 'wb')
img.write(file.read())
img.close()
image = pygame.image.load('a.png').convert_alpha()
rect = image.get_rect()
screen.blit(image,rect)
"""

file = open('Cocoa.rbrb', 'wb')
img_list = {'illustration':[], 'pixel':[], 'special':[], 'music':0}
for i in range(4):
    ch = "Cocoa_illustration_0"+str(i)+".png"
    temp = open(ch, 'rb')
    img_list['illustration'].append(temp.read())
    temp.close()
for i in range(9):
    ch = 'cocoa0' + str(i+1) + '.png'
    temp = open(ch, 'rb')
    img_list['pixel'].append(temp.read())
    temp.close()
temp = open('cocoa10.png', 'rb')
img_list['pixel'].append(temp.read())
temp.close()
temp = open('Cocoa with Cocoa Bomb ~ Get On With It.ogg', 'rb')
img_list['music'] = temp.read()
temp.close()

pickle.dump(img_list, file)
file.close()

