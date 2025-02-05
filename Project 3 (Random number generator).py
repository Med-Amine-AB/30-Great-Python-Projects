import random
from typing import Any


def get_num(amount: int ) -> list[int]:
    if amount <= 0:
        print("please Chose a number that is grater or equal to 1")
        amount = 1
    l: list[Any] = []
    for i in range(amount):
        num: int = random.randint(1, 8)  # Generates a random integer between 1 and 8 (inclusive)
        l.append(num)
    return l

def main():
    l = []
    while True:
        try:
            n = input("How many number you want to generate (type exit to stop the programme): ")
            n = n.lower() # to make sure to treat "Exit" like "exit" and so one
            if n == "exit":
                break
            else:
                n = int(n)
        except ValueError:
            print("Please insert an integer number!")
            continue
        print(f"This is the {n} numbers generated: ")
        print(*get_num(n), sep = ", ") # the * used to unpack the list



if __name__ == "__main__":
    main()