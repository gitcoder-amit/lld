class Coupon:
    def apply(self, cart):
        raise NotImplementedError("Subclasses must implement this method")

class PercentOffEachItemCoupon(Coupon):
    def __init__(self, discount_percent):
        self.discount_percent = discount_percent
    
    def apply(self, cart):
        for product in cart.products:
            product.price *= (1 - self.discount_percent / 100)

class PercentOffNextItemCoupon(Coupon):
    def __init__(self, discount_percent):
        self.discount_percent = discount_percent
    
    def apply(self, cart):
        for i in range(len(cart.products) - 1):
            cart.products[i + 1].price *= (1 - self.discount_percent / 100)

class PercentOffNthItemOfTypeCoupon(Coupon):
    def __init__(self, discount_percent, n, product_type):
        self.discount_percent = discount_percent
        self.n = n
        self.product_type = product_type
    
    def apply(self, cart):
        count = 0
        for product in cart.products:
            if product.product_type == self.product_type:
                count += 1
                if count == self.n:
                    product.price *= (1 - self.discount_percent / 100)
                    break
