'''The Singleton pattern ensures that a class has only one instance and provides a global point of access to that instance. This is useful in scenarios where you need to control access to some shared resource, such as a configuration object or a connection pool.

There are several ways to implement the Singleton pattern in Python. Here are a few common approaches:'''


# 1. Using a Class Variable
# This is a straightforward approach where we use a class variable to store the single instance.

class Singleton:
    _instance = None  # # Class variable to hold the single instance

    def __new__(cls, *args, **kwargs):
        if not cls._instance:   # Check if an instance already exists
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance   # Return the single instance

# Usage
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # Output: True


# 2. Using a Decorator
# A decorator can be used to make any class a Singleton.

def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances: # Check if an instance of the class exists in the dictionary
            instances[cls] = cls(*args, **kwargs) # Create the instance if it does not exist
        return instances[cls]
    
    return get_instance

@singleton
class Singleton1:
    def __init__(self):
        self.value = 42

# Usage
singleton1 = Singleton1()
singleton2 = Singleton1()

print(singleton1 is singleton2)  # Output: True

# 3. Using a Metaclass
# A metaclass can control the creation of classes and can be used to implement the Singleton pattern.

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton2(metaclass=SingletonMeta):
    def __init__(self):
        self.value = 42

# Usage
singleton21 = Singleton2()
singleton22 = Singleton2()

print(singleton21 is singleton22)  # Output: True


# 4. Using a Module
# In Python, a module is itself a singleton, as it is only loaded once and reused. This can be the simplest way to implement a singleton.

import singleton_module

singleton1 = singleton_module.singleton
singleton2 = singleton_module.singleton

print(singleton1 is singleton2)  # Output: True







'''Each approach has its own benefits:

Class Variable: Simple and straightforward, but less flexible.
Decorator: Flexible and can easily convert any class to a singleton.
Metaclass: More advanced and powerful, allowing deeper control over class instantiation.
Module: Simplest approach leveraging Python's built-in module system.'''