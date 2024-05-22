from tkinter import *

class a():
    def __init__(self):
        print("a")

    def b(c,d):
        e = c/(d*d)
        print("tu imc"+ str(e))
    
    def f(g):
        if(g>59 and g<121):
            print("perfecto")
        else:
            print("uy ta mal")

class h():
    def __init__(self, i, c, d, g):
        self.ii = i
        self.cc = c
        self.dd = d
        self.gg = g

    def j(self):
        print("nombre:"+ self.ii)
        a.b(self.cc, self.dd)
        a.f(self.gg)


k = h("fer",20, 120, 700)
k.j()

l = h("javi", 234, 12032, 60)
l.j()
      
