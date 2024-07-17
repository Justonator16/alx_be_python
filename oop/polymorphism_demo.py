import math

class Shape:
    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
        self.pi = math.pi

    def area(self):
        return self.pi * (self.radius ** 2)