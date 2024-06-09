from typing import List
from .user_controller import UserController
from .warehouse_controller import WarehouseController
from .product_category import ProductCategory
from .order_controller import OrderController
from .order import Order


class ProductDeliverySystem:
    def __init__(self, user_list: List['User'], warehouse_list: List['Warehouse']):
        self.user_controller = UserController(user_list)
        self.warehouse_controller = WarehouseController(warehouse_list, None)
        self.order_controller = OrderController()

    # Get user object
    def get_user(self, user_id: int) -> 'User':
        return self.user_controller.get_user(user_id)

    # Get warehouse
    def get_warehouse(self, warehouse_selection_strategy: 'WarehouseSelectionStrategy') -> 'Warehouse':
        return self.warehouse_controller.select_warehouse(warehouse_selection_strategy)

    # Get inventory
    def get_inventory(self, warehouse: 'Warehouse') -> 'Inventory':
        return warehouse.inventory

    # Add product to cart
    def add_product_to_cart(self, user: 'User', product: ProductCategory, count: int):
        cart = user.get_user_cart()
        cart.add_item_in_cart(product.product_category_id, count)

    # Place order
    def place_order(self, user: 'User', warehouse: 'Warehouse') -> Order:
        return self.order_controller.create_new_order(user, warehouse)

    def checkout(self, order: Order):
        order.checkout()