#!/usr/bin/env python3
#coding: utf-8

from hashlib import md5
from PIL import Image, ImageDraw, ImageFilter
from sys import argv
import makeimage
from colorsys import hls_to_rgb
from time import localtime

if len(argv) < 2 or argv[1][:2] == '--':
    username = input('Username : ')
else:
    username = argv[1]
print('Make user "'+username+'"\'s Identicon.')
h = md5()
h.update(username.encode())
hash = h.hexdigest()
print('Hash :', hash)
color_hash = hash[-7:]
print('Color hash :', color_hash)
hash = hash[:15]
info = list()

print(' |'+('-'*11)+'|')
for x in range(5):
    print(' | ', end='')
    info_tmp = list()
    for y in range(-2, 3):
        print(hash[abs(y)+(x*3)], end='')
        info_tmp.append(int('0x'+hash[abs(y)+(x*3)], 16)%2==0)
        if y != 2:
            print(' ', end='')
    info.append(info_tmp)
    print(' |')

print(' |'+('-'*11)+'|')
for x in range(5):
    print(' | ', end='')
    for y in range(5):
        if info[x][y]:
            print('*', end='')
        else:
            print(' ', end='')
        if y != 4:
            print(' ', end='')
    print(' |')
print(' |'+('-'*11)+'|')

color = [color_hash[:3], color_hash[3:5], color_hash[5:]] #色相, 彩度, 輝度
color[0] = int('0x'+color[0], 16) * 360 / 4095
color[1] = 65 - (int('0x'+color[1], 16) * 20 / 255)
color[2] = 75 - (int('0x'+color[2], 16) * 20 / 255)
# HSLをRGBに変換
color = hls_to_rgb(color[0], color[2], color[1])
# 数値に変換
color = list(color)
for x in range(3):
    color[x] = int(color[x])
# タプルに変換
color = tuple(color)
if '--view-only' in argv:
    print('View only, not save.')
    path = ''
elif '--path' in argv and argv.index('--path')+1 < len(argv):
    path = argv[argv.index('--path')+1]
else:
    t = localtime()
    path_hash = md5()
    path_hash.update((str(t.tm_year)+str(t.tm_mon)+str(t.tm_mday)+str(t.tm_hour)+str(t.tm_min)+str(t.tm_sec)+str(t.tm_wday)+str(t.tm_yday)+str(t.tm_isdst)).encode())
    path = username + '_identicon_'+path_hash.hexdigest()[:8]+'.png'

makeimage.make(info=info, color=color, path=path)
