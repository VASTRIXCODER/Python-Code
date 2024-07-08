"""
if(3>2):
    print("statement1")
    print("statement2")
else:
    print("statement3")
    print("statement4")

print("statement5")
"""

#write code to test a given input number is even or odd using conditional statement "if".
'''
num = int(input("enter any integer:"))

if(num%2==0):
    print(num,"is even number")
else:
     print(num,"is odd number")
'''
#Write code to test given input integer is positive, negative, or zero using conditional statements "if"
'''
num = int(input("enter any integer:"))
if(num > 0):
    print(num,"is positive")
elif(num < 0):
    print(num,"is negative")
else:
    print(num,"is zero")
    '''
#Write code to test given input number is divisible by 11 and 13
'''
num = int(input("enter any integer:"))
if(num%11==0 and num%13==0 ):
    print(num, "is divisble by 11 and 13")
else:
    print(num, "is not divisible by 11 and 13")
'''
#write code to test given input lowercase character are vowels: a, e, i, o, u, or consonant
'''
alphabet = input("enter any character between a to z:")
if(alphabet == 'a' or alphabet == 'e' or alphabet == 'i' or alphabet == 'o' or alphabet == 'u'):
    print(alphabet, "is a vowel")
else:
    print(alphabet, "is a consonant")
'''
#Write code to test a given input character is lowercase alphabet or uppercase alphabet
'''
alphabet = input("enter any character:")
if(alphabet >= 'a' and alphabet<='z'):
    print(alphabet, "is lowercase")
elif(alphabet >= 'A' and alphabet <= 'Z'):
    print(alphabet, "is uppercase")
else:
    print(alphabet, "is not a letter")
'''
#Write code to test if given input character is lowercase or uppercase alphabet or digit(0 to 9) or special character
'''
character = input("enter any character between(a - z) or (A - Z) or (0 - 9) or any special character:")
if(character >= 'a' and character<='z'):
    print(character, "is lowercase")
elif(character >= 'A' and character <= 'Z'):
    print(character, "is uppercase")
elif(character >= '0' and character<= '9'):
    print(character, "is a digit")
else:
    print(character, "is a special character")
'''
#Write code to test largest of given 2 input integers
'''

num1 = int(input("enter 1st integer:"))
num2 = int(input("enter 2nd integer:"))
if(num1 > num2):
    print(num1, "is da biggest bird")
elif(num1 < num2):
    print(num2, "is the da biggest bird")
else:
    print(num1, "and", num2, "are equal")
    
'''



#Assignment given on 2/6/2023
#due on 2/13/2023
#:Write code to find largest of given 3 numbers
'''
num1 = int(input("enter 1st integer"))
num2 = int(input("enter 2nd integer"))
num3 = int(input("enter 3rd integer"))
if(num1 > num2 and num1 > num3):
    print(num1, "is da biggest bird")
elif(num2 > num3):
    print(num2," is da biggest bird")
else:
    print(num3,"is da biggest bird")
'''        

#:Write code to find largest of given 4 numbers
'''
num1 = int(input("enter 1st integer"))
num2 = int(input("enter 2nd integer"))
num3 =  int(input("enter 3rd integer"))
num4  = int(input("enter 4th integer"))
if(num1 > num2 and num1 > num3 and num1 > num4):
    print(num1, "is da biggest bird")
elif(num2 > num3 and num2 > num4):
    print(num2," is da biggest bird")
elif(num3 > num4):
    print(num3, "is da biggest bird")
else:
    print(num4,"is da biggest bird")
'''

#:Write code to find smallest of given 3 numbers
'''
num1 = int(input("enter 1st integer:"))
num2 = int(input("enter 2st integer:"))
num3 = int(input("enter 3rd integer:"))
if(num1 < num2 and num1 < num3):
    print(num1, "is da smallest bird")
elif(num2 < num1 and num2 < num3):
    print(num2, "is da smallest bird")
else:
    print(num3, "is da smallest bird")
'''  
#:Write code to find smallest of given 4 numbers
'''
num1 = int(input("enter 1st integer:"))
num2 = int(input("enter 2st integer:"))
num3 = int(input("enter 3rd integer:"))
num4 = int(input("enter 4th integer:"))
if(num1 < num2 and num1 < num3 and num1 < num4):
    print(num1, "is da smallest bird")
elif(num2 < num1 and num2 < num3 and num2 < num4):
    print(num2, "ia da smallest bird")
elif(num3 < num1 and num3 < num2 and num3 < num4):
    print(num3, "is da smallest bird")
else:
    print(num4, "is da smallest bird")
'''
'''
num1 = int(input("enter 1st integer:"))
num2 = int(input("enter 2st integer:"))
num3 = int(input("enter 3rd integer:"))
num4 = int(input("enter 4th integer:"))
if(num1 < num2 and num1 < num3 and num1 < num4):
    print(num1, "is da smallest bird")
elif(num2 < num3 and num2 < num4):
    print(num2, "ia da smallest bird")
elif(num3 < num4):
    print(num3, "is da smallest bird")
else:
    print(num4, "is da smallest bird")
'''
#:Write code to convert celsius temp. to farenheit temp. and vice versa for a given input temp.
'''
usertype = input("farenheit or celsius?:")
if(usertype == "farenheit"):
    num1 = int(input("enter farenheit:"))
    print((num1 - 32) * 5/9, "degrees celsius")
elif(usertype == "celsius"):
    num2 = int(input("enter celsius:"))
    print(num2 * 9/5 + 32, "degrees farenheit")
else:
    print("Invalid choice")
'''



# End of assignment due on 2/13/2023
# Finished by 2/12/2023

#Write to calculate electricity bill
#if units consumed <= 100 then cost per unit is 1.76 rupees
#if units consumed >= 101 and <= 300 then cost per unit is 3.25 rupees
#if units consumed >= 301 and <= 500 then cost per unit is 5 rupees
#if units consumed >= 501 then the cost per unit is 7.5 rupees
'''
units = int(input("enter units consumed:"))
billAmount = 0
if(units <= 100):
    billAmount = units * 1.76
elif(units >= 101 and units <= 300):
    billAmount = 176 + (units - 100) * 3.25
elif(units >= 301 and units <= 500):
    billAmount = 975 + (units - 300) * 5
elif(units >= 501):
    billAmount = 176 + 975 + (units - 500) * 7.5
else:
    print("you have inputed a negative usage count, or it is not supported with this program")
        
print(billAmount)
'''


#Assignment given on 2/20/2023
#Due on 2/27/2023
#Write code to test given three input sides will form triangle or not
#Find area if it is equilateral triangle
#Find perimeter if it is isocoles triangle
#Find area and perimeter if it is scalene triangle
'''
side1 = int(input("enter length of side 1:"))
side2 = int(input("enter length of side 2:"))
side3 = int(input("enter length of side 3:"))



if(side1 + side2 == side3 and side1 == side2 and side2 == side3):
    print("This is an equilateral triangle")
    print("the area of this triangle is ",(side1*side2)/2)
elif(side1 + side2 > side3 and side1 == side2):
    print("the measures ", side1, side2, side3, " make an isocoles triangle")
    print("the perimeter of this isocoles triangle is", side1+side2+side3)
elif(side1 + side2 > side3 and side1 != side2):
    print("the measures ",side1,side2,side3, " make a scalene triangle")
    print("the area is ",(side1*side2)/2, " and the perimeter is ",side1+side2+side3)
else:
    print("The sides you have inputed cannot form a triangle")
    
'''   
#End of assignment
    
#Write code to display week name for a given week numebr between 1-7 from the keyboard
'''
week = int(input("enter a number between 1-7 and the respective day of the week will be outputed:"))
if(week == 1):
    print("Sunday")
elif(week == 2):
    print("Monday")
elif(week == 3):
    print("Tuesday")
elif(week == 4):
    print("Wednesday")
elif(week == 5):
    print("Thursday")
elif(week == 6):
    print("Friday")
elif(week == 7):
    print("Saturday")
else:
    print("this number is not supported with the week names")
'''
#Write code to find the number of days present in a month using the corresponding year and month name
'''
year = int(input("Enter year:"))
month = int(input("Enter Month number:"))
if(year%4 == 0 and year%100 != 0 or year%400 == 0):
    print("Leap year")
    if(month == 1):
      print("January, 31 days")  
    
    elif(month == 2):
      print("February, 29 days")
    
    elif(month == 3):
      print("March, 31 days")
      
    elif(month == 4):
      print("April, 30 days")
    elif(month == 5):
      print("May, 31 days")
    
    elif(month == 6):
      print("June, 30 days")
    
    elif(month == 7):
      print("July, 31 days")
    
    elif(month == 8):
      print("August, 31 days")
    
    elif(month == 9):
      print("September, 30 days")
    
    elif(month == 10):
      print("Ocotober, 31 days")
    
    elif(month == 11):
      print("November, 30 days")
    
    elif(month == 12):
      print("December, 31 days")
    
    
elif(year%4 != 0 or year%100 == 0, year%400 != 0):
    print("Normal Year")
    if(month == 1):
      print("January, 31 days")
    
    elif(month == 2):
      print("February, 28 days")
    
    elif(month == 3):
      print("March, 31 days")
    
    elif(month == 4):
      print("April, 30 days")
    
    elif(month == 5):
      print("May, 31 days")
    
    elif(month == 6):
      print("June, 30 days")
    
    elif(month == 7):
      print("July, 31 days")
    
    elif(month == 8):
      print("August, 31 days")
    
    elif(month == 9):
      print("September, 30 days")
    
    elif(month == 10):
      print("Ocotober, 31 days")
    
    elif(month == 11):
      print("November, 30 days")
    
    elif(month == 12):
      print("December, 31 days")
'''
    #paste it again
    #Write code to find the number of days present in a month using the corresponding year and month name
year = int(input("Enter year:"))
month = int(input("Enter Month number:"))
if(year%4 == 0 and year%100 != 0 or year%400 == 0):
    print("Leap year")
    if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
      print("31 days")  
    
    elif(month == 4 or month == 6 or month == 8 or month == 9 or month == 11):
      print("30 days")
    
    elif(month == 2):
      print("29 days")
    
   
    
    
elif(year%4 != 0 or year%100 == 0, year%400 != 0):
    print("Normal Year")
    if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
      print("31 days")  
    
    elif(month == 4 or month == 6 or month == 8 or month == 9 or month == 11):
      print("30 days")
    
    elif(month == 2):
      print("28 days")
    























''' 
"if" conditional statement: 
syntax:
if(condition):
    statement 1
    statement 2
else:
    statement 3
    statement 4
    
    
statement 5


'''





    