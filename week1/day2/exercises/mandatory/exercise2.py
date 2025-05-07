# Given family dictionary with names and ages
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# Function to calculate the ticket price based on age
def calculate_ticket_price(age):
    if age < 3:
        # Ticket is free if the person is under 3 years old
        return 0
    elif 3 <= age <= 12:
        # Ticket costs $10 if the person is between 3 and 12 years old
        return 10
    else:
        # Ticket costs $15 if the person is over 12 years old
        return 15

# Function to calculate and print the price for each person
def has_to_pay(name, age):
    price = calculate_ticket_price(age)  # Calculate price for the given age
    print(f"{name} has to pay {price} $")  # Print the price to pay for each member
    return price  # Return the price for further calculation

# Function to calculate the total cost for the entire familydef total_cost(prices):
def total_cost(prices):
    total_cost = sum(prices)  # Somme des prix dans la liste
    print(f"\n💰 Total cost for the family is: ${total_cost}")  # Afficher le coût total
    return total_cost  # Retourner le coût total

# Function to compute and print the family ticket prices
def compute_family_cost(family_dict):
    
    print("Ticket Prices Per Person:") # Indicate that ticket prices are about to be printed
    prices = []  # Initialize an empty list to store individual prices
    for name, age in family_dict.items():  # Iterate through each family member
        price = has_to_pay(name, age)  # Call has_to_pay function to print individual prices
        prices.append(price)  # Add each individual price to the prices list
    # Call total_cost function to calculate and print the total cost for the family
    total_cost(prices)

# Call function to compute family cost and print all information
compute_family_cost(family)

#Bonus: Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).

# BONUS: Ask user how many family members and get names and ages
custom_family = {}
is_valid = True

# Demande du nombre de membres
while is_valid:
    try:
        number = int(input("👨‍👩‍👧‍👦 How many family members? "))
        if number <= 0:
            print("⚠️ Please enter a positive number.")
            is_valid = False
        else:
            break  # Sortie de la boucle si c’est valide
    except ValueError:
        print("⚠️ Please enter a valid number.")
        is_valid = False

# Saisie des membres de la famille

while len(custom_family) < number:
    print(f"\nEntering info for family member #{len(custom_family)+1}:")
    name = input("Enter name: ")
    if name in custom_family:
        print("⚠️ This name is already entered. Please use a different name.")
        continue
    try:
        age = int(input(f"Enter age of {name}: "))
        custom_family[name] = age
    except ValueError:
        print("⚠️ Please enter a valid number for the age.")
    

# Appel de la fonction de calcul (si elle est définie ailleurs)
compute_family_cost(custom_family)
