from .product_category import *

class Inventory:
    def __init__(self):
        self.product_category_list = []

    # Add new category
    def add_category(self, category_id, name, price):
        product_category = ProductCategory()
        product_category.price = price
        product_category.category_name = name
        product_category.product_category_id = category_id
        self.product_category_list.append(product_category)

    # Add product to the particular category
    def add_product(self, product, product_category_id):
        # Find the respective productCategory Object
        category_object = self.get_product_category_from_id(product_category_id)
        if category_object:
            category_object.add_product(product)

    # Remove product from the category
    def remove_items(self, product_category_and_count_map):
        for product_category_id, count in product_category_and_count_map.items():
            category = self.get_product_category_from_id(product_category_id)
            if category:
                category.remove_product(count)

    def get_product_category_from_id(self, product_category_id):
        for product_category in self.product_category_list:
            if product_category.product_category_id == product_category_id:
                return product_category
        return None
