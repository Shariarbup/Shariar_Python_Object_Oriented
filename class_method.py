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

emp_str_1 = 'Al-Shariar-5000'

emp1 = Employee.form_string(emp_str_1)

print('Name of the employee :',emp1.full_name())
print("Email of the Employee :",emp1.email)
