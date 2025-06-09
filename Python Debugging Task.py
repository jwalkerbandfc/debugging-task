inventory = {}


def add_item():
    name = input("Enter item name: ").strip()

    if name in inventory:
        print("Item already exists. Use edit option to update.")
        return

    perishable_input = input("Is the item perishable? (yes/no): ").strip().lower()
    perishable = perishable_input == "yes"

    try:
        qty = int(input("Enter quantity: ").strip())
    except ValueError:
        print("Invalid quantity. Please enter a number.")
        return

    description = input("Enter item description: ").strip()

    inventory[name] = {"perishable": perishable, "qty": qty, "description": description}

    print(f"Item {name} added successfully.")


def view_inventory():
    if not inventory:
        print("\nInventory is empty.")
        return

    print("\nCurrent Inventory:")
    for item, details in inventory.items():
        perishable_status = "Yes" if details["perishable"] else "No"
        print(
            f"- {item}: Perishable: {perishable_status}, Qty: {details['qty']}, Description: {details['description']}"
        )
    print()


def edit_item():
    for item in inventory:
        print(f"- {item}")
    name = input("Enter the name of the item to edit: ").strip()
    if name not in inventory:
        print("Item not found. Please add the item first.")
        return
    perishable_input = input("Is the item perishable? (yes/no): ").strip().lower()
    perishable = perishable_input == "yes"
    try:
        qty = int(input("Enter new quantity: ").strip())
    except ValueError:
        print("Invalid quantity. Please enter a number.")
        return
    description = input("Enter new item description: ").strip()
    inventory[name] = {
        "perishable": perishable,
        "qty": qty,
        "description": description
    }
    print(f"Item {name} updated successfully.")


def remove_item():
    for item in inventory:
        print(f"- {item}")
    name = input("Enter the name of the item to remove: ").strip()
    if name not in inventory:
        print("Item not found. Nothing removed.")
        return
    del inventory[name]
    print(f"Item {name} removed successfully.")


def main():
    while True:
        print("\nInventory Management System")
        print("1. View Inventory")
        print("2. Add Item")
        print("3. Edit Item")
        print("4. Remove Item")
        print("5. Quit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_inventory()
        elif choice == "2":
            add_item()
        elif choice == "3":
            edit_item()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            print("Exiting Inventory System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


# Call Main Menu
main()
