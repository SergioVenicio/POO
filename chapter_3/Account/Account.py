class Account:
    def __init__(self, initial_deposit=0):
        self.balance = initial_deposit

    def withdrawFunds(self, amount: float) -> float:
        if amount > self.balance:
            amount = self.balance

        self.balance -= amount

        return amount

    def depositFunds(self, amount: float):
        self.balance += amount


if __name__ == "__main__":
    a = Account(250.0)
    b = Account(999.0)
    c = Account(8850.0)

    print("I have three accounts.")
    print(f"Account 1 has the prope balance of {a.balance}.")
    print(f"Account 2 has the prope balance of {b.balance}.")
    print(f"Account 3 has the prope balance of {c.balance}.")
