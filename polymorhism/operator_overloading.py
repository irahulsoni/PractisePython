# In this we are overriding the basic predefined method of python according to the output we want. Since we are working with classes, there
# are alot of methods which won't work normally, so we need to define them ourselves.
# # For ex:
# Every time when we perform any mathematical function ex: Addition, __add__ function is performed in the back automatically and hinnden
# This function takes 2 values to add but since we are using the class amd passing 2 or more values we can't perform such method'
# So we override these methods ourselves in the class and everytime we perform this method we use one in class not the one that are predefined
class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    # Since student class doesn't know + operator, so we need to loa them ourselves in the function
    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        S3 = Student(m1, m2)
        return S3

    # gt is greater than , ge is greater than equal to
    def __gt__(self, other):
        s1 = self.m1 + self.m2
        s2 = other.m1 + other. m2
        if s1 > s2:
            return True
        else:
            return False

    # To print s1 or s2 or else it will give the address of the object not values. Used format bcs without that it prints tuple
    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)


S1 = Student(56, 76)
S2 = Student(76, 93)

# To make addition work we need to load values ourself in the class method
S3 = S1 + S2

print(S3.m1)

if S1 > S2:
    print("S1 wins")
else:
    print("S2 Wins")

print(S1)

# Or you can do  the remove format but leave self.m1... in return
print(S1.__str__())
