# roulette

import random

#######
bankRoll = 1000
#######

choiceList = ["color", "third", "number"]

colorList = ["green", "black", "red"]

thirdList = ["first", "second", "third"]

firstThird = range(1, 12)

secondThird = range(13, 24)

thirdThird = range(25, 36)

#########


def bankrollLose():
    print("You lost " + str(betAmount) + "!")
    betLose = (int(bankRoll) - int(betAmount))
    print("Your bankroll is now" + " $" + str(betLose))


def betPriceFunc():
    global betAmount
    betAmount = input("How much would you like to bet? ")
    spinFunc()


# Win/Lose for color
def colorWin():
    print("You won" + " $" + str(betAmount) + "!")
    betWin = bankRoll + int(betAmount)
    print("Your bankroll is now" + " $" + str(betWin))
    playAgainFunc()


def colorLose():
    bankrollLose()
    playAgainFunc()


# Win/Lose for third
def thirdWin():
    print("You won" + " $" + str(int(betAmount) * 2) + "!")
    betWin = bankRoll + (int(betAmount) * 2)
    print("Your bankroll is now" + " $" + str(betWin))
    playAgainFunc()


def thirdLose():
    bankrollLose()
    playAgainFunc()


# Win/Lose for number
def numberWin():
    print("You won" + " $" + str(int(betAmount) * 35) + "!")
    betWin = bankRoll + (int(betAmount) * 35)
    print("Your bankroll is now" + " $" + str(betWin))
    playAgainFunc()


def numberLose():
    bankrollLose()
    playAgainFunc()


# Invalid Selection
def invalidFunc():
    tryAgain = input("Invalid selection, try again? Y/N ")
    if tryAgain in ["yes", "y"]:
        rouletteFunc()
    else:
        print("Cancelled.")


# Generates random number assigned to color, "spins"
def spinFunc():
    
    global x
    x = random.randint(0, 36)
    
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


# Roulette game
def rouletteFunc():
    
    global betPrompt
    betPrompt = input("Tubby Roulette - Color, Number, or Third? ")

    betPrompt = betPrompt.lower().strip()

    if betPrompt == choiceList[0]:
        
        color = input("Which color would you like to bet on? ")

        color = color.lower().strip()

        if color == colorList[0]:
            betPriceFunc()
            if x == 0:
                colorWin()
            if x != 0:
                colorLose()

        elif color == colorList[1]:
            betPriceFunc()            
            if x in black:
                colorWin()
            else:
                colorLose()

        elif color == colorList[2]:
            betPriceFunc()
            if x in red:
                colorWin()
            else:
                colorLose()

    if betPrompt == choiceList[1]:
        
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


    if betPrompt.lower() == choiceList[2]:
        
        number = input("Which number would you like to bet on? ")

        number = number.strip()
        
        if number.isnumeric():
            
            if 36 < int(number):
                print("Number is too high; pick a number from 0 to 36")
                invalidFunc()
            
            if 36 >= int(number) >= 0:
                betPriceFunc()
                if x == int(number):
                    numberWin()
                if x != int(number):
                    numberLose()
            if 0 > int(number):
                print("Number is too low; pick a number from 0 to 36")
                invalidFunc()
        else:
            print(str(number) + " " + "is not numeric.")
            invalidFunc()
    
    else:
        invalidFunc()


# Allows user to play again
def playAgainFunc():
    
    playAgain = input("Play again? Y/N ")

    playAgain == playAgain.lower().strip()
    
    if playAgain in ("yes", "y"):
        rouletteFunc()
    elif playAgain in ("no", "n"):
        print("Cancelled.")
    else:
        pass
        

# INVALID OPTIONS
    
    if betPrompt.lower() not in choiceList:
        invalidFunc()         

rouletteFunc()