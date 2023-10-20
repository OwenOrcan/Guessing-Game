import random

cards = ["ace of spades","king of spades","queen of spades", "jack of spades"]
print("                GUESSING GAME!                        ")
while True:
    try:
        balance = int(input("Deposit Balance: "))
        if balance <= 0:
            print("Balance Cannot Be Negative or 0")
        elif balance > 1000:
            print("Maximum Deposit Amount Is $1000.")
        else:
            break
    except Exception:
        print("Please Check Your Money And Try Again.")
        continue

while True:
    if balance == 0:
        print("You Do Not Have Any Money.")
        break
    try:
        print("Dealers Hand:\n", cards)
        print(f"Current Balance: ${balance}")
        random_card = random.choice(cards)
        try:
            bet = int(input("Bet: "))
        except Exception:
            print("!!!!!!!!!!!!!!!!!Please Try Again!!!!!!!!!!!!!!!!!!!!!!!!!!")
            continue
        if bet > balance:
            print("!!!!!!!!!!!!!!!!Unsufficent Funds!!!!!!!!!!!!!!!!!!!!!")
            continue
        if bet < 0:
            print("Cannot Bet 0!")
            continue
        guess = input("Guess The Card: ").lower()
        if guess == random_card:
            print("CORRECT!")
            balance = bet * 2
            print(f"Your balance is ${balance}")

            user_continue_choice = str(input("Do you want to continue? y/n ")).lower()
            if user_continue_choice == "y":
                continue
            elif user_continue_choice == "n":
                print("See You!")
                break
            else:
                print("Could Not Identify Response, Quitting.")
                break
        else:
            balance = 0
            print(f"Sorry, the card was {random_card.upper()}")
            break

    except EOFError:
        print("Goodbye!")
        break




