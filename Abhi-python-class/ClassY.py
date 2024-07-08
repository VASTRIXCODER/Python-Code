class Y:
    x = 10
    def __init__(self,guy):
        self.guy = guy
        
        
    @staticmethod
    def methodWhy():
        print("Yes",self.guy)
Obj = Y(30)
Obj.methodY()