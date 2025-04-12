'''
Proxy Pattern Example
Provides a placeholder or surrogate for another object to control access to it.
Use case: Managing access control or lazy initialization for expensive operations, 
such as when you want to control access to a resource like a large object or a network resource.
'''
class RealObject:
    def operation(self):
        return "Expensive operation completed!"

class Proxy:
    def __init__(self):
        self._real_object = None

    def operation(self):
        if not self._real_object:
            self._real_object = RealObject()
        return self._real_object.operation()

proxy = Proxy()
print(proxy.operation())  # Output: Expensive operation completed!