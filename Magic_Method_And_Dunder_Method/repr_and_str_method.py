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

emp1 = Employee('Al', 'Shariar', 50000)
#print(emp1)
print('Using __repr__() method:',repr(emp1))
print('Using __str__() method: ',str(emp1))

print('2nd rule using __repr__() method:',emp1.__repr__())
print('2nd rule using __str__() method: ',emp1.__str__())
