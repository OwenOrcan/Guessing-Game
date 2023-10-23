import os
import random

os.system('color 2')

playing = True


cards = ["ace of spades","king of spades","queen of spades", "jack of spades"]
cards2 = ["ace of hearts","king of hearts","queen of hearts", "jack of hearts"]
print("                                    GUESS!                      ")
while playing:
    try:
        balance = int(input("Deposit Balance: "))
        if balance <= 0:
            print("Cannot Deposit Amounts That Are Less Than 0.")
        elif balance > 1000:
            print("Maximum Deposit Amount Is $1000.")
        else:
            break
    except Exception:
        print("Could Not Complete Request, Maybe Check Your Bank Account Again?")
        continue

while playing:
    if balance == 0:
        input("You Do Not Have Any Money Left, Press Enter To Quit.....")
        break
    try:
        choose_deck = random.randint(1,2)
        if choose_deck == 1:
            hand = cards
        elif choose_deck == 2:
            hand = cards2
        print("Dealers Hand:\n", hand)
        print(f"Current Balance: ${balance}")
        random_card = random.choice(hand)
        try:
            bet = int(input("Bet: "))
        except Exception:
            print("!!!!!!!!!!!!!!!!!Please Try Again!!!!!!!!!!!!!!!!!!!!!!!!!!")
            continue
        if bet > balance:
            print("!!!!!!!!!!!!!!!!Insufficent Funds!!!!!!!!!!!!!!!!!!!!!")
            continue
        if bet < 0:
            print("Cannot Bet $0!")
            continue
        guess = input("Guess The Card: ").lower().strip()
        if guess == random_card:
            print("CORRECT!")
            balance = balance - bet
            balance = balance + (bet*2)
            print(f"Your balance is now ${balance}")
            user_continue_choice = str(input("Do you want to continue? y/n ")).lower().strip()
            if user_continue_choice == "y":
                continue
            elif user_continue_choice == "n":
                print("See You!")
                input("Press Enter To Quit.....")
                break
            else:
                print("Could Not Identify Response, Quitting.")
                input("Press Enter To Quit.....")
                break
        else:
            balance = balance - bet
            print(f"Sorry, the card was {random_card.upper()}")
            input("Press Enter To Continue.....")
            continue

    except EOFError:
        input("Press Enter To Quit.")
        break




