class BankAccount:
    def __init__(self, amount=0):
        self.balance = amount

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount >= self.balance:
            amount = self.balance

        self.balance = (self.balance - amount)

        return amount


class SavingsAccount(BankAccount):
    def __init__(self, amount, interest_rate):
        super().__init__(amount=amount)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest


class TimedMaturityAccount(BankAccount):
    def __init__(self, amount, interest_rate, fee_rate):
        super().__init__(amount=amount)
        self.interest_rate = interest_rate
        self.fee_rate = fee_rate
        self.mature = False

    def withdraw(self, amount):
        super().withdraw(amount)

        if not self.mature:
            amount -= amount * self.fee_rate

        return amount


class CheckingAccount(BankAccount):
    def __init__(self, amount, transactions_limit, fee):
        super().__init__(amount=amount)
        self.monthly_quota = transactions_limit
        self.fee = fee
        self.transactions = 0

    def withdraw(self, amount):
        self.transactions += 1
        self.balance -= amount
        return super().withdraw(amount)

    def getFees(self):
        extra_transactions = self.transactions - self.monthly_quota

        if extra_transactions > 0:
            total_fee = extra_transactions * self.fee
            self.balance -= total_fee
            self.transactions = 0


class OverdraftAccount(BankAccount):
    def __init__(self, amount, credit_rate):
        super().__init__(amount=amount)
        self.credit_rate = credit_rate

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def charge_interest(self):
        if self.balance < 0:
            charge = self.balance * self.credit_rate
            self.balance += charge
