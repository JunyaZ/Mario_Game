import os
import pyglet as pg
def load_all_gfx(directory,accept=('.png', 'jpg', 'bmp')):
    graphics = {}
    for pic in os.listdir(directory):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pg.image.load(os.path.join(directory, pic))
            graphics[name]=img
    return graphics

a= load_all_gfx(os.path.join("graphics"))
print(a)