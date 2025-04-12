'''
Builder pattern implementation in Python.
This pattern is used to construct a complex object step by step.
It allows you to create different representations of an object using the same construction process.
Use case: When you want to create a complex object with many optional parts or configurations.
For example, building a complex document or a user interface where you want to separate the construction of the object from its representation.
'''
class Builder:
    def __init__(self):
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

    def build(self):
        return " ".join(self.parts)

builder = Builder()
builder.add_part("Hello")
builder.add_part("World")
print(builder.build())  # Output: Hello World