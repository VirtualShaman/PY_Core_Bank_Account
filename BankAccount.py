class BankAccount:
    # don't forget to add some default values for these parameters!
    bank_name = "Bank of Python"
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
            return self
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
            return self

    def display_account_info(self):
        print(f"Balance:${self.balance}, Intrest Rate:{self.int_rate}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
            return self

    @staticmethod
    def can_withdraw(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True

temp1 = BankAccount(.2,0)
temp2 = BankAccount(.2,0)

print(temp1.balance)

temp1.deposit(100).deposit(100).deposit(100).withdraw(100).yield_interest().display_account_info()

temp2.deposit(100).deposit(100).withdraw(20).withdraw(20).withdraw(20).withdraw(20).yield_interest().display_account_info()