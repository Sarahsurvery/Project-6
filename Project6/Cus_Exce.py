# assign 20
#Custom Exception
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older.")
    print("Age is valid.")

try:
    check_age(16)
    check_age(20)
except InvalidAgeError as e:
    print("Error:", e)
# Explanation:
#	Custom exception is raised and caught using try...except.
