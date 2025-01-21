# Dependency Inversion Principle (DIP)
# "Depend on abstractions, not on concrete implementations."

# Meaning: High-level modules should depend on abstractions, not concrete classes.
# Why: Makes the code more flexible and easier to maintain.

# Bad Example
class MySQLDatabase:
    def connect(self):
        print("Connected to MySQL")

class Application1:
    def __init__(self):
        self.db = MySQLDatabase()
# The Application depends on a specific database class (MySQLDatabase).

# Good Example (DIP Applied):

from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

class MySQLDatabase1(Database):
    def connect(self):
        print("Connected to MySQL")

class Application:
    def __init__(self, db: Database):
        self.db = db

app = Application(MySQLDatabase())
app.db.connect()
# Now, Application depends on an abstract Database interface, making it flexible.
