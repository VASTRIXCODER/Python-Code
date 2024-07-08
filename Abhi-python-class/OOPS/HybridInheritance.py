class A:
    def __init__(self,a,i):
        self.a = a
        self.i = i
    
    def aM(self):
        print("Thisis aM function")
    
class B:
    def __init__(self,b,i):
        self.b = b
        self.i = i
    
    def bM(self):
        print("Thisis bM function")

class C(A,B):
    def __init__(selfc,i):
        self.c = c
        self.i = i
    
    def cM(self):
        print("Thisis cM function")
    
class D(C):
    def __init__(self,d,i):
        self.d = d
        self.i = i
    
    def dM(self):
        print("This is dM function")
    
    
class E(C):
    def __init__(self,d,i):
        self.d = d
        self.i = i
        
    
    def eM(self):
        print("This is eM function")
        
    
    
eObj = E(1,2)

eObj.aM()