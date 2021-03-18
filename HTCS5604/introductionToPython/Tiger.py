from introductionToPython.Feline import Feline

class Tiger(Feline):
    def __init__(self):
        self.weight = "heavy"

tiger = Tiger()
print(tiger.head())
print(tiger.eye())
print(tiger.leg())
print(tiger.ear())

feline = Feline()
print(feline.bite(self))
