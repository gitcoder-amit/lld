class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age}, address={self.address})"