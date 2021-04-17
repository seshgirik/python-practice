
class A:

    classvar1 = 'class variable'

    def __init__(self):
        self.classvar1 = 'instance variable in class A'
        pass

class B(A):
    classvar1 = 'instance variable in class B'
    pass

a= A()
b= B()

print(b.classvar1)

class A:

    classvar1 = 'class variable'

    def __init__(self):
        self.classvar1 = 'instance variable in class A'
        self.special = ' special var'
        pass


class B:
    def __init__(self):
        self.classvar1 = 'instance variable in class B'
        # super().__init__()
        self.special = 'special'

        pass

class C(B,A):

    def __init__(self):
        B.__init__(self)
        A.__init__(self)
        # super().__init__()

        # super(A).__init__()
        # self.classvar1 = 'instance variable in class C'
        # super().__init__()

        pass
c= C()
# b= B()

print(c.classvar1)
print(c.special)

print(C.mro())
# print(B.mro())

#watch below video to understand abvoe
#https://www.youtube.com/watch?v=HfmFcj0NmHI&ab_channel=CodeWithHarry