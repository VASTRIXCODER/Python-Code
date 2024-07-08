class P:
    def tesA(self):
        print("😂")
    def cM(self):
        print("cM function from parent class P")
    def __init__(self):
        self.p = p
        self. i = i
class Q(P):
    def tesB(self):
        print("🙂")
    def cM(self):
        print("cM function from child class Q")
    def __init__(self,q,i):
      self.q = q
        self.i = i
class R(P):
    def tesC(self):
        print("💰")
    def cM(self):
        print("cM function from child class R")
        super().cM() # Calling parent class specific overriden function from child class specific overriden function through the use of super()
    def __init__(self,r,i):
        
        self.r = r
        self.i = i
rObj = R(1,2)
rObj.tesC()
rObj.tesA()
rObj.cM()
qObj = Q(3,4)
qObj.tesB()
qObj.tesA()



'''
One parent class will have more than one child classes, or  more than one child will hae same direct parent class - Hierarchal Inheritance


One parent class will have one child that will act as a parent class for subsequent child class - Multi level Inheritance


One child class that possesses a parent class - Single Level Inheritance


Through child class object reference variable (rObj), we can access non-overriden members of parent class P, and all of R class members as well.

Super() function is used to access parent class specific overriden functions from child class specific functions. (This occurs in all inheritances!)
'''