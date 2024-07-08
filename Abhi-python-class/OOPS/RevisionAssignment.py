'''
import math
class RevisionAssignment:
    
    def checkTheSign(self):
        sign = int(input("enter a positive, negative or 0 number: "))
        if sign < 0.0:
            print(sign,"is a negative number")
        elif sign > 0.0:
            print(sign,"is a positive number")
        else:
            print(sign,"is either 0 or a special character")
    
    def sumOfOneToInputNumber(self):
        x = 1
        y = int(input("Enter a number and I will tell you the sum of 1 to the number you give!: "))
        while x <= y:
            z = range(1,y)
            x+=1
        print(sum(z))
    def productOfOneToInputNumber(self):
        x = 1
        y = int(input("Enter a number and I will tell you the product of 1 to the number you give!: "))
        while x >= 1:
            product = math.factorial(y)
            x-=1
        print(product)
    def uniqueFunction(self):
        x = 1
        y = int(input("Enter a number and I will print all even number and number that are not divisble by 5 from 1 to the number you give!: "))
        z = range(x,y)
        for a in z:
            if a % 2 == 0:
                if a%5==0:
                    continue
                print(a)
                
    
            
            
        
RAObj = RevisionAssignment()
#RAObj.sumOfOneToInputNumber()
#RAObj.checkTheSign()
#RAObj.productOfOneToInputNumber()
RAObj.uniqueFunction()
'''
'''

# Write a class with 2 static variables 2 instance variables, 2 instance function
# and 2 static functions and call instance members and static members from instance function and from static function

class BirdCall:
    z = 1
    a = 2
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def m1(self):
        print("Instance variable x value from instance m1 function:",self.x)
        self.m2()
        print("Static variable z from instance m1 function: ",BirdCall.z)
        BirdCall.m3()
    def m2(self):
        print("Entry of m2 instance function")
        print("End of m2 instance function")
       
    @staticmethod
    def m3():
        print("Entry of m3 static function")
        print("End of m3 static function")
    @staticmethod
    def m4():
        print("Entry of m4 static function")
        print("From static m4 function calling static variable a:",BirdCall.a)
        BirdCall.m3()
        obj2 = BirdCall(1,2)
        print("instance varibale x value from static m4 function:",obj2.x)

        obj.m2()
        print("End of m4 static function")
        
        
        
        
obj = BirdCall(1,2)
obj.m1()
obj.m4()


'''
'''
class X:
    a = 1
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def m1(self):
        print("Printing m1 instance function from class X")
class Y:
    b = 2
    xObj = X(3,4) 
    def __init__(self,c,d):
        self.c = c
        self.d = d
    def m2(self):
        print("Printing m2 instance function from class Y")
        print(Y.xObj.x)
        print(Y.b)
        Y.xObj.m1()
    
    
    
    @staticmethod
    def m3():
        print("Printing function m3 static function from class Y")
        print(Y.xObj.y)
        Y.xObj.m1()
        
   
yObj = Y(5,6)
yObj.m2()
yObj.m3()
'''    


class X:
    a = 1
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def m1(self):
        print("Printing m1 instance function from class X")
class Y:
    b = 2
    
    def __init__(self,c,d,xObj):
        self.c = c
        self.d = d
        self.xObj = xObj
    def m2(self):
        print("Printing m2 instance function from class Y")
        print(self.c,self.d)
        print(self.xObj.x,self.xObj.y)
        self.xObj.m1()
      
    @staticmethod
    def m3():
        print("Printing function m3 static function from class Y")
        yObj = Y(7,8,X(900,1000))
        print(yObj.c,yObj.d)
        print(yObj.xObj.x,yObj.xObj.y)
        yObj.xObj.m1()
        
       
        
   
yObj = Y(5,6,X(100,200))
yObj.m2()
yObj.m3()


    
    
    
    
    
    












































