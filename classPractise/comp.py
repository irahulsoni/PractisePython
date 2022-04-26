# User defined class which is also known as the design of the object
class Computer:

    # Special method using __init__  to initiate variable, like constructor in other languages, It's called automatically
    # For every object it is called at least once, so if we have 3 objects it will work 3 times automatically
    # When __init__ is called we pass at least one value with it that's name of the object  which get assigned to the self
    # We can't have an empty class so if we want to leave an empty class use pass inside the class
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    # Instead of using the object name we just use self everytime we need to use the object which has been called
    def config(self):
        print(self.cpu, self.ram)


# so when we call the method within the class we can pass the value of the class like follows:
comp = Computer("i5", 16)
comp2 = Computer('i7', 36)
print(type(comp))

# always mention the object name we want the function to perform on
# Computer.config(comp)

# When the class is called the name of object has been assigned to self argument
# It works the same way bcs config will take comp as argument, more preferred way calling method from object
comp.config()
comp2.config()
