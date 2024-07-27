

from random import randint
EASY_LEVEL= 10
HARD_LEVEL= 5

def check_answer(guess,number,turns) :
    if number == guess:
        print(f"You got it! The answer was {number}")
    elif guess>number:
        print("Too High")
        return turns -1
    elif guess<number:
        print("Too Low")
        return turns -1
        
def check_difficulty():
    difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL   


def game():
    print("Welcome to the Number Guessing Game")
    print("I am thinking of number between 1 and 100")
    number= randint(1,100)

    turns=check_difficulty()
    

    guess=0
    while guess!= number:
        print(f"You have {turns} attempts remaining")
        guess=int(input("Make a guess: "))
        turns=check_answer(guess, number, turns)
        if turns==0:
            print("You've run out of guesses, you lose.")
            return

game()