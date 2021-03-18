#roulette

import random
x = random.randint(0, 36)

bankRoll = 1000

#VARLIST#
colorList = ["green", "black", "red"]

firstThird = range(1, 12)

secondThird = range(13, 24)

thirdThird = range(25, 36)

thirdList = ["first", "second", "third"]
#########

#Defines betting amount
def roulette():
    global betPrompt
    betPrompt = input("Tubby Roulette - Color, Number, or Third? ")

    betPrompt = betPrompt.lower().strip()
    
    betFunc()

def betPriceFunc():
    global betAmount
    betAmount = input("How much would you like to bet? ")
    spinFunc()

#Win/Lose for color
def colorWin():
    print("You won" + " $" + str(betAmount) + "!")
    newBankRoll = int(bankRoll) + int(betAmount)
    print("Your bankroll is now" + " $" + str(newBankRoll))
    playAgainFunc()

def colorLose():
    print("You lost " + str(betAmount) + "!")
    newBankRoll = int(bankRoll) - int(betAmount)
    print("Your bankroll is now" + " $" + str(newBankRoll))
    playAgainFunc()

#Win/Lose for third
def thirdWin():
    print("You won" + " $" + str(betAmount) + "!")
    newBankRoll = int(bankRoll) + (int(betAmount) * 2)
    print("Your bankroll is now" + " $" + str(newBankRoll))
    playAgainFunc()

def thirdLose():
    print("You lost " + str(betAmount) + "!")
    newBankRoll = int(bankRoll) - int(betAmount)
    print("Your bankroll is now" + " $" + str(newBankRoll))
    playAgainFunc()

#Win/Lose for number
def numberWin():
    print("You won" + " $" + str(betAmount) + "!")
    newBankRoll = int(bankRoll) + (int(betAmount) * 35)
    print("Your bankroll is now" + " $" + str(newBankRoll))
    playAgainFunc()

def numberLose():
    print("You lost " + str(betAmount) + "!")
    newBankRoll = int(bankRoll) - int(betAmount)
    print("Your bankroll is now" + " $" + str(newBankRoll))
    playAgainFunc()

#Generates random number assigned to color, "spins"
def spinFunc():
    
    global black
    black = (2, 4, 6, 8, 10, 11, 13, 15, 17, 
             20, 22, 24, 26, 28, 29, 31, 33, 35)
    global red
    red = (1, 3, 5, 7, 9, 12, 14, 16, 18, 
             19, 21, 23, 25, 27, 30, 32, 34, 36)
    
    if x in black:
        print("Black, " + str(x))
    if x in red:
        print("Red, " + str(x))
    if x == 0:
        print("Green, " + str(x))

#Allows user to play again
def playAgainFunc():
    
    playAgain = input("Play again? Y/N ")

    playAgain == playAgain.lower()
    
    if playAgain in ("yes", "y"):
        roulette()
    else:
        pass
    

#Roulette game
def betFunc():

    if betPrompt == "color":
        
        color = input("Which color would you like to bet on? ")

        color = color.lower().strip()

        if color == colorList[0]:
            betPriceFunc()
            if x == 0:
                colorWin()
            if x != 0:
                colorLose()

        if color == colorList[1]:
            betPriceFunc()            
            if x in black:
                colorWin()
            else:
                colorLose()

        if color == colorList[2]:
            betPriceFunc()
            if x in red:
                colorWin()
            else:
                colorLose()

    if betPrompt == "third":
        
        thirds = input("Which third would you like to bet on? ")

        thirds = thirds.lower().strip()

        if thirds == thirdList[0]:
            betPriceFunc()
            if x in firstThird:
                thirdWin()
            else:
                thirdLose()
        
        if thirds == thirdList[1]:
            betPriceFunc()
            if x in secondThird:
                thirdWin()
            else:
                thirdLose()

        if thirds == thirdList[2]:
            betPriceFunc()
            if x in thirdThird:
                thirdWin()
            else:
                thirdLose()


    if betPrompt.lower() == "number":
        
        number = input("Which number would you like to bet on? ")

        number = number.strip()
        
        if 36 >= int(number) >= 0:
            betPriceFunc()
            if x == int(number):
                numberWin()
            if x != int(number):
                numberLose()
    

#INVALID OPTIONS
    if betPrompt.lower() not in ["color", "number", "third"]:
        tryAgain = input("Invalid selection, try again? Y/N ")
        if tryAgain in ["yes", "y"]:
            betFunc()
        else:
            print("Cancelled.")           

roulette()