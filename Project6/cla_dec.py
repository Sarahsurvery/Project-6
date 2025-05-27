# assign 17
#  Class Decorators
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

p = Person("John")
print(p.greet())
# Explanation:
#	Adds a new method to the class via decorator.
