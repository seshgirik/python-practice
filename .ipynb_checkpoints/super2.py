#
# class A:
#
#     classvar1 = 'class variable'
#
#     def __init__(self):
#         # self.classvar1 = 'instance variable in class A'
#         pass
#
# class B(A):
#     classvar1 = 'instance variable in class B'
#     pass
#
# a= A()
# b= B()
#
# print(b.classvar1)
#
class A:

    classvar1 = 'class variable'

    def __init__(self):
        self.classvar1 = 'instance variable in class A'
        self.special = ' special var'
        pass


class B(A):
    def __init__(self):
        super().__init__()
        # super(A).__init__()
        self.classvar1 = 'instance variable in class B'
        super().__init__()

        pass

a= A()
b= B()

print(b.classvar1)
print(b.special)

print(A.mro())
print(B.mro())

#watch below video to understand abvoe
#https://www.youtube.com/watch?v=HfmFcj0NmHI&ab_channel=CodeWithHarry