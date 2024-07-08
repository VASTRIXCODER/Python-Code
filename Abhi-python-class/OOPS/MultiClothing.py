'''
Demonstration of the concept of Multi Level Inheritance


This is demonstrated through sample program "MultiClothing.py"

'''

class Clothing:
    def __init__(self,c,i):
        self.c = c
        self.i = i
        
    def cI(self):
        print("cI function")
        
class Shirt(Clothing):
    def __init__(self,s,i):
         self.s = s
         self.i = i
    
    def sI(self):
        print("sI function")
        
class Pant(Shirt):
    def __init__(self,u,i):
        self.u = u
        self.i = i
    
    def uI(self):
        print("uI function")
        
        
PantObj = Pant(1,2)
ShirtObj = Shirt(3,4)


# Calling non-overidden functions "Shirt" class and "Clothing" class from child class "Pant"  
PantObj.uI()
PantObj.sI()
PantObj.cI()

# Calling non-overriden function from "Clothing" class from child/parent class "Shirt" 
ShirtObj.sI()
ShirtObj.cI()


    
    