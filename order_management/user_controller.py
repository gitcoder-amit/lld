from typing import List, Optional
from .user import User

class UserController:
    def __init__(self, user_list: List[User]):
        self.user_list = user_list

    # Add user
    def add_user(self, user: User):
        self.user_list.append(user)

    # Remove user
    def remove_user(self, user: User):
        self.user_list.remove(user)

    # Get particular user
    def get_user(self, user_id: int) -> Optional[User]:
        for user in self.user_list:
            if user.user_id == user_id:
                return user
        return None