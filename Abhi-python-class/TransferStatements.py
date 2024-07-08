'''
for i in range(1,11):
    print(i)
    if(i % 3 == 0):
        break #when break executes along with remianing statements in the loop and remianing iterations will be skipped from exeecution and control goes out of the loop.
    print("hello")
print("statement outside for loop")
'''
'''
i = 1
while i <= 10:
    print(i)
    if(i%3 == 0):
        break
    print("hello")
    i = i + 1
print("statement outside for loop")
'''
'''
for i in range(1,11):
    print(i)
    if(i % 3 == 0):
       continue # when continue statement executes, remaining statements in the loop will be skipped form executions and control goes for next iteration of the loop
    print("hello")
print("statement outside for loop")
'''
'''
i = 1
while i <= 10:
    print(i)
    i = i + 1
    if(i%3 == 0):
        continue
    print("hello")
    
print("statement outside for loop")
'''

#Write code to to create a factorial using functions
'''
def factorial():
    num = int(input("Enter any number to find the factorial:"))
    factorial = 1
    while num > 0:
        factorial = factorial * num
        num = num-1
        print(factorial)

        
factorial()
'''
#Write a Python function that accepts a string and counts the number of upper and lower case letters,digits and special characters?
'''
def characterCounter(info):
    
    lowercase = 0
    uppercase = 0
    digits = 0
    special = 0
    for character in info:
        if(character >= 'a' and character <= 'z'):
            lowercase = lowercase + 1
    
        elif(character >= 'A' and character <= 'Z'):
            uppercase = uppercase + 1
   
        elif(character >= '0' and character <= '9'):
            digits = digits + 1
        else:
            special = special + 1
    print("there are",lowercase,"letters","There are",uppercase,"uppercase letters","There are",digits,"digits","and",special,"special characters")           
characterCounter('qergwe4ryerew55345DEEF')
    
    

'''
#Write code to reverse given input string
'''
def reverse():
    reversenum = 0
    num = input("Enter string:")
    while num != 0:
        lastdigit = num % 10 # lastdigit = 123 % 10 = 3
        reversenum = reversenum*10 + lastdigit # reversenum = 10*0 + 3
        num = num//10 # 123 = 123//10 = 12
reverse()
'''
#Write a Python function that checks whether a passed string is a palindrome or not?
'''
def palindrome(info):
    pal = ""
    for letter in info:
        pal = letter + pal
    if(info == pal):
        print(info,"is a palindrome")
    else:
        print(info,"is not a palindrome! L")
    
palindrome('bob')
'''
#Write a Python function to find average elements of given input list object
'''
def findAverage(list):
    sum = 0
    average = 0.0
    for element in list:
       sum = sum + element
    average = sum//len(list)
    print(average)

findAverage([1,2,3,4,45,4])
'''
#Write a Python function to find sum of even elements in the input list object
'''
def sumofevenel(list):
    sum = 0
    for element in list:
        if(element%2 == 0):
            sum = sum + element
    print(sum)
            
sumofevenel([1,2,3,4,5,6])
'''
'''
Define a function which will take one input  number between 1 to 10 as parameter
    and write logic to display  left side triangle pattern for given input number using 
   for as outer loop and while as inner loop.

if input is 5
*
* * 
* * *
* * * *
* * * * *
if input is 3
*
* *
* * *
if input is 6 
it should print 6 rows 
'''
'''
def logic():
    num = int(input("enter 5, 3 or 6:"))
    if(num == 5):
        row = 0
        while row <= 4:
            column = 0
            while column <= row:
                print("*",end = " ")
                column = column + 1
            print("\n")
            row = row + 1
    elif(num == 3):
        row = 0
        while row <= 2:
            column = 0
            while column <= row:
                print("*",end = " ")
                column = column + 1
            print("\n")
            row = row + 1
    elif(num == 6):
        row = 0
        while row <= 5:
            column = 0
            while column <= row:
                print("*",end = " ")
                column = column + 1
            print("\n")
            row = row + 1
logic()
'''
#Keyword arguements
'''
def studentInfo(studentName,studentRoleNumber,marksPercentage):
    print("Student name is:",studentName)
    print("Student role number is:",studentRoleNumber)
    print("Student marks are:",marksPercentage)
    
#studentInfo("Jeremiah",14,99.99)
studentInfo(marksPercentage = 99.99,studentRoleNumber = 14,studentName = "Jeremiah")
'''
#DefaultArguements
'''
def addNumber(x,y = 50):
    sum = 0
    sum = x + y
    print(sum)
addNumber(50)
'''

#Arbitrary Keyword arguements
'''
def studentInfo(**kwargs):
    for key,value in kwargs.items():
        print(key," : ",value)
studentInfo(name1 = "Abhi",section = "A",rollNum = 99, marks = 100.00,bob = "sdjfgwejhfb")
'''
#Variable Length Keyword arguements 
'''
'''
'''
def studentInfo(*argv):
    for arg in argv:
        print(arg)
studentInfo("Abhi","A", 99, 100.00,"sdjfgwejhfb")
studentInfo("Abhi","A", "99", "100.00","sdjfgwejhfb")
'''
'''
def addAllArguements(*abhi):
    sum = 0
    #print(type(abhi))
    for arg in abhi:
        sum = sum + arg
    print(sum)
    
addAllArguements(1,4,5)
addAllArguements(1,4,5,6)
addAllArguements(1,4,5,6,8)
'''
#--------------------------------------------------------------------------------#
#Assignment due on 6/6/2023
#Write a function to reverse a given integer input
'''
def reverse(str):  
    str1 = ""     
    for i in str:  
        str1 = i + str1  
    return str1    
     
str = "123abhi"     

print(reverse(str)) 

'''
#Write code to calculate factorial of a given number
'''

def factorial():
    num = int(input("Enter any number to find the factorial:"))
    factorial = 1
    while num > 0:
        factorial = factorial * num
        num = num-1
        print(factorial)

        
factorial()
'''
#Write a  python function to find largest element of a given list object where function takes list object as argument or parameter
#HELP
'''
def lar(list):
    for i in list:
        if(i >= len(list)):
            print(i)
    
    
    
    
lar([1,2,3,4,5,6,7,8,9,10,11])

'''
#Write a python function which will take an integer as argument/parameter and find number of even and odd numbers present in that number where number can contain more than 3 digits ?
def evenOdd(list):
    for i in list:
        if(i % 2 == 0):
            print(i, "is an even number!")
        else:
            print(i,"is an odd number!")
evenOdd([1,2,3,4,5,6,7,8,9,10])

        
    