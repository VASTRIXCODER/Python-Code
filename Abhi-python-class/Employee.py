class Employee:
    EmployeeCount = 1
    
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        
    def EmployeeInfo(self):
        print(self.name)
        print(self.salary)
        print(Employee.EmployeeCount,"Employee")
        

Employee1 = Employee("Abhi",1000000000)

Employee1.EmployeeInfo()