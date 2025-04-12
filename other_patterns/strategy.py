'''
Strategy Pattern Example
Allows you to define a family of algorithms, encapsulate them, and make them interchangeable.
Use case: Selecting the best algorithm at runtime (e.g., sorting strategies).
This example demonstrates the Strategy Pattern, which allows selecting an algorithm's behavior at runtime.  
The Strategy Pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable.
The Strategy Pattern lets the algorithm vary independently from clients that use it.
'''

class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute_strategy(self, data):
        return self.strategy(data)

def strategy_add(data):
    return sum(data)

def strategy_multiply(data):
    result = 1
    for num in data:
        result *= num
    return result

context = Context(strategy_add)
print(context.execute_strategy([1, 2, 3, 4]))  # Output: 10

context.strategy = strategy_multiply
print(context.execute_strategy([1, 2, 3, 4]))  # Output: 24
