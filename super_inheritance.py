

class Base:

    def __init__(self):
        print('Base class')


class Child1(Base):

    # Base().__init__()

    def __init__(self):
        super().__init__()
        print(f'child1 class')


class Child2(Base):

    def __init__(self):
        super().__init__()
        print(f'child2 class')


class GrandChild(Child1, Child2):

    def __init__(self):
        super().__init__()
        print(f'grand child ')


gchild = GrandChild()