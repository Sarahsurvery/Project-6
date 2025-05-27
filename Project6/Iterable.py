# assign 21
#  Iterable Class
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

for num in Countdown(5):
    print(num)
# Explanation:
#	Class implements __iter__() and __next__() to be used in a loop.
