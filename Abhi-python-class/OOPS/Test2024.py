'''
1. Operators
2. If conditional statements
3. Loops
4. Functions
5. Classes
6. Inheritance
7. Static / Non-Static
8. 
'''

'''
# Find sum of all digits
sum = 0
num = 12345
while num > 0:
    lastDigit = num%10
    sum = sum + lastDigit
    num = num//10
print(sum)
# Find prioduct of all digits
product = 1
num = 12345
while num > 0:
    lastDigit = num%10
    product = product * lastDigit
    num = num//10
print(product)
'''
'''
# Write code to print numbers which are ending with 207 as last 3 digits between 200 - 10000
count = 0
for num in range(200,10001):
    lastThreeDigits = num%1000
    if lastThreeDigits == 207:
        print(num)
    count += 1
print(count)
'''
'''
list = []
while True:
    num = int(input("Give number and I will make the sum of all the numbers you have given until you type 0: "))
    list.append(num)
    if(num == 0):
        print(sum(list))
        break
'''
sum = 0
while True:
    num = int(input("Give number and I will make the sum of all the numbers you have given until you type 0: "))
    sum = sum + num
    if(num == 0):
        print(sum)
        break
        
    
    
    



    
