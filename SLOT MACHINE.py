import random


def spin_row():
    symbols = ['🥲', '🤩', '😁', '😂', '😒']
    result = []
    for _ in range(3):
        result.append(random.choice(symbols))
    return result


def print_row(row):
    print("|".join(row))


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🥲':
            return bet * 3
        elif row[0] == '🤩':
            return bet * 4
        elif row[0] == '😁':
            return bet * 5
        elif row[0] == '😂':
            return bet * 6
        elif row[0] == '😒':
            return bet * 7
    return 0


def main():
    balance = 100

    print("*******************************")
    print(" Welcome to Python Slot Machine ")
    print(" Symbols: 🥲 🤩 😁 😂 😒 ")
    print("*******************************")

    while balance > 0:
        print(f"\nYour balance: {balance}")

        bet = input("Enter your bet: ")

        if not bet.isdigit():
            print("Please enter a valid number.")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds.")
            continue

        if bet <= 0:
            print("Bet must be greater than 0.")
            continue

        balance -= bet

        print("\nSpinning...\n")
        row = spin_row()
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"\n🎉 You won {payout}!")
        else:
            print("\n😢 You lost!")

        balance += payout
        while True:
            play_again = input("Would you like to play again? (y/n): ").lower()

            if play_again == 'y':
                break
            elif play_again == 'n':
                print("Thanks for playing!")
                return
            else:
                print("Please enter 'y' or 'n'.")

    print(f"Game Over! Your balance: {balance}.")


if __name__ == "__main__":
    main()