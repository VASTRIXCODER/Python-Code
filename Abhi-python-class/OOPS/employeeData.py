class employeeData:
    
    def __init__(self,name, age, department, salary):
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary
    
    
    
    
    def get_employee_info(self):
        print("Name is:",self.name)
        print("Age is:",self.age)
        print("Department is:",self.department)
        print("Salary is:","$",self.salary)
        
        
    def addEmployee(self):
        self.name = input("Enter new name:")
        self.age = input("Enter new age:")
        self.department = input("Enter new department:")
        self.salary = input("Enter new salary:")
        get_employee_info().append(self.name,self.age,self.department,self.salary)
        
    def removeEmployee(self):
        self.name = input("type name you want to remove:")
        self.age = input("Enter age to remove:")
        self.department = input("Enter department to remove:")
        self.salary = input("Enter salary to remove:")
        get_employee_info().remove(self.name,self.age,self.department,self.salary)
        
employee1 = employeeData("Josh",23,"IT",200000)
employee1.get_employee_info()
employee1.removeEmployee()


dry0897@gmail.com



