class Student:
    school = "High School"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def average(self):
        return (self.m1 + self.m2 + self.m3) / 3

    # If we are working with instance variable we need self but for class variable we don't need self as it is same for everyone
    # For using the class variable and class method we use decorator using: @classmethod,  Or else it will give an error
    # We pass random variable with the function and later assign vale of the class variable to the variable we passed
    @classmethod
    def getSchool(cls):
        return cls.school

    # Static method are used to perform any other functions in which we don't have to use particular variables.
    # to use this we need to use special decorator @staticmethod
    @staticmethod
    def info():
        print("This is an static variable")


s1 = Student(32, 45, 67)
s2 = Student(46, 63, 95)

print(s1.average())

# Since we class variable/ static variable is same for all the object we don't have to use particular object to call it, just use class name
print(Student.getSchool())

# Calling static method, no need to pass ant value
Student.info()
