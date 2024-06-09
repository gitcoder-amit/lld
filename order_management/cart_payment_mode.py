from .payment_mode import *

class CardPaymentMode(PaymentMode):
    def make_payment(self) -> bool:
        return True
