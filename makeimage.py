#!/usr/bin/env python3
#coding: utf-8

from colorsys import hls_to_rgb
from PIL import Image, ImageDraw, ImageFilter

def make(info, color, path):
    print('Color :', str(color))
    im = Image.new("RGB", (420, 420), (0xf0, 0xf0, 0xf0)) # 画像作成
    draw = ImageDraw.Draw(im)
    # 描画
    for x in range(5):
        for y in range(5):
            px = 35+(x*70)
            py = 35+(y*70)
            if info[y][x]:
                draw.rectangle((px, py, px+70, py+70), fill=color)
    # 表示/保存
    # im.show()
    im.save(path, quality=95)
    print('Saved image to', path)
