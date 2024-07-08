'''
logical operators ----> and ,or ,not
relational operators ---> == ,>=,<=,!= , >,<
arithmetic operators ----> ** , + , - , * ,/ ,// , %
assignment operators -----> += , -= , /= ,*= , //= ,%=
membership operators ----> in , not
identity operators -----> is , is not
'''
#Write code to test the last digit of input integer read from the keyboard is ending with 7 or not.
'''
input1 = int(input("Enter a number:"))
lastDigit = input1%10
    
if (lastDigit == 7):
    print("Last Digit of ",input1," ends with 7")
    print("Last Digit is ", lastDigit)
else :
    print("It does not end with 7")
        
'''

#Write code to test inputed character read from the keyboard is a lowercase vowel or lowercase consonents
'''
vowel = ["a","e","i","o","u"]


character = input("Entrez un lettre:")

if character in vowel:
    print(character," et un vowel")
else:
    print(character," et un consonant")
'''




'''

ascii = int(input("Enter any ascii value between 97 and 122:"))

if(chr(ascii) == "a" or chr(ascii) == "e" or chr(ascii) == "i" or chr(ascii) == "o" or chr(ascii) == "u"):
    print(chr(ascii)," et in vowel")
else:
    print(chr(ascii)," et un consonant")

'''

#Write code to test inputed ascii value read from the keyboard represents uppercase alphabet or lowercase alphabet or digit or special character.
'''
ascii = int(input("Enter any ascii value between 0 and 255:"))

if(chr(ascii) >= "a" and chr(ascii) <= "z"):
    print(chr(ascii)," Lowerase")
elif(chr(ascii) >= "A" and chr(ascii) <= "Z"):
    print(chr(ascii)," Uppercase")
elif(chr(ascii) >= "0" and chr(ascii) <= "9"):
    print(chr(ascii)," Digit")
else:
    print("Special character")
'''
#Write code Æo count and display #'s that are ending with 111 as last three digits between 100 to 6000 using for loop and while loop.

for num in range(100,6001):
    if num % 1000 == 111:
        print(num)

num = 100


print("While loop")
while num <= 6001:
    if num % 1000 == 111:
        print(num)
    num+=1


    



    
    
    
    
    
    
    
    
    
    
    
    
    
    