class BankAccount:
    def __init__(self, name , balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Insufficient balance, your account balance is {self.balance} ")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def transfer(self, to_account, amount):
        self.withdraw(amount)
        to_account.deposit(amount)


account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 600)

account1.transfer(account2, 790)
account2.withdraw(1800)




