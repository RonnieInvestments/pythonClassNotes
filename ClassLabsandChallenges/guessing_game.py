import random

# Computer guess
comp_value = random.randint(0,10) # generates random number 0 and 10 (inclusive)

# Player choice
player_value = int(input("Please choose a number between 0 and 10.\n"))

# if-else blocks for the results
if player_value == comp_value:
    print("You guessed correctly.")
elif player_value < comp_value:
    print(f"Your guess is too low. The correct number is {comp_value}.")
else:
    print(f"You guess is too high. The correct number is {comp_value}.")
