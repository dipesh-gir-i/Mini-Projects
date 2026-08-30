import random
def play_game():
    lucky_num = random.randint(1,50)

    while True:
        user_num = int(input("Guess a number between 1 and 50: "))
        if user_num == lucky_num:
            print("Congratulations! You guessed the correct number.")
            break
        elif user_num < lucky_num:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

    print("Thanks for playing the game!")

play_game()    