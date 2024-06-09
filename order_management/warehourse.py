from .inventory import Inventory
from .address import Address 
from typing import Dict

class Warehouse:
    def __init__(self, inventory: Inventory, address: Address):
        self.inventory = inventory
        self.address = address

    # Update inventory
    def remove_item_from_inventory(self, product_category_and_count_map: Dict[int, int]):
        # It will update the items in the inventory based upon product category.
        self.inventory.removeItems(product_category_and_count_map)

    def add_item_to_inventory(self, product_category_and_count_map: Dict[int, int]):
        # It will update the items in the inventory based upon product category.
        self.inventory.addItems(product_category_and_count_map)