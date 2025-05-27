# assign 13
# Composition
class Engine:
    def start(self):
        print("Engine starting...")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_engine(self):
        self.engine.start()

e = Engine()
c = Car(e)
c.start_engine()
# Explanation:
#	Composition: Car "has-a" Engine
