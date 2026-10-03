
class BankAcount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    

    def deposit(self, amount):
        self.balance += amount
        print("Deposit:", self.balance)

    def withdrawn(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Deposit:", self.balance)
        else:
            print("Not enough money!")
    

    def show_info(self):
        print("Owner:", self.owner)
        print("Balance:", self.balance)



user = BankAcount("Thanh", 1000)
user.deposit(100)
user.withdrawn(2000)
user.show_info()

        