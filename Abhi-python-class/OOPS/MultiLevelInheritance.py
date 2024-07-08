class A:
    def __init__(self,a,i):
        self.a = a
        self.i = i
    def mA(self):
        print("mA function from parent class A")
    def cM(self):
        print("cM function from parent class A ")
    
class B(A):
    def __init__(self,b,i):
        self.b = b
        self.i = i
        super().__init__(7,8)
    def mB(self):
        print("mB function from child class B")
    def cM(self):
        print("mB function from child class B")

class C(B):
    def __init__(self,c,i):
        self.c = c
        self.i = i
        super().__init__(5,6)
    def mC(self):
        print("mC function from child class C")
    def cM(self):
        print("cM function from child class C")
    

class D(C):
    def __init__(self,d,i):
        self.d = d
        self.i = i
        super().__init__(3,4)
    def mD(self):
        #Executing parent class C specific overidden members through child class D specific instance method using super() function
        super().cM()
        print(self.i)
        print("mD function from child class D")
    def cM(self):
        print("cM function from child class D")
d1 = D(1,2)
#Executing D class specific members using D class object reference variable. :)
print(d1.i)
print(d1.d)
d1.mD()
d1.cM()
#Executing parent class C specific non-overriden members using child class D object reference variable
print(d1.c)
d1.mC()
#Executing parent class B specific non-overriden members using child class D object reference variable
print(d1.b)
d1.mB()
#Executing parent class B specific non-overriden members using child class D object reference variable
print(d1.a)
d1.mA()

