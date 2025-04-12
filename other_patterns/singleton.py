'''
Singleton Pattern Example
This pattern is used in logging.getLogger() to ensure that only one instance of a logger is created.
Ensures that a class has only one instance, and provides a global point of access to it.
Use case: When exactly one object is needed to coordinate actions across the system.
The Singleton pattern is a design pattern that restricts the instantiation of a class to one single instance.
The Singleton pattern ensures that a class has only one instance and provides a global point of access to it.
It is used when exactly one object is needed to coordinate actions across the system.
The Singleton pattern is often used in logging, driver objects, caching, thread pools, and database connections.
'''

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1 is singleton2)  # Output: True