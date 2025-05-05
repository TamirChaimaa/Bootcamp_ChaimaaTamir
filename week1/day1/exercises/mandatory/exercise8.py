# Exercise 8 : Sandwich Orders
#sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"].

# The deli has run out of pastrami, use a while loop to remove all occurrences of Pastrami sandwich from sandwich_orders.
# We need to prepare the orders of the clients:

# Create an empty list called finished_sandwiches.

# One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
# After all the sandwiches have been made, print a message listing each sandwich that was made, such as:

# Liste initiale des commandes
sandwich_orders = [
    "Tuna sandwich",
    "Pastrami sandwich",
    "Avocado sandwich",
    "Pastrami sandwich",
    "Egg sandwich",
    "Chicken sandwich",
    "Pastrami sandwich"
]

print("Sorry, the deli has run out of Pastrami.\n")

# Supprimer tous les "Pastrami sandwich"
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

# Liste des sandwichs préparés
finished_sandwiches = []

# Préparer les sandwichs restants
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)  # retirer le premier sandwich
    print(f"I made your {sandwich.lower()}.")
    finished_sandwiches.append(sandwich)

# Affichage final
print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")


