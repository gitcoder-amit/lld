'''The Iterator design pattern is a behavioral design pattern that allows you to traverse the elements of a collection without exposing its underlying representation. Python has built-in support for iteration with the iter and next functions, but implementing the Iterator pattern can still be useful for custom data structures.'''

# Here's an example of how you can implement the Iterator design pattern in Python:

# Step 1: Define the Collection Class
# First, we'll define a collection class that we want to iterate over. For this example, let's create a simple collection of numbers.

class NumberCollection:
    def __init__(self):
        self._numbers = []

    def add_number(self, number):
        self._numbers.append(number)

    def __iter__(self):
        return NumberIterator(self._numbers)


# Step 2: Define the Iterator Class
# Next, we need to create an iterator class that implements the iterator protocol, which consists of the __iter__ and __next__ methods.

class NumberIterator:
    def __init__(self, numbers):
        self._numbers = numbers
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._numbers):
            number = self._numbers[self._index]
            self._index += 1
            return number
        else:
            raise StopIteration


# Step 3: Using the Iterator
# Now, you can use the NumberCollection and iterate over its elements using a for loop or manually using the iter and next functions.

if __name__ == "__main__":
    collection = NumberCollection()
    collection.add_number(1)
    collection.add_number(2)
    collection.add_number(3)

    # Using a for loop
    for number in collection:
        print(number)

    # Manually using iter and next
    iterator = iter(collection)
    try:
        while True:
            number = next(iterator)
            print(number)
    except StopIteration:
        pass
