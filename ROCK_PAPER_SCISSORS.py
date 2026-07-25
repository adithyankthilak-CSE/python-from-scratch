import random
options = ("rock", "paper", "scissors")
player_score = 0
computer_score = 0
running = True
while running:
    player = None
    computer = random.choice(options)
    while player not in options :
        player=input("Enter rock, paper, or scissors: ").lower()
    print(f"player chose {player}")
    print(f"computer chose {computer}")
    if player == computer:
        print("Draw")
    elif player == "rock" and computer == "scissors":
        print("You win")
        player_score += 1
    elif player == "paper" and computer == "rock":
        print("You win")
        player_score += 1
    elif player == "scissors" and computer == "paper":
        print("You win")
        player_score += 1
    else:
        print("You lose")
        computer_score += 1
    play_again = input("Do you want to play again? (y/n): ").lower()
    if not play_again == "y":
        running = False
    print(f"Your score is {player_score}")
    print(f"Computer score is {computer_score}")
    if player_score > computer_score:
        print("You win")
    elif player_score == computer_score:
        print("Draw")
    else:
        print("You lose")
print("Thank you for playing")

