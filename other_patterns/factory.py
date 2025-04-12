'''
Factory Method Pattern Example
This script demonstrates the Factory Method design pattern.
Creates objects without specifying the exact class of the object that will be created.
Use case: Abstracting the creation of objects with complex instantiation logic; when a class cannot anticipate the class of objects it must create.
When a class wants its subclasses to specify the objects it creates.
When the classes delegate the responsibility of instantiation to subclasses.
'''

'''
The Factory Method pattern defines an interface for creating an object, but lets subclasses alter the type of objects that will be created.
It allows a class to defer instantiation to subclasses.
'''
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_factory(animal_type):
    if animal_type == "dog":
        return Dog()
    elif animal_type == "cat":
        return Cat()

animal = animal_factory("dog")
print(animal.speak())  # Output: Woof!