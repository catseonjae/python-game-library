import pygame
import input_handler
import math
import tile
import color
from vector import Vector
class World:
    def __init__(self,tileset=tile.Tile(),world_size=[10000,10000],window_size=(640,640),camera=[0,0]):
        self.screen = pygame.display.set_mode(window_size)
        
        self.world_range=[[(world_size[i]/2)*(j*2-1) for j in range(2)] for i in range(2)]
        self.obj={}

        self.maps=[[tileset.base]*world_size[0] for i in range(world_size[1])]
        self.tile_size=tileset.tile_size
        self.tileset=tileset

        self.camera=camera
        self.window_size=window_size
        self.window = [[self.camera[i]+(j*2-1)*(self.window_size[i]/2) for j in range(2)] for i in range(2)]

        self.key_input_handler=input_handler.Pygame_key_input_handler()
        self.mouse_input_handler=input_handler.Pygame_mouse_input_handler()
    def display_tile(self):
        # xwindow=[self.camera[0]-self.window_size[0]/2,self.camera[0]+self.window_size[0]/2]
        # ywindow=[self.camera[1]-self.window_size[1]/2,self.camera[1]+self.window_size[1]/2]

        index=[[math.ploor(self.window[i][j]/self.tile_size) for j in range(2)] for i in range(2)]
        # xindex=[math.floor(xwindow[i]/self.tile_size) for i in range(2)]
        # yindex=[math.floor(ywindow[i]/self.tile_size) for i in range(2)]

        for i in range(index[1][0],index[1][1]+1):
            for j in range(index[0][0],index[0][1]+1):
                loc=Vector(i,j)
                loc=loc*self.tile_size
                loc=loc-Vector(self.window[0][0],self.window[1][0])
                self.screen.blit(self.tileset.tile(self.maps[i][j]), loc.elements())
    def display_object(self):
        for i in self.obj.keys():
            if self.obj[i].image_shape+self.obj[i].location in self.window:
                pos=(self.obj[i].location-Vector(self.window[0][0],self.window[1][0])).elements()
                self.screen.blit(self.obj[i].image,pos)
    def display(self):
        self.screen.fill(self.backgrond)
        self.window = [[self.camera[i]+(j*2-1)*(self.window_size[i]/2) for j in range(2)] for i in range(2)]
        self.display_tile()
        self.display_object()
        pygame.display.update()

    def input_handle():
        pass
    def add_obj(self,id,obj):
        self.obj[id]=obj
        return len(self.obj)

    def loop(self):
        self.display()
        self.key_input_handler.update()
        self.mouse_input_handler.update()
        self.key_input_handler.act()
        self.mouse_input_handler.act()

    def get_event(self,event):
        if event.type == pygame.KEYDOWN:
            self.key_input_handler.activate(event.key)
        if event.type== pygame.KEYUP:
            self.key_input_handler.leave(event.key)
        if event.type==pygame.MOUSEBUTTONDOWN:
            self.mouse_input_handler.activate(event.button)
        if event.type==pygame.MOUSEBUTTONUP:
            self.mouse_input_handler.leave(event.button)
    
    # def min(a,b):
    #     if a<b:
    #         return a
    #     return b
    # def max(a,b):
    #     if a>b:
    #         return a
    #     return b
    # def minmax_x(self,a):
    #     return min(max(self.xrange[0],a),self.xrange[1])
    # def minmax_y(self,a):
    #     return min(max(self.yrange[0],a),self.yrange[1])
