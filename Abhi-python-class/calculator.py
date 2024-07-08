#Create class named calculator with 4 parameterized non-static functions to perform addition, subtraction, multiplication and division operations
class calculator:
    
   def additionSub(self):
       num = int(input("Enter the number you want to add or subtract: "))
       list = [0]
       while True:
           list.append(num)
           num = int(input("Enter the number you want to add or subtract: "))
           if(num == 0):
               print(sum(list))
               break
   def multiplication(self):
       num = int(input("enter: "))
       list.append(num)
       while True:
           #x = list[]
           print(len(list)*x)
           
calculator1 = calculator()

calculator1.additionSub()
#calculator1.multiplication()


       