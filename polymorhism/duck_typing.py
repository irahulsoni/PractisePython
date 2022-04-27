# if an animal is walking, quaking, behaving like a duck, no matter what animal is that, that's a Duck
class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")


class Laptop:
    def code(self, ide):
        ide.execute()


class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")


# Doesn't matter which class we are passing as long as it had the mathod execute
ide = PyCharm()

lap1 = Laptop()
lap1.code(ide)
