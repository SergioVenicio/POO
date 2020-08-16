class Employee:
    def __init__(self, first_name, last_name, wage):
        self.first_name = first_name
        self.last_name = last_name
        self.wage = wage


class CommisionedEmployee(Employee):
    units = 0

    def __init__(self, first_name, last_name, wage, commision):
        super().__init__(first_name, last_name, wage)
        self.commision = commision

    def calculate_pay(self):
        return self.wage + (self.commision * self.units)

    def add_sale(self, units):
        self.units += units

    def reset_sales(self):
        self.units = 0
