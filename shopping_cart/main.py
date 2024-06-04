from .cart import *
from shopping_cart.coupon import PercentOffEachItemCoupon, PercentOffNthItemOfTypeCoupon, PercentOffNextItemCoupon
from shopping_cart.product import Product

if __name__ == "__main__":
    # Create some products
    product1 = Product("Product 1", 100, "A")
    product2 = Product("Product 2", 200, "A")
    product3 = Product("Product 3", 300, "B")
    product4 = Product("Product 4", 400, "B")
    
    # Create a shopping cart and add products
    cart = ShoppingCart()
    cart.add_product(product1)
    cart.add_product(product2)
    cart.add_product(product3)
    cart.add_product(product4)
    
    # Create and add coupons
    coupon1 = PercentOffEachItemCoupon(10)  # 10% off each item
    coupon2 = PercentOffNextItemCoupon(20)  # 20% off the next item
    coupon3 = PercentOffNthItemOfTypeCoupon(30, 2, "A")  # 30% off the 2nd item of type A
    
    cart.add_coupon(coupon1)
    cart.add_coupon(coupon2)
    cart.add_coupon(coupon3)
    
    # Calculate the total
    total_price = cart.calculate_total()
    print(f"Total price after applying coupons: ${total_price:.2f}")
