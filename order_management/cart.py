class Cart:
    def __init__(self):
        self.product_category_id_vs_count_map = {}

    # Add item to cart
    def add_item_to_cart(self, product_category_id, count):
        if product_category_id in self.product_category_id_vs_count_map:
            self.product_category_id_vs_count_map[product_category_id] += count
        else:
            self.product_category_id_vs_count_map[product_category_id] = count

    # Remove item from cart
    def remove_item_from_cart(self, product_category_id, count):
        if product_category_id in self.product_category_id_vs_count_map:
            self.product_category_id_vs_count_map[product_category_id] -= count
            if self.product_category_id_vs_count_map[product_category_id] <= 0:
                del self.product_category_id_vs_count_map[product_category_id]

    # Empty cart
    def empty_cart(self):
        self.product_category_id_vs_count_map.clear()

    # View Cart
    def get_cart_items(self):
        return self.product_category_id_vs_count_map
