from .order import Order
from typing import List

class OrderController:
    def __init__(self):
        self.order_list = []
        self.user_id_vs_orders = {}

    # Create New Order
    def create_new_order(self, user: 'User', warehouse: 'Warehouse') -> 'Order':
        order = Order(user, warehouse)
        self.order_list.append(order)

        if user.user_id in self.user_id_vs_orders:
            self.user_id_vs_orders[user.user_id].append(order)
        else:
            self.user_id_vs_orders[user.user_id] = [order]

        return order

    # Remove order
    def remove_order(self, order: 'Order'):
        # Remove order capability goes here
        pass

    def get_order_by_customer_id(self, user_id: int) -> List['Order']:
        return self.user_id_vs_orders.get(user_id, [])

    def get_order_by_order_id(self, order_id: int) -> 'Order':
        for order in self.order_list:
            if order.order_id == order_id:
                return order
        return None
