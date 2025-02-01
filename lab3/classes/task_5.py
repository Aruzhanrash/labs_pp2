class Bank:
    def __init__(self, account, money):
        self.money = money
        self.account = account

    def balance(self):
        return self.money
    
    def owner(self):
        return self.account
    
    def deposit(self, money):
        self.money += money
        return f"You deposited {money} money"
    
    def withdraw(self, money):
        if self.money - money < 0:
            return "Insufficient funds"
        else:
            self.money -= money
            return f"Your balance: {self.money}, and you withdrew {money}"

bank = Bank("Aruzhan", 5000)

print(bank.balance())
print(bank.owner())
print(bank.deposit(1000))
print(bank.withdraw(3000))
print(bank.withdraw(2000))
