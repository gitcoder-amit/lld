'''The Factory design pattern is a creational pattern that provides an interface for creating objects in a superclass but allows subclasses to alter the type of objects that will be created. This pattern is useful when you need to abstract the process of object creation, making your code more modular and easier to extend. It is used when all the object creation and its business logic we need to keep at one place

Implementation of the Factory Pattern
Define a Factory Method: This method will be responsible for creating objects.
Implement Concrete Products: These are the actual objects that will be created by the factory.
Create the Factory: This factory will use the factory method to create and return instances of the concrete products.
Here is an example in Python:

Step-by-Step Implementation
Define the Product Interface:
This will be an abstract base class that all concrete products will inherit from.

Implement Concrete Products:
These classes will implement the product interface.

Create the Factory:
This class will have a method that decides which concrete product to instantiate based on input parameters.

Example
Let's create a simple factory that creates different types of vehicles.

Step 1: Define the Product Interface'''

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def create(self):
        pass


class Car(Vehicle):
    def create(self):
        return "Car created"

class Bike(Vehicle):
    def create(self):
        return "Bike created"


class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "bike":
            return Bike()
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")

# Usage
factory = VehicleFactory()

car = factory.get_vehicle("car")
print(car.create())  # Output: Car created

bike = factory.get_vehicle("bike")
print(bike.create())  # Output: Bike created


'''Advantages of the Factory Pattern
Decoupling: The client code is decoupled from the object creation code, making it easier to modify and extend.
Single Responsibility Principle: The responsibility of creating objects is separated from the responsibility of using them.
Open/Closed Principle: New product types can be added without modifying existing code, adhering to the open/closed principle.
Conclusion
The Factory pattern is a powerful and flexible way to handle object creation in Python. It provides a way to create objects without specifying the exact class of object that will be created. This makes your code more modular, easier to maintain, and more adaptable to changes.'''
