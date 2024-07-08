'''
class Student:
    studentSectionName = 'A'
    def __init__(self, studentName, studentRoleNumber,  studentMarksPercentage):#Defining contructor block with parameters
        self.studentName = studentName
        self.studentRoleNumber = studentRoleNumber
        self.studentMarksPercentage = studentMarksPercentage
        
    def studentDetails(self):#Function to print student details from student object
        print("Student Name is: ",self.studentName)
        print("Student Role Number is: ",self.studentRoleNumber)
        print("Student Marks Percentage is: ",self.studentMarksPercentage)
        print("Student Section Name is: ",Student.studentSectionName)
        

student1 = Student("Abhinav",10,98.98)#Calling Student class constructor block by supplying arguements into parameters of the constructor block
student1.studentDetails()#Calling te=he printing function to print the values
'''

'''
class Food:
    waterDrink = "Spice level 0"
    def __init__(self,chickenBiryani,muttonBiryani,whiteRice,yogurtRice):
        self.chickenBiryani = chickenBiryani
        self.muttonBiryani = muttonBiryani
        self.whiteRice = whiteRice
        self.yogurtRice = yogurtRice
    def foodSpiceLevels(self):
        print("The levels of spice can range from 0 to 4!")
        print("Spice level for water is: ",Food.waterDrink)
        print("Spice level for Chicken Biryani is: ",self.chickenBiryani)
        print("Spice level for Mutton Biryani is: ",self.muttonBiryani)
        print("Spice level for White rice is: ",self.whiteRice)
        print("Spice level for Yogurt Rice is: ",self.yogurtRice)
food1 = Food(3,4,1,0)
food1.foodSpiceLevels()

'''


'''
class Calculator:
    #--Contructor block is optional--#
    #Define a Non-static Method which can find sum and average of 1 to 10 numbers
    #Define a non-static Method to count number that are ending with 111 between 100 to 10,000 and display them
    #Define a non-static method to count uppercase alphabets, lowercase alphabets, digits, and special characters with the help of ascii values which start from 0 to 2558
    #Define a non-static method to find sum of the digits for a given input integer and display the sum
    #Define a non-static method to display triangle pattern for a given inout number of rows
    def averageSum(self):
        range1 = range(1,11)
        for i in range1:
            average = sum(range1) / len(range1)
        print("The average is: ",average)
        print("The sum is: ",sum(range1))
    def countTripleOne(self):
        counter = 0
        range2 = range(100,10001)
        for triple in range2:
            if(triple/1000 == 111):
                counter = counter + 1
        print("There are ",counter," number between 100 to 10,000 that end with 111")
    
    def uLdS(self):
        string = "RandoMHdhDjjdfhjJdf12414124#@&#^@&"
        countU = 0
        countL = 0
        countD = 0
        countS = 0
        index = 0
        while index < len(string):
            if(string[index] >= 'a' and string[index] <= 'z'):
                countL = countL + 1
            elif(string[index] >= 'A' and string[index] <= 'z'):
                countU = countU + 1
            elif(string[index] >= '0' and string[index] <= '9'):
                countD = countD + 1
            else:
                countS = countS + 1
            index = index + 1 
        print("There are",countL, "lowercase letters")
        print("There are",countU, "uppercase letters")
        print("There are",countD, "digits")
        print("There are",countS, "special characters")
        print(string)
    def countingCharacters(self):
        countU = 0
        countL = 0
        countD = 0
        countS = 0
        asciiValue = 0
        while asciiValue <= 255:
            if(chr(asciiValue) >= "A" and chr(asciiValue) <= "Z"):
                countU = countU + 1
                
            elif(chr(asciiValue) >= "a" and chr(asciiValue) <= "z"):
                countL = countL + 1
                
            elif(chr(asciiValue) >= "0" and chr(asciiValue) <= "9"):
                countD = countD + 1
            
            else:
                countS = countS + 1
            asciiValue = asciiValue + 1
        print("There are",countL, "lowercase letters")
        print("There are",countU, "uppercase letters")
        print("There are",countD, "digits")
        print("There are",countS, "special characters")
         
                
    
    
    def sumOfDigits(self):
        num = int(input("Enter any number: "))
        lastdigit = 0
        sum = 0
        while num > 0:
            lastdigit = num%10
            sum = sum+lastdigit
            num=num//10
        print(sum)
    
    def trianglePattern(self):
        
        num = int(input("Enter the amount of rows you would like: "))
        row = 1
        while row <= num:
            column = 1
            while column <= row:
                print(row,end = " ")
                column = column + 1
            print("\n")
            row = row + 1
        
        
         
        num = int(input("Enter the amount of rows you would like: "))
        for row in range(1,num+1):
            column = 1
            for column in range(1,row+1):
                print(row,end = " ")
                column = column + 1
            print("\n")
            row = row + 1
             
        
calculator1 = Calculator()
calculator1.averageSum()
calculator1.countTripleOne()
calculator1.uLdS()
calculator1.countingCharacters()
#calculator1.sumOfDigits()
calculator1.trianglePattern()

'''
'''
class VendingMachine:
    
        
        def vendingCodes(self):
            money = 20
            
            list = ["Water","Coke","Pepsi","MTW","Sprite","DrPepper","Izzi"]
            print("These are the items available:")
            print(list)
        
            user = input("Enter what drink you need: ")
            
            
            
            
            if(user == "Water"):
                list.remove(list[0])
                print("Okay that will be $1.50")
                follow = input("type 1 to proceed: ")
                if(follow == "1"):
                    print("You have 1 Water")
                    money = money-1.5
                    user = input("Enter what drink you need: ")
        
            if(user == "Coke"):
                list.remove(list[1])
                print("Okay that will be $1.50")
                follow = input("type 2 to proceed: ")
                if(follow == '2'):
                    print("You have 1 Coke")
                    money = money-1.5
                    user = input("Enter what drink you need: ")
            if(user == "list"):
                print(list)
                user = input("Enter what drink you need: ")
            
            if(user == "money"):
                print("$",money)
                user = input("Enter what drink you need: ")
            if(user == "list"):
                print(list)
                user = input("Enter what drink you need: ")
vending1 = VendingMachine()
vending1.vendingCodes()          
'''



        
        
        
        
        
        
        
        