class User:
    def __init__(self, user_id: int, user_name: str, driving_license: int):
        self.user_id = user_id
        self.user_name = user_name
        self.driving_license = driving_license

    def get_user_id(self) -> int:
        return self.user_id

    def set_user_id(self, user_id: int):
        self.user_id = user_id

    def get_user_name(self) -> str:
        return self.user_name

    def set_user_name(self, user_name: str):
        self.user_name = user_name

    def get_driving_license(self) -> int:
        return self.driving_license

    def set_driving_license(self, driving_license: int):
        self.driving_license = driving_license

# Example usage
if __name__ == "__main__":
    # Create a user instance
    user = User(user_id=1, user_name="John Doe", driving_license=1234567890)
    
    # Accessing user attributes
    print(f"User ID: {user.get_user_id()}")
    print(f"User Name: {user.get_user_name()}")
    print(f"Driving License: {user.get_driving_license()}")
