# std.py
#Assign 1
#using self

class Student:
    def __init__(self, name, marks):  # Constructor method
        self.name = name              # 'self' refers to the instance
        self.marks = marks

    def display(self):               # Instance method
        print(f"Name: {self.name}, Marks: {self.marks}")

s1 = Student("Alice", 88)            # Creating an object
s1.display()                         # Calling the method
# Explanation:
#	self refers to the current object (s1).
#	You use it to access attributes and methods of that object.

        

