# When we want to create object step by step
# we can keep homebuiled as abstract so that if in future any new type of specific homebuilder like FlatHomeBuilder DuplexHomeBuilder we can easily implement that as well

'''The Builder Pattern is a creational design pattern used to construct complex objects step by step. It allows you to produce different types and representations of an object using the same construction process. This pattern is particularly useful when an object has many optional parameters, making the construction process more manageable and readable.
'''

# Example: Builder Pattern in Python
# Let's consider an example of a House class where a house can have multiple optional features like a garage, a swimming pool, and a garden.

# Step 1: Define the Product
class House:
    def __init__(self):
        self.has_garage = False
        self.has_swimming_pool = False
        self.has_garden = False

    def __str__(self):
        features = []
        if self.has_garage:
            features.append("Garage")
        if self.has_swimming_pool:
            features.append("Swimming Pool")
        if self.has_garden:
            features.append("Garden")
        return f"House with: {', '.join(features) if features else 'no extra features'}"


# Step 2: Create the Builder


class HouseBuilder:
    def __init__(self):
        self.house = House()

    def add_garage(self):
        self.house.has_garage = True
        return self

    def add_swimming_pool(self):
        self.house.has_swimming_pool = True
        return self

    def add_garden(self):
        self.house.has_garden = True
        return self

    def build(self):
        return self.house

# Step 3: Use the Builder in Client Code

def main():
    builder = HouseBuilder()
    house = (
        builder
        .add_garage()
        .add_swimming_pool()
        .add_garden()
        .build()
    )
    print(house)

if __name__ == "__main__":
    main()
