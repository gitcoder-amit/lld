from typing import Dict
from .invoice import Invoice
from .upi_payment_mode import UPIPaymentMode
from .payment_mode import PaymentMode
from .payment import Payment

class Order:
    def __init__(self, user: 'User', warehouse: 'Warehouse'):
        self.user = user
        self.delivery_address = user.address
        self.product_category_and_count_map = user.get_user_cart().get_cart_items()
        self.warehouse = warehouse
        self.invoice = Invoice()
        self.invoice.generate_invoice(self)

    def checkout(self):
        # 1. Update inventory
        self.warehouse.remove_item_from_inventory(self.product_category_and_count_map)

        # 2. Make Payment
        is_payment_success = self.make_payment(UPIPaymentMode())

        # 3. Make cart empty
        if is_payment_success:
            self.user.get_user_cart().empty_cart()
        else:
            self.warehouse.add_item_to_inventory(self.product_category_and_count_map)

    def make_payment(self, payment_mode: PaymentMode) -> bool:
        self.payment = Payment(payment_mode)
        return self.payment.make_payment()

    def generate_order_invoice(self):
        self.invoice.generate_invoice(self)
