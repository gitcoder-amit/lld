from typing import List
from .cart import Cart

class User:
    def __init__(self):
        self.user_id = None
        self.user_name = None
        self.address = None
        self.user_cart_details = Cart()
        self.order_ids = []

    # Get UserCart
    def get_user_cart(self) -> Cart:
        return self.user_cart_details