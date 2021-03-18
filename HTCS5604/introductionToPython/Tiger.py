from introductionToPython.Feline import Feline

class Tiger(Feline):
    def __init__(self):
        self.weight = "heavy"

tiger = Tiger()
print(tiger.bite())

feline = Feline()
print(feline.eye())
