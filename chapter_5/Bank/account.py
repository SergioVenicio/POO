from abc import ABCMeta

from operator import add
from functools import reduce


class BankAccount(metaclass=ABCMeta):
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
        self.qualifying_deposits = 0

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest


class RewardsAccount(SavingsAccount):
    def __init__(self, amount, interest_rate, min_reward_balance):
        super().__init__(amount, interest_rate)
        self.min_reward_balance = min_reward_balance

    @property
    def rewards(self):
        return self.qualifying_deposits

    def deposit(self, amount):
        super().deposit(amount)

        if self.min_reward_balance <= amount:
            self.qualifying_deposits += 1

    def reset_rewards(self):
        self.qualifying_deposits = 0


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


class Bank:
    def __init__(self, accounts: dict = {}):
        self.accounts = accounts

    def add_account(self, name: str, account: BankAccount):
        if name not in self.accounts:
            self.accounts[name] = account

    def retrieve_account(self, name: str) -> dict:
        return self.accounts.get(name)

    def total_holdings(self):
        return reduce(add, [
            account.balance
            for account in self.accounts.values()
        ], 0)

    def total_accounts(self):
        return len(self.accounts.keys())

    def deposit(self, name: str, amount: float):
        try:
            self.accounts[name].deposit(amount)
        except KeyError:
            pass

    def balanceOf(self, name: str) -> float:
        try:
            return self.accounts[name].balance
        except KeyError:
            return
