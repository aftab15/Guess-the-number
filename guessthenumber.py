import random

randomNum = random.randint(1,100)
print(randomNum)
userGuess = None
guesses = 0

userName = input("Enter you Name : ")

while(randomNum != userGuess):
    userGuess = int(input("Guess the number: "))
    guesses += 1
    if userGuess == randomNum:
        print(f"You guessed right in {guesses} tries, Congrats {userName}")
    else:
        if userGuess > randomNum:
            print(f"Your guess is too high, try lower number")
        elif userGuess < randomNum:
            print(f"Your guess is too low, try higher number")
        

with open('highscore.txt', 'r') as hs:
    hScore = int(hs.read())

if guesses < hScore:
    with open('highscore.txt', 'w') as hs:
        hs.write(f'{userName} guessed in {guesses} tries')

