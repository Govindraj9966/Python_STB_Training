'''
3. Task: Create a class named Bank and create methods for deposit, withdraw, getbalance. 
     Use the class to create multiple instances of bank accounts and use those methods.

'''

#step 1 : Defining class Bank
class Bank:

    #step2 : intialize the class
    def __init__(self, accountHolder, intiBalance):
        self.accountHolder=accountHolder
        self.intiBalance = intiBalance
    
    #step 3: Deposite method
    def deposit(self,amount):
        if amount > 0:
            self.intiBalance +=amount
            # print("----------")
            print(f"Deposite: {amount}")
        else:
            print("Deposit amount must be positive")
    

    #step 4: withdraw method 
    def withdraw(self,amount):
        if amount > 0:
            if amount<=self.intiBalance:
                self.intiBalance-=amount
                print(f"withdrew: {amount}")
            else:
                print("Insufficient funds")
        else:
            print("Withdraw amount must be positive.")

    
    #step 5: getBalance method 
    def getBalance(self):
        return self.intiBalance
    

    #step 6: Implement string represetation
    def __str__(self):
        # print("---------------")
        return f"Account Holder: {self.accountHolder}\nBalance: {self.intiBalance}"



#step 7: Creating instances and use the class
#Create bannk account instances 

account1 = Bank("Govind",1000)
account2 = Bank("Raj",500)


#Display initial balances 
print(account1)
print(account2)


#Perform transctions 
print("------------")
print("Depoiste made by Govind")
account1.deposit(200)
print("Withdraw made by Govind")
account1.withdraw(100)

print("------------")
print("Depoiste made by Raj")
account2.deposit(300)
print("Withdraw made by Raj")
account2.withdraw(900)

#Printing the updated values
print("----------------")
print("Updated Amount:")
print(account1)
print(account2)
