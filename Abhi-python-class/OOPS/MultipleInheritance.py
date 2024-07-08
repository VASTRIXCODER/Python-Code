class X:
    
    def __init__(self,x,i):
        self.x = x
        self.i = i
        
    def mX(self):
        print("This is mX Function ")
    
    def cM(self):
        print("This is cM function from parent class X")
        
class Y:
    
    def __init__(self,y,i):
        self.y = y
        self.i = i
        
    def mY(self):
        print("This is mY Function ") 
    
    def cM(self):
        print("This is cM function from parent class Y")
        
class Z(Y,X):
    
    def __init__(self,z,i):
        X.__init__(self,3,4)
        Y.__init__(self,5,6)
        self.z = z
        self.i = i
        
    def mZ(self):
        print("This is mZ Function ")
        
    def cM(self):
        print("This is cM function from parent class Z")
        Y.cM(self)
        X.cM(self)

zObj = Z(1,2)
zObj.mZ()
zObj.mY()
zObj.mX()

print(zObj.z,zObj.y,zObj.x)
zObj.cM()



        
    