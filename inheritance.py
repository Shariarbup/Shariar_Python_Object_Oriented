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
class Developer(Employee):
    raise_amount = 1.10
"""    The first case
output:
Before raise of Employee : 60000
After raise of Employee : 62400.0 

"""

dev1 = Employee('Al', 'Shariar',60000)
print('Before raise of Employee :',dev1.pay)
dev1.apply_raise()
print('After raise of Employee :',dev1.pay)

"""  The second case
output :
Before raise of Developer : 61000
After raise of Developer : 67100.0
"""
print('\nThe second case :\n')

dev1 = Developer('Al', 'Shariar',61000)
print('Before raise of Developer :',dev1.pay)
dev1.apply_raise()
print('After raise of Developer :',dev1.pay)
