class Parent:

    def __init__(self):
        print(f'parent')


class Child1(Parent):

    def __init__(self):
        super().__init__()
        print(f'Child1')

    def display(self):
        print(f'display in child1')


class Child2(Parent):

    def __init__(self):
        super().__init__()
        print(f'Child2')

    def display(self):
        print(f'display in child1')


class GrandChild(Child1, Child2):

    def __init__(self):
        super().__init__()
        print(f'GrandChild')


rama = GrandChild()
rama.display()
print(GrandChild.mro())