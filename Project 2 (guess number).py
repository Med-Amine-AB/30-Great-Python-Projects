import random

num: int = random.randint(1, 10)  # Generates a random integer between 1 and 10 (inclusive)



print("Guess a number between 1 to 10")

while True:
    try:
        user_num = int(input("Guess: "))
    except ValueError :
        print("Please insert an integer number!")
        continue

    if user_num == num:
        print("You guessed it!")
        break

    if user_num < num:
        print("Your number is Lower")
    else:
        print("Your number is higher")
