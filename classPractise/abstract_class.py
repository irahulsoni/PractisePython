# Abstract class have at least one abstract method which should be defined
# we cannot define objects using abstract class
# It is used to put restriction on the classes or subclasses that they need to have the method declared in abstract class if they want to use that class
# in python, we don't have abstract class, for that we need to import class and decorator:
from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    # every method in the abstract class has to be defined else it will never work, not even in inheritance
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("it's running")


lap1 = Laptop()

lap1.process()
