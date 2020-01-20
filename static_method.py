class Employee:
    raise_amount = 1.04
    no_of_emp = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.no_of_emp += 1
    def full_name(self):
        return f'{self.first} {self.last}'
    def apply_raise(self):
        self.pay = (self.pay * self.raise_amount)
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    @classmethod
    def form_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

import datetime
my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))
