# Track steps and motivate users
goal_steps = 10000

while True:
    user_input = input("Enter your current steps or 'q' to quit.\n")

    if user_input.lower() == 'q':
        break

    try:
        current_steps = int(user_input)

        if current_steps < 0:
            print("Please enter a valid number")
            continue

        if current_steps >= goal_steps:
            print("Congratulations! You reached your goal.")
        else:
            remaining = goal_steps - current_steps
            print(f"Keep going! Only {remaining} steps to go!")
    except ValueError:
        print("Invalid entry")


