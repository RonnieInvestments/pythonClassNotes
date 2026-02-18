# Coin collections game
# Define your variables
coin_milestones = [100, 500, 1000]
messages = [
    "Wow! You earned 100 coins!", 
    "Excellent! You've reached 500 coins!", 
    "Fantastic! You're a coin master!"
]

# Initialize the for loop
for milestone in coin_milestones:
    # Access current milestone and its corresponding message
    current_message = messages[coin_milestones.index(milestone)]
    # Show output
    print(current_message)