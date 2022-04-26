class Person:
    # Any variable outside init is called class variable
    gender = 'male'

    # Any variable inside init is called instance variable
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def config(self):
        print(self.name, self.age)

    # We can also change the value of the object like:
    # self is a pointer which is assigned to particular object who is calling it, this case self wil be assigned to person2
    def update(self):
        self.age = 34

    # This case object calling the function becomes self and other is the one we are comparing it with
    def compare(self, other):
        if self.age == other.age:
            print("same age")
        else:
            print("Different")


person1 = Person('Rahul', 27)
person2 = Person('Poonam', 31)

person1.config()
person2.config()

# We can also change the value of the object like:
person2.name = 'Arpit'

person2.config()
person2.update()

# Using compare function to compare Person1 with Person2, person1 is calling the function, so it becomes self and person2 becomes other
person1.compare(person2)

# Updating class variables
Person.gender = 'female'
