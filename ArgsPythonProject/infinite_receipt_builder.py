# Brain (functional logic)
def sum_bill(*prices):
    total = 0
    for price in prices:
        print("Adding items to bill...")
        total += price
    return total

# Getting user input
price_list = []

while True:
    user_input = input (f"Enter a price or type 'done' to finish")

    if user_input.lower() == 'done': 
        # convert every input into lower case
        break

    try:
        price = float(user_input) 
        # converts user input into a decimal number (float)
        price_list.append(price)
        # adds on item to the end of the list
    except ValueError:
        print("Invalid input. Please enter a number.")

print("Final price list is ", price_list) # To see the list

# Handshake - unpacking the list
final_total = sum_bill(*price)
# (*) use unpacking operator to pass all items in a price list

print(len(price_list)) # show the length of the price list
print(f"Total: {final_total:.2f}") # show total to 2 decimal places
