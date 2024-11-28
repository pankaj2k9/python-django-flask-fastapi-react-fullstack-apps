class Banking:
    def __init__(self, user_name, initial_balance):
        self.name= user_name
        self.balance= initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return amount

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            return amount
        else:
            return f"Insufficient Balance"

ostad = Banking("Ostad", 10000)
print(f"Account Name: {ostad.name}")
print(f"Intial Balance is: {ostad.balance}")
print(f"Deposit Balance: {ostad.deposit(1000)}")
print(f"After deposit , Your balance is: {ostad.get_balance()}")
print(f"Withdraw balance: {ostad.withdraw(2000)}")
print(f"After withdraw , Your balance is: {ostad.get_balance()}")