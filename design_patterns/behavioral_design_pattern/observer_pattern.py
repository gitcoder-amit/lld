''' In this object (Observable) maintains a list of  its dependent (observers) and notitfies them of any changes in its state'''

''' The Observer pattern is a behavioral design pattern that defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically. It is commonly used in event handling systems. '''

# Observer Pattern Example in Python
# Let's create an example where we have a subject (e.g., a news agency) and observers (e.g., news channels) that get notified when the subject's state changes.

class Observer:
    def update(self, message):
        raise NotImplementedError("Subclass must implement the update method.")

class NewsChannel(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received news: {message}")

class NewsAgency:
    def __init__(self):
        self.observers = []
        self.news = ""

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.news)

    def add_news(self, news):
        self.news = news
        self.notify_observers()

# Usage
if __name__ == "__main__":
    agency = NewsAgency()
    
    channel1 = NewsChannel("Channel 1")
    channel2 = NewsChannel("Channel 2")
    
    agency.add_observer(channel1)
    agency.add_observer(channel2)
    
    agency.add_news("Breaking News: Observer Pattern Implemented!")
    agency.add_news("Update: Observer Pattern Example in Python")


# output
# Channel 1 received news: Breaking News: Observer Pattern Implemented!
# Channel 2 received news: Breaking News: Observer Pattern Implemented!
# Channel 1 received news: Update: Observer Pattern Example in Python
# Channel 2 received news: Update: Observer Pattern Example in Python


# Detailed Steps:
# Initialize the Subject: An instance of NewsAgency is created.
# Create Observers: Two instances of NewsChannel are created with different names.
# Add Observers: The NewsChannel instances are added to the NewsAgency's list of observers.
# State Change and Notification: When add_news is called on NewsAgency, it updates its state and calls notify_observers, which in turn calls the update method of each NewsChannel, passing the new news message.
# This example demonstrates how the Observer pattern can be used to decouple the subject from its observers, allowing the subject to notify all interested parties of state changes without needing to know who they are or what they do with the information.
