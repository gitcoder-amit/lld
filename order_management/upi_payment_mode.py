from .payment_mode import PaymentMode

class UPIPaymentMode(PaymentMode):
    def make_payment(self) -> bool:
        return True