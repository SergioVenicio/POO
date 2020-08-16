from abc import ABCMeta, abstractmethod
from typing import List


class Employee(metaclass=ABCMeta):
    def __init__(self, first_name: str, last_name: str, wage: float):
        self.first_name = first_name
        self.last_name = last_name
        self.wage = wage

    @abstractmethod
    def calculated_pay(self):
        raise NotImplementedError()

    @abstractmethod
    def calculated_bonus(self):
        raise NotImplementedError()

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def print_pay_check(self):
        print(f"""\
            {self.full_name}
                Pay:  ${self.calculated_pay()}
                bonus: ${self.calculated_bonus()}""")


class CommisionedEmployee(Employee):
    units = 0

    def __init__(
            self, first_name: str, last_name: str,
            wage: float, commision: float):
        super().__init__(first_name, last_name, wage)
        self.commision = commision

    def calculated_pay(self):
        return self.wage + (self.commision * self.units)

    def calculated_bonus(self):
        return self.units * 100.0

    def add_sales(self, units: int):
        self.units += units

    def reset_sales(self):
        self.units = 0


class HourlyEmployee(Employee):
    hours = 0

    def calculated_pay(self):
        return self.wage + (self.wage * self.hours)

    def calculated_bonus(self):
        return 100.00

    def add_hours(self, hours: int = 1):
        self.hours += hours

    def reset_hours(self):
        self.hours = 0


class PayRoll:
    def __init__(self):
        self.total_hours = 0
        self.total_sales = 0
        self.total_pay = 0
        self.total_bonus = 0

    def payEmployees(self, employees: List[Employee]):
        for employee in employees:
            self.total_pay += employee.calculated_pay()
            self.total_bonus += employee.calculated_bonus()
            employee.print_pay_check()

    def recordEmployeeInfo(self, employee: Employee):
        if isinstance(employee, CommisionedEmployee):
            self.total_sales += employee.sales
        elif isinstance(employee, HourlyEmployee):
            self.total_hours += employee.hours
        else:
            raise ValueError('Invalid Employee!')

    def __str__(self):
        return f"""\
        Payrool Report:
            TOTAL HOURS: {self.total_hours}
            TOTAL SALES: {self.total_sales}
            TOTAL BONUS: {self.total_bonus}
            TOTAL PAID: ${self.total_pay}"""
