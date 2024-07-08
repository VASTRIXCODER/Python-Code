class Person:
    def __init__(self,personFirstName,personMiddleName,personLastName):
        self.personFirstName = personFirstName
        self.personLastName = personLastName
        self.personMiddleName = personMiddleName
        
    def printPersonDetails(self):
        print("Person first name is:" ,self.personFirstName)
        print("Person middle name is:",self.personMiddleName)
        print("Person Last Name is:", self.personLastName)
        
class Student(Person):
    
    def __init__(self,firstName,middleName,lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.middleName = middleName
        
     
        
    def printStudentDetails(self):
        
        print("Person first name is:" ,self.firstName)
        print("Person middle name is:",self.middleName)
        print("Person Last Name is:", self.lastName)

        super().__init__("NIGERIAN","MAN","BOY") 
        


student1 = Student("Bob","Dover","Dickinson")

student1.printStudentDetails()
student1.printPersonDetails()
print(student1.personFirstName)
print(student1.personMiddleName)
print(student1.personLastName)


    