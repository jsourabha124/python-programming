"""
Create a hierarchy of shape classes (e.g., Shape, Circle, Rectangle, Triangle)
where each subclass inherits attributes and methods from the base class Shape.
Implement methods to calculate the area and perimeter for each shape.
"""
import math


# create a base class : shape
class Shape:
    # create constructor
    def __init__(self, color="white"):
        self.color = color

    # methods
    def get_color(self):
        return self.color

    def area(self):
        pass

    def perimeter(self):
        pass


# subclass : circle
class Circle(Shape):
    def __init__(self, radius, color="white"):
        super(Circle, self).__init__(color)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Circle(Shape):
    def __init__(self, radius, color="white"):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# subclass : Rectangle
class Rectangle(Shape):
    def __init__(self, length, width, color="white"):
        super(Rectangle, self).__init__(color)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# subclass : Triangle

class Triangle(Shape):
    def __init__(self, side1, side2, side3, color="white"):
        super(Triangle, self).__init__(color)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


# create an object

circle = Circle(5, "red")
rectangle = Rectangle(4, 6, "blue")
triangle = Triangle(3, 4, 5, "green")

# Print information about the shapes
print(f"Circle - Color: {circle.get_color()}, Area: {circle.area()}, Perimeter: {circle.perimeter()}")
print(f"Rectangle - Color: {rectangle.get_color()}, Area: {rectangle.area()}, Perimeter: {rectangle.perimeter()}")
print(f"Triangle - Color: {triangle.get_color()}, Area: {triangle.area()}, Perimeter: {triangle.perimeter()}")

