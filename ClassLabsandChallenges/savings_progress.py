# Savings tracker application
savings_goal = 10000
current_savings = int(input("Please enter your current savings:\n"))

# While loop
while current_savings < savings_goal:
    print("Keep saving towards your goal.")
    # Ask for additional savings amount
    additional_savings = int(input("Please enter amount you would like to add to your savings:\n"))
    # Update
    current_savings += additional_savings
    print(f"You have added {additional_savings}. You balance now is {current_savings}.")

# When loop exits - savings goal attained
print("Congratulations! You have reached your savings goals.")