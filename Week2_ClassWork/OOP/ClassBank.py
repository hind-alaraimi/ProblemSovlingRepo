class Bank:

    def __init__(self,owner,balance,accType,currency):
        self.owner = owner
        self.balance = balance
        self.accType = accType
        self.currency = currency

    def deposite(self,amount):
        if(amount>0):
            self.balance += amount
            return self.balance
        
        else:
            return "amount cannot be less than 0"
        
    def withdraw(self,amount):
        c=0
        if self.balance > amount:
            self.balance -= amount
            return self.balance
        else:
            return "withdrawal amount is not sufficient"

    def displayBalance(self):
        return self.owner,self.balance,self.accType,self.currency
    
cst1 = Bank("Ahmed",15000,"Savings","OMR")
cst1.deposite(20000)
cst1.withdraw(1500)

print("Name:",cst1.displayBalance()[0])
print("AccountType:",cst1.displayBalance()[2])
print("Current Balance",cst1.displayBalance()[1],cst1.displayBalance()[3])
print("Total diposites:")

        
            