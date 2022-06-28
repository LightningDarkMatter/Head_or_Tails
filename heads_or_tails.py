import random

computer_choice = random.randint(1, 2)
if computer_choice == 1:
    computer_choice = "heads"
else:
    computer_choice = "tails"

print("Lest's flip a coin!")
user_choice = input("Heads or tails? ")
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "heads":
    if computer_choice == "tails":
        print("You win!")
    else:
        print("You lose!")
elif user_choice == "tails":
    if computer_choice == "heads":
        print("You win!")
    else:
        print("You lose!")