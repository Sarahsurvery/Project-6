# assign 16
# Function Decorators
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

say_hello()
# Explanation:
#	Decorators wrap functions to add functionality before/after.
