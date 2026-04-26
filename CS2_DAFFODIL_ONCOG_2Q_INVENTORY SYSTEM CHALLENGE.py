# Inventory System Challenge
# Author: Josue Ruch III G. OnCOG
# Description: Manages product names and prices using parallel arrays

product_names = []
product_prices = []

def add_product():
    name = input("Enter product name: ").strip()
    while True:
        try:
            price = float(input("Enter product price: "))
            if price <= 0:
                print("Price cannot be less than or equal to 0!")
            else:
                break
        except ValueError:
            print("Invalid price. Please enter a number.")
    product_names.append(name)
    product_prices.append(price)
    print(f"{name} added successfully!\n")

def display_products():
    if not product_names:
        print("Add items first!\n")
        return
    for i in range(len(product_names)):
        print(f"{i+1}. {product_names[i]} - {product_prices[i]:.2f}")
    print()

def update_price():
    if not product_names:
        print("Add items first!\n")
        return
    name = input("Enter item name to update price: ").strip()
    if name in product_names:
        index = product_names.index(name)
        while True:
            try:
                new_price = float(input("Enter new price: "))
                if new_price <= 0:
                    print("Price must be greater than 0.")
                else:
                    break
            except ValueError:
                print("Invalid price. Please enter a number.")
        product_prices[index] = new_price
        print(f"{name} updated to {new_price:.2f}\n")
    else:
        print("Item not found!\n")

def search_product():
    if not product_names:
        print("Add items first!\n")
        return
    name = input("Enter item: ").strip()
    if name in product_names:
        index = product_names.index(name)
        print(f"{product_names[index]} - {product_prices[index]:.2f}\n")
    else:
        print("Product not found!\n")

def total_inventory_value():
    if not product_prices:
        print("Add items first!\n")
        return
    total = sum(product_prices)
    print(f"Total inventory value: {total:.2f}\n")

def menu():
    while True:
        print("[1] Add product")
        print("[2] Display all products")
        print("[3] Update a price")
        print("[4] Search for a product")
        print("[5] Total inventory value")
        print("[6] Exit")
        try:
            choice = int(input("Enter choice: "))
            print()
            if choice == 1:
                add_product()
            elif choice == 2:
                display_products()
            elif choice == 3:
                update_price()
            elif choice == 4:
                search_product()
            elif choice == 5:
                total_inventory_value()
            elif choice == 6:
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")

# Start the program
menu()