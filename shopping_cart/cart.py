class ShoppingCart:
    def __init__(self):
        self.products = []
        self.coupons = []
    
    def add_product(self, product):
        self.products.append(product)
    
    def add_coupon(self, coupon):
        self.coupons.append(coupon)
    
    def calculate_total(self):
        for coupon in self.coupons:
            coupon.apply(self)
        
        total = sum(product.price for product in self.products)
        return total
