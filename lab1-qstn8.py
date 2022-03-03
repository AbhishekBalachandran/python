import random

randomNumber = random.randint(1,9)
# print(randomNumber)
guessedNumber = int(input("Guess a number and enter : "))
if (randomNumber == guessedNumber):
    print("The number you guessed matches the randomnly selected number.")
elif (randomNumber < guessedNumber):
    print("The number you guessed is too high than the randomnly selected number.")
else:
    print("The number you guessed is too low than the randomnly selected number.")