from random import choice

def run_game():
    word: str = choice(["hello", "am", "ab", "game"])
    user_name: str = input("What is your name? ")
    print(f"Welcome to the game, {user_name}")
    guessed: str = ""
    tries: int = 4
    while tries > 0:
        blanks: int  = 0
        print("Word: ", end = '')
        for char in word:
            if char in guessed:
                print(char, end = '')
            else:
                print("_", end = '')
                blanks += 1
        print()
        if blanks == 0:
            print("You've Got It!")
            break
        guess: str = input("Enter a letter: ")
        if len(guess) > 2 and guess != word:
            print("You can't play like this, you need to insert letter by letter or insert the correct word!")
            tries -= 1
            print(f"Sorry, that was wrong... ({tries} tries remaining)")
            continue
        if guess in guessed:
            print(f"You already used: '{guess}', please choose an other letter!")
            continue
        guessed += guess
        if guess not in word:
            tries -= 1
            print(f"Sorry, that was wrong... ({tries} tries remaining)")

            if tries == 0:
                print("No more tries remaining! You lost.")
                break

if __name__ == "__main__":
    run_game()
