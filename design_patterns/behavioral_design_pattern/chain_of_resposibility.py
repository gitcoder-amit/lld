''' Allows multiple objects to handle  a request  without the sender  needing  to know  which object  will ultimately process it '''


'''The Chain of Responsibility pattern is a behavioral design pattern that lets you pass requests along a chain of handlers. Each handler either processes the request or passes it to the next handler in the chain.'''

'''Let's create an example where we have a series of logging handlers that process log messages based on their severity levels: Debug, Info, and Error.

Step-by-Step Implementation
'''

# Step 1: Define the Handler Interface
# The handler interface will define a common method that all concrete handlers must implement.

from abc import ABC, abstractmethod

class Handler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass
    
    @abstractmethod
    def handle(self, request):
        pass


# Step 2: Implement the Base Handler Class
# The base handler class will provide default behavior for setting the next handler and passing the request along the chain.

class BaseHandler(Handler):
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

# Step 3: Implement Concrete Handlers
# Implement concrete handlers that process the request or pass it to the next handler.

class DebugHandler(BaseHandler):
    def handle(self, request):
        if request == "DEBUG":
            print("DebugHandler: Handling DEBUG request.")
        else:
            super().handle(request)

class InfoHandler(BaseHandler):
    def handle(self, request):
        if request == "INFO":
            print("InfoHandler: Handling INFO request.")
        else:
            super().handle(request)

class ErrorHandler(BaseHandler):
    def handle(self, request):
        if request == "ERROR":
            print("ErrorHandler: Handling ERROR request.")
        else:
            super().handle(request)


# Step 4: Use the Chain of Responsibility Pattern
# Now, let's use our Chain of Responsibility pattern implementation.

if __name__ == "__main__":
    # Create handlers
    debug_handler = DebugHandler()
    info_handler = InfoHandler()
    error_handler = ErrorHandler()

    # Chain handlers
    debug_handler.set_next(info_handler).set_next(error_handler)

    # Generate requests
    requests = ["DEBUG", "INFO", "ERROR", "UNKNOWN"]

    for request in requests:
        print(f"Processing request: {request}")
        debug_handler.handle(request)


'''
Explanation
Handler Interface: The Handler class is an abstract base class that defines the set_next and handle methods. Each concrete handler must implement these methods.
Base Handler Class: The BaseHandler class implements the default behavior for setting the next handler and passing the request along the chain.
Concrete Handlers:
DebugHandler: Processes DEBUG requests or passes them to the next handler.
InfoHandler: Processes INFO requests or passes them to the next handler.
ErrorHandler: Processes ERROR requests or passes them to the next handler.
Usage Example:
Handlers are created and chained together.
Requests are generated and passed to the first handler in the chain.
Each handler processes the request if it matches its responsibility; otherwise, it passes the request to the next handler in the chain.
'''

# Output
# When you run the code, you should see the following output:



