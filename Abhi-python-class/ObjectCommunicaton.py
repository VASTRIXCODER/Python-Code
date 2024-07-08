class P:
    def __init__(self):
        self.p = 100
    
    def methodP(self):
        print("non-static method P of class p")
class Q:
    def __init__(self):
        self.q = None
    
        
    def access_Members(self,p1):
        #q = p1.p
        self.q = p1.p
        print("variable q value:",self.q)
        
obj1 = P()
obj2 = Q()
obj2.access_Members(obj1)
        

        
        
        

        
        
        
    