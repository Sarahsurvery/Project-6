# assign 12
#  Static Method
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

print(TemperatureConverter.celsius_to_fahrenheit(25))
# Explanation:
#	No access to class or instance data — pure function.
