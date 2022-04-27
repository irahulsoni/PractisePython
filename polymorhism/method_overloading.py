class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    # we are assigning none so if we pass only 2 values than 3 it will not give error since it's already having a default value
    def sum(self, a = None, b = None, c = None):
        if a and b and c != None:
            s = a + b + c
        elif a and b != None:
            s = a + b
        else:
            s = a
        return s


s1 = Student(58, 64)
# s2 = Student(78, 83)

print(s1.sum(5, 8))
