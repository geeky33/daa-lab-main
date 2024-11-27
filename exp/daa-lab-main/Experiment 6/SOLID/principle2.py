"""
Open/Closed Principle
Definition: A class should be open for extension but closed for modification. 
"""
#bad design
class Shape:
    def area(self, shape):
        if shape == "circle":
            return 3.14 * radius * radius
        elif shape == "rectangle":
            return length * breadth


#good design
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
