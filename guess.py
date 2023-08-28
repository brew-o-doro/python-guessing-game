import random

num = random.randint(1,10) # numbers 1 - 10

while True:
    guess = input("Pick a number from 1 to 10: ")
    guess = int(guess)
    print(guess)

    if guess < num:
        print("Too Low")
    elif guess > num:
        print("Too High!")
    else:
        print("You Won!!!")
        play_again = input("Do you want to play again? (y/n) ")

        if play_again == "y":
            
            num = random.randint(1,10) # numbers 1 - 10
            guess = None
        else: 
            print("Thanks for playing")
            break

   
