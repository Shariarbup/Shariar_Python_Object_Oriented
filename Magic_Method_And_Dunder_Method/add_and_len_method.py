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
    def __repr__(self):
        return f'Employee({self.first}, {self.last}, {self.pay})'
    def __str__(self):
        return f'{self.full_name()} - {self.email}'
    def __add__(self, other):
        return self.pay + other.pay
    def __len__(self):
        return len(self.full_name())

emp1 = Employee('Al', 'Shariar', 50000)
emp2 = Employee('Shakib', 'Shuvo', 60000 )
print(int.__add__(8,9))
print(str.__add__('a','b'))
print(emp1 + emp2)
print(len(emp1))
