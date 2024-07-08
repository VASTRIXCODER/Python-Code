class X:
    x = 10
    A = 345678
    def __init__(self,value):#Creating or defining constructer block
        self.value = value
    def methodY(self):
        print("non-static-method-y")
        print("non-static variable value value:",self.value)
    @staticmethod
    def methodX():
        print("staticmethodX")
        
        
#method calling place
X.methodX() #Calling static method on the name of class without using object
print(X.x)  #Calling static method on the name of class without using object
print(X.A)  #Calling static method on the name of class without using object
obj = X(1068) # Creating object to call non-static variables and non-static methods
obj.methodY() # Calling non-static method on the object

