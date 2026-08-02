import random
words = ("apple","orange","banana","pineapple","nothing")
hangman_art = {
    0: (
        "  _______ ",
        " |/      |",
        " |",
        " |",
        " |",
        " |",
        " |",
        "_|___"
    ),
    1: (
        "  _______ ",
        " |/      |",
        " |      (_)",
        " |",
        " |",
        " |",
        " |",
        "_|___"
    ),
    2: (
        "  _______ ",
        " |/      |",
        " |      (_)",
        " |       |",
        " |       |",
        " |",
        " |",
        "_|___"
    ),
    3: (
        "  _______ ",
        " |/      |",
        " |      (_)",
        " |      \\|",
        " |       |",
        " |",
        " |",
        "_|___"
    ),
    4: (
        "  _______ ",
        " |/      |",
        " |      (_)",
        " |      \\|/",
        " |       |",
        " |",
        " |",
        "_|___"
    ),
    5: (
        "  _______ ",
        " |/      |",
        " |      (_)",
        " |      \\|/",
        " |       |",
        " |      /",
        " |",
        "_|___"
    ),
    6: (
        "  _______ ",
        " |/      |",
        " |      (_)",
        " |      \\|/",
        " |       |",
        " |      / \\",
        " |",
        "_|___"
    )}
def display_hangman(wrong_guess):
    for line in hangman_art[wrong_guess]:
        print(line)
def display_hints(hints):
    print(" ".join(hints))
def display_answers(answer):
    print(" ".join(answer))
def main():
    answer = random.choice(words)
    hints= ["_"] * len(answer)
    wrong_guess = 0
    guessed_letter = set()
    is_running = True

    while is_running:
        display_hangman(wrong_guess)
        display_hints(hints)
        guess = input("Enter your guess: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid letter.")
            continue

        if guess in guessed_letter:
            print("You already guessed this letter.")
            continue
        guessed_letter.add(guess)

        if guess in answer:
            for index in range(len(answer)):
                if answer[index] == guess:
                    hints[index] = guess
        else:
            wrong_guess += 1

        if "_" not in hints:
            display_hangman(wrong_guess)
            display_answers(answer)
            print("You win!")
            is_running = False
        elif wrong_guess == 6:
            print("you lose")
            is_running = False

if __name__=="__main__":
    main()