'''The Abstract Factory Pattern is a creational design pattern that provides an interface for creating families of related or dependent objects without specifying their concrete classes. This pattern is particularly useful when a system needs to be independent of how its objects are created.

Here's an example to illustrate the Abstract Factory Pattern in Python. We'll create a simple application that deals with different types of shapes and colors.'''

# Example: Abstract Factory Pattern
# Define Abstract Products:

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Color(ABC):
    @abstractmethod
    def fill(self):
        pass
        
# Implement Concrete Products:


class Circle(Shape):
    def draw(self):
        print("Drawing a Circle")

class Square(Shape):
    def draw(self):
        print("Drawing a Square")

class Red(Color):
    def fill(self):
        print("Filling with Red color")

class Blue(Color):
    def fill(self):
        print("Filling with Blue color")


# Define Abstract Factory:


class AbstractFactory(ABC):
    @abstractmethod
    def create_shape(self):
        pass

    @abstractmethod
    def create_color(self):
        pass


# Implement Concrete Factories:

class ShapeFactory(AbstractFactory):
    def create_shape(self):
        return Circle()  # or return Square()

    def create_color(self):
        # ShapeFactory does not create colors, return None or raise NotImplementedError
        raise NotImplementedError("ShapeFactory does not create colors")

class ColorFactory(AbstractFactory):
    def create_shape(self):
        # ColorFactory does not create shapes, return None or raise NotImplementedError
        raise NotImplementedError("ColorFactory does not create shapes")

    def create_color(self):
        return Red()  # or return Blue()


# CREATE A FACTORY PRODUCER

class FactoryProducer:
    @staticmethod
    def get_factory(factory_type):
        if factory_type == "shape":
            return ShapeFactory()
        elif factory_type == "color":
            return ColorFactory()
        return None


# CLIENT CODE

def main():
    # Get shape factory
    shape_factory = FactoryProducer.get_factory("shape")
    
    # Create shape
    shape = shape_factory.create_shape()
    shape.draw()  # Output: Drawing a Circle
    
    # Get color factory
    color_factory = FactoryProducer.get_factory("color")
    
    # Create color
    color = color_factory.create_color()
    color.fill()  # Output: Filling with Red color

if __name__ == "__main__":
    main()

