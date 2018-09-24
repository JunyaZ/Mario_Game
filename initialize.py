import os
import pyglet as pg

"""
screen_width = 1280
screen_height = 720

pg.init()
screen = pg.display.set_mode((screen_width,screen_height))

BLACK = (0,0,0)
"""
def load_all_gfx(directory, colorkey=(255,0,255), accept=('.png', 'jpg', 'bmp')):
    graphics = {}
    for pic in os.listdir(directory):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pg.image.load(os.path.join(directory, pic))
            graphics[name]=img
    return graphics

GFX= load_all_gfx(os.path.abspath("graphics"))