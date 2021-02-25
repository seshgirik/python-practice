

class Employee:
    def __init__(self, marks):

        self.marks = marks

    def __add__(self, other):

        return self.marks + other.marks

    def __repr__(self):
        return f'emp marks are {self.marks}'   # returning string

    # def __str__(self):
    #     return f'emp1 marks are {self.marks}'


rama = Employee(20)
sita = Employee(30)
print(rama+sita)

print(rama)
