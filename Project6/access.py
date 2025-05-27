# assign 7
# Access Modifiers

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name             # Public
        self._salary = salary        # Protected
        self.__ssn = ssn             # Private

emp = Employee("sarah", 5000, "123-45-6789")
print(emp.name)                      # OK
print(emp._salary)                   # Not recommended, but works
# print(emp.__ssn)                  # Error: private
print(emp._Employee__ssn)            # Name mangling workaround
# Explanation:
#	_var is protected (convention).
#	__var is private (name mangled).
