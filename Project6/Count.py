#assign 2
#using cls

class Counter:
    count = 0                          # Class variable

    def __init__(self):               
        Counter.count += 1            # Increment on object creation

    @classmethod
    def show_count(cls):              # cls refers to the class itself
        print(f"Objects created: {cls.count}")

c1 = Counter()                        # Object created
c2 = Counter()                        # Another object
Counter.show_count()                 # Shows total created
# Explanation:
#	cls is used in class methods to access or modify class-level variables.

