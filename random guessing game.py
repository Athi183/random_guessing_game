import random
print("\t\t\tHello!!!!\nWelcome to the Game of Guessing\n")
n=random.randint(1,100)
print("**********Instructions**********\n----------------------------------\n")
print("->Guess the number from 1-100.\n->If guessed right, you WIN and the game stops")
print("->If guessed wrong, then the player can guess again\n->The player can guess 5 times\n")
print("Lets begin the Game!!!")
for i in range(5):
    guess=int(input("Make a guess : "))
    if (guess==n):
        print("\nWELL DONE!!!YOU WIN THE GAME")
        break
    elif (guess>n):
        print("\nTOO HIGH GUESS!!!TRY AGAIN")
    elif (guess<n):
        print("\nTOO LOW GUESS!!!TRY AGAIN")
    else:
        print("INVALID GUESS")

