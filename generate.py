# coding: utf-8
import pygame
from pygame.locals import *
pygame.init()

import arabic_reshaper as ar
import qrcode
import random


TEMPLATE_FILENAME = "t.png"
FONT_NAME = "bnazanin"
FONT_SIZE = 85
FOREGROUND_COLOR = (255,255,255) #White
QRCODE_FOREGROUND_COLOR = "white"
NAME_LT_COORDINATES = (260, 285)
CODE_LT_COORDINATES = (260, 370)
QRCODE_LT_COORDINATES = (800, 0)



#template = pygame.surface.Surface((1280,720))
template = pygame.image.load(TEMPLATE_FILENAME)


f = pygame.font.SysFont(FONT_NAME, FONT_SIZE)

inp = input()
inp = ar.reshape(inp)
inp = inp[::-1]

name = f.render(inp, True, FOREGROUND_COLOR)
c = input()
code = f.render(c, True, FOREGROUND_COLOR)
qr = qrcode.QRCode()
qr.add_data(c)
im = qr.make_image(fill_color=QRCODE_FOREGROUND_COLOR, back_color="transparent")
fname = str(random.randint(10,1000000))
fname += ".png"
im.save("/tmp/{}".format(fname))
i = pygame.image.load("/tmp/{}".format(fname))



template.blit(name, NAME_LT_COORDINATES)
template.blit(code, CODE_LT_COORDINATES)
template.blit(i, QRCODE_LT_COORDINATES)

pygame.image.save(template, fname)
print("Filename: {}".format(fname))

