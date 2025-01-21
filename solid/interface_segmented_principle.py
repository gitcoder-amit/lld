'''Interface Segregation Principle (ISP)
"Clients should not be forced to depend on methods they do not use."

Meaning: Interfaces should be specific to the client’s needs.
Why: Prevents unnecessary dependencies.'''

# Bad Example
class Worker:
    def work(self):
        pass
    
    def eat(self):
        pass

class Robot(Worker):
    def eat(self):
        raise Exception("Robots don't eat")

# Good Example (ISP Applied):
class Workable:
    def work(self):
        pass

class Eatable:
    def eat(self):
        pass

class Human(Workable, Eatable):
    def work(self):
        print("Working")
    def eat(self):
        print("Eating")

class Robot1(Workable):
    def work(self):
        print("Working")