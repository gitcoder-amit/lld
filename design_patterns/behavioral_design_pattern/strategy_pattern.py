''' Helps to define multiple algorithm for the task and we can select any algorithm depending on the situation'''

'''The Strategy pattern is a behavioral design pattern that allows you to define a family of algorithms, encapsulate each one as a separate class, and make them interchangeable. The Strategy pattern lets the algorithm vary independently from the clients that use it.'''

'''Here's a step-by-step example of implementing the Strategy pattern in Python. We'll use the example of a payment system where different payment methods (strategies) can be used.'''


# Step-by-Step Implementation

# Step 1: Define the Strategy Interface
# The strategy interface will define a common method that all concrete strategies must implement.

from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# Step 2: Implement Concrete Strategies
# Now, let's implement some concrete strategies for different payment methods like Credit Card, PayPal, and Bitcoin.

class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, card_holder_name, cvv, expiration_date):
        self.card_number = card_number
        self.card_holder_name = card_holder_name
        self.cvv = cvv
        self.expiration_date = expiration_date

    def pay(self, amount):
        print(f"Paying {amount} using Credit Card: {self.card_number}")

class PayPalPayment(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"Paying {amount} using PayPal: {self.email}")

class BitcoinPayment(PaymentStrategy):
    def __init__(self, bitcoin_address):
        self.bitcoin_address = bitcoin_address

    def pay(self, amount):
        print(f"Paying {amount} using Bitcoin: {self.bitcoin_address}")

class UPIPayment(PaymentStrategy):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def pay(self, amount):
        print(f"Paying {amount} using UPI: {self.upi_id}")


# Step 3: Define the Context Class
# The context class will use a strategy to perform the payment. It will maintain a reference to the strategy object.

class ShoppingCart:
    def __init__(self):
        self.total_amount = 0
        self.payment_strategy = None

    def add_item(self, price):
        self.total_amount += price

    def set_payment_strategy(self, strategy):
        self.payment_strategy = strategy

    def checkout(self):
        if not self.payment_strategy:
            raise Exception("Payment strategy not set")
        self.payment_strategy.pay(self.total_amount)

# Step 4: Use the Strategy Pattern
# Now, let's use our strategy pattern implementation.


if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item(100)
    cart.add_item(200)

    # Paying with Credit Card
    credit_card = CreditCardPayment("1234-5678-9876-5432", "John Doe", "123", "12/24")
    cart.set_payment_strategy(credit_card)
    cart.checkout()  # Output: Paying 300 using Credit Card: 1234-5678-9876-5432

    # Paying with PayPal
    paypal = PayPalPayment("john.doe@example.com")
    cart.set_payment_strategy(paypal)
    cart.checkout()  # Output: Paying 300 using PayPal: john.doe@example.com

    # Paying with Bitcoin
    bitcoin = BitcoinPayment("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")
    cart.set_payment_strategy(bitcoin)
    cart.checkout()  # Output: Paying 300 using Bitcoin: 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa

    # Paying with UPI
    upi = UPIPayment("john.doe@upi")
    cart.set_payment_strategy(upi)
    cart.checkout()  # Output: Paying 300 using UPI: john.doe@upi
