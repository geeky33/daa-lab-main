"""
Liskov Substitution Principle
Definition: Objects of a superclass should be replaceable with objects of its subclasses without affecting the functionality of the program.
"""
#Bad Design:
#A Bird superclass with a fly() method that a subclass Penguin cannot implement:

class Bird:
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        return "Flying"

class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Penguins can't fly")
    
#Good Design:
#Introduce a more appropriate hierarchy:

class Bird:
    pass

class FlyingBird(Bird):
    def fly(self):
        pass

class Sparrow(FlyingBird):
    def fly(self):
        return "Flying"

class Penguin(Bird):
    def swim(self):
        return "Swimming"
