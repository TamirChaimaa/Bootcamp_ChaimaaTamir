# Ask the user to input a number from 1 to 9 (including).  # Demande à l'utilisateur de saisir un nombre entre 1 et 9 inclus
# Get a random number between 1 and 9. Hint: random module.  # Génère un nombre aléatoire entre 1 et 9 (utiliser le module random)
# If the user guesses the correct number print a message that says “Winner”.  # Si l'utilisateur devine correctement, afficher "Winner"
# If the user guesses the wrong number print a message that says “Better luck next time.”  # Sinon, afficher "Better luck next time."
# Bonus: use a loop that allows the user to keep guessing until they want to quit.  # Bonus : utiliser une boucle pour rejouer jusqu’à ce que l’utilisateur souhaite quitter
# Bonus 2: on exiting the loop, tally up and display total games won and lost.  # Bonus 2 : à la sortie de la boucle, afficher le nombre de victoires et de défaites
import random

# Initialize win and loss counters
wins = 0
losses = 0

print("Welcome to the Number Guessing Game!")

# Main loop to let the user keep playing
while True:
    # Get a random number between 1 and 9
    secret_number = random.randint(1, 9)
    
    # Ask the user to guess
    guess = input("Guess a number between 1 and 9")

    # Check if the user wants to quit
    if guess.lower() == 'quit':
        break

    # Check if the input is a number
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    # Convert input to integer
    guess = int(guess)

    # Check if number is in the correct range
    if guess < 1 or guess > 9:
        print("Number must be between 1 and 9.")
        continue

    # Compare guess with the random number
    if guess == secret_number:
        print("Winner!")
        wins += 1
    else:
        print(f"Better luck next time. The correct number was {secret_number}.")
        losses += 1

# Show total wins and losses
print("\nGame Over.")
print(f"Total games won: {wins}")
print(f"Total games lost: {losses}")
