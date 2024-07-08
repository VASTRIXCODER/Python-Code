#You are tasked with implementing an Employee Management System in Python.
#The system should be able to perform basic operations such as adding, displaying, removing, and updating employee information.
class WorkerData:
    
    def __init__(self):
       
        self.worklist = []
    
    
    def get_worker_info(self):
        for worker in self.worklist:
            
           wname =worker[0]
           wage = worker[1]
           wdepartment = worker[2]
           wsalary = worker[3]
           wemail=worker[4]
           #print("Name:",ename,"Age:",eage,"Department:",edepartment,"Salary:",esalary)
           print(f"Name: {wname},Age: {wage},Department: {wdepartment},Salary: {wsalary} Email: {wemail}")
    def addWorker(self):
        opinion = True
        
        while(opinion == True):
            
            
            name = input("Enter new name:")
            age = int(input("Enter new age:"))
            department = input("Enter new department:")
            salary = float(input("Enter new salary:"))
            email = input("Enter new email")
            worktuple = (name,age,department,salary,email)
            self.worklist.append(worktuple)
            opinion = eval(input("Do you want to add one more employee?"))
            if(opinion == False):
                break
        
    def removeWorker(self):
        
        
            name = input("type name you want to remove:")
            age = int(input("Enter age to remove:"))
            department = input("Enter department to remove:")
            salary = int(input("Enter salary to remove:"))
            email = input("Enter email to remove")
            worktuple = (name,age,department,salary,email)
            self.worklist.remove(worktuple)
    def searchWorker(self,email):
        for worker in self.worklist:
            if(worker[4]==email):
                name = worker[0]
                age = worker[1]
                department = worker[2]
                salary = worker[3]
                email = worker[4]
                print("Employee found with data:",name,age,department,salary,email)
            else:
                print("No employee found with such email")
        
        
    def updateWorker(self,name,age,department,salary,email):
        for worker in self.worklist:
            a = input("Enter data to update:")
            name = worker[0]
            age = worker[1]
            department = worker[2]
            salary = worker[3]
            email = worker[4]
            if(a == "name"):
                worker[0].pop()
                name = input("Enter new name:")
                worker.append(name)
        
        
empobject=WorkerData()
while(True):
    a = input("Enter function")
    if(a == "getWorkerInfo"):
        empobject.get_worker_info()
    elif(a == "addWorker"):
        empobject.addWorker()
    elif(a == "removeWorker"):
        empobject.removeWorker()
    elif(a == "searchWorker"):
        empobject.searchWorker("dry0897@gmail.com")
    elif(a == "updateWorker"):
        empobject.updateWorker()
    else:
        break










