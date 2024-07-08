# Write code to display numbers between 100 to 6000 with last digits that is triple 1. Use while AND for loop
'''
print("For loop")
count = 0
for num in range(100,6001):
    if num % 1000 == 111:
        print(num)
        count+=1
print("Total count is ",count)

print("While loop")
'''
'''
count = 0
num = 100
while num <= 6000:
    if num % 1000 == 111:
        print(num)
        count+=1
    num+=1
print("Total count is ",count)
'''
# Write code to produce below pattern using nested for loops and nested while loops
'''
1 1
1 2
1 3
1 4
1 5
hello
2 1
2 2
2 3
2 4
2 5
hello
3 1
3 2
3 3
3 4
3 5
hello
bye
'''
'''
for i in range(1,4):
    for j in range(1,6):
        print(i,j)
    print("hello")
print("bye")  
'''
'''
num = 1
while num <= 3:
    num2 = 1
    while num2 <= 5:
        print(num,num2)
        num2+=1
    print("hello")
    num+=1
print("Bye")
'''
'''
for i in range(1,4):
    j = 1
    while j <= 5:
        print(i,j)
        j+=1
    print("hello")
print("Bye")
'''
'''
i = 1
while i <= 3:
    j = 1
    for j in range(1,6):
        print(i,j)
    print("hello")
    i+=1
print("Bye")
'''
'''
*
**
***
****
*****
'''
'''
row = 1

while row <= 5:
    column = 1
    while column <= row:
        print("*",end = " ")
        column += 1
    print("\n")
    row += 1
'''


#____________________________________________________________ASSIGNMENT 3/15/2024__________________________________________________________________________________________________________________________
# Write code to print the same pattern using for loops


'''
1
1 0
1 0 1
1 0 1 0
1 0 1 0 1 using for as outer while as inner and vice versa.
'''

'''
0 1 2 3 4 5
0 1 2 3 4
0 1 2 3
0 1 2
0 1
0 using while as outer for as inner and vice versa.
'''

'''
9 8 7 6 5 4 3 2 1
9 8 7 6 5 4 3 2
9 8 7 6 5 4 3
9 8 7 6 5 4
9 8 7 6 5
9 8 7 6
9 8 7
9 8
9 using while as outer for as inner and vice versa.
'''

'''
6 6 6 6 6 6
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1 using while as outer for as inner and vice versa. 
'''
'''
row = 6
while row >=1:
    column = 1
    while column <= row:
        print(row, end=" ")
        column += 1
    print("\n")
    row -= 1
        
'''
'''

for row in range(6,0,-1):
    column = 1
    while column <= row:
        print(row, end=" ")
        column += 1
    print("\n")
'''
'''
row = 6
while row >= 1:
    for column in range(0,row):
        print(row, end=" ")
    row-=1
    print("\n")
'''
'''
for row in range(6,0,-1):
    for column in range(0,row):
        print(row, end=" ")
    row-=1
    print("\n")
'''
'''
#Write function which will take 3 integer inputs or parameters to find and return largest number
def findLargestNumber(num1,num2,num3):
    maxNumber = 0
    if (num1 > num2 and num1 > num3):
        #print(num1, " is the largest")
        maxNumber = num1
    elif (num2 > num3):
        #print(num2, " is the largest")
        maxNumber = num2
    else:
        #print(num3, " is the largest")
        maxNumber = num3
    return maxNumber

result = findLargestNumber(9,10,11)
print("the largest number is", result)
'''
'''
# Write a function that finds sum of the digits in a given integer
def sumOfDigits(num):
    numTotal = 0
    
    while num > 0:
        numTotal+=num%10
        
        num//=10
    return numTotal

number = 1000601
result = sumOfDigits(number)
print("The sum of the digits is",result)
'''
'''
#Write a function which contains logic to read integer inputs from the keyboard one by one and display the sum of all the integers until user enters 0
def a():
    sum = 0
    b = int(input("Start entering integers:"))
    while b != 0:
        sum = sum + b
        b = int(input("Start entering integers:"))
        if(b == 0):
            break
    return sum    
result = a()
print(result)
'''

'''
64 32 16 8 4 2 1

1  0  0  1 0 1 1

75-64 = 11
11 - 8 = 3
3-2 = 1
    = 1 leftover
'''

T = [[3-i for i in range(0,3)]for j in range(0,3)]
s=0
for i in range(0,3):
    s+=T[i][i]
print(s)


    
    

