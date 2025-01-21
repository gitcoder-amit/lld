'''
Liskov Substitution Principle (LSP)
"Objects of a superclass should be replaceable with objects of its subclasses without affecting correctness."

Meaning: Subclasses should be substitutable for their base class.
Why: Prevents runtime errors and preserves behavior.

The Liskov Substitution Principle (LSP) emphasizes that objects of a base class (superclass) should be replaceable with objects of its subclasses without breaking the behavior of the program. This ensures the system remains correct and predictable even when subclass objects are used in place of the base class.

Explanation of Replaceability
Base Class (Bird):

Defines general behavior and attributes common to all birds.
In this example, the Bird class provides a make_sound method that all subclasses can implement or override in their specific way.
Subclass 1 (FlyingBird):

Represents birds that can fly.
Inherits from Bird and adds a specific fly method, which is applicable only to flying birds.
It extends the base class's behavior without violating its expectations.
Subclass 2 (Penguin):

Represents birds that cannot fly but still make sounds.
Overrides the make_sound method to provide behavior specific to penguins.
Does not implement a fly method because it does not make sense for penguins.
Replaceability in Action
Suppose you have a function that uses a Bird object, like this:

python
Copy
Edit
def describe_bird(bird: Bird):
    bird.make_sound()  # All birds can make sounds
When Passing a FlyingBird:

The method make_sound will execute correctly for FlyingBird because it inherits and optionally overrides make_sound from Bird.
Additional functionality, like fly, can be used when applicable, but it does not break the expectations of Bird.
When Passing a Penguin:

The method make_sound will execute correctly for Penguin, providing its specific sound behavior.
It does not attempt to fly (as fly is not defined), avoiding the conflict seen in the "bad example" where Penguin.fly raised an exception.
Why This Works
Behavioral Consistency: Each subclass respects the behavior expected of a Bird. A Bird should be able to "make a sound," and both FlyingBird and Penguin can do this.

No Surprises: If you replace a Bird with FlyingBird or Penguin, the describe_bird function behaves predictably, avoiding unexpected runtime errors.

Key Takeaway
By organizing the class hierarchy this way:

Each subclass provides behavior consistent with the base class.
You can safely substitute Bird with any subclass (FlyingBird or Penguin) without breaking the program.
The subclasses only extend or specialize the behavior where applicable, maintaining the LSP.
'''


# Bad Example
class Bird:
    def fly(self):
        print("Flying")

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins can't fly")
# Penguin violates LSP because it cannot behave like a Bird.

# Good Example (LSP Applied):
class Bird1:
    def make_sound(self):
        print("Bird sound")

class FlyingBird(Bird1):
    def fly(self):
        print("Flying")

class Penguin1(Bird1):
    def make_sound(self):
        print("Penguin sound")
# FlyingBird and Penguin11 respect LSP by adhering to their specific behaviors.







