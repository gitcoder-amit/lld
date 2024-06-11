import copy
from abc import ABC, abstractmethod

# Define the Prototype interface using an abstract base class
class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

# Concrete class that implements the Prototype interface
class ConcreteClass(Prototype):
    def __init__(self, name, age, attributes):
        self.name = name
        self.age = age
        self.attributes = attributes

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}, Attributes: {self.attributes}'

# Usage
original = ConcreteClass("John Doe", 30, {"hobby": "painting"})
print("Original:", original)

# Cloning the original object
clone = original.clone()
print("Clone:", clone)

# Modifying the clone to demonstrate that it is a deep copy
clone.name = "Jane Doe"
clone.attributes["hobby"] = "dancing"
print("Modified Clone:", clone)
print("Original after modifying clone:", original)
