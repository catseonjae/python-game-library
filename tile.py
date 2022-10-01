import pygame
from PIL import Image
class Tile:
    def __init__(self, tile_set={'black':'images/black.png'},base=None,tile_size=64):
        self.tile_size=tile_size
        self.tile_set=tile_set
        if base is None:
            for i in self.tile_set.keys():
                base=i
                break
        self.base=base
        for i in self.tile_set.keys():
            self.normalize(i)
    def add_tile(self, name,image):
        self.tile_set[name]=image
        self.normalize(name)
    def normalize(self, name):
        Image.open(self.tile_set[name]).resize((self.tile_size,self.tile_size)).save(self.tile_set[name])
    def tile(self, name):
        return pygame.image.load(self.tile_set[name])
