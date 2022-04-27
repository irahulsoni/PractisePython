class A:

    def show(self):
        print(" in A Show")

class B(A):
    pass

a1 = A()
a1.show()
b1 = B()
b1.show()
