# assign 15
#  MRO and Diamond Inheritance
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

d = D()
d.show()
print(D.__mro__)  # Method Resolution Order
# Explanation:
#	Python resolves methods from left to right (B before C).
