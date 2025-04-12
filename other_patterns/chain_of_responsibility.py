''' Chain of Responsibility Pattern Example
Allows multiple objects to handle a request, passing it along a chain until one object takes responsibility.
Use Case: Event handling, logging systems where messages are passed up a chain of handlers.
The Chain of Responsibility pattern is a behavioral design pattern that allows an object to pass a request along a chain of 
potential handlers until one of them handles the request. This pattern decouples the sender and receiver of a request, allowing 
multiple objects to handle it without the sender needing to know which object will handle it.
'''
class Handler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)
        return None

class ConcreteHandlerA(Handler):
    def handle(self, request):
        if request == "A":
            return "Handled by A"
        return super().handle(request)

class ConcreteHandlerB(Handler):
    def handle(self, request):
        if request == "B":
            return "Handled by B"
        return super().handle(request)

chain = ConcreteHandlerA(ConcreteHandlerB())
print(chain.handle("A"))  # Output: Handled by A
print(chain.handle("B"))  # Output: Handled by B
print(chain.handle("C"))  # Output: None