from menu_item import MenuItem
from menu_manager import MenuManager

def show_user_menu():
    while True:
        print("\n--- Menu du programme ---")
        print("V - Voir un élément")
        print("A - Ajouter un élément")
        print("D - Supprimer un élément")
        print("U - Mettre à jour un élément")
        print("S - Afficher le menu du restaurant")
        print("Q - Quitter")

        choice = input("Choisissez une option : ").strip().upper()

        if choice == "V":
            name = input("Entrez le nom de l'élément à rechercher : ")
            item = MenuManager.get_by_name(name)
            if item:
                print(f"Nom : {item.name}, Prix : {item.price}€")
            else:
                print("Élément non trouvé.")
        elif choice == "A":
            add_item_to_menu()
        elif choice == "D":
            remove_item_from_menu()
        elif choice == "U":
            update_item_from_menu()
        elif choice == "S":
            show_restaurant_menu()
        elif choice == "Q":
            print("Fermeture du programme.")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

def add_item_to_menu():
    name = input("Entrez le nom de l'article : ")
    try:
        price = float(input("Entrez le prix : "))
        item = MenuItem(name, price)
        item.save()
        print("✔ Élément ajouté avec succès.")
    except ValueError:
        print("Erreur : Le prix doit être un nombre.")

def remove_item_from_menu():
    name = input("Entrez le nom de l'article à supprimer : ")
    item = MenuItem(name, 0)  # Prix fictif car non utilisé
    item.delete()
    print("✔ Élément supprimé avec succès.")

def update_item_from_menu():
    name = input("Entrez le nom de l'article à mettre à jour : ")
    item = MenuManager.get_by_name(name)
    if not item:
        print("❌ Élément non trouvé.")
        return

    new_name = input("Entrez le nouveau nom : ")
    try:
        new_price = float(input("Entrez le nouveau prix : "))
        item.update(new_name, new_price)
        print("✔ Élément mis à jour avec succès.")
    except ValueError:
        print("Erreur : Le prix doit être un nombre.")

def show_restaurant_menu():
    items = MenuManager.all_items()
    if not items:
        print("Le menu est vide.")
    else:
        print("\n--- Menu du restaurant ---")
        for item in items:
            print(f"{item.name} : {item.price} €")

if __name__ == "__main__":
    show_user_menu()
