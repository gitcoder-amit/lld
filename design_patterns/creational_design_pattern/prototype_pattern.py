'''The Prototype pattern is a creational design pattern that allows you to create new objects by copying existing ones. This is particularly useful when the cost of creating a new instance is expensive or complex. In Python, this can be implemented using the copy module which provides the copy and deepcopy methods for this purpose.

Here is a simple example to illustrate the Prototype pattern in Python:

Step-by-Step Implementation
Define a Prototype class:
This class will have a method to clone itself.

Use the copy module:
Use copy.copy for shallow copies and copy.deepcopy for deep copies.'''


import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

# Concrete class that we want to prototype
class ConcreteClass(Prototype):
    def __init__(self, name, age, attributes):
        self.name = name
        self.age = age
        self.attributes = attributes

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}, Attributes: {self.attributes}'

# Usage
original = ConcreteClass("John Doe", 30, {"hobby": "painting"})
print("Original:", original)
print("id: ", id(original))

# Cloning the original object
clone = original.clone()
print("Clone:", clone)
print("id: ,", id(clone))

# Modifying the clone to demonstrate that it is a deep copy
clone.name = "Jane Doe"
clone.attributes["hobby"] = "dancing"
print("Modified Clone:", clone)
print("Original after modifying clone:", original)
