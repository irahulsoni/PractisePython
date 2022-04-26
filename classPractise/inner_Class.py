# Class inside the Class
# We use it when we know the class has no other function but only once particular reason for it, then we don't have to create a new file
# Don't forget to call the class inside the init function to declare class inside class:

class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        # Declaring the class created inside the class
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i7'
            self.ram = 32

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student('Rahul', 1)
s2 = Student('Poonam', 2)

# Using the class laptop
# Always use the name assigned inside the init method
lap1 = s1.lap
print(s1.lap.brand)

# OR

lap1 = Student.Laptop()

Student.show(s1)
