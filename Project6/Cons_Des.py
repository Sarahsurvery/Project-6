# assign 6
# Constructors and Destructors
class Logger:
    def __init__(self):              # Constructor
        print("Logger object created.")

    def __del__(self):               # Destructor
        print("Logger object destroyed.")

log = Logger()
del log                              # Manually delete to trigger destructor
# Explanation:
#	__init__() runs when the object is created.
#	__del__() runs when the object is deleted.
