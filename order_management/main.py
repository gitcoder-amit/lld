from .product_delivery_system import ProductDeliverySystem
from .warehourse import Warehouse
from .inventory import Inventory
from .product import Product
from .address import Address 
from .user import User

from DesignOrderManagementSystem import *

def main():
    # Create warehouses in the system
    warehouse_list = [add_warehouse_and_its_inventory()]

    # Create users in the system
    user_list = [create_user()]

    # Feed the system with the initial information
    product_delivery_system = ProductDeliverySystem(user_list, warehouse_list)

    run_delivery_flow(product_delivery_system, 1)

def add_warehouse_and_its_inventory():
    warehouse = Warehouse()
    inventory = Inventory()

    inventory.add_category('0001', "Peppsii Large Cold Drink", 100)
    inventory.add_category('0004', "Doovee small Soap", 50)

    # Create 3 Products
    product1 = Product(1, "Peepsii")
    product2 = Product(2, "Peepsii")
    product3 = Product(3, "Doovee")

    inventory.add_product(product1, '0001')
    inventory.add_product(product2, '0001')
    inventory.add_product(product3, '0004')

    warehouse.inventory = inventory
    return warehouse

def create_user():
    address = Address(230011, "city", "state")
    return User(1, "SJ", address)

def run_delivery_flow(product_delivery_system, user_id):
    # Get the user object
    user = product_delivery_system.get_user(user_id)

    # Get warehouse based on user preference
    warehouse = product_delivery_system.get_warehouse(NearestWarehouseSelectionStrategy())

    # Get all the inventory to show the user
    inventory = product_delivery_system.get_inventory(warehouse)

    product_category_i_want_to_order = None
    for product_category in inventory.product_category_list:
        if product_category.category_name == "Peppsii Large Cold Drink":
            product_category_i_want_to_order = product_category

    # Add product to the cart
    product_delivery_system.add_product_to_cart(user, product_category_i_want_to_order, 2)

    # Place order
    order = product_delivery_system.place_order(user, warehouse)

    # Checkout
    product_delivery_system.checkout(order)

if __name__ == "__main__":
    main()
