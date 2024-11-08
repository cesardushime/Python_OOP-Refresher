class Employee():
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
    @property    
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)
    
    @property
    def fullName(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullName.setter
    def fullName(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
        
    @fullName.deleter
    def fullName(self):
        print('Deleted Name!')
        self.first = ''
        self.last = ''

emp_1 = Employee('Jackob', 'Akpra')

emp_1.fullName = 'Cesar Analyst'

del emp_1.fullName

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullName)