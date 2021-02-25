class Employee():
    raise1 = 10

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def increment(self):
        print(f'increment is percentage {self.raise1}')  # to access class variable we should use either class name or class instance


rama = Employee('rama', 10)
rama.increment()

print(Employee.__dict__)   # class variables are displayed
print(f'===================================')
print(f'raise variable not created for instance,it uses class variable,  {rama.__dict__}')  # instance varaibles are displayed

rama.raise1 = 100  # This is applicable only for instance rama not for other instances
print(f'===================================')
print(f'raise variable created for instance with above statement {rama.__dict__}')  # instance varaibles are displayed
