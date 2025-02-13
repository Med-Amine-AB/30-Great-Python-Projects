from random import choice

list_of_choices = ["rock", "paper", "scissors"]

print("Hello There are you ready for some fun? ")
while True:
    computer_rps: str = choice(list_of_choices)
    user_rps = input("Rock, Paper or Scissors? (type Exit to stop the Game) >> ").lower()
    if user_rps == "exit":
        print("have a good day")
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
        elif (user_rps == "rock" and computer_rps == "scissors") or \
                (user_rps == "scissors" and computer_rps == "paper") or \
                (user_rps == "paper" and computer_rps == "rock"):
            print("You win!")
        else:
            print("You lost!")


