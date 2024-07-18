import random
#import randint

#Print the Welcome message:

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
#answer = randint(1, 100)
#global difficulty
global easy
global hard
easy = 10
hard = 5
turns = 0


#Set the difficulty level
def game_challenge():
    global difficulty 
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return easy
        #print("You have 10 attempts remaining to guess the number.")
    elif difficulty == "hard":
        return hard
        #print("You have 5 attempts remaining to guess the number.")
    else:
        print("Invalid input. Please try again.")
turns = game_challenge()

#taking random inputs
def random_number():
    number = random.randint(1, 100)
    #initializing the number of guesses
    attempts = 0
    guessing = True
    while guessing:
        #taking input from the user
        guess = int(input("Make a guess: "))
        global turns
        #checking if the guess is correct
        if guess == number:
            print(f"You got it! The answer was {number}.")
            guessing = True
            #checking if the guess is too high
        elif guess > number:
            print("Too high.")
            print("Guess again")
            
            turns -= 1
            #checking if the guess is too low
        elif guess < number:
            print("Too low.")
            print("Guess again")
            turns -= 1
        #checking if the guess is correct
        if guess != number:
            attempts += 1
            print(f"You have {turns} attempts remaining to guess the number")
        #checking if the user has exceeded the number of guesses
        if attempts == 10 and difficulty == "easy":
            print("You've run out of guesses, you lose.")
        elif attempts == 5 and difficulty == "hard":
            print("You've run out of guesses, you lose.")
            break
random_number()

