class Employee:
    
    no_of_emp = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last
        Employee.no_of_emp += 1

    @property
    def email(self):
        return f'{self.first}.{self.last}@gmail.com'

    @property
    def full_name(self):
        return f'{self.first} {self.last}'

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
   

emp1 = Employee('Al', 'Shariar')
emp2 = Employee('Shakib', 'Shuvo')

emp1.full_name ='Corey Schafer'

print(emp1.first)
print(emp1.email)
print(emp1.full_name)
