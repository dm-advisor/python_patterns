'''
State Pattern Example
Allows an object to alter its behavior when its internal state changes. Essentially, the object appears to change its class.
Use case: Finite state machines, game development (player states like "idle," "running," "jumping").
This example demonstrates the State Pattern, which allows an object to alter its behavior when its internal state changes.
The object will appear to change its class.
The example consists of a `Context` class that maintains a reference to a `State` object, and several concrete state classes that implement the `State` interface.
'''
class State:
    def handle(self):
        pass

class StateA(State):
    def handle(self):
        print("Handling State A")

class StateB(State):
    def handle(self):
        print("Handling State B")

class Context:
    def __init__(self, state):
        self.state = state

    def set_state(self, state):
        self.state = state

    def execute(self):
        self.state.handle()

context = Context(StateA())
context.execute()  # Output: Handling State A
context.set_state(StateB())
context.execute()  # Output: Handling State B