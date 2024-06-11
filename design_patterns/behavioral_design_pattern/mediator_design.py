'''The Mediator Design Pattern is a behavioral design pattern that promotes loose coupling by keeping objects from referring to each other explicitly. Instead, they communicate through a mediator object. This pattern is useful when you want to decouple the communication between a set of objects.'''


# Step 1: Define the Mediator Interface
# The Mediator interface declares methods for communication with Colleague objects.


from abc import ABC, abstractmethod

class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: object, event: str) -> None:
        pass

    @abstractmethod
    def execute(self, action: str) -> None:
        pass


# Step 2: Create Concrete Mediator
# The Concrete Mediator class implements the communication between Colleague objects.

class ConcreteMediator(Mediator):
    def __init__(self):
        self._colleague1 = None
        self._colleague2 = None

    def set_colleague1(self, colleague):
        self._colleague1 = colleague

    def set_colleague2(self, colleague):
        self._colleague2 = colleague

    def notify(self, sender: object, event: str) -> None:
        if event == "A":
            print("Mediator reacts on A and triggers following operations:")
            self._colleague2.do_c()
        elif event == "D":
            print("Mediator reacts on D and triggers following operations:")
            self._colleague1.do_b()
            self._colleague2.do_c()

    def execute(self, action: str) -> None:
        if action == "A":
            self._colleague1.do_a()
        elif action == "D":
            self._colleague2.do_d()

# Step 3: Create Colleague Classes
# Colleague classes communicate with each other via the mediator.

class BaseColleague:
    def __init__(self, mediator: Mediator) -> None:
        self._mediator = mediator

class Colleague1(BaseColleague):
    def do_a(self) -> None:
        print("Colleague1 does A.")
        self._mediator.notify(self, "A")

    def do_b(self) -> None:
        print("Colleague1 does B.")

class Colleague2(BaseColleague):
    def do_c(self) -> None:
        print("Colleague2 does C.")

    def do_d(self) -> None:
        print("Colleague2 does D.")
        self._mediator.notify(self, "D")


# Step 4: Client Code
# Create instances of the colleagues and the mediator, and set up their relationships.
if __name__ == "__main__":
    mediator = ConcreteMediator()

    colleague1 = Colleague1(mediator)
    colleague2 = Colleague2(mediator)

    mediator.set_colleague1(colleague1)
    mediator.set_colleague2(colleague2)

    print("Client triggers operation A.")
    colleague1.do_a()

    print("\nClient triggers operation D.")
    colleague2.do_d()
