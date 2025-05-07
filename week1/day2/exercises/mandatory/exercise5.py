#🌟 Exercise 5 : Random
#Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100. Use the random module.
#Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.
import random
def guess_random_number(user_number):
    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)

    # Compare the user's number with the random number
    if user_number == random_number:
        # If the numbers match, print a success message
        print(f" Congratulations! You guessed the correct number: {random_number}")
    else:
        # If the numbers don't match, print a failure message with both numbers
        print(f"Too bad! Your number: {user_number}, Random number: {random_number}")

guess_random_number(45)
guess_random_number(100)
guess_random_number(1)
guess_random_number(50)
guess_random_number(75)
guess_random_number(99)
guess_random_number(10)
guess_random_number(25)
guess_random_number(60)
guess_random_number(80)
guess_random_number(90)
guess_random_number(30)
guess_random_number(70)
guess_random_number(55)
guess_random_number(85)
guess_random_number(40)
guess_random_number(20)
guess_random_number(65)       
guess_random_number(35)
guess_random_number(95)







