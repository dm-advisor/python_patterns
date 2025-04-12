'''
Command Pattern Example
Encapsulates requests or actions as objects, allowing them to be parameterized, queued, or logged. This decouples the sender 
of a request from the receiver.
Use case: When you want to decouple the sender and receiver of a request, or when you want to support undoable operations. Or,
when implementing undo/redo functionality in applications or scheduling tasks.
This example demonstrates the Command Pattern, which encapsulates a request as an object,   
allowing for parameterization of clients with queues, requests, and operations. It also supports undoable operations.
'''

class Command:
    def execute(self):
        pass

class PrintCommand(Command):
    def __init__(self, message):
        self.message = message

    def execute(self):
        print(self.message)

class Invoker:
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def execute_commands(self):
        for command in self.commands:
            command.execute()

invoker = Invoker()
invoker.add_command(PrintCommand("Hello, World!"))
invoker.add_command(PrintCommand("Executing commands..."))
invoker.execute_commands()