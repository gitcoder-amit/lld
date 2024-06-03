from typing import List
from store import Store
from user import User
from location import Location

class VehicleRentalSystem:
    def __init__(self, stores: List[Store], users: List[User]):
        self.store_list = stores
        self.user_list = users

    def get_store(self, location: Location) -> Store:
        # Based on location, filter out the Store from store_list.
        # For simplicity, just return the first store in the list.
        return self.store_list[0]

    # Additional methods for adding/removing users and stores can be added here

# Example usage
if __name__ == "__main__":
    # Creating some sample stores and users
    stores = [Store(store_id=1, store_location=Location("123 Main St", "Springfield", "IL", "62701"))]
    users = [User(user_id=1, user_name="John Doe", driving_license=1234567890)]

    # Creating a vehicle rental system
    rental_system = VehicleRentalSystem(stores, users)

    # Getting a store based on location
    location = Location("123 Main St", "Springfield", "IL", "62701")
    store = rental_system.get_store(location)
    print(f"Store ID: {store.store_id}, Location: {store.store_location.address}")

