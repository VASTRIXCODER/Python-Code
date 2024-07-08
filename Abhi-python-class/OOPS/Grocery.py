class GroceryData:
    
    def __init__(self):
       
        self.Grocerylist = []
    
    
    def get_grocery_info(self):
        for grocery in self.glist:
            
           apple =grocery[0]
           orange = grocery[1]
           broccoli = grocery[2]
           milk = grocery[3]
           egg=grocery[4]
           print(f"{gname}, {gage}, {gdepartment}, {gsalary}, {gemail} ")
    def addgrocery(self):
        opinion = True
        
        while(opinion == True):
            
            
            apple = input("Enter new apple:")
            orange = int(input("Enter new orange:"))
            broccoli = input("Enter new broccoli:")
            milk = float(input("Enter new milk:"))
            egg = input("Enter new egg")
            gtuple = (apple,orange,broccoli,milk,egg)
            self.glist.append(gtuple)
            opinion = eval(input("Do you want to add one more item?"))
            if(opinion == False):
                break
        
    def removegrocery(self):
        
        
            
            apple = input("Remove apple:")
            orange = int(input("Remove orange:"))
            broccoli = input("Remove broccoli:")
            milk = float(input("Remove milk:"))
            egg = input("Remove egg")
            gtuple = (apple,orange,broccoli,milk,egg)
            self.glist.remove(gtuple)
    '''
    def searchgrocery(self,):
        for grocery in self.worklist:
            if(grocery[4]==email):
                name = grocery[0]
                age = grocery[1]
                department = grocery[2]
                salary = grocery[3]
                email = grocery[4]
                print("Employee found with data:",name,age,department,salary,email)
            else:
                print("No employee found with such email")
        
        
    def updategrocery(self,name,age,department,salary,email):
        for grocery in self.worklist:
            a = input("Enter data to update:")
            name = grocery[0]
            age = grocery[1]
            department = grocery[2]
            salary = grocery[3]
            email = grocery[4]
            if(a == "name"):
                grocery[0].pop()
                name = input("Enter new name:")
                grocery.append(name)
        '''
        
empobject=groceryData()
while(True):
    a = input("Enter function")
    if(a == "getgroceryInfo"):
        empobject.get_grocery_info()
    elif(a == "addgrocery"):
        empobject.addgrocery()
    elif(a == "removegrocery"):
        empobject.removegrocery()
    elif(a == "searchgrocery"):
        empobject.searchgrocery("dry0897@gmail.com")
    elif(a == "updategrocery"):
        empobject.updategrocery()
    else:
        break










