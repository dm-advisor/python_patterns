'''
Observer Pattern Example
This is a simple implementation of the Observer design pattern in Python.
Allows objects to notify other objects (observers) of changes in their state.
Use case: Allows objects to notify other objects (observers) of changes in their state.
The Observer pattern is a behavioral design pattern that defines a one-to-many relationship between objects so that 
when one object changes state, all its dependents are notified and updated automatically. 
This is useful for implementing distributed event handling systems.
'''

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()

class Observer:
    def update(self):
        print("Observer notified!")

subject = Subject()
observer = Observer()
subject.attach(observer)
subject.notify()  # Output: Observer notified!