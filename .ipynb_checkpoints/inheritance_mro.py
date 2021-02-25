# Python program showing
# how MRO works

class A:
    def rk(self):
        print(" In class A")


# class B():
class B(A):

    def rk(self):
        print(" In class B")


class C(A):
    def rk(self):
        print("In class C")

    # classes ordering


class D(B, C):
    pass


r = D()
r.rk()
print(D.mro())

# in above comment B(A) and uncomment B() and see the difference
#https://www.geeksforgeeks.org/method-resolution-order-in-python-inheritance/


#In the above Example algorithm first looks into the instance class for the invoked method.
# If not present, then it looks into the first parent, if that too is not present then-parent of
# the parent is looked into. This continues till the end of the depth of class and finally, till the end of inherited classes.
# So, the resolution order in our last example will be D, B, A, C, A. But, A cannot be twice present thus, the order will be D, B, A, C.
# But this algorithm varying in different ways and showing different behaviours at different times .So Samuele Pedroni first discovered an inconsistency and introduce C3 Linearization algorithm.
