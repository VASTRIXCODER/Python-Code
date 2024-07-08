class BankAccount:
    bankBalance = 0
    def __init__(self,initialBalance): # Defining constructer block to create object😂 
        self.balance = initialBalance
        
    @staticmethod
    def getBankBalance():
        return BankAccount.bankBalance
    def deposit(self,amount):
        self.balance += amount # Means self.balance = self.balance + amount
        BankAccount.bankBalance += amount
    def withdraw(self,amount):
        
        if(self.balance >= amount):
            self.balance -= amount # This means self.balance = self.balance - amount
            BankAccount.bankBalance -= amount
       else:
            print("insufficient funds in your account! Please go work a job and get more money!")
            
account1 = BankAccount(100) #calling constructer block to create object 😂
account2 = BankAccount(500)
account1.deposit(200)
account2.withdraw(100)
totalBalance = BankAccount.getBankBalance()
print(totalBalance)
    