# Rock, Paper, and Scissors Game
import random

print("1: Rock\n")
print("2: Paper\n")
print("3: Scissors\n")

player_choice = int(input("Please choose 1, 2, or 3:\n"))
computer_choice = random.randint(1, 3)

# Game logic
if player_choice == computer_choice:
    print("This is a tie.")
elif player_choice == 1 and computer_choice == 3:
    print("You win.")
elif player_choice == 2 and computer_choice == 1:
    print("You win.")
elif player_choice == 3 and computer_choice == 2:
    print("You win.")
elif player_choice == 3 and computer_choice == 1:
    print("Computer wins.")
elif player_choice == 2 and computer_choice == 3:
    print("Computer wins.")
elif player_choice == 1 and computer_choice == 2:
    print("Computer wins.")
else: 
    print("Invalid input.")