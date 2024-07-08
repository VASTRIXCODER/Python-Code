class Y:
    x = 10
    def __init__(self,guy):
        self.guy = guy
        
        
    @staticmethod
    def methodWhy():
        print("Satic Method why")
    
    def methodWhat(self):
        print("Yes",self.guy)



Y.methodWhy()
print(Y.x)
Obj = Y(4578)
Obj.methodWhat()
print(Obj.guy)