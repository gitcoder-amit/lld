''' Allows an object to alter its behaviour when its internal state changes'''

'''The State pattern is a behavioral design pattern that allows an object to change its behavior when its internal state changes. It is a way to manage state transitions within an object by encapsulating the state-specific behaviors into separate state objects.'''


# Here is a basic example of the State pattern implemented in Python:


class State:
    def handle(self, context):
        raise NotImplementedError("Handle method must be overridden.")

class RedState(State):
    def handle(self, context):
        # Altering behavior
        print("Red light - Stop!")
        # Changing state
        context.state = GreenState()

class GreenState(State):
    def handle(self, context):
        # Altering behavior
        print("Green light - Go!")
        # Changing state
        context.state = YellowState()

class YellowState(State):
    def handle(self, context):
        # Altering behavior
        print("Yellow light - Caution!")
        # Changing state
        context.state = RedState()

class TrafficLightContext:
    def __init__(self, state):
        self.state = state
    
    def request(self):
        self.state.handle(self)

# Usage
if __name__ == "__main__":
    # Initialize the traffic light with the initial state (Red)
    initial_state = RedState()
    traffic_light = TrafficLightContext(initial_state)

    # Simulate the traffic light state transitions
    for _ in range(6):  # Cycle through the states twice
        traffic_light.request()


'''  Initial State: The traffic light starts in the RedState.
First Request: traffic_light.request() calls RedState.handle(), which prints "Red light - Stop!" and transitions to GreenState.
Second Request: traffic_light.request() calls GreenState.handle(), which prints "Green light - Go!" and transitions to YellowState.
Third Request: traffic_light.request() calls YellowState.handle(), which prints "Yellow light - Caution!" and transitions back to RedState.
This cycle repeats, demonstrating how the object's behavior changes as its state changes.'''