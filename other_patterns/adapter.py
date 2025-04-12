'''
Adapter Pattern Example
Translates the interface of one class into another interface that clients expect.
For example, if you have a legacy class that you want to use in a new system but its methods are not compatible with the new system's interface.
Use case: When you want to use an existing class but its interface does not match the one you need.
This is a common scenario when integrating with third-party libraries or legacy code. 
'''

class OldPrinter:
    def old_print(self):
        return "Printing from OldPrinter"

class Adapter:
    def __init__(self, old_printer):
        self.old_printer = old_printer

    def new_print(self):
        return self.old_printer.old_print()

adapter = Adapter(OldPrinter())
print(adapter.new_print())  # Output: Printing from OldPrinter