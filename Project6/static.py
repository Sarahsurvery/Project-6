#assign 5
#  Static Method
class MathUtils:
    @staticmethod
    def add(a, b):                   # No self or cls
        return a + b

print(MathUtils.add(5, 7))          # Direct call
# Explanation:
#	Static methods don’t depend on class or instance. Used for utility functions.
