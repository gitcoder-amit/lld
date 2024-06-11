''' When we want  all classes  to follow specific steps to process the tasks  but provide  flexibility that each class 
can have their own logic in that specific step'''


# Scenario:
# You are developing a system that processes data from different file formats, like CSV and JSON. The general steps for processing data are:

# Read the file.
# Parse the data.
# Process the data.
# Save the processed data.
# The specific steps for reading and parsing the files differ depending on the file format, but the overall structure remains the same.


from abc import ABC, abstractmethod
import csv
import json

class DataProcessor(ABC):
    def process(self):
        """Template method defining the algorithm structure."""
        data = self.read_file()
        parsed_data = self.parse_data(data)
        self.process_data(parsed_data)
        self.save_data(parsed_data)

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def parse_data(self, data):
        pass

    @abstractmethod
    def process_data(self, parsed_data):
        pass

    @abstractmethod
    def save_data(self, parsed_data):
        pass


class CSVDataProcessor(DataProcessor):
    def read_file(self):
        print("Reading CSV file")
        # For demonstration purposes, we'll use a hardcoded CSV string
        return "name,age\nJohn,30\nJane,25"

    def parse_data(self, data):
        print("Parsing CSV data")
        parsed_data = list(csv.DictReader(data.splitlines()))
        return parsed_data

    def process_data(self, parsed_data):
        print("Processing CSV data")
        for row in parsed_data:
            row['age'] = int(row['age']) + 1  # Example processing

    def save_data(self, parsed_data):
        print("Saving CSV data")
        for row in parsed_data:
            print(f"Name: {row['name']}, Age: {row['age']}")


class JSONDataProcessor(DataProcessor):
    def read_file(self):
        print("Reading JSON file")
        # For demonstration purposes, we'll use a hardcoded JSON string
        return '{"people": [{"name": "John", "age": 30}, {"name": "Jane", "age": 25}]}'

    def parse_data(self, data):
        print("Parsing JSON data")
        parsed_data = json.loads(data)['people']
        return parsed_data

    def process_data(self, parsed_data):
        print("Processing JSON data")
        for person in parsed_data:
            person['age'] = person['age'] + 1  # Example processing

    def save_data(self, parsed_data):
        print("Saving JSON data")
        for person in parsed_data:
            print(f"Name: {person['name']}, Age: {person['age']}")


def client_code(data_processor: DataProcessor):
    """Client code works with an instance of DataProcessor."""
    data_processor.process()


if __name__ == "__main__":
    print("Processing CSV data:")
    client_code(CSVDataProcessor())
    print()
    print("Processing JSON data:")
    client_code(JSONDataProcessor())


''' Example 2'''

# Certainly! Let's consider a real-life example of the Template Method pattern in the context of a payment processing system. The steps involved in processing payments might include:

# Authenticate the payment method.
# Validate the transaction details.
# Process the payment.
# Send a confirmation.
# Different payment methods (e.g., credit card, PayPal, cryptocurrency) will implement these steps differently, but the overall structure remains the same.

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    def process_payment(self):
        """Template method defining the algorithm structure."""
        self.authenticate()
        self.validate_transaction()
        self.process_transaction()
        self.send_confirmation()

    @abstractmethod
    def authenticate(self):
        pass

    @abstractmethod
    def validate_transaction(self):
        pass

    @abstractmethod
    def process_transaction(self):
        pass

    @abstractmethod
    def send_confirmation(self):
        pass


class CreditCardPayment(PaymentProcessor):
    def authenticate(self):
        print("Authenticating credit card details")
        # Implement authentication logic here

    def validate_transaction(self):
        print("Validating credit card transaction")
        # Implement validation logic here

    def process_transaction(self):
        print("Processing credit card payment")
        # Implement payment processing logic here

    def send_confirmation(self):
        print("Sending credit card payment confirmation")
        # Implement confirmation sending logic here


class PayPalPayment(PaymentProcessor):
    def authenticate(self):
        print("Authenticating PayPal account")
        # Implement authentication logic here

    def validate_transaction(self):
        print("Validating PayPal transaction")
        # Implement validation logic here

    def process_transaction(self):
        print("Processing PayPal payment")
        # Implement payment processing logic here

    def send_confirmation(self):
        print("Sending PayPal payment confirmation")
        # Implement confirmation sending logic here


class CryptoPayment(PaymentProcessor):
    def authenticate(self):
        print("Authenticating cryptocurrency wallet")
        # Implement authentication logic here

    def validate_transaction(self):
        print("Validating cryptocurrency transaction")
        # Implement validation logic here

    def process_transaction(self):
        print("Processing cryptocurrency payment")
        # Implement payment processing logic here

    def send_confirmation(self):
        print("Sending cryptocurrency payment confirmation")
        # Implement confirmation sending logic here


def client_code1(payment_processor: PaymentProcessor):
    """Client code works with an instance of PaymentProcessor."""
    payment_processor.process_payment()


if __name__ == "__main__":
    print("Processing credit card payment:")
    client_code1(CreditCardPayment())
    print()
    print("Processing PayPal payment:")
    client_code1(PayPalPayment())
    print()
    print("Processing cryptocurrency payment:")
    client_code1(CryptoPayment())
