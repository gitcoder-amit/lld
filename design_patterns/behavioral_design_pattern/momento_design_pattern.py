'''The Memento Design Pattern is a behavioral design pattern that allows an object to save and restore its state without revealing its implementation details. This pattern is useful for implementing features like undo mechanisms in applications.'''

# Step 1: Define the Memento Class
# The Memento class stores the state of the Originator.

class Memento:
    def __init__(self, state: str):
        self._state = state

    def get_state(self) -> str:
        return self._state

# Step 2: Create the Originator Class
# The Originator creates a memento containing a snapshot of its current internal state and uses the memento to restore its internal state.

class Originator:
    def __init__(self, state: str):
        self._state = state

    def set_state(self, state: str) -> None:
        print(f"Originator: Setting state to {state}")
        self._state = state

    def get_state(self) -> str:
        return self._state

    def save(self) -> Memento:
        print(f"Originator: Saving state to Memento.")
        return Memento(self._state)

    def restore(self, memento: Memento) -> None:
        self._state = memento.get_state()
        print(f"Originator: State after restoring from Memento: {self._state}")

# Step 3: Create the Caretaker Class
# The Caretaker is responsible for keeping the mementos. It doesn't modify or inspect the contents of the mementos.

class Caretaker:
    def __init__(self, originator: Originator):
        self._mementos = []
        self._originator = originator

    def backup(self) -> None:
        print("Caretaker: Saving Originator's state...")
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not self._mementos:
            print("Caretaker: No mementos to restore.")
            return

        memento = self._mementos.pop()
        print("Caretaker: Restoring state to:", memento.get_state())
        self._originator.restore(memento)

    def show_history(self) -> None:
        print("Caretaker: Here's the list of mementos:")
        for memento in self._mementos:
            print(memento.get_state())


# Step 4: Client Code
# The client interacts with the Originator and Caretaker to demonstrate the Memento pattern.

if __name__ == "__main__":
    originator = Originator("Initial State")
    caretaker = Caretaker(originator)

    caretaker.backup()
    originator.set_state("State 1")

    caretaker.backup()
    originator.set_state("State 2")

    caretaker.backup()
    originator.set_state("State 3")

    print("\nCurrent State:", originator.get_state())
    caretaker.show_history()

    print("\nUndo to previous state:")
    caretaker.undo()
    print("Current State:", originator.get_state())

    print("\nUndo to previous state:")
    caretaker.undo()
    print("Current State:", originator.get_state())

    print("\nUndo to previous state:")
    caretaker.undo()
    print("Current State:", originator.get_state())
