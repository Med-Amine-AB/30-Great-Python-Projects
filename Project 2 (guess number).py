import random

num = random.randint(1, 10)  # Generates a random integer between 1 and 10 (inclusive)

print("Guess a number between 1 to 10")
user_num = int(input("Guess: "))

while user_num != num:
    if user_num < num:
        print("Your number is Lower")
        user_num = int(input("Guess: "))
    else:
        print("Your number is higher")
        user_num = int(input("Guess: "))
print("You guessed it!")
