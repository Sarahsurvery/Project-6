# assign 14
# Aggregation
class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee

emp = Employee("Sarah")
dept = Department("Computer Teacher", emp)
print(dept.dept_name, dept.employee.name)
# Explanation:
#	Aggregation: Objects exist independently, but are used together.
