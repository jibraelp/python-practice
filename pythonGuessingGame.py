
import random

print("I’m thinking of a number in the range 0-50. You have five tries to guess it.")
randomNumber = random.randrange(0,50)
guess = False
guessNumber = 0


while guess == False:
    userGuess = int(input("Guess {}: ".format(guessNumber)))
    if guessNumber == 5:
        print ("Game over! The correct answer was {}.".format(randomNumber))
        break
    if userGuess == randomNumber:
        guess = True
        print("You are right! I was thinking of {}!".format(randomNumber))
    elif userGuess > randomNumber:
        print("{} is too high.".format(userGuess))
        guessNumber += 1
    elif userGuess < randomNumber:
        print("{} is too low.".format(userGuess))
        guessNumber += 1
    
