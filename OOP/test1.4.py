class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        

    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposit:", self.balance)
        else:
            print("Amount must be greater than 0!")
    
    def withdraw(self, amount):

        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Withdraw:", self.balance)
        else:
            print("Invalid or not enough money")
    
    def show_info(self):
        print("Owner", self.owner)
        print("Balance", self.balance)
    


class SavingAccount(BankAccount):
    def add_interest(self):
        interest = self.balance * 0.05
        self.balance += interest
        print("Interest:", interest)
        print("After interest:", self.balance)


class CheckingAccount(BankAccount):
    def charge_fee(self):
        fee = 100
        self.balance -= fee
        print("Fee:", fee)
        print("After fee:", self.balance)


#object1
print("---User1---")
user1 = BankAccount("Thanh", 1000)
user1.deposit(100)
user1.withdraw(-200)

print("---User2---")
user2 = BankAccount("Kiet", 1000)
user2.deposit(300)
user2.withdraw(-400)

print("---Final---")
user1.show_info()
user2.show_info()