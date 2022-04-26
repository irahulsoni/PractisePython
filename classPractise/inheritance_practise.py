# Child class getting all the features of Parent class

class A:
    def feature1(self):
        print("This is Feature 1")

    def feature2(self):
        print("This is Feature 2")


# Class B is the child class / Sub class which wants to have all the feature os class A
# To do that we just pass the class A while creating the class
class B(A):
    def feature3(self):
        print("This is Feature 3")

    def feature4(self):
        print("This is Feature 4")

# C is now grand child and have all the methods of A & B
class C(B):
    def feature5(self):
        print("This is Feature 5")


# D is another grand child not having features of C
class D(A, B):
    def feature6(self):
        print("This is Feature 6")


a1 = A()
a1.feature1()

b1 = B()
b1.feature1()
