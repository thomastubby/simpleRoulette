#roulette

import random
x = random.randint(0, 36)

bankRoll = 1000

def spinFunc():
    
    global black
    black = (2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35)
    global red
    red = (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36)
    
    if x in black:
        print("Black, " + str(x))
    if x in red:
        print("Red, " + str(x))
    if x == 0:
        print("Green, " + str(x))

def betFunc():

    #VARLIST#
    betInput = input("Tubby Roulette - Color, Number, or Third? ")

    betInput = betInput.lower().strip()

    colorList = ["green", "black", "red"]
    
    firstThird = range(1, 12)
    
    secondThird = range(13, 24)

    thirdThird = range(25, 36)

    thirdList = ["first", "second", "third"]
    #########
    if betInput == "color":
        
        color = input("Which color would you like to bet on? ")

        color = color.lower().strip()

        if color == colorList[0]:
            betPrompt = input("How much would you like to bet? ")
            spinFunc()
            if x == 0:
                print("You won" + " $" + str(betPrompt) + "!")
                newBankRoll = int(bankRoll) + int(betPrompt)
                print("Your bankroll is now" + " $" + str(newBankRoll))
            if x != 0:
                print("You lost " + str(betPrompt) + "!")
                newBankRoll = int(bankRoll) - int(betPrompt)
                print("Your bankroll is now" + " $" + str(newBankRoll))

        if color == colorList[1]:
            betPrompt = input("How much would you like to bet? ")
            spinFunc()
            if x in black:
                print("You won" + " $" + str(betPrompt) + "!")
                newBankRoll = int(bankRoll) + int(betPrompt)
                print("Your bankroll is now" + " $" + str(newBankRoll))
            else:
                print("You lost " + str(betPrompt) + "!")
                newBankRoll = int(bankRoll) - int(betPrompt)
                print("Your bankroll is now" + " $" + str(newBankRoll))

        if color == colorList[2]:
            betPrompt = input("How much would you like to bet? ")
            spinFunc()
            if x in red:
                print("You won" + " $" + str(betPrompt) + "!")
                newBankRoll = int(bankRoll) + int(betPrompt)
                print("Your bankroll is now" + " $" + str(newBankRoll))
            else:
                print("You lost " + str(betPrompt) + "!")
                newBankRoll = int(bankRoll) - int(betPrompt)
                print("Your bankroll is now" + " $" + str(newBankRoll))
        """else:
            tryAgain = input("Invalid selection, try again? Y/N ")
            if tryAgain in ["yes", "y"]:
                betFunc()
            else:
                print("Cancelled.")"""


    if betInput == "third":
        
        thirds = input("Which third would you like to bet on? ")

        thirds = thirds.lower().strip()

        if thirds == thirdList[0]:
            betPrompt = input("How much would you like to bet? ")
            spinFunc()
            if x in firstThird:
                print("You won" + " $" + str(betPrompt) + "!")
                newBankRoll = int(bankRoll) + (int(betPrompt) * 2)
                print("Your bankroll is now" + " $" + str(newBankRoll))
            else:
                print("You lost " + str(betPrompt) + "!")
                newBankRoll = int(bankRoll) - int(betPrompt)
                print("Your bankroll is now" + " $" + str(newBankRoll))
        
        if thirds == thirdList[1]:
            betPrompt = input("How much would you like to bet? ")
            spinFunc()
            if x in secondThird:
                print("You won" + " $" + str(betPrompt) + "!")
                newBankRoll = int(bankRoll) + (int(betPrompt) * 2)
                print("Your bankroll is now" + " $" + str(newBankRoll))
            else:
                print("You lost " + str(betPrompt) + "!")
                newBankRoll = int(bankRoll) - int(betPrompt)
                print("Your bankroll is now" + " $" + str(newBankRoll))

        if thirds == thirdList[2]:
            betPrompt = input("How much would you like to bet? ")
            spinFunc()
            if x in thirdThird:
                print("You won" + " $" + str(betPrompt) + "!")
                newBankRoll = int(bankRoll) + (int(betPrompt) * 2)
                print("Your bankroll is now" + " $" + str(newBankRoll))
            else:
                print("You lost " + str(betPrompt) + "!")
                newBankRoll = int(bankRoll) - int(betPrompt)
                print("Your bankroll is now" + " $" + str(newBankRoll))


    if betInput.lower() == "number":
        
        number = input("Which number would you like to bet on? ")

        number = number.strip()
        
        if 36 >= int(number) >= 0:
            betPrompt = input("How much would you like to bet? ")
            spinFunc()
            if x == int(number):
                print("You won" + " $" + str(betPrompt) + "!")
                newBankRoll = int(bankRoll) + (int(betPrompt) * 35)
                print("Your bankroll is now" + " $" + str(newBankRoll))
            if x != int(number):
                print("You lost " + str(betPrompt) + "!")
                newBankRoll = int(bankRoll) - int(betPrompt)
                print("Your bankroll is now" + " $" + str(newBankRoll))
    

#INVALID OPTIONS
    if betInput.lower() not in ["color", "number", "third"]:
        tryAgain = input("Invalid selection, try again? Y/N ")
        if tryAgain in ["yes", "y"]:
            betFunc()
        else:
            print("Cancelled.")           

betFunc()

#TO DO
"""

-Make outcome affect original bankroll

"""