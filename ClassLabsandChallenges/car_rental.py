# Inputs - number of days, daily rental price, includes weekend
number_of_days = int(input("Please enter the number of days: "))
daily_rental_price = int(input("What is the current daily rental price: "))
includes_weekend = input("Does the rental period include weekend? (yes/no)")

# Base cost
base_cost = number_of_days * daily_rental_price

# Weekend discounts
if includes_weekend == "yes":
    total_cost = base_cost * 0.9 # gives 10 percent discount
    print(f"The total cost of the car rental for {number_of_days} days at ${daily_rental_price} per day and with a 10% weekend discount comes to {total_cost}.")
else:
    print(f"The total cost of the car rental for {number_of_days} days at ${daily_rental_price} per day comes out to {base_cost}.")