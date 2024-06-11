''' It used when we need to interpret specific meaning for an expression'''

'''Defines  a grammar  for interpreting  and evaluating an expression '''
'''
The Interpreter Design Pattern is a behavioral design pattern that is used to define the grammar of a language and to interpret sentences in that language. It involves creating a class hierarchy representing the elements of the language's grammar and defining an interpreter that uses this hierarchy to interpret sentences in the language.'''


# Here's a breakdown of its components:

# Abstract Expression: This defines the interface for interpreting the language. It usually consists of an interpret() method.

# Terminal Expression: These are concrete implementations of the abstract expression that represent the terminal symbols of the grammar. Terminal expressions usually do not have any sub-expressions.

# Non-Terminal Expression: These are concrete implementations of the abstract expression that represent the non-terminal symbols of the grammar. They usually contain other expressions as sub-expressions.

# Context: This contains information that is global to the interpreter.

# Client: This builds (or is given) the syntax tree and invokes the interpret operation.

# The Interpreter pattern is useful when you need to interpret a language or grammar and perform operations based on it. It's often used in compilers, parsers, and other language processing systems.

# Example

class Expression:
    def interpret(self, context):
        pass

# Terminal 
class Number(Expression):
    def __init__(self, value):
        self.value = value
    
    def interpret(self, context):
        return self.value

# non terminal
class Plus(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def interpret(self, context):
        return self.left.interpret(context) + self.right.interpret(context)

# Client code
if __name__ == "__main__":
    context = {}
    # Construct the syntax tree
    expression = Plus(Number(3), Number(5))
    # Interpret the syntax tree
    result = expression.interpret(context)
    print("Result:", result)


# In this example, we have a simple language with two types of expressions: Number and Plus. The Plus expression adds two numbers together. We construct a syntax tree representing the expression "3 + 5", then interpret it to get the result.









