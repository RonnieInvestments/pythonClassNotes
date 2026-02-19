# Managing Inventory Data using Dictionaries
'''
By utilizing dictionaries, you'll create a program that allows users to:
   -> Add new products to the inventory.
   -> View existing product information (name, quantity, price).
   -> Update product quantities.
   -> Remove products from the inventory (if out of stock).
'''
# Set up the inventory dictionary
inventory = {}

# Adding products
def add_product(inventory, name, quantity, price):
    # Check if the product already exists
    if name not in inventory:
        # Add new product with quantity and price
        inventory[name] = {
            "quantity": quantity,
            "price": price
        }
    else:
        # Print entry message
        print(f"Product '{name}' already exists in inventory.")

# Viewing product information
def view_product(name):
    # Check if name exists and retrieve a nested dictionary (if exists)
    if name in inventory:
        product_information = inventory[name]
        print(f"Product: {name}")
        print(f"\tQuantity: {product_information['quantity']}")
        print(f"\tPrice: ${product_information['price']:.2f}")  # Format price with 2 decimal places
    else: # Does not exist -> product not found
        print(f"Product '{name}' not found in inventory.")

# Updating inventory information
def update_quantity(name, new_quantity):
    if name in inventory: # if it exists update the quantity value
        inventory[name]["quantity"] = new_quantity
        print(f"Product '{name}' quantity updated.")
    else: # does not exist -> indicate for missing product
        print(f"Product '{name}' not found in inventory.")

# Remove a product
def remove_product(name):
    if name in inventory: # check if name exists
        inventory.pop(name) # remove name using pop method
        print(f"Product '{name}' removed from inventory.")
    else:
        print(f"Product '{name}' not found in inventory.")

# Main program function/logic
def main():
    while True:
        print("\nInventory Management System")
        print("1. Add New Product")
        print("2. View Product Information")
        print("3. Update Product Quantity")
        print("4. Remove Product")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter product name: ")
            quantity = int(input("Enter initial quantity: "))
            price = float(input("Enter product price: "))
            add_product(name, quantity, price)
        elif choice == "2":
            name = input("Enter product name to view: ")
            view_product(name)
        elif choice == "3":
            name = input("Enter product name to update: ")
            new_quantity = int(input("Enter new quantity: "))
            update_quantity(name, new_quantity)
        elif choice == "4":
            name = input("Enter product name to remove: ")
            remove_product(name)
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

