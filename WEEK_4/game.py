import random

def get_positive_integer(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
        except ValueError:
            pass  # ignore invalid input and re-prompt

def main():
    # 1. Prompt for level
    level = get_positive_integer("Level: ")

    # 2. Generate secret number between 1 and level
    secret = random.randint(1, level)

    # 3. Let the user guess until they get it right
    while True:
        guess = get_positive_integer("Guess: ")

        if guess < secret:
            print("Too small!")
        elif guess > secret:
            print("Too large!")
        else:
            print("Just right!")
            break  # Exit the loop and program

if __name__ == "__main__":
    main()
