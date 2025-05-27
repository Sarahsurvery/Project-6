# assign 8
# super()
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)       # Call parent constructor
        self.subject = subject

t = Teacher("Sir Bilal", "Math")
print(t.name, t.subject)
# Explanation:
#	super() is used to call the base class method (constructor in this case).
