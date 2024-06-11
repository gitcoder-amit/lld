'''The Command design pattern is a behavioral design pattern that turns a request into a stand-alone object that contains all information about the request. This transformation allows for parameterizing methods with different requests, queuing or logging requests, and supporting undoable operations.

Key Components of the Command Pattern
Command Interface: Declares the execution method.
Concrete Commands: Implement the command interface and define the binding between a receiver and an action.
Invoker: Responsible for initiating the request.
Receiver: Knows how to perform the work needed to carry out the request.
Client: Creates the concrete command and sets its receiver.
'''


# Step-by-Step Implementation
# Define the Command Interface:

from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


# Concrete Commands:


class AddProductCommand(Command):
    def __init__(self, receiver, product):
        self.receiver = receiver
        self.product = product

    def execute(self):
        self.receiver.add_product(self.product)

    def undo(self):
        self.receiver.delete_product(self.product.product_id)

class UpdateInventoryCommand(Command):
    def __init__(self, receiver, product_id, quantity):
        self.receiver = receiver
        self.product_id = product_id
        self.quantity = quantity

    def execute(self):
        self.receiver.add_inventory(self.product_id, self.quantity)

    def undo(self):
        self.receiver.reduce_inventory(self.product_id, self.quantity)

class CreateOrderCommand(Command):
    def __init__(self, receiver, order_id, product_id, quantity, user_id):
        self.receiver = receiver
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.user_id = user_id

    def execute(self):
        self.receiver.create_order(self.order_id, self.product_id, self.quantity, self.user_id)

    def undo(self):
        self.receiver.cancel_order(self.order_id)


# Receiver Classes:


class ProductService:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.product_id] = product
        print(f"Product {product.name} added.")

    def delete_product(self, product_id):
        if product_id in self.products:
            print(f"Product {self.products[product_id].name} deleted.")
            del self.products[product_id]

class InventoryService:
    def __init__(self):
        self.inventory = {}

    def add_inventory(self, product_id, quantity):
        if product_id in self.inventory:
            self.inventory[product_id].update_quantity(quantity)
        else:
            self.inventory[product_id] = Inventory(product_id, quantity)
        print(f"Inventory for product {product_id} increased by {quantity}.")

    def reduce_inventory(self, product_id, quantity):
        if product_id in self.inventory and self.inventory[product_id].quantity >= quantity:
            self.inventory[product_id].update_quantity(-quantity)
            print(f"Inventory for product {product_id} reduced by {quantity}.")
        else:
            raise ValueError("Insufficient inventory or product not found.")

    def check_inventory(self, product_id):
        return self.inventory.get(product_id).quantity if product_id in self.inventory else 0

class OrderService:
    def __init__(self, inventory_service):
        self.orders = {}
        self.inventory_service = inventory_service

    def create_order(self, order_id, product_id, quantity, user_id):
        if self.inventory_service.check_inventory(product_id) >= quantity:
            order = Order(order_id, product_id, quantity, user_id)
            self.orders[order_id] = order
            self.inventory_service.reduce_inventory(product_id, quantity)
            print(f"Order {order_id} created.")
            return order
        else:
            raise ValueError("Insufficient inventory.")

    def cancel_order(self, order_id):
        if order_id in self.orders:
            order = self.orders[order_id]
            self.inventory_service.add_inventory(order.product_id, order.quantity)
            print(f"Order {order_id} cancelled.")
            del self.orders[order_id]

# Invoker:
class CommandInvoker:
    def __init__(self):
        self.history = []

    def execute_command(self, command):
        command.execute()
        self.history.append(command)

    def undo_last_command(self):
        if self.history:
            command = self.history.pop()
            command.undo()

# Client:

# Initialize services
product_service = ProductService()
inventory_service = InventoryService()
order_service = OrderService(inventory_service)

# Initialize the invoker
invoker = CommandInvoker()

# Example product
product = Product(product_id=1, name='Laptop', description='Gaming Laptop', price=1500, category='Electronics')

# Create commands
add_product_command = AddProductCommand(product_service, product)
update_inventory_command = UpdateInventoryCommand(inventory_service, product.product_id, 10)
create_order_command = CreateOrderCommand(order_service, 1, product.product_id, 2, 1)

# Execute commands via invoker
invoker.execute_command(add_product_command)
invoker.execute_command(update_inventory_command)
invoker.execute_command(create_order_command)

# Undo last command
invoker.undo_last_command()  # This will cancel the order



# Explanation
# Command Interface: Defines execute and undo methods.
# Concrete Commands: Implement the command interface to perform specific actions.
# Receiver: Classes that know how to perform the actual work (e.g., ProductService, InventoryService, OrderService).
# Invoker: Manages and executes commands, keeping a history for undo operations.
# Client: Sets up the commands and invoker, and demonstrates usage.
# This pattern allows encapsulating requests as objects, supporting undoable operations, and separating the command execution logic from the request itself, providing flexibility and extensibility in your design.