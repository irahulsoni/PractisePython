#User defined class
class computer:
    def config(self):
        print("i5","16GB ", "1TB")

comp = computer()
print(type(comp))

#always mention the object name we want the function to perform on
computer.config(comp)
#It works the same way bcs config will take comp as argument
comp.config()

a = 5
print(a.bit_length())
