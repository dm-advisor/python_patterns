'''
Mediator Pattern Example
Defines an object that facilitates communication between other objects, preventing them from referring to each other explicitly.
Use Case: Managing interactions in GUI components (e.g., buttons, textboxes) or modular systems.
This example demonstrates the Mediator pattern, which is used to reduce coupling between classes by introducing a mediator object 
that handles communication between them.
The example consists of a `Mediator` class and two `Colleague` classes (`ConcreteColleague1` and `ConcreteColleague2`). The mediator 
coordinates the interaction between the colleagues.
The `ConcreteColleague1` and `ConcreteColleague2` classes can communicate with each other only through the mediator, which helps to 
decouple their interactions.
'''
class Mediator:
    def notify(self, sender, event):
        pass

class ConcreteMediator(Mediator):
    def __init__(self, component_a, component_b):
        self.component_a = component_a
        self.component_b = component_b

    def notify(self, sender, event):
        if event == "A":
            self.component_b.do_action()
        elif event == "B":
            self.component_a.do_action()

class Component:
    def __init__(self, mediator):
        self.mediator = mediator

class ComponentA(Component):
    def do_action(self):
        print("Component A action")

class ComponentB(Component):
    def do_action(self):
        print("Component B action")

mediator = ConcreteMediator(ComponentA(None), ComponentB(None))
mediator.component_a = ComponentA(mediator)
mediator.component_b = ComponentB(mediator)

mediator.notify(None, "A")  # Output: Component B action
mediator.notify(None, "B")  # Output: Component A action