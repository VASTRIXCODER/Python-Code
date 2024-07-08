#You are tasked with implementing an Employee Management System in Python.
#The system should be able to perform basic operations such as adding, displaying, removing, and updating employee information.
class EmployeeData:
    
    def __init__(self):
       
        self.emplist = []
    
    
    def get_employee_info(self):
        for employee in self.emplist:
            
           ename = employee[0]
           eage = employee[1]
           edepartment = employee[2]
           esalary = employee[3]
           #print("Name:",ename,"Age:",eage,"Department:",edepartment,"Salary:",esalary)
           print(f"Name: {ename},Age: {eage},Department: {edepartment},Salary: {esalary}")
    def addEmployee(self):
        opinion = True
        
        while(opinion == True):
            
            
            name = input("Enter new name:")
            age = int(input("Enter new age:"))
            department = input("Enter new department:")
            salary = float(input("Enter new salary:"))
            emptuple = (name,age,department,salary)
            self.emplist.append(emptuple)
            opinion = eval(input("Do you want to add one more employee?"))
            if(opinion == False):
                break
        
    def removeEmployee(self):
        self.name = input("type name you want to remove:")
        self.age = int(input("Enter age to remove:"))
        self.department = input("Enter department to remove:")
        self.salary = int(input("Enter salary to remove:"))
        emptuple = (name,age,department,salary)
        self.emplist.remove(emptuple)
        
        

empobject=EmployeeData()
empobject.addEmployee()
empobject.get_employee_info()





