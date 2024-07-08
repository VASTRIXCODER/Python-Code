#Write code to print numbers from 1-10 using while loop
'''
i = 1
while i <= 10:
    print(i)
    i = i+1
'''
#---------------------#
'''
While loop syntax:

Initialization

While condition:
    body statements
    increment or decrement
'''

#---------------------#

#Write code to print numbers from 10-1
'''
i=10

while i >= 1:
    print(i)
    i = i - 1
'''
#---------------------#
#Write code to count and print numbers between 1-500 which are divisble by 11 and 13
'''
i = 1
count = 0
while i<=500:
    if(i%11 == 0 and i%13 == 0):
        count = count+1
        print(i)
        
    i = i+1
    
print("There are",count,"numbers divisble by 11 and 13!")
'''
#---------------------#
#Write code to count and find sum of all numbers whose last digit is divisible by 3 between 1-100
'''
i = 0
count = 0
sum = 0
while i<=100:
    i = i+1
    if(i%3 == 0):
        sum = sum+count
        count = count + 1
        print(i)
print("There are",count,"numbers divisble by 3 between 1-100")
print("The sum of all these numbers are",sum)
'''
#-----------------------------------------------------------------------------------------------------#
#Assignment for 3/13/2023 due on 3/20/2023
#Write code to count and display whose last 2 digits are divisble by 7 between 1-500
'''
i = 0
count = 0

while i<=500:
    i = i+1
    if(i%7 == 0):
        count = count + 1
        print(i)
print("There are",count,"numbers divisble by 7 between 1-500")
'''
#Write code to display mathematical(times) table for a given input number
while True:
    while True:
        num = int(input("Enter any number to display its table:"))
        i = int(input("Enter any number to display its table:"))
        exit2 = input("Type A to exit (type anything other than A to proceed with the next number you want to multiply!)): ")
        if(exit2 == "A"):
            continue
    exit1 = input("Type A to exit (type anything other than A to proceed with the next number you want to multiply!)): ")
    if(exit1 == "A"):
        print(num*i)
        break
   

#Write code to find sum of the digits in a given number using while loop
'''
lastdigit = 0
sum = 0
num = int(input("Enter any number!:"))
while num > 0:
    lastdigit = num%10
    sum = sum+lastdigit
    num=num//10


print(sum)
'''   
#Write code to find sum of all inputs entered by the user from the keyboard until user enters 0
'''
sum = 0
num = int(input("Enter any number or zero to quit:"))
while num != 0:
    sum = sum + num
    num = int(input("Enter more numbers or zero to quit:"))
    if(num == 0):
        break
print(sum)   
'''      
#End of assignment for 3/13/2023 due on 3/20/2023 (DONE)
#-----------------------------------------------------------------------------------------------------#


#Write code to count and display numbers that are ending with 0 between 1-100
'''
count = 0
lastdigit = 0
num = 1
while num <= 100:
    lastdigit = num%10
    if(lastdigit == 0):
        print(num)
        count = count + 1 
    num = num+1
    
print("There are",count,"numbers with last digit 0!")
'''
#Write code to count and display numbers whose last 2 digits are ending with 77 between 100-1000
'''
count = 0
lastdigit = 0
num = 100
while num <= 1000:
    lastdigit = num%100
    if(lastdigit == 77):
        print(num)
        count = count + 1
    num = num + 1
print("There are",count,"numbers with last digits 77!")
'''
#Write code to count and display numbers whose last 3 digits are ending with 111 between 100-2000
'''
count = 0
lastdigit = 0
num = 100
while num <= 2000:
    lastdigit = num%1000
    if(lastdigit == 111):
        print(num)
        count = count + 1
    num = num + 1
print("There are",count,"numbers with last digits 111!")
'''
#-----------------------------------------------------------------------------------------------------#
#Start of assignment for 3/20/2023 due on 3/27/2023 (DONE)
#Write code to count the number of digits in a given input number?
'''
count = 0
lastdigit = 0
num = int(input("Enter any number:"))
while num > 0:
    lastdigit = num % 10
    num = num//10
    count = count + 1
print(count)
'''
#Write code to reverse a given input number using while and for loops ?
'''
reversenum = 0
num = int(input("Enter any number:"))
while num != 0:
    lastdigit = num % 10 # lastdigit = 123 % 10 = 3
    reversenum = reversenum*10 + lastdigit # reversenum = 10*0 + 3
    num = num//10 # 123 = 123//10 = 12
print(reversenum)
'''
#Write python code to print all numbers between 1 to 100 except multiples of  3 and 15 ?
'''
num = 1
while num <= 100:
    if(num % 3 != 0 and num % 15 != 0):
        print(num)
    num = num + 1
'''   

#Write a Python program that iterates the integers from 1 to 50. For multiples of three print "HELLO" instead of the number and for multiples of five print "BYE". For numbers that are multiples of three and five, print "GOOD BYE".
'''
num = 1
while num <= 50:
    if(num % 3 == 0):
        print("HELLO")
    if(num % 5 == 0):
        print("BYE")
    if(num % 3 == 0 and num % 5 == 0):
        print("GOODBYE")
    num = num + 1
print(num)
'''
#End of assignment for 3/20/2023 due on 3/27/2023 (NOT DONE)
#-----------------------------------------------------------------------------------------------------#
#Write code to display each character present inside a given string object
'''
name = "Abhinav"
index = 0
while index < len(name):
    print(name[index])
    index = index + 1
'''
#Write code to count and display vowels from a given string object
'''
info = "Abhinav living in USA"
index = 0
count = 0
while index < len(info):
    if(info[index] == 'A' or info[index]=='a' or info[index]=='E' or info[index]=='e' or info[index]=='I'or info[index]=='i'or info[index]=='O'or info[index]=='o'or info[index]=='U'or info[index]=='u'):
        print(info[index],"found at index:",index)
        count = count + 1
    index = index + 1
print("There are",count,"vowels")
'''
#Write code to count lowercase alphabets, uppercase alphabets, digits, and special characters
'''
string = "Trump Indicted 12123Aasdwd%^&^**"
countL = 0
countU = 0
countD = 0
countS = 0
index1 = 0
while index1 < len(string):
    if(string[index1] >= 'a' and string[index1] <= 'z'):
        countL = countL + 1
    elif(string[index1] >= 'A' and string[index1] <= 'Z'):
        countU = countU + 1
    elif(string[index1] >= '0'):
        countD = countD + 1
    else:
        countS = countS + 1
    index1 = index1 + 1
print("There are",countL, "lowercase letters")
print("There are",countU, "uppercase letters")
print("There are",countD, "digits")
print("There are",countS, "special characters")
'''
#-----------------------------------------------------------------------------------------------------#
'''
Write code to display below pattern using nested while loop

* 
* *
* * *
* * * *
* * * * *

'''
'''
row = 0
while row <= 5:
    column = 0
    while column <= row:
        print("*",end = " ")
        column = column + 1
    print("\n")
    row = row + 1
    
'''   
'''
#Write code to display below pattern
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
'''
'''

'''
#Write code to display below pattern
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''
'''
row = 1
while row <= 5:
    column = 1
    while column <= row:
        print(row,end = " ")
        column = column + 1
    print("\n")
    row = row + 1
'''
'''
#Write code to display below pattern

A
A B
A B C
A B C D
A B C D E
'''
'''
row = 65
while row <= 69:
    column = 65
    while column <= row:
        print(chr(column),end=" ")
        column = column + 1
    print("\n")
    row = row + 1
'''



#Write code to display all 256 Ascii characters for a given ascii number from 0 - 255dw

'''
ascii = 0

while ascii <= 255:
    print("ascii value ",ascii,"and its ascii character is ",chr(ascii))
    ascii = ascii + 1
'''   
    
#Assignment due on 4/10/2023
#Write code to find factorial of a given input number
'''
num = int(input("Enter any number to find the factorial:"))
factorial = 1
while num > 0:
    factorial = factorial * num
    num = num-1
    print(factorial)
'''
#Write code to find the cubes of all numbers 1 through given input number
'''
num = int(input("Enter any number:"))
i = 1
while i <= num:
    print(num**3)
    i = i + 1
'''

'''
55555
4444
333
22
1
'''
'''
row = 5
while row >= 1:
    column = 1
    while column <= row:
        print(row,end = " ")
        column = column + 1
    print("\n")
    row = row - 1
'''
'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14 
'''
'''
k = 1
row = 1
while row <= 5:
    column = 1
    while column <= row:
        print(k,end = " ")
        k = k + 1
        column = column + 1
    print("\n")
    row = row + 1
    
'''

'''
A
BC
DEF
GHIJ
KLMNO
'''
'''
k = 65
row = 65
while row <= 69:
    column = 65
    while column <= row:
        print(chr(k),end= " ")
        k = k + 1
        column = column + 1
    print("\n")
    row = row + 1

'''

#----------------------------------------------#
#Range in use
'''
for item in range(1,11):#[1,2,3,4,5,6,7,8,9,10]
    print(item)
    #When needing to print horizontally
    #print(range)
    
''' 
#List in use
'''
list = [1,2,3,4,5,6,7,8,9,10]
for item in list:
    print(item)
    
    #When needing to print horizontally
    #print(list)
'''
#Assignment start on 4/6/2023
'''
row = 5
while row >= 1:
    column = 1
    while column <= row:
        print(row,end = " ")
        column = column + 1
    print("\n")
    row = row - 1
'''

'''
row = 65
while row <= 69:
    column = 65
    while column <= row:
        print(chr(column),end = " ")
        column = column + 1
    print("\n")
    row = row + 1
'''

'''
k = 65
row = 65
while row <= 69:
    column = 65
    while column <= row:
        print(chr(k),end = " ")
        k = k + 1
        column = column + 1
    print("\n")
    row = row + 1
'''
'''
k = 1
row = 1
while row <= 5:
    column = 1
    while column <= row:
        print(k,end = " ")
        k = k + 1
        column = column + 1
    print("\n")
    row = row + 1
'''
'''
row = 5
while row >= 1:
    column = 1
    while column <= row:
        print("*",end = " ")
        column = column + 1
    print("\n")
    row = row - 1
'''





#For loops  
     
'''
A
AB
ABC
ABCD
ABCDE
'''

'''
for row in range(65,71):
    column = 65
    for row in range(column,row):
        print(chr(column),end = " ")
        column = column + 1
    print("\n")
    row = row + 1
'''
'''
A
BC
DEF
GHIJ
KLMNO
'''
'''
k = 65
for row in range(65,71):
    column = 65
    for row in range(column,row):
        print(chr(k),end = " ")
        k = k + 1
        column = column + 1
    print("\n")
    row = row + 1
'''
'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14
'''
'''
k = 1
row = 1
for row in range(0,7):
    column = 1
    for row in range(column,row):
        print(k,end = " ")
        k = k + 1
        column = column + 1
    print("\n")
    row = row + 1
'''
'''
55555
4444
333
22
1
'''
'''
row = 5
for row in range(row,0,-1):
    column = 0
    for column in range(0,row):
        print(row,end = " ")
        
    print("\n")
'''  
    
    
    

'''
*****
****
***
**
*
'''
'''
row = 5
for row in range(row,0,-1):
    column = 0
    for column in range(0,row):
        print("*",end = " ")
    print("\n")
'''
#Write code to count and display all vowels from the elements of list object
'''
count = 0
list = ["Bob","John","Jack","Spencer","Jeremiah"]
for element in list:
    for letter in element:
        if(letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'):
            print(letter)
            count = count + 1
print("There are",count,"Vowels")
'''
#Write code to display even length strings from a given list object
'''
list = ["1","12","123","1234","12345","123456","1234567"]
for element in list:
        if(len(element)%2 == 0):
            print(element)
'''
#Write code to find average elements of given list object that contains integer list elements
'''
sum = 0
average = 0
list = [9,8,2,7,3,5]
for element in list:
    sum = sum + element
average = sum/len(list)
print(average)
'''

'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14
'''
'''

k = 0
row = 1
for row in range(0,7):
    column = 1
    for row in range(column,row):
        print(k,end = " ")
        k = k + 1
        column = column + 1
    print("\n")
    row = row + 1
'''

'''
55555
4444
333
22
1
'''

row = 5
for row in range(row,0,-1):
    column = 0
    for column in range(0,row):
        print(row,end = " ")
        
    print("\n")


'''
012345
01234
0123
012
01
0
NEED HELP
'''
row = 5
for i in range(row,0,-1):
    for j in range(0,i+1):
        print(j,end = " ")
    print("\n")
