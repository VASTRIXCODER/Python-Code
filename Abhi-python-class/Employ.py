class Employ:
    companyName = 'Aryaka'
    
    def __init__(self,employeeMobileNumber,employeeEmail,employeeSalary,employeeId):
        print("Address of current object: ",self)
        self.employeeMobileNumber = employeeMobileNumber
        self.employeeEmail = employeeEmail
        self.employeeSalary = employeeSalary
        self.employeeId = employeeId
    def companyInformation(self):
        print(Employ.companyName)
        print(self.employeeMobileNumber)
        print(self.employeeEmail)
        print('$',self.employeeSalary)
        print(self.employeeId,"is the id number")
employ1 = Employ('123-456-7890',"Aryaka.company@gmail.com",10000,1003)
#employ1.companyInformation()
employ1.employeeMobileNumber = '132-425-9084'
employ1.employeeSalary = 40000
employ1.employeeId = 1006
employ1.companyInformation()


employ2 = Employ('234-678-1456',"Bob.Schnieder@hotmail.com",150000,2009)
employ2.employeeSalary = 500440
employ2.companyInformation()
