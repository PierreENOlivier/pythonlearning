import pygame as pg
import os

BASE_IMG_PATH = '../data/images/'

"""
Load one image in pygame system
"""
def load_image(path):
    img = pg.image.load(BASE_IMG_PATH + path)
    img.set_colorkey((0, 0, 0))
    return img

"""
Load series of images
"""
def load_images(path):
    images = []
    for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
        images.append(load_image(path + '/' + img_name))
    return images

"""
Split tileset
:param intersect: (row, col) tuple of position on the tilesheet
"""
def extract_tile(path, tile_size=(16, 16), intersect=(1,1)):
    img = load_image(path)
    x_pos = 0 + (intersect[1] - 1) * tile_size[1]
    y_pos = 0 + (intersect[0] - 1) * tile_size[0]
    tile = img.subsurface(pg.Rect(x_pos,
                                  y_pos,
                                  tile_size[0],
                                  tile_size[1]))
    return tile