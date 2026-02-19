# Generating Password Logic
# Prompt users for input
password = input("Please, enter your password:\n")

# Check password length -> len function
min_length = 8 # Sets minimum password length
password_length = len(password)

if password_length < min_length:
    print(f"Password is too short. Minimum length is {min_length} characters.")
else:
    print("Good for a start.")

# Validating character types - upper case, lower case, has numbers, has symbols. 
# Set them to false initially.
has_upper_case = False
has_lower_case = False
has_number = False
has_symbol = False

# For loop to iterate through each character
for char in password:
    if char.isupper(): # A-Z
        has_upper_case = True
    elif char.islower(): # a-z
        has_lower_case = True
    elif char.isdigit(): # 0-9
        has_number = True
    else:
        has_symbol = not char.isalnum() # Negating this check identifies symbols -> not alphanumeric

# Evaluating password strength
# Gives recommendations 
if has_upper_case and has_lower_case and has_number and has_symbol:
    print("Strong password! Good mix of characters.")
else:
    print("Password could be improved. Consider including:")
    if not has_upper_case:
        print("- Upper case letters (A-Z)")
    if not has_lower_case:
        print("- Lower case letters (a-z)")
    if not has_number:
        print("- Numbers (0-9)")
    if not has_symbol:
        print("- Symbols (e.g, !@#$%&*)")