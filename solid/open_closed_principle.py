'''Open/Closed Principle (OCP)
"Software entities should be open for extension but closed for modification."

Meaning: You should be able to add new functionality without altering existing code.
Why: Avoids breaking existing functionality.'''


# Bad Example
class PaymentProcessor:
    def process_payment(self, payment_type):
        if payment_type == "credit":
            print("Processing Credit Card Payment")
        elif payment_type == "paypal":
            print("Processing PayPal Payment")
# Adding a new payment method requires modifying the PaymentProcessor.

# Good Example (OCP Applied):

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self):
        pass

class CreditPayment(Payment):
    def process_payment(self):
        print("Processing Credit Card Payment")

class PayPalPayment(Payment):
    def process_payment(self):
        print("Processing PayPal Payment")

class PaymentProcessor1:
    def process_payment(self, payment: Payment):
        payment.process_payment()
# Adding new payment methods (e.g., CryptoPayment) can be done without changing the PaymentProcessorq.
