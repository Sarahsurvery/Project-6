# assign 10
# Instance Methods
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking!")

d = Dog("tommy", "Labrador")
d.bark()
# Explanation:
#	Instance methods take self and operate on object data.
