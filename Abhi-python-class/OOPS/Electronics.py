'''
Demonstration of the concept of Single Level Inheritance


This is demonstrated through sample program "Electronics.py"

'''

class Electronics:
    def __init__(self,e,i):
        self.e = e
        self.i = i
        
    def eI(self):
        print("eI function")
        
class SubElectronics(Electronics):
    def __init__(self,s,i):
        self.s = s
        self.i = i
    def sI(self):
        print("sI function")
        
SubElectronicsObj = SubElectronics(1,2)
SubElectronicsObj.sI()


# Calling eI function from parent class "Electronics" through child class "SubElectronics"
SubElectronicsObj.eI()

        
    