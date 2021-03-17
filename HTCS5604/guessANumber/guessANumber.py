import HTCS5604.guessANumber.library as g

myNum = g.generateANumber()

tryTime = 0
TotalTime = 10
guessNum = 0

while g.stillHaveChance(tryTime, TotalTime) and (not g.win(guessNum, myNum)):
    print("You have " + str(g.tryTimesLeft(tryTime, TotalTime)) + "chances left")
    guessNum = input("Please guess a Number")
    if g.isValidInput(guessNum):
        guessNum = int(guessNum)
        print(g.feedback(guessNum, myNum))
    else:
        print("The number should be between 0 and 100")
    tryTime = tryTime + 1

if not g.stillHaveChance(tryTime, TotalTime):
    print("You Lost!")
