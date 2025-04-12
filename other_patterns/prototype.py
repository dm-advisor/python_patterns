import copy

'''
Prototype Pattern
This pattern is used when the cost of creating a new object is more expensive than copying an existing object.
It allows for the creation of new objects by copying an existing object, known as the prototype.
This is particularly useful when the object is complex or expensive to create.
'''
class Prototype:
    def __init__(self, value):
        self.value = value

    def clone(self):
        return copy.deepcopy(self)

obj1 = Prototype([1, 2, 3])
obj2 = obj1.clone()

print(obj1 is obj2)  # Output: False (new instance created)
print(obj2.value)    # Output: [1, 2, 3]