# Create a class with one instance function which will take 3 integers as parameters(inputs) to test whether the last 2 digits of those 3 parameters same or not 
class Test:
    
    def comparingLast2Digits(self,input1,input2,input3):
        
        last2Digits_input1 = input1%100
        last2Digits_input2 = input2%100
        last2Digits_input3 = input3%100
        
        if (last2Digits_input1 > last2Digits_input2 and last2Digits_input1 > last2Digits_input3):
            print("The last 2 digits of ",input1,"is greater than the last 2 digits of ",input2,"and ",input3)
        elif(last2Digits_input2 > last2Digits_input3):
             print("The last 2 digits of ",input2,"is greater than the last 2 digits of ",input3,"and ",input1)
        else:
             print("The last 2 digits of ",input3,"is greater than the last 2 digits of ",input1,"and ",input2)
    # Create an instance function to produce output as 100, 95, 90, 85, 80, 75, 70, 65, 60
                
        
    
    
    
t = Test()
x = int(input("Enter any 3 or more digit number as first input:"))
y = int(input("Enter any 3 or more digit number as second input:"))
z = int(input("Enter any 3 or more digit number as third input:"))
t.comparingLast2Digits(x,y,z)



    