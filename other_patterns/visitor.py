'''
Visitor Pattern Example
Separates an algorithm from the object structure it operates on. This allows adding new operations to existing objects without modifying their structure.
Use case: Traversing or processing hierarchical structures (e.g., XML trees, file systems).
The Visitor pattern allows you to separate an algorithm from the object structure on which it operates. This is useful when you want to add new operations to existing object structures without modifying their classes.
The example consists of a simple structure of shapes (Circle and Square) and a visitor that calculates the area of these shapes.
'''
class Element:
    def accept(self, visitor):
        pass

class ElementA(Element):
    def accept(self, visitor):
        visitor.visit(self)

    def operation(self):
        return "ElementA"

class Visitor:
    def visit(self, element):
        pass

class ConcreteVisitor(Visitor):
    def visit(self, element):
        print(f"Visiting {element.operation()}")

element = ElementA()
visitor = ConcreteVisitor()
element.accept(visitor)  # Output: Visiting ElementA