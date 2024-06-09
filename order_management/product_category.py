from .product import Product

class ProductCategory:
    def __init__(self, product_category_id: int, category_name: str, price: float):
        self.product_category_id = product_category_id
        self.category_name = category_name
        self.products = []
        self.price = price

    def add_product(self, product: Product):
        self.products.append(product)

    # Remove products
    def remove_product(self, count: int):
        for _ in range(count):
            if self.products:
                self.products.pop(0)

    # Get products
    def get_products(self) -> list:
        return self.products
