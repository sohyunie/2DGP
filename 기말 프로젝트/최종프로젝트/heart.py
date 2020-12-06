import random
from pico2d import *
import gfw
import gobj

JELLY_BORDER = 2
JELLY_SIZE = 66
BB_RADIUS = 30

def get_heart_rect():
    ix, iy = 30, 30
    x = ix * (JELLY_BORDER + JELLY_SIZE) + JELLY_BORDER
    y = iy * (JELLY_BORDER + JELLY_SIZE) + JELLY_BORDER
    return x, y, JELLY_SIZE, JELLY_SIZE


class Heart:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.image = gfw.image.load(gobj.res('heart.png'))
        self.rect = get_heart_rect()
    def update(self): pass
    def draw(self):
        #self.image.clip_draw(*self.rect, self.x, self.y)
        self.image.draw(self.x, self.y)
    def move(self, dx):
        pass
    def get_bb(self):
        return (
            self.x - BB_RADIUS, self.y - BB_RADIUS, 
            self.x + BB_RADIUS, self.y + BB_RADIUS
        )

