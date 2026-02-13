# Rigid thinking
'''
Function to sum exactly 3 items 


def sum_receipts(a, b, c):
    sum = a + b + c
    print("Sum is ", sum)
    return sum

sum_receipts(10, 20, 30) # Sum is 60

sum_receipts(10, 20) 
# Error missing 1 required positional argument
# If a customer buys two items, 
# the program crashes because it's missing the third.

sum_receipts(10, 20, 20, 30) 
# sum_receipts() takes 3 positional arguments but 4 were given
# If a customer buys four items, 
# the program ignores the fourth because it has no "slot" for it.

'''
# Solving the issue
def sum_receipts(*args):
    print(args)
    sum = 0
    
    for n in args:
        sum = sum + n
    print("Sum is ", sum)
    
def main():
    prices_list = []

    while True:
        user_input = input("Enter a price of type 'done' to end").lower()

        if user_input == 'done':
            break

        # safety check
        try:
            price = float(user_input)
            prices_list.append(price)
        except Exception as e:
            print("Invalid input. Please enter a number.")
            # print(e) # see the error
            print(prices_list)
    sum_receipts(*prices_list)

main()