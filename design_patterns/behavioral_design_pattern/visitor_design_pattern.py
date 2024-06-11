'''
 Behavioual Design Pattern
 this allows us to add new operations  to existing classes without changing their structure
 It achieves  this by separating the operation  from the objects on which it operates
 It does double dispatch to achieve this (Double dispatch means, method which need to be invoked decided by the caller  object  and the object passed in the argument)
'''


'''
The Visitor Design Pattern is a behavioral design pattern that allows you to add further operations to objects without having to modify them. This pattern is particularly useful when you have a structure of objects with different types and you want to perform operations on these objects that depend on their types.
'''

'''
Components of the Visitor Pattern
Visitor Interface: Declares a visit method for each type of element.
Concrete Visitor: Implements the visit methods for each type of element.
Element Interface: Declares an accept method that takes a visitor object.
Concrete Elements: Implement the accept method, which calls the appropriate visit method on the visitor.
'''

# 1. Visitor Interface

from abc import ABC, abstractmethod

class ShapeVisitor(ABC):
    @abstractmethod
    def visit_circle(self, circle):
        pass

    @abstractmethod
    def visit_rectangle(self, rectangle):
        pass

# 2. Concrete Visitor

import math

class AreaCalculator(ShapeVisitor):
    def visit_circle(self, circle):
        return math.pi * (circle.radius ** 2)

    def visit_rectangle(self, rectangle):
        return rectangle.width * rectangle.height

class ShapeDrawer(ShapeVisitor):
    def visit_circle(self, circle):
        print(f"Drawing a circle with radius {circle.radius}")

    def visit_rectangle(self, rectangle):
        print(f"Drawing a rectangle with width {rectangle.width} and height {rectangle.height}")



# 3. Element Interface
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def accept(self, visitor: ShapeVisitor):
        pass

# 4. Concrete Elements
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor: ShapeVisitor):
        return visitor.visit_circle(self)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def accept(self, visitor: ShapeVisitor):
        return visitor.visit_rectangle(self)

# 5. Using the Visitor Pattern

# Create some shapes
circle = Circle(5)
rectangle = Rectangle(3, 4)

# Create visitors
area_calculator = AreaCalculator()
shape_drawer = ShapeDrawer()

# Calculate areas
circle_area = circle.accept(area_calculator)
rectangle_area = rectangle.accept(area_calculator)

print(f"Circle area: {circle_area}")
print(f"Rectangle area: {rectangle_area}")

# Draw shapes
circle.accept(shape_drawer)
rectangle.accept(shape_drawer)


# Explanation
# Visitor Interface: ShapeVisitor is an abstract class with methods for visiting each concrete element type.
# Concrete Visitor: AreaCalculator and ShapeDrawer implement the ShapeVisitor interface. They provide specific implementations for visiting Circle and Rectangle.
# Element Interface: Shape is an abstract class with an accept method that accepts a ShapeVisitor.
# Concrete Elements: Circle and Rectangle implement the Shape interface. Their accept methods call the appropriate visitor methods.
# This pattern makes it easy to add new operations to objects without changing their structure, which adheres to the Open/Closed Principle.

