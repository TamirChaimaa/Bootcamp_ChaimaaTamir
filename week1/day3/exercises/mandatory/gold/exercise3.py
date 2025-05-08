# Exercise 3: Restaurant Menu Manager
class MenuManager:
    def __init__(self):
        self.menu = [
            {"name": "Soup", "price": 10, "spice": "B", "gluten": False},
            {"name": "Hamburger", "price": 15, "spice": "A", "gluten": True},
            {"name": "Salad", "price": 18, "spice": "A", "gluten": False},
            {"name": "French Fries", "price": 5, "spice": "C", "gluten": False},
            {"name": "Beef bourguignon", "price": 25, "spice": "B", "gluten": True}
        ]

    def add_item(self, name, price, spice, gluten):
        new_dish = {
            "name": name,
            "price": price,
            "spice": spice,
            "gluten": gluten
        }
        self.menu.append(new_dish)
        print(f"The dish '{name}' has been added to the menu.")

    def update_item(self, name, price, spice, gluten):
        for dish in self.menu:
            if dish["name"].lower() == name.lower():
                dish["price"] = price
                dish["spice"] = spice
                dish["gluten"] = gluten
                print(f"The dish '{name}' has been updated.")
                return
        print(f"Error: The dish '{name}' is not in the menu.")

    def remove_item(self, name):
        for dish in self.menu:
            if dish["name"].lower() == name.lower():
                self.menu.remove(dish)
                print(f"The dish '{name}' has been removed from the menu.")
                print("Updated menu:", self.menu)
                return
        print(f"Error: The dish '{name}' is not in the menu.")

if __name__ == "__main__":
    manager = MenuManager()
    
    print("Initial menu:")
    for dish in manager.menu:
        print(dish)
    
    print("\nTesting methods:")

    manager.add_item("Pizza", 20, "B", True)
    
    manager.update_item("Soup", 12, "A", False)
    
    manager.remove_item("Salad")
    