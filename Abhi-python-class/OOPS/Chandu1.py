#fibonacci series from a series of 100 numbers

limit = int(input())
num1 = 0
num2 = 1
print("Fibonacci series")
for x in range(1,limit):
    
    if x <= 1:
        
        num3 = x
    else:
        
        num3 = num1+num2
        num1 = num2
        num2 = num3
print(num3)

    



