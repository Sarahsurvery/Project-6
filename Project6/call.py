# assign 19
#callable() and __call__()
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value

m = Multiplier(5)
print(callable(m))  # True
print(m(10))        # Works like a function
# Explanation:
#	Classes with __call__()
#behave like functions.
