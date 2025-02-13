from random import choice

list_of_choices = ["rock", "paper", "scissors"]

ai_scour: int = 0
user_scour: int = 0
def display_scour(ai, user):
    print("--------")
    print(f"Your Scour: {user}")
    print(f"Ai Scour: {ai}")
    print("--------")

print("Hello There are you ready for some fun? ")
while True:
    computer_rps: str = choice(list_of_choices)
    user_rps = input("Rock, Paper or Scissors? (type Exit to stop the Game) >> ").lower()
    if user_rps == "exit":
        print("Thanks for Playing!")
        break
    elif user_rps not in list_of_choices:
        print("invade input: Please choose one of Rock, Paper or Scissors")
        continue
    else:
        print("========")
        print("You: ", user_rps)
        print("AI: ", computer_rps)
        print("========")
        if user_rps == computer_rps:
            print("It's a tie!")
            display_scour(ai_scour, user_scour)
        elif (user_rps == "rock" and computer_rps == "scissors") or \
                (user_rps == "scissors" and computer_rps == "paper") or \
                (user_rps == "paper" and computer_rps == "rock"):
            print("You win!")
            user_scour += 1
            display_scour(ai_scour, user_scour)
        else:
            print("Ai win!")
            ai_scour += 1
            display_scour(ai_scour, user_scour)


