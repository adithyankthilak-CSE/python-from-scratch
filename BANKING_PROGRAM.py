def show_balance(balance):
    print(f"Your current balance is {balance:.2f}")
def deposite():
    amount=float(input("Enter amount:  "))
    if amount<0:
        print("Enter a valid amount")
        return deposite()
    else:
        return amount
def withdraw(balance):
    amount=float(input("Enter amount to withdraw:  "))
    if amount>balance:
        print("Insufficient Balance")
        return 0
    elif amount<0:
        print("Enter a valid amount")
        return 0
    else:
        return amount
def main():
    balance=0
    is_running=True

    while is_running:
        print("_____________________________")
        print("Welcome to Banking Program")
        print("_____________________________")
        print("Enter 1 for checking balance")
        print("Enter 2 for deposit")
        print("Enter 3 for withdraw")
        print("Enter 4 for Exit")
        print("_____________________________")

        choice=input("Enter your choice:")
        if choice=="1":
            show_balance(balance)
        elif choice=="2":
            balance+=deposite()
        elif choice=="3":
            balance-=withdraw(balance)
        elif choice=="4":
            is_running=False
        else:
            print("Enter a valid choice")
    print("************************************")
    print("Thank you for using Banking Program")
    print("************************************")
if __name__ == "__main__":
    main()