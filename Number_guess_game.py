import random
low_num = 1
high_num = 1000
answer = random.randint(low_num, high_num)
guesses = 0
is_running = True
print(f"Enter a number between {low_num} and {high_num}")
while is_running:
    guess=input(f"Enter a number between {low_num} and {high_num}: ")
    if guess.isdigit():
        guess=int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("out of range")
        elif guess < answer:
            print("Your guess is too low")
        elif guess > answer:
            print("Your guess is too high")
        else:
            print(f"your answer is correct {answer}")
            print(f"number of guess ={guess}")
            is_running = False
    else:
        print(f"your answer is invalid")
        print(f"Enter a number between {low_num} and {high_num}")