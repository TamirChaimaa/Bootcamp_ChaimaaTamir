from menu_item import MenuItem
from menu_manager import MenuManager

def show_user_menu():
    while True:
        print("\n--- Program Menu ---")
        print("V - View an item")
        print("A - Add an item")
        print("D - Delete an item")
        print("U - Update an item")
        print("S - Show the restaurant menu")
        print("Q - Quit")

        choice = input("Choose an option: ").strip().upper()

        if choice == "V":
            name = input("Enter the name of the item to search for: ")
            item = MenuManager.get_by_name(name)
            if item:
                print(f"Name: {item.name}, Price: {item.price}€")
            else:
                print("Item not found.")
        elif choice == "A":
            add_item_to_menu()
        elif choice == "D":
            remove_item_from_menu()
        elif choice == "U":
            update_item_from_menu()
        elif choice == "S":
            show_restaurant_menu()
        elif choice == "Q":
            print("Closing the program.")
            break
        else:
            print("Invalid choice. Please try again.")

def add_item_to_menu():
    name = input("Enter the item name: ")
    try:
        price = float(input("Enter the price: "))
        item = MenuItem(name, price)
        item.save()
        print("✔ Item added successfully.")
    except ValueError:
        print("Error: Price must be a number.")

def remove_item_from_menu():
    name = input("Enter the name of the item to delete: ")
    item = MenuItem(name, 0)  # Dummy price since it's not used
    item.delete()
    print("✔ Item deleted successfully.")

def update_item_from_menu():
    name = input("Enter the name of the item to update: ")
    item = MenuManager.get_by_name(name)
    if not item:
        print(" Item not found.")
        return

    new_name = input("Enter the new name: ")
    try:
        new_price = float(input("Enter the new price: "))
        item.update(new_name, new_price)
        print("✔ Item updated successfully.")
    except ValueError:
        print("Error: Price must be a number.")

def show_restaurant_menu():
    items = MenuManager.all_items()
    if not items:
        print("The menu is empty.")
    else:
        print("\n--- Restaurant Menu ---")
        for item in items:
            print(f"{item.name} : {item.price} €")

if __name__ == "__main__":
    show_user_menu()