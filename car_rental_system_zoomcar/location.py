class Location:
    def __init__(self, pincode: int, city: str, state: str, country: str, address: str = ''):
        self.pincode = pincode
        self.city = city
        self.state = state
        self.country = country
        self.address = address

# Example usage
if __name__ == "__main__":
    location = Location(pincode=123456, city="Springfield", state="IL", country="USA", address="123 Main St")
    print(f"Address: {location.address}, Pincode: {location.pincode}, City: {location.city}, State: {location.state}, Country: {location.country}")
