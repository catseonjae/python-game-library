import pygame

class Input_handler:
    def __init__(self,inputs=[]):
        self.inputs=inputs
        self.attributes=["just_activated", "activated", "just_leaved", "leaved"]
        key_holder = {}
        for i in self.attributes:
            key_holder[i]=False

        self.key_container={}
        for i in self.inputs:
            self.key_container[i]=key_holder


        func_holder = {}
        for i in self.attributes:
            func_holder[i]=[]

        self.func_container={}
        for i in self.inputs:
            self.func_container[i]=func_holder
        

        self.activated_buffer=[]
        self.leaved_buffer=[]

    def act(self):
        for i in self.func_container.keys():
            for j in self.func_container[i].keys():
                for f in self.func_container[i][j]:
                    f()

    def set_func(self, piece, attribute, func):
        if type(func)==list:
            self.func_container[piece][attribute]=func
        else:
            self.func_container[piece][attribute]=[func]

    def append_func(self, piece, attribute, func):
        if type(func)==list:
            for f in func:
                self.func_container[piece][attribute].append(f)
        else:
            self.func_container[piece][attribute].append(func)
    def activate(self, piece):
        self.activated_buffer[piece]=True
    def leave(self, piece):
        self.leaved_buffer[piece]=True
    def update(self):
        for i in self.activated_buffer.keys():
            if self.activated_buffer[i]:
                if not self.key_container[i]["activated"]:
                    self.key_container[i]["activated"]=True
                    self.key_container[i]["just_activated"]=True
                else:
                    self.key_container[i]["just_activated"]=False
        for i in self.leaved_buffer.keys():
            if self.leaved_buffer[i]:
                if not self.key_container[i]["leaved"]:
                    self.key_container[i]["leaved"]=True
                    self.key_container[i]["just_leaved"]=True
                else:
                    self.key_container[i]["just_leaved"]=False

class Pygame_key_input_handler(Input_handler):

    def __init__(self):
        self.inputs=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        super().init(self.inputs)

    def update_pygame(self, key):
        char=""
        if key == pygame.K_a:
            char='a'     
        if key == pygame.K_b:
            char='b'     
        if key == pygame.K_c:
            char='c'     
        if key == pygame.K_d:
            char='d'     
        if key == pygame.K_e:
            char='e'     
        if key == pygame.K_f:
            char='f'     
        if key == pygame.K_g:
            char='g'     
        if key == pygame.K_h:
            char='h'     
        if key == pygame.K_i:
            char='i'     
        if key == pygame.K_j:
            char='j'     
        if key == pygame.K_k:
            char='k'     
        if key == pygame.K_l:
            char='l'     
        if key == pygame.K_m:
            char='m'     
        if key == pygame.K_n:
            char='n'     
        if key == pygame.K_o:
            char='o'     
        if key == pygame.K_p:
            char='p'     
        if key == pygame.K_q:
            char='q'     
        if key == pygame.K_r:
            char='r'
        if key == pygame.K_s:
            char='s'
        if key == pygame.K_t:
            char='t'
        if key == pygame.K_u:
            char='u'
        if key == pygame.K_v:
            char='v'
        if key == pygame.K_w:
            char='w'
        if key == pygame.K_x:
            char='x'
        if key == pygame.K_y:
            char='y'
        if key == pygame.K_z:
            char='z'
        self.activated_buffer[char]=True

    def update_pygame_up(self,key):
        char=""
        if key == pygame.K_a:
            char='a'     
        if key == pygame.K_b:
            char='b'     
        if key == pygame.K_c:
            char='c'     
        if key == pygame.K_d:
            char='d'     
        if key == pygame.K_e:
            char='e'     
        if key == pygame.K_f:
            char='f'     
        if key == pygame.K_g:
            char='g'     
        if key == pygame.K_h:
            char='h'     
        if key == pygame.K_i:
            char='i'     
        if key == pygame.K_j:
            char='j'     
        if key == pygame.K_k:
            char='k'     
        if key == pygame.K_l:
            char='l'     
        if key == pygame.K_m:
            char='m'     
        if key == pygame.K_n:
            char='n'     
        if key == pygame.K_o:
            char='o'     
        if key == pygame.K_p:
            char='p'     
        if key == pygame.K_q:
            char='q'     
        if key == pygame.K_r:
            char='r'
        if key == pygame.K_s:
            char='s'
        if key == pygame.K_t:
            char='t'
        if key == pygame.K_u:
            char='u'
        if key == pygame.K_v:
            char='v'
        if key == pygame.K_w:
            char='w'
        if key == pygame.K_x:
            char='x'
        if key == pygame.K_y:
            char='y'
        if key == pygame.K_z:
            char='z'
        self.leaved_buffer[char]=True

class Pygame_mouse_input_handler(Input_handler):
    def __init__(self):
        self.inputs=['left click','right click','whill click']
        super().init(self.inputs)
    def update_pygame(self, button):
        char=""
        if button==1:
            char='left click'
        if button==2:
            char='whill click'
        if button==3:
            char='right click'
        super().activate(char)
    def update_pygame_up(self,button):
        char=""
        if button==1:
            char='left click'
        if button==2:
            char='whill click'
        if button==3:
            char='right click'
        super().leave(char)
