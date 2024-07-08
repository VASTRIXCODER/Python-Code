'''
class calculator:
    
   def addition(self):
       num1 = int(input("Enter 1st integer: "))
       num2 = int(input("Enter 2nd integer: "))
       sum = num1 + num2
       print(sum)
   def subtraction(self):
       num = int(input("enter: "))
calculator1 = calculator()

calculator1.additionSub()
#calculator1.multiplication()
'''
'''
list1 = []
while True:
    num = int(input("Enter: "))
    list1.append(num)
    
    if(num == 1):
        break
print(list1)
list2 = []
product = 1
index = 0
while index < len(list1):
    #product = list[index]*list[index+1]
    product = product * list1[index]
    #list2.append(product)
    index = index+1
list2.append(product)
print(list2)
'''


list1 = []
while True:
    num = int(input("Enter: "))
    list1.append(num)
    if(num == 1):
        break
print(list1)
list2 = []
quotient = list1[0]
index = 1
while index < len(list1):
    #product = list[index]*list[index+1]
    
    quotient = quotient / list1[index]
    
    #list2.append(product)
    index = index+1
list2.append(quotient)
print(list2)


