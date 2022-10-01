class Vector:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __add__(self, v):
        return Vector(self.x+v.x, self.y+v.y)
    def __sub__(self,v):
        return Vector(self.x-v.x,self.y-v.y)
    def __mul__(self, c):
        return Vector(self.x*c,self.y*c)
    def __rmul__(self, c):
        return Vector(self.x*c,self.y*c)
    def length(self):
        return (self.x**2+self.y**2)**0.5
    def normalize(self):
        length=self.length()
        self.x/=length
        self.y/=length
    def elements(self):
        return (self.x,self.y)
